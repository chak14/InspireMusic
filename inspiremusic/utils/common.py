# Copyright (c) 2020 Mobvoi Inc (Binbin Zhang)
#               2024 Alibaba Inc
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# Modified from ESPnet(https://github.com/espnet/espnet)
"""Unility functions for Transformer."""

from typing import List
import torch
IGNORE_ID = -1

def pad_list(xs: List[torch.Tensor], pad_value: int):
    """Perform padding for the list of tensors.

    Args:
        xs (List): List of Tensors [(T_1, `*`), (T_2, `*`), ..., (T_B, `*`)].
        pad_value (float): Value for padding.

    Returns:
        Tensor: Padded tensor (B, Tmax, `*`).

    Examples:
        >>> x = [torch.ones(4), torch.ones(2), torch.ones(1)]
        >>> x
        [tensor([1., 1., 1., 1.]), tensor([1., 1.]), tensor([1.])]
        >>> pad_list(x, 0)
        tensor([[1., 1., 1., 1.],
                [1., 1., 0., 0.],
                [1., 0., 0., 0.]])

    """
    max_len = max([len(item) for item in xs])
    batchs = len(xs)
    ndim = xs[0].ndim
    if ndim == 1:
        pad_res = torch.zeros(batchs,
                              max_len,
                              dtype=xs[0].dtype,
                              device=xs[0].device)
    elif ndim == 2:
        pad_res = torch.zeros(batchs,
                              max_len,
                              xs[0].shape[1],
                              dtype=xs[0].dtype,
                              device=xs[0].device)
    elif ndim == 3:
        pad_res = torch.zeros(batchs,
                              max_len,
                              xs[0].shape[1],
                              xs[0].shape[2],
                              dtype=xs[0].dtype,
                              device=xs[0].device)
    else:
        raise ValueError(f"Unsupported ndim: {ndim}")
    pad_res.fill_(pad_value)
    for i in range(batchs):
        pad_res[i, :len(xs[i])] = xs[i]
    return pad_res


def th_accuracy(pad_outputs: torch.Tensor, pad_targets: torch.Tensor,
                ignore_label: int) -> torch.Tensor:
    """Calculate accuracy.

    Args:
        pad_outputs (Tensor): Prediction tensors (B * Lmax, D).
        pad_targets (LongTensor): Target label tensors (B, Lmax).
        ignore_label (int): Ignore label id.

    Returns:
        torch.Tensor: Accuracy value (0.0 - 1.0).

    """
    pad_pred = pad_outputs.view(pad_targets.size(0), pad_targets.size(1),
                                pad_outputs.size(1)).argmax(2)
    mask = pad_targets != ignore_label
    numerator = torch.sum(
        pad_pred.masked_select(mask) == pad_targets.masked_select(mask))
    denominator = torch.sum(mask)
    return (numerator / denominator).detach()

def get_padding(kernel_size, dilation=1):
    return int((kernel_size * dilation - dilation) / 2)

def init_weights(m, mean=0.0, std=0.01):
    classname = m.__class__.__name__
    if classname.find("Conv") != -1:
        m.weight.data.normal_(mean, std)

def keep_rhythm(next_token, current_time_signature):
    allowed_durations = get_allowed_durations(current_time_signature)
    if next_token not in allowed_durations:
        next_token = random.choice(allowed_durations)
    return next_token

def keep_harmony(next_token, current_chord):
    allowed_notes = get_allowed_notes(current_chord)  # Define allowed notes for the chord
    if next_token not in allowed_notes:
        next_token = random.choice(allowed_notes)  # Replace with a valid note
    return next_token

def relieve_repetition(weighted_scores, recent_tokens, repetition_penalty=1.2):
    for token in recent_tokens:
        if weighted_scores[token] > 0:
            weighted_scores[token] /= repetition_penalty
    return weighted_scores

def top_p_sampling_with_constraints(weighted_scores, decoded_tokens, top_p=0.85, temperature=1.1, current_chord=None, current_time_signature=None, recent_tokens=None):
    # Apply temperature scaling
    weighted_scores = weighted_scores ** (1 / temperature)
    weighted_scores /= weighted_scores.sum()

    if recent_tokens:
        weighted_scores = relieve_repetition(weighted_scores, recent_tokens)

    # Sort weighted scores in descending order
    sorted_weighted_scores, _ = torch.sort(weighted_scores, descending=True)

    # Compute cumulative weighted scores
    cumulative_weighted_scores = torch.cumsum(sorted_weighted_scores, dim=0)

    # Find the threthold index of top-p
    cutoff_index = torch.where(cumulative_weighted_scores >= top_p)[0][0]
    selected_weighted_scores = sorted_weighted_scores[:cutoff_index + 1]

    # Apply domain-specific constraints
    if current_chord:
        selected_weighted_scores = keep_harmony(selected_weighted_scores, current_chord)
    if current_time_signature:
        selected_weighted_scores = keep_rhythm(selected_weighted_scores, current_time_signature)

    # Normalize selected probabilities
    selected_weighted_scores /= selected_weighted_scores.sum()

    # Sample top-p tokens from the distribution
    return random_sampling(selected_weighted_scores, decoded_tokens)
def topk_sampling(weighted_scores, decoded_tokens, top_k=25):
    zeros = weighted_scores.new_ones(weighted_scores.shape) * float('-inf')
    values,indices =  torch.topk(weighted_scores,top_k)
    zeros.scatter_(-1, indices, values)
    return random_sampling(zeros,decoded_tokens)

# Repetition Aware Sampling in VALL-E 2

def ras_sampling(weighted_scores, decoded_tokens, top_p=0.8, top_k=25, win_size=10, tau_r=0.1):
    top_ids = nucleus_sampling(weighted_scores, top_p=top_p, top_k=top_k)
    rep_num = (torch.tensor(decoded_tokens[-win_size:]).to(weighted_scores.device) == top_ids).sum().item()
    if rep_num >= win_size * tau_r:
        top_ids = random_sampling(weighted_scores, decoded_tokens)
    return top_ids

def caras_sampling(weighted_scores, decoded_tokens, top_p=0.8, top_k=25, win_size=10, tau_r=0.1):
    weighted_scores, cfg_weighted_scores = weighted_scores
    top_ids = nucleus_sampling(weighted_scores, top_p=top_p, top_k=top_k)
    rep_num = (torch.tensor(decoded_tokens[-win_size:]).to(weighted_scores.device) == top_ids).sum().item()
    if rep_num >= win_size * tau_r:
        top_ids = random_sampling(cfg_weighted_scores, decoded_tokens)
    return top_ids

def nucleus_sampling(weighted_scores, top_p=0.8, top_k=25):
    prob, indices = [], []
    cum_prob = 0.0
    sorted_value, sorted_idx = weighted_scores.softmax(dim=0).sort(descending=True, stable=True)
    for i in range(len(sorted_idx)):
        # sampling both top-p and numbers.
        if cum_prob < top_p and len(prob) < top_k:
            cum_prob += sorted_value[i]
            prob.append(sorted_value[i])
            indices.append(sorted_idx[i])
        else:
            break
    prob = torch.tensor(prob).to(weighted_scores)
    indices = torch.tensor(indices, dtype=torch.long).to(weighted_scores.device)
    top_ids = indices[prob.multinomial(1, replacement=True)]
    return top_ids


def random_sampling(weighted_scores, decoded_tokens):
    top_ids = weighted_scores.softmax(dim=0).multinomial(1, replacement=True)
    return top_ids


def fade_in_out(fade_in_mel, fade_out_mel, window):
    device = fade_in_mel.device
    fade_in_mel, fade_out_mel = fade_in_mel.cpu(), fade_out_mel.cpu()
    mel_overlap_len = int(window.shape[0] / 2)
    fade_in_mel[:, :, :mel_overlap_len] = fade_in_mel[:, :, :mel_overlap_len] * window[:mel_overlap_len] + \
        fade_out_mel[:, :, -mel_overlap_len:] * window[mel_overlap_len:]
    return fade_in_mel.to(device)

def set_all_random_seed(seed):
    random.seed(seed)
    np.random.seed(seed)
    torch.manual_seed(seed)
    torch.cuda.manual_seed_all(seed)

def mask_to_bias(mask: torch.Tensor, dtype: torch.dtype) -> torch.Tensor:
    assert mask.dtype == torch.bool
    assert dtype in [torch.float32, torch.bfloat16, torch.float16]
    mask = mask.to(dtype)
    # attention mask bias
    # NOTE(Mddct): torch.finfo jit issues
    #     chunk_masks = (1.0 - chunk_masks) * torch.finfo(dtype).min
    mask = (1.0 - mask) * torch.finfo(dtype).min
    return mask
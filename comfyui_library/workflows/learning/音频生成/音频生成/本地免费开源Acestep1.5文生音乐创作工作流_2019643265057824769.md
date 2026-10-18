---
key: 音频生成/音频生成/本地免费开源Acestep1.5文生音乐创作工作流_2019643265057824769.json
name: 本地免费开源Acestep1.5文生音乐创作工作流_2019643265057824769
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/音频生成/音频生成/本地免费开源Acestep1.5文生音乐创作工作流_2019643265057824769.json
hash: 7a18bdb19023cd32
coverage: 0.65
learned_at: 2026-10-18 02:07:11
nodes: [ConditioningZeroOut, KSampler, ModelSamplingAuraFlow, Fast Groups Muter (rgthree), VAELoader, PrimitiveNode, Any Switch (rgthree), DualCLIPLoader, Any Switch (rgthree), CheckpointLoaderSimple, Any Switch (rgthree), UNETLoader, EmptyAceStep1.5LatentAudio, Text Multiline, Text Multiline, PrimitiveNode, MarkdownNote, VAEDecodeAudio, SaveAudioMP3, TextEncodeAceStepAudio1.5]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换]
parameters: {"cfg": 1, "checkpoint": "ace_step_1.5_turbo_aio.safetensors", "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 33, "steps": 8}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换]
---

# 音频生成/音频生成/本地免费开源Acestep1.5文生音乐创作工作流_2019643265057824769.json

> 来源文件 `comfyui_library/workflows/音频生成/音频生成/本地免费开源Acestep1.5文生音乐创作工作流_2019643265057824769.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Output → Other

**节点**（20 个）：
- `ConditioningZeroOut`
- `KSampler` ★核心
- `ModelSamplingAuraFlow`
- `Fast Groups Muter (rgthree)`
- `VAELoader`
- `PrimitiveNode`
- `Any Switch (rgthree)`
- `DualCLIPLoader`
- `Any Switch (rgthree)`
- `CheckpointLoaderSimple` ★核心
- `Any Switch (rgthree)`
- `UNETLoader` ★核心
- `EmptyAceStep1.5LatentAudio`
- `Text Multiline`
- `Text Multiline`
- `PrimitiveNode`
- `MarkdownNote`
- `VAEDecodeAudio` ★核心
- `SaveAudioMP3`
- `TextEncodeAceStepAudio1.5`

## 关键参数

- `seed` = `33`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`
- `checkpoint` = `ace_step_1.5_turbo_aio.safetensors`

## 知识

覆盖率 **65%**（13/20）

**有卡**：`ConditioningZeroOut`、`KSampler`、`ModelSamplingAuraFlow`、`VAELoader`、`DualCLIPLoader`、`CheckpointLoaderSimple`、`UNETLoader`、`EmptyAceStep1.5LatentAudio`、`Text Multiline`、`VAEDecodeAudio`、`SaveAudioMP3`、`TextEncodeAceStepAudio1.5`

**用到的条目**：KSampler、VAELoader、CheckpointLoaderSimple、UNETLoader、ConditioningZeroOut、VAEDecodeAudio、EmptyAceStep1.5LatentAudio、TextEncodeAceStepAudio1.5

## 参数体检

发现 2 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换

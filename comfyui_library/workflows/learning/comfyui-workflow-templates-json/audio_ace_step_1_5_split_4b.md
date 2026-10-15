---
key: comfyui-workflow-templates-json/audio_ace_step_1_5_split_4b.json
name: audio_ace_step_1_5_split_4b
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/comfyui-workflow-templates-json/audio_ace_step_1_5_split_4b.json
hash: 881a395d6fe6f19b
official: true
coverage: 0.769231
learned_at: 2026-10-15 22:24:52
nodes: [UNETLoader, VAELoader, PrimitiveNode, PrimitiveNode, EmptyAceStep1.5LatentAudio, ConditioningZeroOut, KSampler, ModelSamplingAuraFlow, VAEDecodeAudio, DualCLIPLoader, TextEncodeAceStepAudio1.5, SaveAudioMP3, MarkdownNote]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 31, "steps": 8}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换]
---

# comfyui-workflow-templates-json/audio_ace_step_1_5_split_4b.json

> 来源文件 `comfyui_library/workflows/comfyui-workflow-templates-json/audio_ace_step_1_5_split_4b.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Output → Other

**节点**（13 个）：
- `UNETLoader` ★核心
- `VAELoader`
- `PrimitiveNode`
- `PrimitiveNode`
- `EmptyAceStep1.5LatentAudio`
- `ConditioningZeroOut`
- `KSampler` ★核心
- `ModelSamplingAuraFlow`
- `VAEDecodeAudio` ★核心
- `DualCLIPLoader`
- `TextEncodeAceStepAudio1.5`
- `SaveAudioMP3`
- `MarkdownNote`

## 关键参数

- `seed` = `31`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **77%**（10/13）

**有卡**：`UNETLoader`、`VAELoader`、`EmptyAceStep1.5LatentAudio`、`ConditioningZeroOut`、`KSampler`、`ModelSamplingAuraFlow`、`VAEDecodeAudio`、`DualCLIPLoader`、`TextEncodeAceStepAudio1.5`、`SaveAudioMP3`

**用到的条目**：KSampler、VAELoader、ConditioningZeroOut、UNETLoader、VAEDecodeAudio、EmptyAceStep1.5LatentAudio、TextEncodeAceStepAudio1.5、SaveAudioMP3

## 参数体检

发现 2 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换

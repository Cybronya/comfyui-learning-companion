---
key: comfyui-workflow-templates-json/audio_ace_step1_5_xl_turbo.json
name: audio_ace_step1_5_xl_turbo
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/comfyui-workflow-templates-json/audio_ace_step1_5_xl_turbo.json
hash: 5b0445de2e7ced8f
official: true
coverage: 0.769231
learned_at: 2026-10-15 22:24:52
nodes: [UNETLoader, VAELoader, PrimitiveNode, EmptyAceStep1.5LatentAudio, ConditioningZeroOut, KSampler, ModelSamplingAuraFlow, VAEDecodeAudio, DualCLIPLoader, TextEncodeAceStepAudio1.5, PrimitiveInt, MarkdownNote, SaveAudioAdvanced]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 0, "steps": 8}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换]
---

# comfyui-workflow-templates-json/audio_ace_step1_5_xl_turbo.json

> 来源文件 `comfyui_library/workflows/comfyui-workflow-templates-json/audio_ace_step1_5_xl_turbo.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Output → Other

**节点**（13 个）：
- `UNETLoader` ★核心
- `VAELoader`
- `PrimitiveNode`
- `EmptyAceStep1.5LatentAudio`
- `ConditioningZeroOut`
- `KSampler` ★核心
- `ModelSamplingAuraFlow`
- `VAEDecodeAudio` ★核心
- `DualCLIPLoader`
- `TextEncodeAceStepAudio1.5`
- `PrimitiveInt`
- `MarkdownNote`
- `SaveAudioAdvanced`

## 关键参数

- `seed` = `0`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **77%**（10/13）

**有卡**：`UNETLoader`、`VAELoader`、`EmptyAceStep1.5LatentAudio`、`ConditioningZeroOut`、`KSampler`、`ModelSamplingAuraFlow`、`VAEDecodeAudio`、`DualCLIPLoader`、`TextEncodeAceStepAudio1.5`、`SaveAudioAdvanced`

**用到的条目**：KSampler、VAELoader、ConditioningZeroOut、UNETLoader、VAEDecodeAudio、EmptyAceStep1.5LatentAudio、TextEncodeAceStepAudio1.5、SaveAudioAdvanced

## 参数体检

发现 2 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换

---
key: comfyui-workflow-templates-json/audio_ace_step_1_5_split.json
name: audio_ace_step_1_5_split
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/comfyui-workflow-templates-json/audio_ace_step_1_5_split.json
hash: 4f4a2dd9055c0d12
official: true
coverage: 0.615385
learned_at: 2026-10-10 22:46:55
nodes: [UNETLoader, DualCLIPLoader, VAELoader, PrimitiveNode, PrimitiveNode, EmptyAceStep1.5LatentAudio, ConditioningZeroOut, KSampler, ModelSamplingAuraFlow, VAEDecodeAudio, SaveAudioMP3, TextEncodeAceStepAudio1.5, MarkdownNote]
patterns: []
missing: [EmptyAceStep1.5LatentAudio, TextEncodeAceStepAudio1.5]
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 31, "steps": 8}
discoveries: [次要节点 `EmptyAceStep1.5LatentAudio` 仅有 VAE 的通用知识，没有该节点自己的说明, 次要节点 `TextEncodeAceStepAudio1.5` 仅有 VAE 的通用知识，没有该节点自己的说明, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换]
---

# comfyui-workflow-templates-json/audio_ace_step_1_5_split.json

> 来源文件 `comfyui_library/workflows/comfyui-workflow-templates-json/audio_ace_step_1_5_split.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Output → Other

**节点**（13 个）：
- `UNETLoader` ★核心
- `DualCLIPLoader`
- `VAELoader`
- `PrimitiveNode`
- `PrimitiveNode`
- `EmptyAceStep1.5LatentAudio`
- `ConditioningZeroOut`
- `KSampler` ★核心
- `ModelSamplingAuraFlow`
- `VAEDecodeAudio` ★核心
- `SaveAudioMP3`
- `TextEncodeAceStepAudio1.5`
- `MarkdownNote`

## 关键参数

- `seed` = `31`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **62%**（8/13）

**有卡**：`UNETLoader`、`DualCLIPLoader`、`VAELoader`、`ConditioningZeroOut`、`KSampler`、`ModelSamplingAuraFlow`、`VAEDecodeAudio`、`SaveAudioMP3`

**缺卡**（2）：`EmptyAceStep1.5LatentAudio`、`TextEncodeAceStepAudio1.5`

**用到的条目**：KSampler、VAELoader、ConditioningZeroOut、UNETLoader、VAEDecodeAudio、SaveAudioMP3、DualCLIPLoader、ModelSamplingAuraFlow

## 参数体检

发现 2 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换

## 学习发现

- 次要节点 `EmptyAceStep1.5LatentAudio` 仅有 VAE 的通用知识，没有该节点自己的说明
- 次要节点 `TextEncodeAceStepAudio1.5` 仅有 VAE 的通用知识，没有该节点自己的说明
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换

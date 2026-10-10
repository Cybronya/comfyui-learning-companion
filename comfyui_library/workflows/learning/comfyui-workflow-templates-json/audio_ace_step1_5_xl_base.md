---
key: comfyui-workflow-templates-json/audio_ace_step1_5_xl_base.json
name: audio_ace_step1_5_xl_base
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/comfyui-workflow-templates-json/audio_ace_step1_5_xl_base.json
hash: 1fa288961b107b7a
official: true
coverage: 0.615385
learned_at: 2026-10-10 22:46:51
nodes: [UNETLoader, VAELoader, PrimitiveNode, EmptyAceStep1.5LatentAudio, ConditioningZeroOut, KSampler, VAEDecodeAudio, DualCLIPLoader, PrimitiveInt, MarkdownNote, TextEncodeAceStepAudio1.5, ModelSamplingAuraFlow, SaveAudioAdvanced]
patterns: []
missing: [EmptyAceStep1.5LatentAudio, TextEncodeAceStepAudio1.5]
problems: [[high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换]
parameters: {"cfg": 6, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 0, "steps": 50}
discoveries: [次要节点 `EmptyAceStep1.5LatentAudio` 仅有 VAE 的通用知识，没有该节点自己的说明, 次要节点 `TextEncodeAceStepAudio1.5` 仅有 VAE 的通用知识，没有该节点自己的说明, [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换]
---

# comfyui-workflow-templates-json/audio_ace_step1_5_xl_base.json

> 来源文件 `comfyui_library/workflows/comfyui-workflow-templates-json/audio_ace_step1_5_xl_base.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Output → Other

**节点**（13 个）：
- `UNETLoader` ★核心
- `VAELoader`
- `PrimitiveNode`
- `EmptyAceStep1.5LatentAudio`
- `ConditioningZeroOut`
- `KSampler` ★核心
- `VAEDecodeAudio` ★核心
- `DualCLIPLoader`
- `PrimitiveInt`
- `MarkdownNote`
- `TextEncodeAceStepAudio1.5`
- `ModelSamplingAuraFlow`
- `SaveAudioAdvanced`

## 关键参数

- `seed` = `0`
- `steps` = `50`
- `cfg` = `6`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **62%**（8/13）

**有卡**：`UNETLoader`、`VAELoader`、`ConditioningZeroOut`、`KSampler`、`VAEDecodeAudio`、`DualCLIPLoader`、`ModelSamplingAuraFlow`、`SaveAudioAdvanced`

**缺卡**（2）：`EmptyAceStep1.5LatentAudio`、`TextEncodeAceStepAudio1.5`

**用到的条目**：KSampler、VAELoader、ConditioningZeroOut、UNETLoader、VAEDecodeAudio、SaveAudioAdvanced、DualCLIPLoader、ModelSamplingAuraFlow

## 参数体检

发现 1 个问题：
- [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换

## 学习发现

- 次要节点 `EmptyAceStep1.5LatentAudio` 仅有 VAE 的通用知识，没有该节点自己的说明
- 次要节点 `TextEncodeAceStepAudio1.5` 仅有 VAE 的通用知识，没有该节点自己的说明
- [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换

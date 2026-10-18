---
key: 音频生成/音频生成/[🛫书墨]Acestep1.5文生音乐创作工作流_2018940506566303746.json
name: [🛫书墨]Acestep1.5文生音乐创作工作流_2018940506566303746
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/音频生成/音频生成/[🛫书墨]Acestep1.5文生音乐创作工作流_2018940506566303746.json
hash: cd8655e0bde6b65b
coverage: 0.611111
learned_at: 2026-10-18 02:07:07
nodes: [ConditioningZeroOut, KSampler, ModelSamplingAuraFlow, VAEDecodeAudio, PrimitiveNode, Any Switch (rgthree), Any Switch (rgthree), Any Switch (rgthree), Fast Groups Muter (rgthree), SaveAudioMP3, TextEncodeAceStepAudio1.5, UNETLoader, VAELoader, MarkdownNote, CheckpointLoaderSimple, PrimitiveNode, EmptyAceStep1.5LatentAudio, DualCLIPLoader]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换]
parameters: {"cfg": 1, "checkpoint": "ace_step_1.5_turbo_aio.safetensors", "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 33, "steps": 8}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换]
---

# 音频生成/音频生成/[🛫书墨]Acestep1.5文生音乐创作工作流_2018940506566303746.json

> 来源文件 `comfyui_library/workflows/音频生成/音频生成/[🛫书墨]Acestep1.5文生音乐创作工作流_2018940506566303746.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Output → Other

**节点**（18 个）：
- `ConditioningZeroOut`
- `KSampler` ★核心
- `ModelSamplingAuraFlow`
- `VAEDecodeAudio` ★核心
- `PrimitiveNode`
- `Any Switch (rgthree)`
- `Any Switch (rgthree)`
- `Any Switch (rgthree)`
- `Fast Groups Muter (rgthree)`
- `SaveAudioMP3`
- `TextEncodeAceStepAudio1.5`
- `UNETLoader` ★核心
- `VAELoader`
- `MarkdownNote`
- `CheckpointLoaderSimple` ★核心
- `PrimitiveNode`
- `EmptyAceStep1.5LatentAudio`
- `DualCLIPLoader`

## 关键参数

- `seed` = `33`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`
- `checkpoint` = `ace_step_1.5_turbo_aio.safetensors`

## 知识

覆盖率 **61%**（11/18）

**有卡**：`ConditioningZeroOut`、`KSampler`、`ModelSamplingAuraFlow`、`VAEDecodeAudio`、`SaveAudioMP3`、`TextEncodeAceStepAudio1.5`、`UNETLoader`、`VAELoader`、`CheckpointLoaderSimple`、`EmptyAceStep1.5LatentAudio`、`DualCLIPLoader`

**用到的条目**：KSampler、VAELoader、CheckpointLoaderSimple、UNETLoader、ConditioningZeroOut、VAEDecodeAudio、EmptyAceStep1.5LatentAudio、TextEncodeAceStepAudio1.5

## 参数体检

发现 2 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换

---
key: 音频生成/音频生成/Acestep1.5最新文生音乐_2020056560453558273.json
name: Acestep1.5最新文生音乐_2020056560453558273
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/音频生成/音频生成/Acestep1.5最新文生音乐_2020056560453558273.json
hash: 285083dc7b4d77cf
coverage: 0.636364
learned_at: 2026-10-18 02:06:55
nodes: [KSampler, ModelSamplingAuraFlow, VAEDecodeAudio, Any Switch (rgthree), Any Switch (rgthree), Any Switch (rgthree), UNETLoader, VAELoader, CheckpointLoaderSimple, EmptyAceStep1.5LatentAudio, Note Plus (mtb), Note Plus (mtb), Note, Fast Groups Muter (rgthree), MarkdownNote, ConditioningZeroOut, PrimitiveNode, DualCLIPLoader, PrimitiveNode, SaveAudioMP3, TextEncodeAceStepAudio1.5, DF_Text_Box]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换]
parameters: {"cfg": 1, "checkpoint": "ace_step_1.5_turbo_aio.safetensors", "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 33, "steps": 8}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换]
---

# 音频生成/音频生成/Acestep1.5最新文生音乐_2020056560453558273.json

> 来源文件 `comfyui_library/workflows/音频生成/音频生成/Acestep1.5最新文生音乐_2020056560453558273.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Output → Other

**节点**（22 个）：
- `KSampler` ★核心
- `ModelSamplingAuraFlow`
- `VAEDecodeAudio` ★核心
- `Any Switch (rgthree)`
- `Any Switch (rgthree)`
- `Any Switch (rgthree)`
- `UNETLoader` ★核心
- `VAELoader`
- `CheckpointLoaderSimple` ★核心
- `EmptyAceStep1.5LatentAudio`
- `Note Plus (mtb)`
- `Note Plus (mtb)`
- `Note`
- `Fast Groups Muter (rgthree)`
- `MarkdownNote`
- `ConditioningZeroOut`
- `PrimitiveNode`
- `DualCLIPLoader`
- `PrimitiveNode`
- `SaveAudioMP3`
- `TextEncodeAceStepAudio1.5`
- `DF_Text_Box`

## 关键参数

- `seed` = `33`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`
- `checkpoint` = `ace_step_1.5_turbo_aio.safetensors`

## 知识

覆盖率 **64%**（14/22）

**有卡**：`KSampler`、`ModelSamplingAuraFlow`、`VAEDecodeAudio`、`UNETLoader`、`VAELoader`、`CheckpointLoaderSimple`、`EmptyAceStep1.5LatentAudio`、`Note Plus (mtb)`、`ConditioningZeroOut`、`DualCLIPLoader`、`SaveAudioMP3`、`TextEncodeAceStepAudio1.5`、`DF_Text_Box`

**用到的条目**：KSampler、VAELoader、CheckpointLoaderSimple、UNETLoader、ConditioningZeroOut、VAEDecodeAudio、EmptyAceStep1.5LatentAudio、TextEncodeAceStepAudio1.5

## 参数体检

发现 2 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换

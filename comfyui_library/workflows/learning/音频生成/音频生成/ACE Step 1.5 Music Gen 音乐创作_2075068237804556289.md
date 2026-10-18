---
key: 音频生成/音频生成/ACE Step 1.5 Music Gen 音乐创作_2075068237804556289.json
name: ACE Step 1.5 Music Gen 音乐创作_2075068237804556289
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/音频生成/音频生成/ACE Step 1.5 Music Gen 音乐创作_2075068237804556289.json
hash: 345db5068634753f
coverage: 0.666667
learned_at: 2026-10-18 03:04:45
nodes: [CheckpointLoaderSimple, SaveAudioMP3, SaveAudio, VAEDecodeAudio, MarkdownNote, Note, ModelSamplingAuraFlow, PrimitiveNode, PrimitiveNode, EmptyAceStep1.5LatentAudio, KSampler, PreviewAudio, ConditioningZeroOut, PrimitiveStringMultiline, PrimitiveStringMultiline, TextEncodeAceStepAudio1.5, LoadImage, SaveImage]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换]
parameters: {"cfg": 1, "checkpoint": "ace_step_1.5_turbo_aio.safetensors", "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 805825403264690, "steps": 8}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换]
---

# 音频生成/音频生成/ACE Step 1.5 Music Gen 音乐创作_2075068237804556289.json

> 来源文件 `comfyui_library/workflows/音频生成/音频生成/ACE Step 1.5 Music Gen 音乐创作_2075068237804556289.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Output → Other

**节点**（18 个）：
- `CheckpointLoaderSimple` ★核心
- `SaveAudioMP3`
- `SaveAudio`
- `VAEDecodeAudio` ★核心
- `MarkdownNote`
- `Note`
- `ModelSamplingAuraFlow`
- `PrimitiveNode`
- `PrimitiveNode`
- `EmptyAceStep1.5LatentAudio`
- `KSampler` ★核心
- `PreviewAudio`
- `ConditioningZeroOut`
- `PrimitiveStringMultiline`
- `PrimitiveStringMultiline`
- `TextEncodeAceStepAudio1.5`
- `LoadImage`
- `SaveImage`

## 关键参数

- `checkpoint` = `ace_step_1.5_turbo_aio.safetensors`
- `seed` = `805825403264690`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **67%**（12/18）

**有卡**：`CheckpointLoaderSimple`、`SaveAudioMP3`、`SaveAudio`、`VAEDecodeAudio`、`ModelSamplingAuraFlow`、`EmptyAceStep1.5LatentAudio`、`KSampler`、`PreviewAudio`、`ConditioningZeroOut`、`TextEncodeAceStepAudio1.5`、`LoadImage`、`SaveImage`

**用到的条目**：KSampler、CheckpointLoaderSimple、ConditioningZeroOut、LoadImage、VAEDecodeAudio、EmptyAceStep1.5LatentAudio、TextEncodeAceStepAudio1.5、SaveImage

## 参数体检

发现 2 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换

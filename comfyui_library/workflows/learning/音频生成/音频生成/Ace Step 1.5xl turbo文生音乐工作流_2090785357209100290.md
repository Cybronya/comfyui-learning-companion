---
key: 音频生成/音频生成/Ace Step 1.5xl turbo文生音乐工作流_2090785357209100290.json
name: Ace Step 1.5xl turbo文生音乐工作流_2090785357209100290
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/音频生成/音频生成/Ace Step 1.5xl turbo文生音乐工作流_2090785357209100290.json
hash: 61559e86848a3cfc
coverage: 0.666667
learned_at: 2026-10-18 17:45:27
nodes: [Label (rgthree), LoadImage, Note, TextEncodeAceStepAudio1.5, Note, MarkdownNote, TextEncodeAceStepAudio1.5, LoadImage, UNETLoader, ModelSamplingAuraFlow, DualCLIPLoader, EmptyAceStep1.5LatentAudio, VAELoader, ConditioningZeroOut, VAEDecodeAudio, PreviewAudio, SaveAudioAdvanced, KSampler, PrimitiveInt, PrimitiveNode, PrimitiveInt, Label (rgthree), PrimitiveStringMultiline, PrimitiveStringMultiline]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 0, "steps": 8}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换]
---

# 音频生成/音频生成/Ace Step 1.5xl turbo文生音乐工作流_2090785357209100290.json

> 来源文件 `comfyui_library/workflows/音频生成/音频生成/Ace Step 1.5xl turbo文生音乐工作流_2090785357209100290.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Output → Other

**节点**（24 个）：
- `Label (rgthree)`
- `LoadImage`
- `Note`
- `TextEncodeAceStepAudio1.5`
- `Note`
- `MarkdownNote`
- `TextEncodeAceStepAudio1.5`
- `LoadImage`
- `UNETLoader` ★核心
- `ModelSamplingAuraFlow`
- `DualCLIPLoader`
- `EmptyAceStep1.5LatentAudio`
- `VAELoader`
- `ConditioningZeroOut`
- `VAEDecodeAudio` ★核心
- `PreviewAudio`
- `SaveAudioAdvanced`
- `KSampler` ★核心
- `PrimitiveInt`
- `PrimitiveNode`
- `PrimitiveInt`
- `Label (rgthree)`
- `PrimitiveStringMultiline`
- `PrimitiveStringMultiline`

## 关键参数

- `seed` = `0`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **67%**（16/24）

**有卡**：`Label (rgthree)`、`LoadImage`、`TextEncodeAceStepAudio1.5`、`UNETLoader`、`ModelSamplingAuraFlow`、`DualCLIPLoader`、`EmptyAceStep1.5LatentAudio`、`VAELoader`、`ConditioningZeroOut`、`VAEDecodeAudio`、`PreviewAudio`、`SaveAudioAdvanced`、`KSampler`

**用到的条目**：KSampler、VAELoader、ConditioningZeroOut、LoadImage、UNETLoader、VAEDecodeAudio、EmptyAceStep1.5LatentAudio、TextEncodeAceStepAudio1.5

## 参数体检

发现 2 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换

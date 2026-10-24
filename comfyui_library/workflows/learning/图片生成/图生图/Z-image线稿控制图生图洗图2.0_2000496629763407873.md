---
key: 图片生成/图生图/Z-image线稿控制图生图洗图2.0_2000496629763407873.json
name: Z-image线稿控制图生图洗图2.0_2000496629763407873
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Z-image线稿控制图生图洗图2.0_2000496629763407873.json
hash: f90fbb167abe78e0
coverage: 0.947368
learned_at: 2026-10-23 11:31:53
nodes: [UNETLoader, CLIPLoader, VAEDecode, VAELoader, VAEEncode, VAEDecode, ConditioningZeroOut, VAEEncode, LayerUtility: ImageScaleByAspectRatio V2, SaveImage, QwenImageDiffsynthControlnet, KSampler, ModelPatchLoader, KSampler, RH_Captioner, AIO_Preprocessor, LoadImage, MarkdownNote, CLIPTextEncode]
patterns: [image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 0.16000000000000003, "sampler_name": "euler", "scheduler": "simple", "seed": 817309667416880, "steps": 9}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/Z-image线稿控制图生图洗图2.0_2000496629763407873.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Z-image线稿控制图生图洗图2.0_2000496629763407873.json`

## 结构

**生成流程**：Model → Encode → Condition → Control → Sampling → Decode → Process → Output → Other

**节点**（19 个）：
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAEDecode` ★核心
- `VAELoader`
- `VAEEncode` ★核心
- `VAEDecode` ★核心
- `ConditioningZeroOut`
- `VAEEncode` ★核心
- `LayerUtility: ImageScaleByAspectRatio V2`
- `SaveImage`
- `QwenImageDiffsynthControlnet`
- `KSampler` ★核心
- `ModelPatchLoader`
- `KSampler` ★核心
- `RH_Captioner`
- `AIO_Preprocessor`
- `LoadImage`
- `MarkdownNote`
- `CLIPTextEncode` ★核心

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `817309667416880`
- `steps` = `9`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `0.16000000000000003`

## 知识

覆盖率 **95%**（18/19）

**有卡**：`UNETLoader`、`CLIPLoader`、`VAEDecode`、`VAELoader`、`VAEEncode`、`ConditioningZeroOut`、`LayerUtility: ImageScaleByAspectRatio V2`、`SaveImage`、`QwenImageDiffsynthControlnet`、`KSampler`、`ModelPatchLoader`、`RH_Captioner`、`AIO_Preprocessor`、`LoadImage`、`CLIPTextEncode`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、LoadImage、UNETLoader

## 参数体检

发现 2 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

---
key: 图片生成/图生图/Z-image线稿控制图生图洗图2.1_2001578550618648578.json
name: Z-image线稿控制图生图洗图2.1_2001578550618648578
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Z-image线稿控制图生图洗图2.1_2001578550618648578.json
hash: fae691e3781cdf02
coverage: 1
learned_at: 2026-10-23 11:31:53
nodes: [UNETLoader, CLIPLoader, VAEDecode, VAELoader, VAEEncode, VAEDecode, ConditioningZeroOut, VAEEncode, LayerUtility: ImageScaleByAspectRatio V2, SaveImage, QwenImageDiffsynthControlnet, KSampler, KSampler, RH_Captioner, AIO_Preprocessor, LoadImage, CLIPTextEncode, ModelPatchLoader]
patterns: [image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 0.16000000000000003, "sampler_name": "euler", "scheduler": "simple", "seed": 86987779438748, "steps": 9}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/Z-image线稿控制图生图洗图2.1_2001578550618648578.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Z-image线稿控制图生图洗图2.1_2001578550618648578.json`

## 结构

**生成流程**：Model → Encode → Condition → Control → Sampling → Decode → Process → Output → Other

**节点**（18 个）：
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
- `KSampler` ★核心
- `RH_Captioner`
- `AIO_Preprocessor`
- `LoadImage`
- `CLIPTextEncode` ★核心
- `ModelPatchLoader`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `86987779438748`
- `steps` = `9`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `0.16000000000000003`

## 知识

覆盖率 **100%**（18/18）

**有卡**：`UNETLoader`、`CLIPLoader`、`VAEDecode`、`VAELoader`、`VAEEncode`、`ConditioningZeroOut`、`LayerUtility: ImageScaleByAspectRatio V2`、`SaveImage`、`QwenImageDiffsynthControlnet`、`KSampler`、`RH_Captioner`、`AIO_Preprocessor`、`LoadImage`、`CLIPTextEncode`、`ModelPatchLoader`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、LoadImage、UNETLoader

## 参数体检

发现 2 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

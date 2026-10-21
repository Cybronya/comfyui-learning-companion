---
key: 图片生成/文生图/z-image CN2.0+自动遮罩重绘_2073291532668596225.json
name: z-image CN2.0+自动遮罩重绘_2073291532668596225
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/z-image CN2.0+自动遮罩重绘_2073291532668596225.json
hash: ec70058384348aa9
coverage: 0.807692
learned_at: 2026-10-20 00:02:08
nodes: [MaskToImage, PreviewImage, SaveImage, ConditioningZeroOut, VAEDecode, LoadSAM3Model, SetLatentNoiseMask, PreviewImage, ModelPatchLoader, QwenImageDiffsynthControlnet, UNETLoader, Note, InpaintModelConditioning, ModelSamplingAuraFlow, easy cleanGpuUsed, PreviewImage, ImageScaleToTotalPixels, KSampler, VAELoader, Image Comparer (rgthree), GrowMaskWithBlur, CLIPLoader, AIO_Preprocessor, LoadImage, SAM3Segmentation, CLIPTextEncode]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "sgm_uniform", "seed": 471030859868871, "steps": 9}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/文生图/z-image CN2.0+自动遮罩重绘_2073291532668596225.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/z-image CN2.0+自动遮罩重绘_2073291532668596225.json`

## 结构

**生成流程**：Model → Condition → Control → Sampling → Decode → Process → Output → Other

**节点**（26 个）：
- `MaskToImage`
- `PreviewImage`
- `SaveImage`
- `ConditioningZeroOut`
- `VAEDecode` ★核心
- `LoadSAM3Model`
- `SetLatentNoiseMask`
- `PreviewImage`
- `ModelPatchLoader`
- `QwenImageDiffsynthControlnet`
- `UNETLoader` ★核心
- `Note`
- `InpaintModelConditioning`
- `ModelSamplingAuraFlow`
- `easy cleanGpuUsed`
- `PreviewImage`
- `ImageScaleToTotalPixels`
- `KSampler` ★核心
- `VAELoader`
- `Image Comparer (rgthree)`
- `GrowMaskWithBlur`
- `CLIPLoader`
- `AIO_Preprocessor`
- `LoadImage`
- `SAM3Segmentation`
- `CLIPTextEncode` ★核心

## 关键参数

- `seed` = `471030859868871`
- `steps` = `9`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `sgm_uniform`
- `denoise` = `1`

## 知识

覆盖率 **81%**（21/26）

**有卡**：`MaskToImage`、`SaveImage`、`ConditioningZeroOut`、`VAEDecode`、`LoadSAM3Model`、`SetLatentNoiseMask`、`ModelPatchLoader`、`QwenImageDiffsynthControlnet`、`UNETLoader`、`InpaintModelConditioning`、`ModelSamplingAuraFlow`、`easy cleanGpuUsed`、`ImageScaleToTotalPixels`、`KSampler`、`VAELoader`、`GrowMaskWithBlur`、`CLIPLoader`、`AIO_Preprocessor`、`LoadImage`、`SAM3Segmentation`、`CLIPTextEncode`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、LoadImage、UNETLoader

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

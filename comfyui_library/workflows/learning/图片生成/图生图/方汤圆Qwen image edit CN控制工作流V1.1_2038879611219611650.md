---
key: 图片生成/图生图/方汤圆Qwen image edit CN控制工作流V1.1_2038879611219611650.json
name: 方汤圆Qwen image edit CN控制工作流V1.1_2038879611219611650
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/方汤圆Qwen image edit CN控制工作流V1.1_2038879611219611650.json
hash: b91b35f920831245
coverage: 0.58209
learned_at: 2026-10-23 13:04:04
nodes: [ControlNetLoader, Any Switch (rgthree), CFGNorm, CLIPLoader, ModelSamplingAuraFlow, UNETLoader, UNETLoader, Image Save, SaveImage, PreviewImage, ConditioningZeroOut, VAELoader, VAEEncodeTiled, ConditioningCombine, ConditioningCombine, Any Switch (rgthree), SimpleMathSlider+, DepthAnything_V2, PreviewImage, ConditioningSetTimestepRange, ConditioningSetTimestepRange, ConditioningSetTimestepRange, ConditioningSetTimestepRange, LoraLoaderModelOnly, Reroute, Reroute, Reroute, ImageScaleToTotalPixels, PreviewImage, Image Comparer (rgthree), PreviewImage, JWImageResizeByLongerSide, PreviewImage, VAEDecodeTiled, Image Filter Adjustments, AnyLineArtPreprocessor_aux, TextEncodeQwenImageEditPlus, Image Comparer (rgthree), Reroute, Any Switch (rgthree), PreviewImage, KSampler, ImageBlend, Fast Groups Muter (rgthree), TextEncodeQwenImageEditPlus, Note, Note, LayerUtility: ImageReel, Note, PreviewImage, Fast Groups Muter (rgthree), ImageScaleToTotalPixels, InpaintCropImproved, Fast Groups Muter (rgthree), ImageBlend, PreviewImage, Note, Note, Fast Groups Muter (rgthree), LoadImage, LayerUtility: ImageReel, PreviewImage, LoadImage, DownloadAndLoadDepthAnythingV2Model, LayerUtility: ImageReelComposit, PreviewImage, Image Save]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 663506124759599, "steps": 8}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换]
---

# 图片生成/图生图/方汤圆Qwen image edit CN控制工作流V1.1_2038879611219611650.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/方汤圆Qwen image edit CN控制工作流V1.1_2038879611219611650.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（67 个）：
- `ControlNetLoader`
- `Any Switch (rgthree)`
- `CFGNorm`
- `CLIPLoader`
- `ModelSamplingAuraFlow`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `Image Save`
- `SaveImage`
- `PreviewImage`
- `ConditioningZeroOut`
- `VAELoader`
- `VAEEncodeTiled` ★核心
- `ConditioningCombine`
- `ConditioningCombine`
- `Any Switch (rgthree)`
- `SimpleMathSlider+`
- `DepthAnything_V2`
- `PreviewImage`
- `ConditioningSetTimestepRange`
- `ConditioningSetTimestepRange`
- `ConditioningSetTimestepRange`
- `ConditioningSetTimestepRange`
- `LoraLoaderModelOnly` ★核心
- `Reroute`
- `Reroute`
- `Reroute`
- `ImageScaleToTotalPixels`
- `PreviewImage`
- `Image Comparer (rgthree)`
- `PreviewImage`
- `JWImageResizeByLongerSide`
- `PreviewImage`
- `VAEDecodeTiled` ★核心
- `Image Filter Adjustments`
- `AnyLineArtPreprocessor_aux`
- `TextEncodeQwenImageEditPlus`
- `Image Comparer (rgthree)`
- `Reroute`
- `Any Switch (rgthree)`
- `PreviewImage`
- `KSampler` ★核心
- `ImageBlend`
- `Fast Groups Muter (rgthree)`
- `TextEncodeQwenImageEditPlus`
- `Note`
- `Note`
- `LayerUtility: ImageReel`
- `Note`
- `PreviewImage`
- `Fast Groups Muter (rgthree)`
- `ImageScaleToTotalPixels`
- `InpaintCropImproved`
- `Fast Groups Muter (rgthree)`
- `ImageBlend`
- `PreviewImage`
- `Note`
- `Note`
- `Fast Groups Muter (rgthree)`
- `LoadImage`
- `LayerUtility: ImageReel`
- `PreviewImage`
- `LoadImage`
- `DownloadAndLoadDepthAnythingV2Model`
- `LayerUtility: ImageReelComposit`
- `PreviewImage`
- `Image Save`

## 关键参数

- `seed` = `663506124759599`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **58%**（39/67）

**有卡**：`ControlNetLoader`、`CFGNorm`、`CLIPLoader`、`ModelSamplingAuraFlow`、`UNETLoader`、`Image Save`、`SaveImage`、`ConditioningZeroOut`、`VAELoader`、`VAEEncodeTiled`、`ConditioningCombine`、`SimpleMathSlider+`、`DepthAnything_V2`、`ConditioningSetTimestepRange`、`LoraLoaderModelOnly`、`ImageScaleToTotalPixels`、`JWImageResizeByLongerSide`、`VAEDecodeTiled`、`Image Filter Adjustments`、`AnyLineArtPreprocessor_aux`、`TextEncodeQwenImageEditPlus`、`KSampler`、`ImageBlend`、`LayerUtility: ImageReel`、`InpaintCropImproved`、`LoadImage`、`DownloadAndLoadDepthAnythingV2Model`、`LayerUtility: ImageReelComposit`

**用到的条目**：KSampler、VAELoader、LoraLoaderModelOnly、CLIPLoader、ConditioningZeroOut、LoadImage、UNETLoader、ControlNetLoader

## 参数体检

发现 2 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换

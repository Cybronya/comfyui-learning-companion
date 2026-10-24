---
key: 图片生成/图生图/Qwen-Eidt-2511+SeedVR2.5零偏移遮罩精细化改图局部重绘图像编辑自用_2013925887216984065.json
name: Qwen-Eidt-2511+SeedVR2.5零偏移遮罩精细化改图局部重绘图像编辑自用_2013925887216984065
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen-Eidt-2511+SeedVR2.5零偏移遮罩精细化改图局部重绘图像编辑自用_2013925887216984065.json
hash: 419e08e86917e8f1
coverage: 0.846154
learned_at: 2026-10-23 11:16:15
nodes: [VAELoader, CLIPLoader, LoraLoaderModelOnly, TextEncodeQwenImageEditPlusCustom_lrzjason, InpaintCrop, ConditioningZeroOut, FluxKontextMultiReferenceLatentMethod, FluxKontextMultiReferenceLatentMethod, ImageAndMaskPreview, QwenEditConfigPreparer, KSampler, VAEDecode, LayerUtility: PurgeVRAM V2, UNETLoader, InpaintStitch, Image Comparer (rgthree), CropWithPadInfo, QwenEditOutputExtractor, LoadImage, SaveImage, SeedVR2LoadVAEModel, SeedVR2LoadDiTModel, PrimitiveStringMultiline, MarkdownNote, Fast Groups Bypasser (rgthree), SeedVR2VideoUpscaler]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 692144270173329, "steps": 8}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/Qwen-Eidt-2511+SeedVR2.5零偏移遮罩精细化改图局部重绘图像编辑自用_2013925887216984065.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen-Eidt-2511+SeedVR2.5零偏移遮罩精细化改图局部重绘图像编辑自用_2013925887216984065.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（26 个）：
- `VAELoader`
- `CLIPLoader`
- `LoraLoaderModelOnly` ★核心
- `TextEncodeQwenImageEditPlusCustom_lrzjason`
- `InpaintCrop`
- `ConditioningZeroOut`
- `FluxKontextMultiReferenceLatentMethod`
- `FluxKontextMultiReferenceLatentMethod`
- `ImageAndMaskPreview`
- `QwenEditConfigPreparer`
- `KSampler` ★核心
- `VAEDecode` ★核心
- `LayerUtility: PurgeVRAM V2`
- `UNETLoader` ★核心
- `InpaintStitch`
- `Image Comparer (rgthree)`
- `CropWithPadInfo`
- `QwenEditOutputExtractor`
- `LoadImage`
- `SaveImage`
- `SeedVR2LoadVAEModel`
- `SeedVR2LoadDiTModel`
- `PrimitiveStringMultiline`
- `MarkdownNote`
- `Fast Groups Bypasser (rgthree)`
- `SeedVR2VideoUpscaler`

## 关键参数

- `seed` = `692144270173329`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **85%**（22/26）

**有卡**：`VAELoader`、`CLIPLoader`、`LoraLoaderModelOnly`、`TextEncodeQwenImageEditPlusCustom_lrzjason`、`InpaintCrop`、`ConditioningZeroOut`、`FluxKontextMultiReferenceLatentMethod`、`ImageAndMaskPreview`、`QwenEditConfigPreparer`、`KSampler`、`VAEDecode`、`LayerUtility: PurgeVRAM V2`、`UNETLoader`、`InpaintStitch`、`CropWithPadInfo`、`QwenEditOutputExtractor`、`LoadImage`、`SaveImage`、`SeedVR2LoadVAEModel`、`SeedVR2LoadDiTModel`、`SeedVR2VideoUpscaler`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPLoader、ConditioningZeroOut、SaveImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

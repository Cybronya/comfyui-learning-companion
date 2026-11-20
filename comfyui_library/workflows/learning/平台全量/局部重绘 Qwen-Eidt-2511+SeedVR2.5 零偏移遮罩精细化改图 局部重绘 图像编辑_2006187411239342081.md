---
key: 平台全量/局部重绘 Qwen-Eidt-2511+SeedVR2.5 零偏移遮罩精细化改图 局部重绘 图像编辑_2006187411239342081.json
name: 局部重绘 Qwen-Eidt-2511+SeedVR2.5 零偏移遮罩精细化改图 局部重绘 图像编辑_2006187411239342081
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/局部重绘 Qwen-Eidt-2511+SeedVR2.5 零偏移遮罩精细化改图 局部重绘 图像编辑_2006187411239342081.json
hash: e64591d1c11334e9
coverage: 0.888889
learned_at: 2026-11-14 02:01:47
nodes: [VAELoader, CLIPLoader, LoraLoaderModelOnly, TextEncodeQwenImageEditPlusCustom_lrzjason, InpaintCrop, ConditioningZeroOut, FluxKontextMultiReferenceLatentMethod, FluxKontextMultiReferenceLatentMethod, QwenEditConfigPreparer, KSampler, VAEDecode, LayerUtility: PurgeVRAM V2, InpaintStitch, Image Comparer (rgthree), CropWithPadInfo, QwenEditOutputExtractor, UNETLoader, ImageAndMaskPreview, SeedVR2LoadDiTModel, SeedVR2VideoUpscaler, SeedVR2LoadVAEModel, LoadImage, LoadImage, LoadImage, PrimitiveStringMultiline, Fast Groups Bypasser (rgthree), SaveImage]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 251070798243381, "steps": 8}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 平台全量/局部重绘 Qwen-Eidt-2511+SeedVR2.5 零偏移遮罩精细化改图 局部重绘 图像编辑_2006187411239342081.json

> 来源文件 `comfyui_library/workflows/平台全量/局部重绘 Qwen-Eidt-2511+SeedVR2.5 零偏移遮罩精细化改图 局部重绘 图像编辑_2006187411239342081.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（27 个）：
- `VAELoader`
- `CLIPLoader`
- `LoraLoaderModelOnly` ★核心
- `TextEncodeQwenImageEditPlusCustom_lrzjason`
- `InpaintCrop`
- `ConditioningZeroOut`
- `FluxKontextMultiReferenceLatentMethod`
- `FluxKontextMultiReferenceLatentMethod`
- `QwenEditConfigPreparer`
- `KSampler` ★核心
- `VAEDecode` ★核心
- `LayerUtility: PurgeVRAM V2`
- `InpaintStitch`
- `Image Comparer (rgthree)`
- `CropWithPadInfo`
- `QwenEditOutputExtractor`
- `UNETLoader` ★核心
- `ImageAndMaskPreview`
- `SeedVR2LoadDiTModel`
- `SeedVR2VideoUpscaler`
- `SeedVR2LoadVAEModel`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `PrimitiveStringMultiline`
- `Fast Groups Bypasser (rgthree)`
- `SaveImage`

## 关键参数

- `seed` = `251070798243381`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **89%**（24/27）

**有卡**：`VAELoader`、`CLIPLoader`、`LoraLoaderModelOnly`、`TextEncodeQwenImageEditPlusCustom_lrzjason`、`InpaintCrop`、`ConditioningZeroOut`、`FluxKontextMultiReferenceLatentMethod`、`QwenEditConfigPreparer`、`KSampler`、`VAEDecode`、`LayerUtility: PurgeVRAM V2`、`InpaintStitch`、`CropWithPadInfo`、`QwenEditOutputExtractor`、`UNETLoader`、`ImageAndMaskPreview`、`SeedVR2LoadDiTModel`、`SeedVR2VideoUpscaler`、`SeedVR2LoadVAEModel`、`LoadImage`、`SaveImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPLoader、ConditioningZeroOut、SaveImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

---
key: 图片生成/图生图/全能图片V1指哪打哪万物融图+Wan2.2洗图（手动编辑）_1966034816619679745.json
name: 全能图片V1指哪打哪万物融图+Wan2.2洗图（手动编辑）_1966034816619679745
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/全能图片V1指哪打哪万物融图+Wan2.2洗图（手动编辑）_1966034816619679745.json
hash: ca28373bd9d45d84
coverage: 0.791667
learned_at: 2026-10-23 12:18:23
nodes: [UNETLoader, CLIPTextEncode, VAEEncode, LoraLoaderModelOnly, VAELoader, RandomNoise, SplitSigmas, SamplerCustomAdvanced, DisableNoise, SamplerCustomAdvanced, ModelSamplingSD3, KSamplerSelect, CLIPTextEncode, RH_Captioner, WanVideoNAG, CFGGuider, CLIPLoader, Image Comparer (rgthree), easy cleanGpuUsed, DeepTranslatorTextNode, FastCanvasTool, preview_mask, PreviewImage, ShowText|pysssss, LayerMask: LoadSegmentAnythingModels, LoadImage, LayerMask: SegmentAnythingUltra V3, Image Comparer (rgthree), Image Comparer (rgthree), SaveImage, FastCanvas, PreviewImage, LayerUtility: ImageScaleByAspectRatio V2, InpaintCrop, RH_Nano_Banana_Image2Image, DF_Get_image_size, ImageResizeKJv2, InpaintStitch, Image Comparer (rgthree), PreviewImage, Image Comparer (rgthree), Text, GrowMaskWithBlur, BasicScheduler, LoadImage, SeedVR2, VAEDecode, PreviewImage]
patterns: []
missing: []
---

# 图片生成/图生图/全能图片V1指哪打哪万物融图+Wan2.2洗图（手动编辑）_1966034816619679745.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/全能图片V1指哪打哪万物融图+Wan2.2洗图（手动编辑）_1966034816619679745.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（48 个）：
- `UNETLoader` ★核心
- `CLIPTextEncode` ★核心
- `VAEEncode` ★核心
- `LoraLoaderModelOnly` ★核心
- `VAELoader`
- `RandomNoise`
- `SplitSigmas`
- `SamplerCustomAdvanced` ★核心
- `DisableNoise`
- `SamplerCustomAdvanced` ★核心
- `ModelSamplingSD3`
- `KSamplerSelect` ★核心
- `CLIPTextEncode` ★核心
- `RH_Captioner`
- `WanVideoNAG`
- `CFGGuider`
- `CLIPLoader`
- `Image Comparer (rgthree)`
- `easy cleanGpuUsed`
- `DeepTranslatorTextNode`
- `FastCanvasTool`
- `preview_mask`
- `PreviewImage`
- `ShowText|pysssss`
- `LayerMask: LoadSegmentAnythingModels`
- `LoadImage`
- `LayerMask: SegmentAnythingUltra V3`
- `Image Comparer (rgthree)`
- `Image Comparer (rgthree)`
- `SaveImage`
- `FastCanvas`
- `PreviewImage`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `InpaintCrop`
- `RH_Nano_Banana_Image2Image`
- `DF_Get_image_size`
- `ImageResizeKJv2`
- `InpaintStitch`
- `Image Comparer (rgthree)`
- `PreviewImage`
- `Image Comparer (rgthree)`
- `Text`
- `GrowMaskWithBlur`
- `BasicScheduler`
- `LoadImage`
- `SeedVR2`
- `VAEDecode` ★核心
- `PreviewImage`

## 知识

覆盖率 **79%**（38/48）

**有卡**：`UNETLoader`、`CLIPTextEncode`、`VAEEncode`、`LoraLoaderModelOnly`、`VAELoader`、`RandomNoise`、`SplitSigmas`、`SamplerCustomAdvanced`、`DisableNoise`、`ModelSamplingSD3`、`KSamplerSelect`、`RH_Captioner`、`WanVideoNAG`、`CFGGuider`、`CLIPLoader`、`easy cleanGpuUsed`、`DeepTranslatorTextNode`、`FastCanvasTool`、`preview_mask`、`LayerMask: LoadSegmentAnythingModels`、`LoadImage`、`LayerMask: SegmentAnythingUltra V3`、`SaveImage`、`FastCanvas`、`LayerUtility: ImageScaleByAspectRatio V2`、`InpaintCrop`、`RH_Nano_Banana_Image2Image`、`DF_Get_image_size`、`ImageResizeKJv2`、`InpaintStitch`、`Text`、`GrowMaskWithBlur`、`BasicScheduler`、`SeedVR2`、`VAEDecode`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、LayerUtility: ImageScaleByAspectRatio V2

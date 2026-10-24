---
key: 图片生成/图生图/Qwen-image2.1-终极局部重绘（完美解决接缝色差）_2104548066190774274.json
name: Qwen-image2.1-终极局部重绘（完美解决接缝色差）_2104548066190774274
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen-image2.1-终极局部重绘（完美解决接缝色差）_2104548066190774274.json
hash: 60047b999add28c3
coverage: 0.842105
learned_at: 2026-10-23 11:18:27
nodes: [Mask Fill Holes, LayerUtility: ImageScaleByAspectRatio V2, KSamplerSelect, SamplerCustom, InpaintModelConditioning, ManualSigmas, VAEDecode, InpaintCropImproved, PreviewImage, UNETLoader, CLIPLoader, VAELoader, PreviewImage, ColorMatchV2, Image Comparer (rgthree), InpaintStitchImproved, SaveImage, LoadImage, TextEncodeQwenImage21]
patterns: []
missing: []
---

# 图片生成/图生图/Qwen-image2.1-终极局部重绘（完美解决接缝色差）_2104548066190774274.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen-image2.1-终极局部重绘（完美解决接缝色差）_2104548066190774274.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（19 个）：
- `Mask Fill Holes`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `KSamplerSelect` ★核心
- `SamplerCustom` ★核心
- `InpaintModelConditioning`
- `ManualSigmas`
- `VAEDecode` ★核心
- `InpaintCropImproved`
- `PreviewImage`
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `PreviewImage`
- `ColorMatchV2`
- `Image Comparer (rgthree)`
- `InpaintStitchImproved`
- `SaveImage`
- `LoadImage`
- `TextEncodeQwenImage21`

## 知识

覆盖率 **84%**（16/19）

**有卡**：`Mask Fill Holes`、`LayerUtility: ImageScaleByAspectRatio V2`、`KSamplerSelect`、`SamplerCustom`、`InpaintModelConditioning`、`ManualSigmas`、`VAEDecode`、`InpaintCropImproved`、`UNETLoader`、`CLIPLoader`、`VAELoader`、`ColorMatchV2`、`InpaintStitchImproved`、`SaveImage`、`LoadImage`、`TextEncodeQwenImage21`

**用到的条目**：VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、LoadImage、UNETLoader、KSamplerSelect、SamplerCustom

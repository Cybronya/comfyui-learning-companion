---
key: 图片生成/图生图/Qwen-image2.1-万能局部重绘（低像素重绘）_2108895200159559681.json
name: Qwen-image2.1-万能局部重绘（低像素重绘）_2108895200159559681
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen-image2.1-万能局部重绘（低像素重绘）_2108895200159559681.json
hash: 8f993d60c18f7730
coverage: 0.888889
learned_at: 2026-10-23 11:18:24
nodes: [UNETLoader, CLIPLoader, VAELoader, Mask Fill Holes, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LayerUtility: CropByMask V2, LayerUtility: ImageScaleRestore V2, ImageScale, PreviewImage, TextEncodeQwenImage21, InpaintModelConditioning, KSampler, VAEDecode, GetImageSize, LayerUtility: RestoreCropBox, SaveImage, Image Comparer (rgthree)]
patterns: []
missing: []
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 547617555386385, "steps": 25}
---

# 图片生成/图生图/Qwen-image2.1-万能局部重绘（低像素重绘）_2108895200159559681.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen-image2.1-万能局部重绘（低像素重绘）_2108895200159559681.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（18 个）：
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `Mask Fill Holes`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LayerUtility: CropByMask V2`
- `LayerUtility: ImageScaleRestore V2`
- `ImageScale`
- `PreviewImage`
- `TextEncodeQwenImage21`
- `InpaintModelConditioning`
- `KSampler` ★核心
- `VAEDecode` ★核心
- `GetImageSize`
- `LayerUtility: RestoreCropBox`
- `SaveImage`
- `Image Comparer (rgthree)`

## 关键参数

- `seed` = `547617555386385`
- `steps` = `25`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **89%**（16/18）

**有卡**：`UNETLoader`、`CLIPLoader`、`VAELoader`、`Mask Fill Holes`、`LayerUtility: ImageScaleByAspectRatio V2`、`LoadImage`、`LayerUtility: CropByMask V2`、`LayerUtility: ImageScaleRestore V2`、`ImageScale`、`TextEncodeQwenImage21`、`InpaintModelConditioning`、`KSampler`、`VAEDecode`、`GetImageSize`、`LayerUtility: RestoreCropBox`、`SaveImage`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、LoadImage、UNETLoader、InpaintModelConditioning

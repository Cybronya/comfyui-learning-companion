---
key: 视频生成/文生视频/Qwen-Image-2.1｜商品_主体任意溶图｜40步质量 + Viggle加速双路线_2107775767450046466.json
name: Qwen-Image-2.1｜商品_主体任意溶图｜40步质量 + Viggle加速双路线_2107775767450046466
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/Qwen-Image-2.1｜商品_主体任意溶图｜40步质量 + Viggle加速双路线_2107775767450046466.json
hash: 567b24ad7e67a241
coverage: 0.875
learned_at: 2026-10-10 23:04:56
nodes: [ImageCropper, VAELoader, CLIPLoader, KSamplerAdvanced, TTP_Expand_And_Mask, Image Rembg (Remove Background), TextEncodeQwenImage21, UNETLoader, UpscaleModelLoader, ImageUpscaleWithModel, ImageScaleToTotalPixels, FastCanvasTool, LoadImage, LoadImage, FastCanvas, PreviewImage, LoraLoaderModelOnly, KSamplerAdvanced, LoraLoaderModelOnly, FluxGuidance, KSamplerAdvanced, CR Prompt Text, UNETLoader, LoraLoaderModelOnly, SaveImageAdvanced, LoadImage, SaveImageAdvanced, VAEDecode, VAEDecode, SaveImage, Image Comparer (rgthree), SaveImage]
patterns: []
missing: [Image Rembg (Remove Background), CR Prompt Text]
parameters: {"cfg": 26, "denoise": "simple", "sampler_name": 1, "scheduler": "euler", "seed": "enable", "steps": "fixed"}
discoveries: [次要节点 `Image Rembg (Remove Background)` 知识库中没有该节点类型的任何知识, 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明]
---

# 视频生成/文生视频/Qwen-Image-2.1｜商品_主体任意溶图｜40步质量 + Viggle加速双路线_2107775767450046466.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/Qwen-Image-2.1｜商品_主体任意溶图｜40步质量 + Viggle加速双路线_2107775767450046466.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（32 个）：
- `ImageCropper`
- `VAELoader`
- `CLIPLoader`
- `KSamplerAdvanced` ★核心
- `TTP_Expand_And_Mask`
- `Image Rembg (Remove Background)`
- `TextEncodeQwenImage21`
- `UNETLoader` ★核心
- `UpscaleModelLoader`
- `ImageUpscaleWithModel`
- `ImageScaleToTotalPixels`
- `FastCanvasTool`
- `LoadImage`
- `LoadImage`
- `FastCanvas`
- `PreviewImage`
- `LoraLoaderModelOnly` ★核心
- `KSamplerAdvanced` ★核心
- `LoraLoaderModelOnly` ★核心
- `FluxGuidance`
- `KSamplerAdvanced` ★核心
- `CR Prompt Text`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `SaveImageAdvanced`
- `LoadImage`
- `SaveImageAdvanced`
- `VAEDecode` ★核心
- `VAEDecode` ★核心
- `SaveImage`
- `Image Comparer (rgthree)`
- `SaveImage`

## 关键参数

- `seed` = `enable`
- `steps` = `fixed`
- `cfg` = `26`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `simple`

## 知识

覆盖率 **88%**（28/32）

**有卡**：`ImageCropper`、`VAELoader`、`CLIPLoader`、`KSamplerAdvanced`、`TTP_Expand_And_Mask`、`TextEncodeQwenImage21`、`UNETLoader`、`UpscaleModelLoader`、`ImageUpscaleWithModel`、`ImageScaleToTotalPixels`、`FastCanvasTool`、`LoadImage`、`FastCanvas`、`LoraLoaderModelOnly`、`FluxGuidance`、`SaveImageAdvanced`、`VAEDecode`、`SaveImage`

**缺卡**（2）：`Image Rembg (Remove Background)`、`CR Prompt Text`

**用到的条目**：VAEDecode、TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPLoader、LoadImage、FluxGuidance

## 学习发现

- 次要节点 `Image Rembg (Remove Background)` 知识库中没有该节点类型的任何知识
- 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明

---
key: 视频生成/文生视频/Qwen Image 2.1商品主体任意溶图40步质量加Viggle加速双路线工作流，图生视频_2108276276401360897.json
name: Qwen Image 2.1商品主体任意溶图40步质量加Viggle加速双路线工作流，图生视频_2108276276401360897
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/Qwen Image 2.1商品主体任意溶图40步质量加Viggle加速双路线工作流，图生视频_2108276276401360897.json
hash: db55e2654a101243
coverage: 0.868852
learned_at: 2026-10-10 00:07:22
nodes: [ImageCropper, VAELoader, CLIPLoader, KSamplerAdvanced, TTP_Expand_And_Mask, Image Rembg (Remove Background), TextEncodeQwenImage21, UNETLoader, UpscaleModelLoader, ImageUpscaleWithModel, ImageScaleToTotalPixels, FastCanvasTool, LoadImage, LoadImage, FastCanvas, PreviewImage, LoraLoaderModelOnly, KSamplerAdvanced, LoraLoaderModelOnly, FluxGuidance, KSamplerAdvanced, CR Prompt Text, UNETLoader, LoraLoaderModelOnly, SaveImageAdvanced, LoadImage, SaveImageAdvanced, VAEDecode, VAEDecode, SaveImage, Image Comparer (rgthree), SaveImage, 孤海注释, 孤海注释, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, KSampler, EmptyLatentImage, JjkText, CLIPTextEncode, CLIPTextEncode, solarL_SaveImagesToZip, VAEDecode, CLIPLoader, VAELoader, Note]
patterns: [text_to_image]
missing: [Image Rembg (Remove Background), CR Prompt Text]
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [次要节点 `Image Rembg (Remove Background)` 知识库中没有该节点类型的任何知识, 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/文生视频/Qwen Image 2.1商品主体任意溶图40步质量加Viggle加速双路线工作流，图生视频_2108276276401360897.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/Qwen Image 2.1商品主体任意溶图40步质量加Viggle加速双路线工作流，图生视频_2108276276401360897.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（61 个）：
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
- `孤海注释`
- `孤海注释`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `KSampler` ★核心
- `EmptyLatentImage` ★核心
- `JjkText`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `solarL_SaveImagesToZip`
- `VAEDecode` ★核心
- `CLIPLoader`
- `VAELoader`
- `Note`

**识别到的模式**：text_to_image

## 关键参数

- `seed` = `598626327129635`
- `steps` = `4`
- `cfg` = `4.5`
- `sampler_name` = `er_sde`
- `scheduler` = `beta`
- `denoise` = `1`
- `width` = `80`
- `height` = `80`
- `batch_size` = `1`

## 知识

覆盖率 **87%**（53/61）

**有卡**：`ImageCropper`、`VAELoader`、`CLIPLoader`、`KSamplerAdvanced`、`TTP_Expand_And_Mask`、`TextEncodeQwenImage21`、`UNETLoader`、`UpscaleModelLoader`、`ImageUpscaleWithModel`、`ImageScaleToTotalPixels`、`FastCanvasTool`、`LoadImage`、`FastCanvas`、`LoraLoaderModelOnly`、`FluxGuidance`、`SaveImageAdvanced`、`VAEDecode`、`SaveImage`、`KSampler`、`EmptyLatentImage`、`CLIPTextEncode`、`solarL_SaveImagesToZip`

**缺卡**（2）：`Image Rembg (Remove Background)`、`CR Prompt Text`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPTextEncode、CLIPLoader

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- 次要节点 `Image Rembg (Remove Background)` 知识库中没有该节点类型的任何知识
- 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

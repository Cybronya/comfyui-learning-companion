---
key: 图片生成/图生图/Qwen Image 2.1洗图反推提示词，图生图图像分析与提示词提取工具_2103236925317537793.json
name: Qwen Image 2.1洗图反推提示词，图生图图像分析与提示词提取工具_2103236925317537793
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen Image 2.1洗图反推提示词，图生图图像分析与提示词提取工具_2103236925317537793.json
hash: 5079d9e1bb8b7fbd
coverage: 0.820896
learned_at: 2026-10-21 00:42:41
nodes: [easy imageSize, ImageResize+, easy imageSize, TTP_Image_Tile_Batch, TTP_Tile_image_size, SeedVR2VideoUpscaler, ImageScaleBy, ImageResize+, SeedVR2LoadVAEModel, SaveImage, Image Comparer (rgthree), CLIPLoader, VAELoader, LineArtPreprocessor, SetNode, GetNode, SeedVR2LoadDiTModel, EmptyLatentImage, ResolutionSelector, DepthAnythingV2Preprocessor, VAEDecode, UNETLoader, TextEncodeQwenImage21, DWPreprocessor, ComfySwitchNode, KSampler, QwenImage21Cache, ImageScaleBy, TTP_Image_Assy, ComfySwitchNode, Fast Groups Bypasser (rgthree), LoadImage, PreviewImage, ComfySwitchNode, LayerUtility: ImageReel, LayerUtility: ImageReelComposit, SaveImage, SaveImage, 孤海注释, 孤海注释, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, KSampler, EmptyLatentImage, JjkText, CLIPTextEncode, CLIPTextEncode, solarL_SaveImagesToZip, VAEDecode, CLIPLoader, VAELoader, Note]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/Qwen Image 2.1洗图反推提示词，图生图图像分析与提示词提取工具_2103236925317537793.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen Image 2.1洗图反推提示词，图生图图像分析与提示词提取工具_2103236925317537793.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（67 个）：
- `easy imageSize`
- `ImageResize+`
- `easy imageSize`
- `TTP_Image_Tile_Batch`
- `TTP_Tile_image_size`
- `SeedVR2VideoUpscaler`
- `ImageScaleBy`
- `ImageResize+`
- `SeedVR2LoadVAEModel`
- `SaveImage`
- `Image Comparer (rgthree)`
- `CLIPLoader`
- `VAELoader`
- `LineArtPreprocessor`
- `SetNode`
- `GetNode`
- `SeedVR2LoadDiTModel`
- `EmptyLatentImage` ★核心
- `ResolutionSelector`
- `DepthAnythingV2Preprocessor`
- `VAEDecode` ★核心
- `UNETLoader` ★核心
- `TextEncodeQwenImage21`
- `DWPreprocessor`
- `ComfySwitchNode`
- `KSampler` ★核心
- `QwenImage21Cache`
- `ImageScaleBy`
- `TTP_Image_Assy`
- `ComfySwitchNode`
- `Fast Groups Bypasser (rgthree)`
- `LoadImage`
- `PreviewImage`
- `ComfySwitchNode`
- `LayerUtility: ImageReel`
- `LayerUtility: ImageReelComposit`
- `SaveImage`
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

- `width` = `80`
- `height` = `80`
- `batch_size` = `1`
- `seed` = `598626327129635`
- `steps` = `4`
- `cfg` = `4.5`
- `sampler_name` = `er_sde`
- `scheduler` = `beta`
- `denoise` = `1`

## 知识

覆盖率 **82%**（55/67）

**有卡**：`easy imageSize`、`ImageResize+`、`TTP_Image_Tile_Batch`、`TTP_Tile_image_size`、`SeedVR2VideoUpscaler`、`ImageScaleBy`、`SeedVR2LoadVAEModel`、`SaveImage`、`CLIPLoader`、`VAELoader`、`LineArtPreprocessor`、`SeedVR2LoadDiTModel`、`EmptyLatentImage`、`ResolutionSelector`、`DepthAnythingV2Preprocessor`、`VAEDecode`、`UNETLoader`、`TextEncodeQwenImage21`、`DWPreprocessor`、`KSampler`、`QwenImage21Cache`、`TTP_Image_Assy`、`LoadImage`、`LayerUtility: ImageReel`、`LayerUtility: ImageReelComposit`、`LoraLoaderModelOnly`、`CLIPTextEncode`、`solarL_SaveImagesToZip`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

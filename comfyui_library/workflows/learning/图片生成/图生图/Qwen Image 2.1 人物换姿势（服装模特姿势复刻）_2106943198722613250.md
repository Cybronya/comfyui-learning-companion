---
key: 图片生成/图生图/Qwen Image 2.1 人物换姿势（服装模特姿势复刻）_2106943198722613250.json
name: Qwen Image 2.1 人物换姿势（服装模特姿势复刻）_2106943198722613250
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen Image 2.1 人物换姿势（服装模特姿势复刻）_2106943198722613250.json
hash: a6afde2a15eabe92
coverage: 0.7
learned_at: 2026-10-21 00:42:09
nodes: [LayerUtility: ImageReel, LayerUtility: ImageReelComposit, SetNode, UNETLoader, QwenImage21Cache, CLIPLoader, CLIPLoader, CLIPLoader, VAELoader, PreviewImage, SaveImage, Anything Everywhere3, SetNode, LoadImage, LoadImage, CR Prompt Text, ResolutionSelector, BatchImagesNode, GetNode, TextGenerateLTX2Prompt, TextEncodeQwenImage21, PreviewAny, EmptyLatentImage, ComfySwitchNode, VAEDecode, LoraLoaderModelOnly, KSampler, SetNode, Fast Groups Bypasser (rgthree), easy imageSize, TTP_Image_Tile_Batch, SeedVR2LoadVAEModel, LayerUtility: PurgeVRAM, SeedVR2VideoUpscaler, PreviewImage, ImageResize+, ImageScaleBy, SeedVR2LoadDiTModel, ImageResize+, PreviewImage, easy imageSize, easy imageSize, ImageScaleBy, MarkdownNote, Image Comparer (rgthree), TTP_Image_Assy, Image Comparer (rgthree), GetNode, TTP_Tile_image_size, SaveImage]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 1042136426256720, "steps": 35, "width": 1024}
---

# 图片生成/图生图/Qwen Image 2.1 人物换姿势（服装模特姿势复刻）_2106943198722613250.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen Image 2.1 人物换姿势（服装模特姿势复刻）_2106943198722613250.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（50 个）：
- `LayerUtility: ImageReel`
- `LayerUtility: ImageReelComposit`
- `SetNode`
- `UNETLoader` ★核心
- `QwenImage21Cache`
- `CLIPLoader`
- `CLIPLoader`
- `CLIPLoader`
- `VAELoader`
- `PreviewImage`
- `SaveImage`
- `Anything Everywhere3`
- `SetNode`
- `LoadImage`
- `LoadImage`
- `CR Prompt Text`
- `ResolutionSelector`
- `BatchImagesNode`
- `GetNode`
- `TextGenerateLTX2Prompt`
- `TextEncodeQwenImage21`
- `PreviewAny`
- `EmptyLatentImage` ★核心
- `ComfySwitchNode`
- `VAEDecode` ★核心
- `LoraLoaderModelOnly` ★核心
- `KSampler` ★核心
- `SetNode`
- `Fast Groups Bypasser (rgthree)`
- `easy imageSize`
- `TTP_Image_Tile_Batch`
- `SeedVR2LoadVAEModel`
- `LayerUtility: PurgeVRAM`
- `SeedVR2VideoUpscaler`
- `PreviewImage`
- `ImageResize+`
- `ImageScaleBy`
- `SeedVR2LoadDiTModel`
- `ImageResize+`
- `PreviewImage`
- `easy imageSize`
- `easy imageSize`
- `ImageScaleBy`
- `MarkdownNote`
- `Image Comparer (rgthree)`
- `TTP_Image_Assy`
- `Image Comparer (rgthree)`
- `GetNode`
- `TTP_Tile_image_size`
- `SaveImage`

## 关键参数

- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`
- `seed` = `1042136426256720`
- `steps` = `35`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **70%**（35/50）

**有卡**：`LayerUtility: ImageReel`、`LayerUtility: ImageReelComposit`、`UNETLoader`、`QwenImage21Cache`、`CLIPLoader`、`VAELoader`、`SaveImage`、`LoadImage`、`CR Prompt Text`、`ResolutionSelector`、`BatchImagesNode`、`TextGenerateLTX2Prompt`、`TextEncodeQwenImage21`、`EmptyLatentImage`、`VAEDecode`、`LoraLoaderModelOnly`、`KSampler`、`easy imageSize`、`TTP_Image_Tile_Batch`、`SeedVR2LoadVAEModel`、`LayerUtility: PurgeVRAM`、`SeedVR2VideoUpscaler`、`ImageResize+`、`ImageScaleBy`、`SeedVR2LoadDiTModel`、`TTP_Image_Assy`、`TTP_Tile_image_size`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、CLIPLoader、EmptyLatentImage、ResolutionSelector

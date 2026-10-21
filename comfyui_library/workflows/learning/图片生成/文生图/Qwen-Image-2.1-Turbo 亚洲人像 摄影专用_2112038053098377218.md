---
key: 图片生成/文生图/Qwen-Image-2.1-Turbo 亚洲人像 摄影专用_2112038053098377218.json
name: Qwen-Image-2.1-Turbo 亚洲人像 摄影专用_2112038053098377218
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Qwen-Image-2.1-Turbo 亚洲人像 摄影专用_2112038053098377218.json
hash: 4f86d477431292dc
coverage: 0.783784
learned_at: 2026-10-21 02:54:28
nodes: [TextEncodeQwenImage21, ResolutionSelector, EmptyLatentImage, ComfySwitchNode, CLIPLoader, VAELoader, QwenImage21Cache, VAEDecode, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, KSampler, easy imageSize, TTP_Image_Tile_Batch, SeedVR2LoadVAEModel, LayerUtility: PurgeVRAM, SeedVR2VideoUpscaler, PreviewImage, ImageResize+, ImageScaleBy, SeedVR2LoadDiTModel, ImageResize+, PreviewImage, easy imageSize, easy imageSize, ImageScaleBy, MarkdownNote, GetNode, TTP_Tile_image_size, Fast Groups Bypasser (rgthree), SaveImage, Color Grading JK, TTP_Image_Assy, Image Comparer (rgthree), SetNode, SaveImage, CR Prompt Text]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 284354550584363, "steps": 9, "width": 1024}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/文生图/Qwen-Image-2.1-Turbo 亚洲人像 摄影专用_2112038053098377218.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Qwen-Image-2.1-Turbo 亚洲人像 摄影专用_2112038053098377218.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（37 个）：
- `TextEncodeQwenImage21`
- `ResolutionSelector`
- `EmptyLatentImage` ★核心
- `ComfySwitchNode`
- `CLIPLoader`
- `VAELoader`
- `QwenImage21Cache`
- `VAEDecode` ★核心
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `KSampler` ★核心
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
- `GetNode`
- `TTP_Tile_image_size`
- `Fast Groups Bypasser (rgthree)`
- `SaveImage`
- `Color Grading JK`
- `TTP_Image_Assy`
- `Image Comparer (rgthree)`
- `SetNode`
- `SaveImage`
- `CR Prompt Text`

## 关键参数

- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`
- `seed` = `284354550584363`
- `steps` = `9`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **78%**（29/37）

**有卡**：`TextEncodeQwenImage21`、`ResolutionSelector`、`EmptyLatentImage`、`CLIPLoader`、`VAELoader`、`QwenImage21Cache`、`VAEDecode`、`UNETLoader`、`LoraLoaderModelOnly`、`KSampler`、`easy imageSize`、`TTP_Image_Tile_Batch`、`SeedVR2LoadVAEModel`、`LayerUtility: PurgeVRAM`、`SeedVR2VideoUpscaler`、`ImageResize+`、`ImageScaleBy`、`SeedVR2LoadDiTModel`、`TTP_Tile_image_size`、`SaveImage`、`Color Grading JK`、`TTP_Image_Assy`、`CR Prompt Text`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、CLIPLoader、EmptyLatentImage、ResolutionSelector

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

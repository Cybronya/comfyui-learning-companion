---
key: 图片生成/文生图/Qwen-Image-2.1 亚洲人像 _ 摄影胶片_2112163425462865921.json
name: Qwen-Image-2.1 亚洲人像 _ 摄影胶片_2112163425462865921
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Qwen-Image-2.1 亚洲人像 _ 摄影胶片_2112163425462865921.json
hash: a65e2c1c70a97bc8
coverage: 0.777778
learned_at: 2026-10-21 02:54:26
nodes: [EmptyLatentImage, ComfySwitchNode, VAEDecode, TextEncodeQwenImage21, UNETLoader, QwenImage21Cache, KSampler, ResolutionSelector, CLIPLoader, VAELoader, CR Prompt Text, LoraLoaderModelOnly, SaveImage, easy imageSize, TTP_Image_Tile_Batch, SeedVR2LoadVAEModel, LayerUtility: PurgeVRAM, SeedVR2VideoUpscaler, PreviewImage, ImageResize+, ImageScaleBy, SeedVR2LoadDiTModel, ImageResize+, PreviewImage, easy imageSize, easy imageSize, ImageScaleBy, MarkdownNote, TTP_Image_Assy, SaveImage, GetNode, TTP_Tile_image_size, Image Comparer (rgthree), Color Grading JK, SetNode, Fast Groups Bypasser (rgthree)]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 104217411427215, "steps": 7, "width": 1024}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/文生图/Qwen-Image-2.1 亚洲人像 _ 摄影胶片_2112163425462865921.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Qwen-Image-2.1 亚洲人像 _ 摄影胶片_2112163425462865921.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（36 个）：
- `EmptyLatentImage` ★核心
- `ComfySwitchNode`
- `VAEDecode` ★核心
- `TextEncodeQwenImage21`
- `UNETLoader` ★核心
- `QwenImage21Cache`
- `KSampler` ★核心
- `ResolutionSelector`
- `CLIPLoader`
- `VAELoader`
- `CR Prompt Text`
- `LoraLoaderModelOnly` ★核心
- `SaveImage`
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
- `TTP_Image_Assy`
- `SaveImage`
- `GetNode`
- `TTP_Tile_image_size`
- `Image Comparer (rgthree)`
- `Color Grading JK`
- `SetNode`
- `Fast Groups Bypasser (rgthree)`

## 关键参数

- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`
- `seed` = `104217411427215`
- `steps` = `7`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **78%**（28/36）

**有卡**：`EmptyLatentImage`、`VAEDecode`、`TextEncodeQwenImage21`、`UNETLoader`、`QwenImage21Cache`、`KSampler`、`ResolutionSelector`、`CLIPLoader`、`VAELoader`、`CR Prompt Text`、`LoraLoaderModelOnly`、`SaveImage`、`easy imageSize`、`TTP_Image_Tile_Batch`、`SeedVR2LoadVAEModel`、`LayerUtility: PurgeVRAM`、`SeedVR2VideoUpscaler`、`ImageResize+`、`ImageScaleBy`、`SeedVR2LoadDiTModel`、`TTP_Image_Assy`、`TTP_Tile_image_size`、`Color Grading JK`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、CLIPLoader、EmptyLatentImage、ResolutionSelector

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

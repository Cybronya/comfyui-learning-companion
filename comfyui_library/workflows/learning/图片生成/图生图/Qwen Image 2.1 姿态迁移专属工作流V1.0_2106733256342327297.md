---
key: 图片生成/图生图/Qwen Image 2.1 姿态迁移专属工作流V1.0_2106733256342327297.json
name: Qwen Image 2.1 姿态迁移专属工作流V1.0_2106733256342327297
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen Image 2.1 姿态迁移专属工作流V1.0_2106733256342327297.json
hash: b85d88c726da687d
coverage: 0.746667
learned_at: 2026-10-21 00:42:13
nodes: [SetNode, LayerUtility: ImageScaleByAspectRatio V2, SetNode, LayerUtility: ImageScaleByAspectRatio V2, PixaromaGroupSwitch, ResolutionSelector, EmptyLatentImage, GetNode, GetNode, KSampler, CR Prompt Text, ShowText|pysssss, MarkdownNote, VRAM_Debug, TextEncodeQwenImage21, GetNode, PreviewImage, SetNode, easy showAnything, easy showAnything, CM_NumberToInt, GetImageSize, LayerUtility: ImageScaleRestore, easy imageSize, easy imageSize, LayerUtility: ImageScaleByAspectRatio V2, ImageCASharpening+, ttN concat, SetNode, GetNode, SetNode, GetNode, GetNode, ttN concat, PixaromaGroupSwitch, VAEDecode, SaveImage, PixaromaGroupSwitch, GetNode, GetNode, QwenPERewriteT8, LoadImage, DWPreprocessor, UNETLoader, CLIPLoader, VAELoader, LoraLoaderModelOnly, ImageRGBA2RGB, ImageResize+, LayerUtility: NumberCalculatorV2, TTP_Tile_image_size, ImageScaleBy, GetImageSize, CM_NumberBinaryOperation, LayerUtility: NumberCalculatorV2, easy imageSize, ImageCASharpening+, ImageResize+, TTP_Image_Assy, CR Prompt Text, LoadImage, LoadImage, PathchSageAttentionKJ, QwenImage21Cache, ModelAttentionBackend, TTP_Image_Tile_Batch, SaveImage, SeedVR2VideoUpscaler, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, LoadImage, PixaromaLabel, PixaromaLabel, MarkdownNote, CR Prompt Text]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 376345615583396, "steps": 40, "width": 1024}
---

# 图片生成/图生图/Qwen Image 2.1 姿态迁移专属工作流V1.0_2106733256342327297.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen Image 2.1 姿态迁移专属工作流V1.0_2106733256342327297.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（75 个）：
- `SetNode`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `SetNode`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `PixaromaGroupSwitch`
- `ResolutionSelector`
- `EmptyLatentImage` ★核心
- `GetNode`
- `GetNode`
- `KSampler` ★核心
- `CR Prompt Text`
- `ShowText|pysssss`
- `MarkdownNote`
- `VRAM_Debug`
- `TextEncodeQwenImage21`
- `GetNode`
- `PreviewImage`
- `SetNode`
- `easy showAnything`
- `easy showAnything`
- `CM_NumberToInt`
- `GetImageSize`
- `LayerUtility: ImageScaleRestore`
- `easy imageSize`
- `easy imageSize`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `ImageCASharpening+`
- `ttN concat`
- `SetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `ttN concat`
- `PixaromaGroupSwitch`
- `VAEDecode` ★核心
- `SaveImage`
- `PixaromaGroupSwitch`
- `GetNode`
- `GetNode`
- `QwenPERewriteT8`
- `LoadImage`
- `DWPreprocessor`
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `LoraLoaderModelOnly` ★核心
- `ImageRGBA2RGB`
- `ImageResize+`
- `LayerUtility: NumberCalculatorV2`
- `TTP_Tile_image_size`
- `ImageScaleBy`
- `GetImageSize`
- `CM_NumberBinaryOperation`
- `LayerUtility: NumberCalculatorV2`
- `easy imageSize`
- `ImageCASharpening+`
- `ImageResize+`
- `TTP_Image_Assy`
- `CR Prompt Text`
- `LoadImage`
- `LoadImage`
- `PathchSageAttentionKJ`
- `QwenImage21Cache`
- `ModelAttentionBackend`
- `TTP_Image_Tile_Batch`
- `SaveImage`
- `SeedVR2VideoUpscaler`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `LoadImage`
- `PixaromaLabel`
- `PixaromaLabel`
- `MarkdownNote`
- `CR Prompt Text`

## 关键参数

- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`
- `seed` = `376345615583396`
- `steps` = `40`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **75%**（56/75）

**有卡**：`LayerUtility: ImageScaleByAspectRatio V2`、`PixaromaGroupSwitch`、`ResolutionSelector`、`EmptyLatentImage`、`KSampler`、`CR Prompt Text`、`VRAM_Debug`、`TextEncodeQwenImage21`、`CM_NumberToInt`、`GetImageSize`、`LayerUtility: ImageScaleRestore`、`easy imageSize`、`ImageCASharpening+`、`ttN concat`、`VAEDecode`、`SaveImage`、`QwenPERewriteT8`、`LoadImage`、`DWPreprocessor`、`UNETLoader`、`CLIPLoader`、`VAELoader`、`LoraLoaderModelOnly`、`ImageRGBA2RGB`、`ImageResize+`、`LayerUtility: NumberCalculatorV2`、`TTP_Tile_image_size`、`ImageScaleBy`、`CM_NumberBinaryOperation`、`TTP_Image_Assy`、`PathchSageAttentionKJ`、`QwenImage21Cache`、`ModelAttentionBackend`、`TTP_Image_Tile_Batch`、`SeedVR2VideoUpscaler`、`SeedVR2LoadDiTModel`、`SeedVR2LoadVAEModel`、`PixaromaLabel`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、CLIPLoader、EmptyLatentImage、ResolutionSelector

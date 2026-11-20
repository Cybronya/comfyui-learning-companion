---
key: 图片生成/图生图/（自动化）MSQcompose_1.2合成工作流_2116567648644452354.json
name: （自动化）MSQcompose_1.2合成工作流_2116567648644452354
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/（自动化）MSQcompose_1.2合成工作流_2116567648644452354.json
hash: 1db16d60f25fbab9
coverage: 0.95
learned_at: 2026-11-02 19:15:08
nodes: [LoadImage, LoadImage, GetImageSize, LayerUtility: ImageScaleByAspectRatio V2, math_calculate, LayerUtility: ImageScaleByAspectRatio V2, GetImageSize, math_calculate, ttN int, NumberComparison, ComfySwitchNode, ComfySwitchNode, NumberComparison, CR Text, RH_DolaSeedream50ProImageToImage, ImageScaleToTotalPixelsX, easy imageSize, TTP_Image_Tile_Batch, easy imageBatchToImageList, ImageScaleToTotalPixels, CLIPTextEncode, ReferenceLatent, VAEEncode, VAELoader_Any, CLIPLoader_Any, UNETLoader_Any, LoraLoaderModelOnly, BasicGuider, KSamplerSelect, BasicScheduler, VAEDecode, SamplerCustomAdvanced, RandomNoise, easy imageListToImageBatch, easy imageColorMatch, TTP_Image_Assy, UpscaleModelLoader, ImageUpscaleWithModel, easy imageColorMatch, SaveImage]
patterns: []
missing: []
---

# 图片生成/图生图/（自动化）MSQcompose_1.2合成工作流_2116567648644452354.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/（自动化）MSQcompose_1.2合成工作流_2116567648644452354.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（40 个）：
- `LoadImage`
- `LoadImage`
- `GetImageSize`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `math_calculate`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `GetImageSize`
- `math_calculate`
- `ttN int`
- `NumberComparison`
- `ComfySwitchNode`
- `ComfySwitchNode`
- `NumberComparison`
- `CR Text`
- `RH_DolaSeedream50ProImageToImage`
- `ImageScaleToTotalPixelsX`
- `easy imageSize`
- `TTP_Image_Tile_Batch`
- `easy imageBatchToImageList`
- `ImageScaleToTotalPixels`
- `CLIPTextEncode` ★核心
- `ReferenceLatent`
- `VAEEncode` ★核心
- `VAELoader_Any`
- `CLIPLoader_Any`
- `UNETLoader_Any` ★核心
- `LoraLoaderModelOnly` ★核心
- `BasicGuider`
- `KSamplerSelect` ★核心
- `BasicScheduler`
- `VAEDecode` ★核心
- `SamplerCustomAdvanced` ★核心
- `RandomNoise`
- `easy imageListToImageBatch`
- `easy imageColorMatch`
- `TTP_Image_Assy`
- `UpscaleModelLoader`
- `ImageUpscaleWithModel`
- `easy imageColorMatch`
- `SaveImage`

## 知识

覆盖率 **95%**（38/40）

**有卡**：`LoadImage`、`GetImageSize`、`LayerUtility: ImageScaleByAspectRatio V2`、`math_calculate`、`ttN int`、`NumberComparison`、`CR Text`、`RH_DolaSeedream50ProImageToImage`、`ImageScaleToTotalPixelsX`、`easy imageSize`、`TTP_Image_Tile_Batch`、`easy imageBatchToImageList`、`ImageScaleToTotalPixels`、`CLIPTextEncode`、`ReferenceLatent`、`VAEEncode`、`VAELoader_Any`、`CLIPLoader_Any`、`UNETLoader_Any`、`LoraLoaderModelOnly`、`BasicGuider`、`KSamplerSelect`、`BasicScheduler`、`VAEDecode`、`SamplerCustomAdvanced`、`RandomNoise`、`easy imageListToImageBatch`、`easy imageColorMatch`、`TTP_Image_Assy`、`UpscaleModelLoader`、`ImageUpscaleWithModel`、`SaveImage`

**用到的条目**：VAEDecode、LoraLoaderModelOnly、CLIPTextEncode、LoadImage、KSamplerSelect、RH_DolaSeedream50ProImageToImage、SamplerCustomAdvanced、ReferenceLatent

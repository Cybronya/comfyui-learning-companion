---
key: 图片生成/图生图/Qwen image2.1洗图工作流_2102617237571067905.json
name: Qwen image2.1洗图工作流_2102617237571067905
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen image2.1洗图工作流_2102617237571067905.json
hash: 5ffa4ccfb296a482
coverage: 0.571429
learned_at: 2026-10-10 20:48:08
nodes: [easy imageSize, ImageResize+, easy imageSize, TTP_Image_Tile_Batch, TTP_Tile_image_size, SeedVR2VideoUpscaler, ImageScaleBy, ImageResize+, SeedVR2LoadVAEModel, SaveImage, Image Comparer (rgthree), CLIPLoader, VAELoader, LineArtPreprocessor, SetNode, GetNode, SeedVR2LoadDiTModel, EmptyLatentImage, ResolutionSelector, DepthAnythingV2Preprocessor, VAEDecode, Label (rgthree), Label (rgthree), UNETLoader, TextEncodeQwenImage21, DWPreprocessor, ComfySwitchNode, KSampler, QwenImage21Cache, ImageScaleBy, TTP_Image_Assy, ComfySwitchNode, Label (rgthree), Fast Groups Bypasser (rgthree), LoadImage, PreviewImage, ComfySwitchNode, LayerUtility: ImageReel, LayerUtility: ImageReelComposit, SaveImage, Note, SaveImage]
patterns: []
missing: [Label (rgthree), Label (rgthree), Label (rgthree), LayerUtility: ImageReel, LayerUtility: ImageReelComposit, ImageResize+, ImageResize+, easy imageSize, easy imageSize]
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 305201027536943, "steps": 36, "width": 1024}
discoveries: [次要节点 `Label (rgthree)` 知识库中没有该节点类型的任何知识, 次要节点 `Label (rgthree)` 知识库中没有该节点类型的任何知识, 次要节点 `Label (rgthree)` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: ImageReel` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: ImageReelComposit` 知识库中没有该节点类型的任何知识, 次要节点 `ImageResize+` 仅有 Resolution 的通用知识，没有该节点自己的说明, 次要节点 `ImageResize+` 仅有 Resolution 的通用知识，没有该节点自己的说明, 次要节点 `easy imageSize` 仅有 Resolution 的通用知识，没有该节点自己的说明, 次要节点 `easy imageSize` 仅有 Resolution 的通用知识，没有该节点自己的说明]
---

# 图片生成/图生图/Qwen image2.1洗图工作流_2102617237571067905.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen image2.1洗图工作流_2102617237571067905.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（42 个）：
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
- `Label (rgthree)`
- `Label (rgthree)`
- `UNETLoader` ★核心
- `TextEncodeQwenImage21`
- `DWPreprocessor`
- `ComfySwitchNode`
- `KSampler` ★核心
- `QwenImage21Cache`
- `ImageScaleBy`
- `TTP_Image_Assy`
- `ComfySwitchNode`
- `Label (rgthree)`
- `Fast Groups Bypasser (rgthree)`
- `LoadImage`
- `PreviewImage`
- `ComfySwitchNode`
- `LayerUtility: ImageReel`
- `LayerUtility: ImageReelComposit`
- `SaveImage`
- `Note`
- `SaveImage`

## 关键参数

- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`
- `seed` = `305201027536943`
- `steps` = `36`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **57%**（24/42）

**有卡**：`TTP_Image_Tile_Batch`、`TTP_Tile_image_size`、`SeedVR2VideoUpscaler`、`ImageScaleBy`、`SeedVR2LoadVAEModel`、`SaveImage`、`CLIPLoader`、`VAELoader`、`LineArtPreprocessor`、`SeedVR2LoadDiTModel`、`EmptyLatentImage`、`ResolutionSelector`、`DepthAnythingV2Preprocessor`、`VAEDecode`、`UNETLoader`、`TextEncodeQwenImage21`、`DWPreprocessor`、`KSampler`、`QwenImage21Cache`、`TTP_Image_Assy`、`LoadImage`

**缺卡**（9）：`Label (rgthree)`、`Label (rgthree)`、`Label (rgthree)`、`LayerUtility: ImageReel`、`LayerUtility: ImageReelComposit`、`ImageResize+`、`ImageResize+`、`easy imageSize`、`easy imageSize`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、EmptyLatentImage、ResolutionSelector、LoadImage

## 学习发现

- 次要节点 `Label (rgthree)` 知识库中没有该节点类型的任何知识
- 次要节点 `Label (rgthree)` 知识库中没有该节点类型的任何知识
- 次要节点 `Label (rgthree)` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: ImageReel` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: ImageReelComposit` 知识库中没有该节点类型的任何知识
- 次要节点 `ImageResize+` 仅有 Resolution 的通用知识，没有该节点自己的说明
- 次要节点 `ImageResize+` 仅有 Resolution 的通用知识，没有该节点自己的说明
- 次要节点 `easy imageSize` 仅有 Resolution 的通用知识，没有该节点自己的说明
- 次要节点 `easy imageSize` 仅有 Resolution 的通用知识，没有该节点自己的说明

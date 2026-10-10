---
key: 图片生成/图生图/Texture Restoration质感修复SeedVR2.5+图像高清修复High_2107279324872265729.json
name: Texture Restoration质感修复SeedVR2.5+图像高清修复High_2107279324872265729
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Texture Restoration质感修复SeedVR2.5+图像高清修复High_2107279324872265729.json
hash: 0b89bacde79dce49
coverage: 0.566667
learned_at: 2026-10-10 20:48:11
nodes: [TTP_Image_Tile_Batch, INTConstant, ImageScaleToTotalPixels, PreviewImage, SeedVR2VideoUpscaler, Image Comparer (rgthree), SeedVR2LoadVAEModel, LoadImage, ImageScale, easy imageListToImageBatch, TTP_Image_Assy, easy imageSize, easy imageSizeBySide, SeedVR2LoadVAEModel, TTP_Tile_image_size, SeedVR2LoadDiTModel, SeedVR2LoadDiTModel, LayerUtility: ImageScaleByAspectRatio V2, PreviewImage, SeedVR2VideoUpscaler, LayerUtility: ImageScaleByAspectRatio V2, Fast Groups Bypasser (rgthree), Image Comparer (rgthree), SaveImage, SaveImage, easy imageBatchToImageList, INTConstant, LoadImage, Note, Note]
patterns: []
missing: [LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: ImageScaleByAspectRatio V2, easy imageBatchToImageList, easy imageListToImageBatch, easy imageSize, easy imageSizeBySide]
discoveries: [次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识, 次要节点 `easy imageBatchToImageList` 知识库中没有该节点类型的任何知识, 次要节点 `easy imageListToImageBatch` 知识库中没有该节点类型的任何知识, 次要节点 `easy imageSize` 仅有 Resolution 的通用知识，没有该节点自己的说明, 次要节点 `easy imageSizeBySide` 仅有 Resolution 的通用知识，没有该节点自己的说明]
---

# 图片生成/图生图/Texture Restoration质感修复SeedVR2.5+图像高清修复High_2107279324872265729.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Texture Restoration质感修复SeedVR2.5+图像高清修复High_2107279324872265729.json`

## 结构

**生成流程**：Process → Output → Other

**节点**（30 个）：
- `TTP_Image_Tile_Batch`
- `INTConstant`
- `ImageScaleToTotalPixels`
- `PreviewImage`
- `SeedVR2VideoUpscaler`
- `Image Comparer (rgthree)`
- `SeedVR2LoadVAEModel`
- `LoadImage`
- `ImageScale`
- `easy imageListToImageBatch`
- `TTP_Image_Assy`
- `easy imageSize`
- `easy imageSizeBySide`
- `SeedVR2LoadVAEModel`
- `TTP_Tile_image_size`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadDiTModel`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `PreviewImage`
- `SeedVR2VideoUpscaler`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `Fast Groups Bypasser (rgthree)`
- `Image Comparer (rgthree)`
- `SaveImage`
- `SaveImage`
- `easy imageBatchToImageList`
- `INTConstant`
- `LoadImage`
- `Note`
- `Note`

## 知识

覆盖率 **57%**（17/30）

**有卡**：`TTP_Image_Tile_Batch`、`INTConstant`、`ImageScaleToTotalPixels`、`SeedVR2VideoUpscaler`、`SeedVR2LoadVAEModel`、`LoadImage`、`ImageScale`、`TTP_Image_Assy`、`TTP_Tile_image_size`、`SeedVR2LoadDiTModel`、`SaveImage`

**缺卡**（6）：`LayerUtility: ImageScaleByAspectRatio V2`、`LayerUtility: ImageScaleByAspectRatio V2`、`easy imageBatchToImageList`、`easy imageListToImageBatch`、`easy imageSize`、`easy imageSizeBySide`

**用到的条目**：LoadImage、SeedVR2LoadDiTModel、SeedVR2LoadVAEModel、SeedVR2VideoUpscaler、TTP_Tile_image_size、SaveImage、ImageScale、ImageScaleToTotalPixels

## 学习发现

- 次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识
- 次要节点 `easy imageBatchToImageList` 知识库中没有该节点类型的任何知识
- 次要节点 `easy imageListToImageBatch` 知识库中没有该节点类型的任何知识
- 次要节点 `easy imageSize` 仅有 Resolution 的通用知识，没有该节点自己的说明
- 次要节点 `easy imageSizeBySide` 仅有 Resolution 的通用知识，没有该节点自己的说明

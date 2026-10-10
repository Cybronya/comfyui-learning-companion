---
key: 视频生成/文生视频/高清修复SeedVR2.5,FlashVSR1.1（4K_8K）_2002479902790152193.json
name: 高清修复SeedVR2.5,FlashVSR1.1（4K_8K）_2002479902790152193
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/高清修复SeedVR2.5,FlashVSR1.1（4K_8K）_2002479902790152193.json
hash: 90c5ec04cbaddcfe
coverage: 0.55
learned_at: 2026-10-11 02:57:41
nodes: [ImageScaleToTotalPixels, SeedVR2VideoUpscaler, PreviewImage, SaveImage, Note, Note, Image Comparer (rgthree), LoadImage, SaveImage, LayerUtility: ImageScaleByAspectRatio V2, Note, Note, LayerUtility: ImageScaleByAspectRatio V2, TTP_Tile_image_size, TTP_Image_Tile_Batch, LayerUtility: ImageScaleByAspectRatio V2, easy imageBatchToImageList, SeedVR2LoadVAEModel, easy imageSize, SeedVR2VideoUpscaler, easy imageListToImageBatch, ImageScale, TTP_Image_Assy, INTConstant, Image Comparer (rgthree), easy imageSizeBySide, SaveImage, SeedVR2LoadDiTModel, LoadImage, Image Comparer (rgthree), Note, INTConstant, INTConstant, INTConstant, FlashVSRNode, Note, LoadImage, Fast Groups Bypasser (rgthree), SeedVR2LoadDiTModel, SeedVR2LoadVAEModel]
patterns: []
missing: [LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: ImageScaleByAspectRatio V2, easy imageBatchToImageList, easy imageListToImageBatch, easy imageSize, easy imageSizeBySide]
discoveries: [次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识, 次要节点 `easy imageBatchToImageList` 知识库中没有该节点类型的任何知识, 次要节点 `easy imageListToImageBatch` 知识库中没有该节点类型的任何知识, 次要节点 `easy imageSize` 仅有 Resolution 的通用知识，没有该节点自己的说明, 次要节点 `easy imageSizeBySide` 仅有 Resolution 的通用知识，没有该节点自己的说明]
---

# 视频生成/文生视频/高清修复SeedVR2.5,FlashVSR1.1（4K_8K）_2002479902790152193.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/高清修复SeedVR2.5,FlashVSR1.1（4K_8K）_2002479902790152193.json`

## 结构

**生成流程**：Process → Output → Other

**节点**（40 个）：
- `ImageScaleToTotalPixels`
- `SeedVR2VideoUpscaler`
- `PreviewImage`
- `SaveImage`
- `Note`
- `Note`
- `Image Comparer (rgthree)`
- `LoadImage`
- `SaveImage`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `Note`
- `Note`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `TTP_Tile_image_size`
- `TTP_Image_Tile_Batch`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `easy imageBatchToImageList`
- `SeedVR2LoadVAEModel`
- `easy imageSize`
- `SeedVR2VideoUpscaler`
- `easy imageListToImageBatch`
- `ImageScale`
- `TTP_Image_Assy`
- `INTConstant`
- `Image Comparer (rgthree)`
- `easy imageSizeBySide`
- `SaveImage`
- `SeedVR2LoadDiTModel`
- `LoadImage`
- `Image Comparer (rgthree)`
- `Note`
- `INTConstant`
- `INTConstant`
- `INTConstant`
- `FlashVSRNode`
- `Note`
- `LoadImage`
- `Fast Groups Bypasser (rgthree)`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`

## 知识

覆盖率 **55%**（22/40）

**有卡**：`ImageScaleToTotalPixels`、`SeedVR2VideoUpscaler`、`SaveImage`、`LoadImage`、`TTP_Tile_image_size`、`TTP_Image_Tile_Batch`、`SeedVR2LoadVAEModel`、`ImageScale`、`TTP_Image_Assy`、`INTConstant`、`SeedVR2LoadDiTModel`、`FlashVSRNode`

**缺卡**（7）：`LayerUtility: ImageScaleByAspectRatio V2`、`LayerUtility: ImageScaleByAspectRatio V2`、`LayerUtility: ImageScaleByAspectRatio V2`、`easy imageBatchToImageList`、`easy imageListToImageBatch`、`easy imageSize`、`easy imageSizeBySide`

**用到的条目**：LoadImage、SeedVR2LoadDiTModel、SeedVR2LoadVAEModel、SeedVR2VideoUpscaler、TTP_Tile_image_size、SaveImage、ImageScale、ImageScaleToTotalPixels

## 学习发现

- 次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识
- 次要节点 `easy imageBatchToImageList` 知识库中没有该节点类型的任何知识
- 次要节点 `easy imageListToImageBatch` 知识库中没有该节点类型的任何知识
- 次要节点 `easy imageSize` 仅有 Resolution 的通用知识，没有该节点自己的说明
- 次要节点 `easy imageSizeBySide` 仅有 Resolution 的通用知识，没有该节点自己的说明

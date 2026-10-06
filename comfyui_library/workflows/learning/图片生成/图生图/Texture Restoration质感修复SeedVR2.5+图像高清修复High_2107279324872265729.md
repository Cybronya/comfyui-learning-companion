---
key: 图片生成/图生图/Texture Restoration质感修复SeedVR2.5+图像高清修复High_2107279324872265729.json
name: Texture Restoration质感修复SeedVR2.5+图像高清修复High_2107279324872265729
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Texture Restoration质感修复SeedVR2.5+图像高清修复High_2107279324872265729.json
hash: 0b89bacde79dce49
coverage: 0.133333
learned_at: 2026-10-06 21:42:44
nodes: [TTP_Image_Tile_Batch, INTConstant, ImageScaleToTotalPixels, PreviewImage, SeedVR2VideoUpscaler, Image Comparer (rgthree), SeedVR2LoadVAEModel, LoadImage, ImageScale, easy imageListToImageBatch, TTP_Image_Assy, easy imageSize, easy imageSizeBySide, SeedVR2LoadVAEModel, TTP_Tile_image_size, SeedVR2LoadDiTModel, SeedVR2LoadDiTModel, LayerUtility: ImageScaleByAspectRatio V2, PreviewImage, SeedVR2VideoUpscaler, LayerUtility: ImageScaleByAspectRatio V2, Fast Groups Bypasser (rgthree), Image Comparer (rgthree), SaveImage, SaveImage, easy imageBatchToImageList, INTConstant, LoadImage, Note, Note]
patterns: []
missing: [Fast Groups Bypasser (rgthree), INTConstant, INTConstant, ImageScale, ImageScaleToTotalPixels, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: ImageScaleByAspectRatio V2, TTP_Image_Assy, TTP_Image_Tile_Batch, easy imageBatchToImageList, easy imageListToImageBatch, SeedVR2LoadDiTModel, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, SeedVR2VideoUpscaler, TTP_Tile_image_size, easy imageSize, easy imageSizeBySide]
discoveries: [次要节点 `Fast Groups Bypasser (rgthree)` 知识库中没有该节点类型的任何知识, 次要节点 `INTConstant` 知识库中没有该节点类型的任何知识, 次要节点 `INTConstant` 知识库中没有该节点类型的任何知识, 次要节点 `ImageScale` 知识库中没有该节点类型的任何知识, 次要节点 `ImageScaleToTotalPixels` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识, 次要节点 `TTP_Image_Assy` 知识库中没有该节点类型的任何知识, 次要节点 `TTP_Image_Tile_Batch` 知识库中没有该节点类型的任何知识, 次要节点 `easy imageBatchToImageList` 知识库中没有该节点类型的任何知识, 次要节点 `easy imageListToImageBatch` 知识库中没有该节点类型的任何知识, 次要节点 `SeedVR2LoadDiTModel` 仅有 KSampler 的通用知识，没有该节点自己的说明, 次要节点 `SeedVR2LoadDiTModel` 仅有 KSampler 的通用知识，没有该节点自己的说明, 次要节点 `SeedVR2LoadVAEModel` 仅有 KSampler/VAE 的通用知识，没有该节点自己的说明, 次要节点 `SeedVR2LoadVAEModel` 仅有 KSampler/VAE 的通用知识，没有该节点自己的说明, 次要节点 `SeedVR2VideoUpscaler` 仅有 KSampler 的通用知识，没有该节点自己的说明, 次要节点 `SeedVR2VideoUpscaler` 仅有 KSampler 的通用知识，没有该节点自己的说明, 次要节点 `TTP_Tile_image_size` 仅有 Resolution 的通用知识，没有该节点自己的说明, 次要节点 `easy imageSize` 仅有 Resolution 的通用知识，没有该节点自己的说明, 次要节点 `easy imageSizeBySide` 仅有 Resolution 的通用知识，没有该节点自己的说明]
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

覆盖率 **13%**（4/30）

**有卡**：`LoadImage`、`SaveImage`

**缺卡**（20）：`Fast Groups Bypasser (rgthree)`、`INTConstant`、`INTConstant`、`ImageScale`、`ImageScaleToTotalPixels`、`LayerUtility: ImageScaleByAspectRatio V2`、`LayerUtility: ImageScaleByAspectRatio V2`、`TTP_Image_Assy`、`TTP_Image_Tile_Batch`、`easy imageBatchToImageList`、`easy imageListToImageBatch`、`SeedVR2LoadDiTModel`、`SeedVR2LoadDiTModel`、`SeedVR2LoadVAEModel`、`SeedVR2LoadVAEModel`、`SeedVR2VideoUpscaler`、`SeedVR2VideoUpscaler`、`TTP_Tile_image_size`、`easy imageSize`、`easy imageSizeBySide`

**用到的条目**：LoadImage、SaveImage、sd15-t2i-basic、sd15-t2i-lora、sampler_name 调整经验、steps 调整经验、cfg 调整经验、VAEDecode

## 学习发现

- 次要节点 `Fast Groups Bypasser (rgthree)` 知识库中没有该节点类型的任何知识
- 次要节点 `INTConstant` 知识库中没有该节点类型的任何知识
- 次要节点 `INTConstant` 知识库中没有该节点类型的任何知识
- 次要节点 `ImageScale` 知识库中没有该节点类型的任何知识
- 次要节点 `ImageScaleToTotalPixels` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识
- 次要节点 `TTP_Image_Assy` 知识库中没有该节点类型的任何知识
- 次要节点 `TTP_Image_Tile_Batch` 知识库中没有该节点类型的任何知识
- 次要节点 `easy imageBatchToImageList` 知识库中没有该节点类型的任何知识
- 次要节点 `easy imageListToImageBatch` 知识库中没有该节点类型的任何知识
- 次要节点 `SeedVR2LoadDiTModel` 仅有 KSampler 的通用知识，没有该节点自己的说明
- 次要节点 `SeedVR2LoadDiTModel` 仅有 KSampler 的通用知识，没有该节点自己的说明
- 次要节点 `SeedVR2LoadVAEModel` 仅有 KSampler/VAE 的通用知识，没有该节点自己的说明
- 次要节点 `SeedVR2LoadVAEModel` 仅有 KSampler/VAE 的通用知识，没有该节点自己的说明
- 次要节点 `SeedVR2VideoUpscaler` 仅有 KSampler 的通用知识，没有该节点自己的说明
- 次要节点 `SeedVR2VideoUpscaler` 仅有 KSampler 的通用知识，没有该节点自己的说明
- 次要节点 `TTP_Tile_image_size` 仅有 Resolution 的通用知识，没有该节点自己的说明
- 次要节点 `easy imageSize` 仅有 Resolution 的通用知识，没有该节点自己的说明
- 次要节点 `easy imageSizeBySide` 仅有 Resolution 的通用知识，没有该节点自己的说明

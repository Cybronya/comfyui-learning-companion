---
key: 平台全量/Comfyui节点系列65-Resize+Image_Mask_2061293440083775490.json
name: Comfyui节点系列65-Resize+Image_Mask_2061293440083775490
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/Comfyui节点系列65-Resize+Image_Mask_2061293440083775490.json
hash: ee3e1b378e131a9b
coverage: 0.648649
learned_at: 2026-11-14 00:22:39
nodes: [GetNode, ImageAndMaskPreview, GetNode, ImageAndMaskPreview, ImageAndMaskPreview, ImageAndMaskPreview, ImageAndMaskPreview, Note, SetNode, LoadImage, SetNode, ImageAndMaskPreview, GetNode, ImageAndMaskPreview, GetNode, ImageAndMaskPreview, ImageAndMaskPreview, GetNode, ResizeImageMaskNode, GetNode, GetNode, ResizeImageMaskNode, ResizeImageMaskNode, ResizeImageMaskNode, GetNode, ImageScaleToTotalPixels, ResizeImageMaskNode, LoadImage, GetNode, LayerUtility: ImageScaleByAspectRatio V2, ImageResizeKJv2, ResizeImageMaskNode, GetNode, ResizeImageMaskNode, ResizeImageMaskNode, SaveImage, ResizeImageMaskNode]
patterns: []
missing: []
---

# 平台全量/Comfyui节点系列65-Resize+Image_Mask_2061293440083775490.json

> 来源文件 `comfyui_library/workflows/平台全量/Comfyui节点系列65-Resize+Image_Mask_2061293440083775490.json`

## 结构

**生成流程**：Process → Output → Other

**节点**（37 个）：
- `GetNode`
- `ImageAndMaskPreview`
- `GetNode`
- `ImageAndMaskPreview`
- `ImageAndMaskPreview`
- `ImageAndMaskPreview`
- `ImageAndMaskPreview`
- `Note`
- `SetNode`
- `LoadImage`
- `SetNode`
- `ImageAndMaskPreview`
- `GetNode`
- `ImageAndMaskPreview`
- `GetNode`
- `ImageAndMaskPreview`
- `ImageAndMaskPreview`
- `GetNode`
- `ResizeImageMaskNode`
- `GetNode`
- `GetNode`
- `ResizeImageMaskNode`
- `ResizeImageMaskNode`
- `ResizeImageMaskNode`
- `GetNode`
- `ImageScaleToTotalPixels`
- `ResizeImageMaskNode`
- `LoadImage`
- `GetNode`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `ImageResizeKJv2`
- `ResizeImageMaskNode`
- `GetNode`
- `ResizeImageMaskNode`
- `ResizeImageMaskNode`
- `SaveImage`
- `ResizeImageMaskNode`

## 知识

覆盖率 **65%**（24/37）

**有卡**：`ImageAndMaskPreview`、`LoadImage`、`ResizeImageMaskNode`、`ImageScaleToTotalPixels`、`LayerUtility: ImageScaleByAspectRatio V2`、`ImageResizeKJv2`、`SaveImage`

**用到的条目**：LayerUtility: ImageScaleByAspectRatio V2、LoadImage、ImageResizeKJv2、ResizeImageMaskNode、ImageAndMaskPreview、SaveImage、ImageScaleToTotalPixels、image_to_image_controlnet_lora_sampler_10

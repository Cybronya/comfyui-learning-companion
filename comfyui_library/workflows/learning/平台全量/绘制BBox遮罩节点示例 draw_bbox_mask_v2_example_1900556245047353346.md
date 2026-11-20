---
key: 平台全量/绘制BBox遮罩节点示例 draw_bbox_mask_v2_example_1900556245047353346.json
name: 绘制BBox遮罩节点示例 draw_bbox_mask_v2_example_1900556245047353346
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/绘制BBox遮罩节点示例 draw_bbox_mask_v2_example_1900556245047353346.json
hash: baeacff14d7face1
coverage: 0.875
learned_at: 2026-11-14 02:29:18
nodes: [LayerMask: LoadFlorence2Model, LayerMask: ObjectDetectorFL2, PreviewImage, LayerMask: MaskPreview, LayerMask: DrawBBoxMaskV2, LoadImage, LayerUtility: ImageCombineAlpha, SaveImage]
patterns: []
missing: []
---

# 平台全量/绘制BBox遮罩节点示例 draw_bbox_mask_v2_example_1900556245047353346.json

> 来源文件 `comfyui_library/workflows/平台全量/绘制BBox遮罩节点示例 draw_bbox_mask_v2_example_1900556245047353346.json`

## 结构

**生成流程**：Process → Output → Other

**节点**（8 个）：
- `LayerMask: LoadFlorence2Model`
- `LayerMask: ObjectDetectorFL2`
- `PreviewImage`
- `LayerMask: MaskPreview`
- `LayerMask: DrawBBoxMaskV2`
- `LoadImage`
- `LayerUtility: ImageCombineAlpha`
- `SaveImage`

## 知识

覆盖率 **88%**（7/8）

**有卡**：`LayerMask: LoadFlorence2Model`、`LayerMask: ObjectDetectorFL2`、`LayerMask: MaskPreview`、`LayerMask: DrawBBoxMaskV2`、`LoadImage`、`LayerUtility: ImageCombineAlpha`、`SaveImage`

**用到的条目**：LoadImage、LayerMask: MaskPreview、SaveImage、LayerMask: DrawBBoxMaskV2、LayerMask: LoadFlorence2Model、LayerMask: ObjectDetectorFL2、LayerUtility: ImageCombineAlpha、image_to_image_controlnet_face_detailer_lora

---
key: 平台全量/图层变换 _遮罩变换节点示例 layer_image_transform_example_1899799948114669569.json
name: 图层变换 _遮罩变换节点示例 layer_image_transform_example_1899799948114669569
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/图层变换 _遮罩变换节点示例 layer_image_transform_example_1899799948114669569.json
hash: f7447babbcec29b4
coverage: 0.888889
learned_at: 2026-11-14 01:54:09
nodes: [LoadImage, LoadImage, LayerUtility: ImageBlend, LayerMask: SegmentAnythingUltra, LayerMask: MaskPreview, PreviewImage, SaveImage, LayerUtility: LayerMaskTransform, LayerUtility: LayerImageTransform]
patterns: []
missing: []
---

# 平台全量/图层变换 _遮罩变换节点示例 layer_image_transform_example_1899799948114669569.json

> 来源文件 `comfyui_library/workflows/平台全量/图层变换 _遮罩变换节点示例 layer_image_transform_example_1899799948114669569.json`

## 结构

**生成流程**：Process → Output → Other

**节点**（9 个）：
- `LoadImage`
- `LoadImage`
- `LayerUtility: ImageBlend`
- `LayerMask: SegmentAnythingUltra`
- `LayerMask: MaskPreview`
- `PreviewImage`
- `SaveImage`
- `LayerUtility: LayerMaskTransform`
- `LayerUtility: LayerImageTransform`

## 知识

覆盖率 **89%**（8/9）

**有卡**：`LoadImage`、`LayerUtility: ImageBlend`、`LayerMask: SegmentAnythingUltra`、`LayerMask: MaskPreview`、`SaveImage`、`LayerUtility: LayerMaskTransform`、`LayerUtility: LayerImageTransform`

**用到的条目**：LoadImage、LayerMask: MaskPreview、SaveImage、LayerMask: SegmentAnythingUltra、LayerUtility: ImageBlend、LayerUtility: LayerImageTransform、LayerUtility: LayerMaskTransform、image_to_image_controlnet_face_detailer_lora

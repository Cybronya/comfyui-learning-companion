---
key: 平台全量/裁切局部及还原示例 crop_by_mask_&_restore_crop_box_example_1899392724292816898.json
name: 裁切局部及还原示例 crop_by_mask_&_restore_crop_box_example_1899392724292816898
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/裁切局部及还原示例 crop_by_mask_&_restore_crop_box_example_1899392724292816898.json
hash: 02df3b07f239dfdc
coverage: 0.727273
learned_at: 2026-11-14 02:33:38
nodes: [LayerUtility: CropByMask, PreviewImage, Note, PreviewImage, LayerMask: MaskPreview, LayerUtility: ImageScaleRestore, LayerUtility: ImageScaleRestore, LoadImage, LayerMask: RemBgUltra, LayerUtility: RestoreCropBox, SaveImage]
patterns: []
missing: []
---

# 平台全量/裁切局部及还原示例 crop_by_mask_&_restore_crop_box_example_1899392724292816898.json

> 来源文件 `comfyui_library/workflows/平台全量/裁切局部及还原示例 crop_by_mask_&_restore_crop_box_example_1899392724292816898.json`

## 结构

**生成流程**：Process → Output → Other

**节点**（11 个）：
- `LayerUtility: CropByMask`
- `PreviewImage`
- `Note`
- `PreviewImage`
- `LayerMask: MaskPreview`
- `LayerUtility: ImageScaleRestore`
- `LayerUtility: ImageScaleRestore`
- `LoadImage`
- `LayerMask: RemBgUltra`
- `LayerUtility: RestoreCropBox`
- `SaveImage`

## 知识

覆盖率 **73%**（8/11）

**有卡**：`LayerUtility: CropByMask`、`LayerMask: MaskPreview`、`LayerUtility: ImageScaleRestore`、`LoadImage`、`LayerMask: RemBgUltra`、`LayerUtility: RestoreCropBox`、`SaveImage`

**用到的条目**：LoadImage、LayerMask: MaskPreview、SaveImage、LayerMask: RemBgUltra、LayerUtility: CropByMask、LayerUtility: ImageScaleRestore、LayerUtility: RestoreCropBox、image_to_image_controlnet_face_detailer_lora

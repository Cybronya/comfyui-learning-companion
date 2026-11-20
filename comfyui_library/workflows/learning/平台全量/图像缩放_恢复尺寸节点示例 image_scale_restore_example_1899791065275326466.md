---
key: 平台全量/图像缩放_恢复尺寸节点示例 image_scale_restore_example_1899791065275326466.json
name: 图像缩放_恢复尺寸节点示例 image_scale_restore_example_1899791065275326466
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/图像缩放_恢复尺寸节点示例 image_scale_restore_example_1899791065275326466.json
hash: 97eebb646d06af4c
coverage: 0.888889
learned_at: 2026-11-14 01:53:45
nodes: [LayerUtility: ImageScaleRestore, LayerUtility: ImageScaleRestore, PreviewImage, LayerMask: MaskPreview, SaveImage, LayerMask: MaskPreview, LayerMask: MaskPreview, LayerMask: RmBgUltra V2, LoadImage]
patterns: []
missing: []
---

# 平台全量/图像缩放_恢复尺寸节点示例 image_scale_restore_example_1899791065275326466.json

> 来源文件 `comfyui_library/workflows/平台全量/图像缩放_恢复尺寸节点示例 image_scale_restore_example_1899791065275326466.json`

## 结构

**生成流程**：Process → Output → Other

**节点**（9 个）：
- `LayerUtility: ImageScaleRestore`
- `LayerUtility: ImageScaleRestore`
- `PreviewImage`
- `LayerMask: MaskPreview`
- `SaveImage`
- `LayerMask: MaskPreview`
- `LayerMask: MaskPreview`
- `LayerMask: RmBgUltra V2`
- `LoadImage`

## 知识

覆盖率 **89%**（8/9）

**有卡**：`LayerUtility: ImageScaleRestore`、`LayerMask: MaskPreview`、`SaveImage`、`LayerMask: RmBgUltra V2`、`LoadImage`

**用到的条目**：LoadImage、LayerMask: MaskPreview、SaveImage、LayerMask: RmBgUltra V2、LayerUtility: ImageScaleRestore、image_to_image_controlnet_face_detailer_lora、image_to_image_controlnet_face_detailer_lora_2、image_to_image_controlnet_face_detailer_sampler

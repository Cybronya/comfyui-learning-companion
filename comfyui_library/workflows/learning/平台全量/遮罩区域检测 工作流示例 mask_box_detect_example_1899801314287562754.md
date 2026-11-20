---
key: 平台全量/遮罩区域检测 工作流示例 mask_box_detect_example_1899801314287562754.json
name: 遮罩区域检测 工作流示例 mask_box_detect_example_1899801314287562754
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/遮罩区域检测 工作流示例 mask_box_detect_example_1899801314287562754.json
hash: 4787a72a49dde6f1
coverage: 0.857143
learned_at: 2026-11-14 02:48:47
nodes: [LoadImage, LayerMask: MaskPreview, PreviewImage, LoadImage, LayerUtility: ImageBlendAdvance, SaveImage, LayerMask: MaskBoxDetect]
patterns: []
missing: []
---

# 平台全量/遮罩区域检测 工作流示例 mask_box_detect_example_1899801314287562754.json

> 来源文件 `comfyui_library/workflows/平台全量/遮罩区域检测 工作流示例 mask_box_detect_example_1899801314287562754.json`

## 结构

**生成流程**：Process → Output → Other

**节点**（7 个）：
- `LoadImage`
- `LayerMask: MaskPreview`
- `PreviewImage`
- `LoadImage`
- `LayerUtility: ImageBlendAdvance`
- `SaveImage`
- `LayerMask: MaskBoxDetect`

## 知识

覆盖率 **86%**（6/7）

**有卡**：`LoadImage`、`LayerMask: MaskPreview`、`LayerUtility: ImageBlendAdvance`、`SaveImage`、`LayerMask: MaskBoxDetect`

**用到的条目**：LoadImage、LayerMask: MaskPreview、SaveImage、LayerMask: MaskBoxDetect、LayerUtility: ImageBlendAdvance、image_to_image_controlnet_face_detailer_lora、image_to_image_controlnet_face_detailer_lora_2、image_to_image_controlnet_face_detailer_sampler

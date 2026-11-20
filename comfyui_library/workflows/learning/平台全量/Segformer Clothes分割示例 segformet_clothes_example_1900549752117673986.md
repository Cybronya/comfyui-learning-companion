---
key: 平台全量/Segformer Clothes分割示例 segformet_clothes_example_1900549752117673986.json
name: Segformer Clothes分割示例 segformet_clothes_example_1900549752117673986
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/Segformer Clothes分割示例 segformet_clothes_example_1900549752117673986.json
hash: 924ba573630739b2
coverage: 1
learned_at: 2026-11-14 01:00:37
nodes: [LayerMask: SegformerClothesPipelineLoader, LoadImage, LayerMask: SegformerUltraV2, LayerMask: MaskPreview, SaveImage]
patterns: []
missing: []
---

# 平台全量/Segformer Clothes分割示例 segformet_clothes_example_1900549752117673986.json

> 来源文件 `comfyui_library/workflows/平台全量/Segformer Clothes分割示例 segformet_clothes_example_1900549752117673986.json`

## 结构

**生成流程**：Model → Output → Other

**节点**（5 个）：
- `LayerMask: SegformerClothesPipelineLoader`
- `LoadImage`
- `LayerMask: SegformerUltraV2`
- `LayerMask: MaskPreview`
- `SaveImage`

## 知识

覆盖率 **100%**（5/5）

**有卡**：`LayerMask: SegformerClothesPipelineLoader`、`LoadImage`、`LayerMask: SegformerUltraV2`、`LayerMask: MaskPreview`、`SaveImage`

**用到的条目**：LoadImage、LayerMask: MaskPreview、SaveImage、LayerMask: SegformerClothesPipelineLoader、LayerMask: SegformerUltraV2、image_to_image_controlnet_face_detailer_lora、image_to_image_controlnet_face_detailer_lora_2、image_to_image_controlnet_face_detailer_sampler

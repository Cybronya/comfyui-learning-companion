---
key: 平台全量/去除_合并alph通道节点示例 image_remove_alpha & image_combine_1899717950851469313.json
name: 去除_合并alph通道节点示例 image_remove_alpha & image_combine_1899717950851469313
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/去除_合并alph通道节点示例 image_remove_alpha & image_combine_1899717950851469313.json
hash: 056ec21e04e6434d
coverage: 0.625
learned_at: 2026-11-14 01:50:14
nodes: [PreviewImage, LayerMask: RemBgUltra, PreviewImage, LayerUtility: ImageRemoveAlpha, Reroute, LayerUtility: ImageCombineAlpha, SaveImage, LoadImage]
patterns: []
missing: []
---

# 平台全量/去除_合并alph通道节点示例 image_remove_alpha & image_combine_1899717950851469313.json

> 来源文件 `comfyui_library/workflows/平台全量/去除_合并alph通道节点示例 image_remove_alpha & image_combine_1899717950851469313.json`

## 结构

**生成流程**：Process → Output → Other

**节点**（8 个）：
- `PreviewImage`
- `LayerMask: RemBgUltra`
- `PreviewImage`
- `LayerUtility: ImageRemoveAlpha`
- `Reroute`
- `LayerUtility: ImageCombineAlpha`
- `SaveImage`
- `LoadImage`

## 知识

覆盖率 **62%**（5/8）

**有卡**：`LayerMask: RemBgUltra`、`LayerUtility: ImageRemoveAlpha`、`LayerUtility: ImageCombineAlpha`、`SaveImage`、`LoadImage`

**用到的条目**：LoadImage、SaveImage、LayerMask: RemBgUltra、LayerUtility: ImageCombineAlpha、LayerUtility: ImageRemoveAlpha、image_to_image_controlnet_face_detailer_lora、image_to_image_controlnet_face_detailer_lora_2、image_to_image_controlnet_face_detailer_sampler

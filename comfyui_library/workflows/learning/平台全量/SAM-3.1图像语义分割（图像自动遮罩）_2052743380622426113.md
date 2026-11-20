---
key: 平台全量/SAM-3.1图像语义分割（图像自动遮罩）_2052743380622426113.json
name: SAM-3.1图像语义分割（图像自动遮罩）_2052743380622426113
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/SAM-3.1图像语义分割（图像自动遮罩）_2052743380622426113.json
hash: 9225829b21975c9a
coverage: 1
learned_at: 2026-11-14 00:55:00
nodes: [LoadImage, CheckpointLoaderSimple, ImageAndMaskPreview, CLIPTextEncode, SAM3_Detect, SaveImage]
patterns: []
missing: []
parameters: {"checkpoint": "sam3.1-multiplex-fp16.safetensors"}
---

# 平台全量/SAM-3.1图像语义分割（图像自动遮罩）_2052743380622426113.json

> 来源文件 `comfyui_library/workflows/平台全量/SAM-3.1图像语义分割（图像自动遮罩）_2052743380622426113.json`

## 结构

**生成流程**：Model → Condition → Output → Other

**节点**（6 个）：
- `LoadImage`
- `CheckpointLoaderSimple` ★核心
- `ImageAndMaskPreview`
- `CLIPTextEncode` ★核心
- `SAM3_Detect`
- `SaveImage`

## 关键参数

- `checkpoint` = `sam3.1-multiplex-fp16.safetensors`

## 知识

覆盖率 **100%**（6/6）

**有卡**：`LoadImage`、`CheckpointLoaderSimple`、`ImageAndMaskPreview`、`CLIPTextEncode`、`SAM3_Detect`、`SaveImage`

**用到的条目**：CheckpointLoaderSimple、CLIPTextEncode、LoadImage、ImageAndMaskPreview、SaveImage、SAM3_Detect、image_to_image_controlnet_face_detailer_lora、image_to_image_controlnet_face_detailer_lora_2

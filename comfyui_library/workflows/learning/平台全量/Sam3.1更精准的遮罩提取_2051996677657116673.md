---
key: 平台全量/Sam3.1更精准的遮罩提取_2051996677657116673.json
name: Sam3.1更精准的遮罩提取_2051996677657116673
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/Sam3.1更精准的遮罩提取_2051996677657116673.json
hash: 723a8eb2edbc328d
coverage: 1
learned_at: 2026-11-14 00:56:51
nodes: [VHS_VideoInfoLoaded, CheckpointLoaderSimple, CLIPTextEncode, VHS_VideoCombine, SAM3_Detect, VHS_LoadVideo, MaskToImage]
patterns: []
missing: []
parameters: {"checkpoint": "sam3.1_multiplex_fp16.safetensors"}
---

# 平台全量/Sam3.1更精准的遮罩提取_2051996677657116673.json

> 来源文件 `comfyui_library/workflows/平台全量/Sam3.1更精准的遮罩提取_2051996677657116673.json`

## 结构

**生成流程**：Model → Condition → Other

**节点**（7 个）：
- `VHS_VideoInfoLoaded`
- `CheckpointLoaderSimple` ★核心
- `CLIPTextEncode` ★核心
- `VHS_VideoCombine`
- `SAM3_Detect`
- `VHS_LoadVideo`
- `MaskToImage`

## 关键参数

- `checkpoint` = `sam3.1_multiplex_fp16.safetensors`

## 知识

覆盖率 **100%**（7/7）

**有卡**：`VHS_VideoInfoLoaded`、`CheckpointLoaderSimple`、`CLIPTextEncode`、`VHS_VideoCombine`、`SAM3_Detect`、`VHS_LoadVideo`、`MaskToImage`

**用到的条目**：CheckpointLoaderSimple、CLIPTextEncode、MaskToImage、SAM3_Detect、VHS_LoadVideo、VHS_VideoCombine、VHS_VideoInfoLoaded、image_to_image_controlnet_face_detailer_lora

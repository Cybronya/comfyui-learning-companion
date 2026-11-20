---
key: 平台全量/视频Sam3.1遮罩提取_2054085347423866881.json
name: 视频Sam3.1遮罩提取_2054085347423866881
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/视频Sam3.1遮罩提取_2054085347423866881.json
hash: f8a133727f81c292
coverage: 1
learned_at: 2026-11-14 02:34:51
nodes: [MaskToImage, VHS_VideoInfoLoaded, CLIPTextEncode, VHS_LoadVideo, SAM3_Detect, VHS_VideoCombine, DeepTranslatorTextNode, CheckpointLoaderSimple]
patterns: []
missing: []
parameters: {"checkpoint": "sam3.1_multiplex_fp16.safetensors"}
---

# 平台全量/视频Sam3.1遮罩提取_2054085347423866881.json

> 来源文件 `comfyui_library/workflows/平台全量/视频Sam3.1遮罩提取_2054085347423866881.json`

## 结构

**生成流程**：Model → Condition → Other

**节点**（8 个）：
- `MaskToImage`
- `VHS_VideoInfoLoaded`
- `CLIPTextEncode` ★核心
- `VHS_LoadVideo`
- `SAM3_Detect`
- `VHS_VideoCombine`
- `DeepTranslatorTextNode`
- `CheckpointLoaderSimple` ★核心

## 关键参数

- `checkpoint` = `sam3.1_multiplex_fp16.safetensors`

## 知识

覆盖率 **100%**（8/8）

**有卡**：`MaskToImage`、`VHS_VideoInfoLoaded`、`CLIPTextEncode`、`VHS_LoadVideo`、`SAM3_Detect`、`VHS_VideoCombine`、`DeepTranslatorTextNode`、`CheckpointLoaderSimple`

**用到的条目**：CheckpointLoaderSimple、CLIPTextEncode、DeepTranslatorTextNode、MaskToImage、SAM3_Detect、VHS_LoadVideo、VHS_VideoCombine、VHS_VideoInfoLoaded

---
key: 平台全量/SAM-3.1-视频自动扣图_2052747925532495873.json
name: SAM-3.1-视频自动扣图_2052747925532495873
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/SAM-3.1-视频自动扣图_2052747925532495873.json
hash: 0418c31260af5b9e
coverage: 1
learned_at: 2026-11-14 00:54:59
nodes: [VHS_VideoCombine, DrawMaskOnImage, SAM3_TrackToMask, VHS_LoadVideo, CheckpointLoaderSimple, CLIPTextEncode, SAM3_VideoTrack, VHS_VideoInfo]
patterns: []
missing: []
parameters: {"checkpoint": "sam3.1-multiplex-fp16.safetensors"}
---

# 平台全量/SAM-3.1-视频自动扣图_2052747925532495873.json

> 来源文件 `comfyui_library/workflows/平台全量/SAM-3.1-视频自动扣图_2052747925532495873.json`

## 结构

**生成流程**：Model → Condition → Other

**节点**（8 个）：
- `VHS_VideoCombine`
- `DrawMaskOnImage`
- `SAM3_TrackToMask`
- `VHS_LoadVideo`
- `CheckpointLoaderSimple` ★核心
- `CLIPTextEncode` ★核心
- `SAM3_VideoTrack`
- `VHS_VideoInfo`

## 关键参数

- `checkpoint` = `sam3.1-multiplex-fp16.safetensors`

## 知识

覆盖率 **100%**（8/8）

**有卡**：`VHS_VideoCombine`、`DrawMaskOnImage`、`SAM3_TrackToMask`、`VHS_LoadVideo`、`CheckpointLoaderSimple`、`CLIPTextEncode`、`SAM3_VideoTrack`、`VHS_VideoInfo`

**用到的条目**：CheckpointLoaderSimple、CLIPTextEncode、DrawMaskOnImage、SAM3_TrackToMask、SAM3_VideoTrack、VHS_LoadVideo、VHS_VideoCombine、VHS_VideoInfo

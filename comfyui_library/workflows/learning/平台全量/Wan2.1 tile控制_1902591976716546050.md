---
key: 平台全量/Wan2.1 tile控制_1902591976716546050.json
name: Wan2.1 tile控制_1902591976716546050
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/Wan2.1 tile控制_1902591976716546050.json
hash: 4ec3956d27f3a893
coverage: 0.833333
learned_at: 2026-11-14 01:04:28
nodes: [WanVideoModelLoader, ImageBlur, WanVideoLoraSelect, PrimitiveNode, PrimitiveNode, LoadWanVideoT5TextEncoder, WanVideoEncode, ImageScale, WanVideoVAELoader, Anything Everywhere, WanVideoControlEmbeds, WanVideoSampler, WanVideoDecode, VHS_VideoCombine, RIFE VFI, VHS_VideoCombine, WanVideoTextEncode, VHS_LoadVideo]
patterns: []
missing: []
---

# 平台全量/Wan2.1 tile控制_1902591976716546050.json

> 来源文件 `comfyui_library/workflows/平台全量/Wan2.1 tile控制_1902591976716546050.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（18 个）：
- `WanVideoModelLoader`
- `ImageBlur`
- `WanVideoLoraSelect`
- `PrimitiveNode`
- `PrimitiveNode`
- `LoadWanVideoT5TextEncoder`
- `WanVideoEncode`
- `ImageScale`
- `WanVideoVAELoader`
- `Anything Everywhere`
- `WanVideoControlEmbeds`
- `WanVideoSampler` ★核心
- `WanVideoDecode`
- `VHS_VideoCombine`
- `RIFE VFI`
- `VHS_VideoCombine`
- `WanVideoTextEncode`
- `VHS_LoadVideo`

## 知识

覆盖率 **83%**（15/18）

**有卡**：`WanVideoModelLoader`、`ImageBlur`、`WanVideoLoraSelect`、`LoadWanVideoT5TextEncoder`、`WanVideoEncode`、`ImageScale`、`WanVideoVAELoader`、`WanVideoControlEmbeds`、`WanVideoSampler`、`WanVideoDecode`、`VHS_VideoCombine`、`RIFE VFI`、`WanVideoTextEncode`、`VHS_LoadVideo`

**用到的条目**：WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoEncode、WanVideoTextEncode、WanVideoVAELoader、WanVideoLoraSelect、ImageBlur

---
key: 视频生成/图生视频/wan2.1-i2v+首尾帧_1918496114579017729.json
name: wan2.1-i2v+首尾帧_1918496114579017729.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/wan2.1-i2v+首尾帧_1918496114579017729.json
hash: 91f992093bb6b80d
coverage: 0.545455
learned_at: 2026-10-15 22:29:40
nodes: [WanVideoTorchCompileSettings, WanVideoSEModelLoader, SetNode, WanVideoBlockSwap, WanVideoSESampler, WanVideoEnhanceAVideo, WanVideoTeaCache, WanVideoSLG, LoadWanVideoT5TextEncoder, GetNode, GetNode, WanVideoSEVAELoader, SetNode, LoadWanVideoClipTextEncoder, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, SetNode, GetNode, SetNode, SetNode, SetNode, LoadImage, LoadImage, WanVideoSEDecode, VHS_VideoCombine, VHS_VideoCombine, RIFE VFI, WanVideoSEImageClipEncode, WanVideoTextEncode]
patterns: []
missing: []
---

# 视频生成/图生视频/wan2.1-i2v+首尾帧_1918496114579017729.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1918496114579017729.json`

## 结构

**生成流程**：Model → Condition → Sampling → Other

**节点**（33 个）：
- `WanVideoTorchCompileSettings`
- `WanVideoSEModelLoader`
- `SetNode`
- `WanVideoBlockSwap`
- `WanVideoSESampler` ★核心
- `WanVideoEnhanceAVideo`
- `WanVideoTeaCache`
- `WanVideoSLG`
- `LoadWanVideoT5TextEncoder`
- `GetNode`
- `GetNode`
- `WanVideoSEVAELoader`
- `SetNode`
- `LoadWanVideoClipTextEncoder` ★核心
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `LoadImage`
- `LoadImage`
- `WanVideoSEDecode`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `RIFE VFI`
- `WanVideoSEImageClipEncode`
- `WanVideoTextEncode`

## 知识

覆盖率 **55%**（18/33）

**有卡**：`WanVideoTorchCompileSettings`、`WanVideoSEModelLoader`、`WanVideoBlockSwap`、`WanVideoSESampler`、`WanVideoEnhanceAVideo`、`WanVideoTeaCache`、`WanVideoSLG`、`LoadWanVideoT5TextEncoder`、`WanVideoSEVAELoader`、`LoadWanVideoClipTextEncoder`、`LoadImage`、`WanVideoSEDecode`、`VHS_VideoCombine`、`RIFE VFI`、`WanVideoSEImageClipEncode`、`WanVideoTextEncode`

**用到的条目**：LoadImage、WanVideoSESampler、LoadWanVideoClipTextEncoder、LoadWanVideoT5TextEncoder、WanVideoTextEncode、WanVideoSEDecode、WanVideoSEImageClipEncode、WanVideoSEVAELoader

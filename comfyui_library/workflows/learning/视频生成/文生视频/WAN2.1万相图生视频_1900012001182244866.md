---
key: 视频生成/文生视频/WAN2.1万相图生视频_1900012001182244866.json
name: WAN2.1万相图生视频_1900012001182244866.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/WAN2.1万相图生视频_1900012001182244866.json
hash: c263fedb283164c4
coverage: 0.857143
learned_at: 2026-10-15 22:43:21
nodes: [WanVideoDecode, WanVideoImageClipEncode, LoadWanVideoClipTextEncoder, Note, LoadWanVideoT5TextEncoder, LoadImage, WanVideoModelLoader, WanVideoSampler, VHS_VideoCombine, Note, WanVideoTextEncode, WanVideoTorchCompileSettings, WanVideoBlockSwap, WanVideoVAELoader]
patterns: []
missing: []
---

# 视频生成/文生视频/WAN2.1万相图生视频_1900012001182244866.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/1900012001182244866.json`

## 结构

**生成流程**：Model → Condition → Sampling → Other

**节点**（14 个）：
- `WanVideoDecode`
- `WanVideoImageClipEncode`
- `LoadWanVideoClipTextEncoder` ★核心
- `Note`
- `LoadWanVideoT5TextEncoder`
- `LoadImage`
- `WanVideoModelLoader`
- `WanVideoSampler` ★核心
- `VHS_VideoCombine`
- `Note`
- `WanVideoTextEncode`
- `WanVideoTorchCompileSettings`
- `WanVideoBlockSwap`
- `WanVideoVAELoader`

## 知识

覆盖率 **86%**（12/14）

**有卡**：`WanVideoDecode`、`WanVideoImageClipEncode`、`LoadWanVideoClipTextEncoder`、`LoadWanVideoT5TextEncoder`、`LoadImage`、`WanVideoModelLoader`、`WanVideoSampler`、`VHS_VideoCombine`、`WanVideoTextEncode`、`WanVideoTorchCompileSettings`、`WanVideoBlockSwap`、`WanVideoVAELoader`

**用到的条目**：LoadImage、WanVideoSampler、LoadWanVideoClipTextEncoder、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoImageClipEncode、WanVideoTextEncode、WanVideoVAELoader

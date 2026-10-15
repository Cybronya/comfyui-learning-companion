---
key: 视频生成/文生视频/Wan2.1-NAG反向应用_1934538720651747329.json
name: Wan2.1-NAG反向应用_1934538720651747329
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/Wan2.1-NAG反向应用_1934538720651747329.json
hash: dd2bf5b033c359db
coverage: 1
learned_at: 2026-10-15 22:47:08
nodes: [WanVideoTextEncodeSingle, WanVideoTextEncodeSingle, WanVideoDecode, WanVideoBlockSwap, VHS_VideoCombine, WanVideoApplyNAG, WanVideoEmptyEmbeds, LoadWanVideoT5TextEncoder, String Literal, WanVideoEnhanceAVideo, WanVideoTeaCache, WanVideoVAELoader, WanVideoSampler, WanVideoTorchCompileSettings, WanVideoModelLoader]
patterns: []
missing: []
---

# 视频生成/文生视频/Wan2.1-NAG反向应用_1934538720651747329.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/Wan2.1-NAG反向应用_1934538720651747329.json`

## 结构

**生成流程**：Model → Sampling → Other

**节点**（15 个）：
- `WanVideoTextEncodeSingle`
- `WanVideoTextEncodeSingle`
- `WanVideoDecode`
- `WanVideoBlockSwap`
- `VHS_VideoCombine`
- `WanVideoApplyNAG`
- `WanVideoEmptyEmbeds`
- `LoadWanVideoT5TextEncoder`
- `String Literal`
- `WanVideoEnhanceAVideo`
- `WanVideoTeaCache`
- `WanVideoVAELoader`
- `WanVideoSampler` ★核心
- `WanVideoTorchCompileSettings`
- `WanVideoModelLoader`

## 知识

覆盖率 **100%**（15/15）

**有卡**：`WanVideoTextEncodeSingle`、`WanVideoDecode`、`WanVideoBlockSwap`、`VHS_VideoCombine`、`WanVideoApplyNAG`、`WanVideoEmptyEmbeds`、`LoadWanVideoT5TextEncoder`、`String Literal`、`WanVideoEnhanceAVideo`、`WanVideoTeaCache`、`WanVideoVAELoader`、`WanVideoSampler`、`WanVideoTorchCompileSettings`、`WanVideoModelLoader`

**用到的条目**：WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoVAELoader、WanVideoTextEncodeSingle、VHS_VideoCombine、WanVideoBlockSwap、WanVideoModelLoader

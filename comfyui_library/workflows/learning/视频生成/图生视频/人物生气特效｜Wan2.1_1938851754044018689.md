---
key: 视频生成/图生视频/人物生气特效｜Wan2.1_1938851754044018689.json
name: 人物生气特效｜Wan2.1_1938851754044018689.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/人物生气特效｜Wan2.1_1938851754044018689.json
hash: cff5ea0e309f7a86
coverage: 1
learned_at: 2026-10-15 22:30:32
nodes: [WanVideoTorchCompileSettings, WanVideoBlockSwap, LoadWanVideoT5TextEncoder, WanVideoModelLoader, WanVideoLoraSelect, WanVideoImageClipEncode, WanVideoSampler, WanVideoDecode, VHS_VideoCombine, LoadImage, LoadWanVideoClipTextEncoder, WanVideoVAELoader, WanVideoTextEncode]
patterns: []
missing: []
---

# 视频生成/图生视频/人物生气特效｜Wan2.1_1938851754044018689.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1938851754044018689.json`

## 结构

**生成流程**：Model → Condition → Sampling → Other

**节点**（13 个）：
- `WanVideoTorchCompileSettings`
- `WanVideoBlockSwap`
- `LoadWanVideoT5TextEncoder`
- `WanVideoModelLoader`
- `WanVideoLoraSelect`
- `WanVideoImageClipEncode`
- `WanVideoSampler` ★核心
- `WanVideoDecode`
- `VHS_VideoCombine`
- `LoadImage`
- `LoadWanVideoClipTextEncoder` ★核心
- `WanVideoVAELoader`
- `WanVideoTextEncode`

## 知识

覆盖率 **100%**（13/13）

**有卡**：`WanVideoTorchCompileSettings`、`WanVideoBlockSwap`、`LoadWanVideoT5TextEncoder`、`WanVideoModelLoader`、`WanVideoLoraSelect`、`WanVideoImageClipEncode`、`WanVideoSampler`、`WanVideoDecode`、`VHS_VideoCombine`、`LoadImage`、`LoadWanVideoClipTextEncoder`、`WanVideoVAELoader`、`WanVideoTextEncode`

**用到的条目**：LoadImage、WanVideoSampler、LoadWanVideoClipTextEncoder、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoImageClipEncode、WanVideoTextEncode、WanVideoVAELoader

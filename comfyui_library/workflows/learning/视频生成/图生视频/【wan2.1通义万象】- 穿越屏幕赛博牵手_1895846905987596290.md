---
key: 视频生成/图生视频/【wan2.1通义万象】- 穿越屏幕赛博牵手_1895846905987596290.json
name: 【wan2.1通义万象】- 穿越屏幕赛博牵手_1895846905987596290.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/【wan2.1通义万象】- 穿越屏幕赛博牵手_1895846905987596290.json
hash: cb42a16642b19264
coverage: 0.764706
learned_at: 2026-10-15 22:29:17
nodes: [WanVideoSampler, LoadWanVideoClipTextEncoder, WanVideoTorchCompileSettings, WanVideoDecode, GetNode, GetNode, LoadWanVideoT5TextEncoder, WanVideoBlockSwap, SetNode, WanVideoImageClipEncode, WanVideoVAELoader, LoadImage, SetNode, String, WanVideoModelLoader, WanVideoTextEncode, VHS_VideoCombine]
patterns: []
missing: []
---

# 视频生成/图生视频/【wan2.1通义万象】- 穿越屏幕赛博牵手_1895846905987596290.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1895846905987596290.json`

## 结构

**生成流程**：Model → Condition → Sampling → Other

**节点**（17 个）：
- `WanVideoSampler` ★核心
- `LoadWanVideoClipTextEncoder` ★核心
- `WanVideoTorchCompileSettings`
- `WanVideoDecode`
- `GetNode`
- `GetNode`
- `LoadWanVideoT5TextEncoder`
- `WanVideoBlockSwap`
- `SetNode`
- `WanVideoImageClipEncode`
- `WanVideoVAELoader`
- `LoadImage`
- `SetNode`
- `String`
- `WanVideoModelLoader`
- `WanVideoTextEncode`
- `VHS_VideoCombine`

## 知识

覆盖率 **76%**（13/17）

**有卡**：`WanVideoSampler`、`LoadWanVideoClipTextEncoder`、`WanVideoTorchCompileSettings`、`WanVideoDecode`、`LoadWanVideoT5TextEncoder`、`WanVideoBlockSwap`、`WanVideoImageClipEncode`、`WanVideoVAELoader`、`LoadImage`、`String`、`WanVideoModelLoader`、`WanVideoTextEncode`、`VHS_VideoCombine`

**用到的条目**：LoadImage、WanVideoSampler、LoadWanVideoClipTextEncoder、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoImageClipEncode、WanVideoTextEncode、WanVideoVAELoader

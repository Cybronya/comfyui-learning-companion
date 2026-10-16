---
key: 视频生成/图生视频/5秒图生视频生成 - Wan2.1_1898064124872740866.json
name: 5秒图生视频生成 - Wan2.1_1898064124872740866.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1898064124872740866.json
hash: c634f59e753190b5
coverage: 1
learned_at: 2026-10-15 22:29:19
nodes: [WanVideoBlockSwap, WanVideoTorchCompileSettings, VHS_VideoCombine, WanVideoVAELoader, WanVideoImageClipEncode, WanVideoDecode, LayerUtility: PurgeVRAM, LoadImage, Note _O, WanVideoTextEncode, WanVideoSampler, LoadWanVideoT5TextEncoder, WanVideoModelLoader, LoadWanVideoClipTextEncoder]
patterns: []
missing: []
---

# 视频生成/图生视频/5秒图生视频生成 - Wan2.1_1898064124872740866.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1898064124872740866.json`

## 结构

**生成流程**：Model → Condition → Sampling → Other

**节点**（14 个）：
- `WanVideoBlockSwap`
- `WanVideoTorchCompileSettings`
- `VHS_VideoCombine`
- `WanVideoVAELoader`
- `WanVideoImageClipEncode`
- `WanVideoDecode`
- `LayerUtility: PurgeVRAM`
- `LoadImage`
- `Note _O`
- `WanVideoTextEncode`
- `WanVideoSampler` ★核心
- `LoadWanVideoT5TextEncoder`
- `WanVideoModelLoader`
- `LoadWanVideoClipTextEncoder` ★核心

## 知识

覆盖率 **100%**（14/14）

**有卡**：`WanVideoBlockSwap`、`WanVideoTorchCompileSettings`、`VHS_VideoCombine`、`WanVideoVAELoader`、`WanVideoImageClipEncode`、`WanVideoDecode`、`LayerUtility: PurgeVRAM`、`LoadImage`、`Note _O`、`WanVideoTextEncode`、`WanVideoSampler`、`LoadWanVideoT5TextEncoder`、`WanVideoModelLoader`、`LoadWanVideoClipTextEncoder`

**用到的条目**：LoadImage、WanVideoSampler、LoadWanVideoClipTextEncoder、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoImageClipEncode、WanVideoTextEncode、WanVideoVAELoader

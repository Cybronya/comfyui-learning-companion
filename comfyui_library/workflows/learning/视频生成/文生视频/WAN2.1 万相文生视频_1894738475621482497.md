---
key: 视频生成/文生视频/WAN2.1 万相文生视频_1894738475621482497.json
name: WAN2.1 万相文生视频_1894738475621482497.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/1894738475621482497.json
hash: 3d496a0caf816a29
coverage: 1
learned_at: 2026-10-15 22:43:20
nodes: [WanVideoVAELoader, WanVideoTextEncode, WanVideoEmptyEmbeds, easy cleanGpuUsed, WanVideoModelLoader, WanVideoSampler, WanVideoDecode, ImageUpscaleWithModel, RIFE VFI, UpscaleModelLoader, easy cleanGpuUsed, VHS_VideoCombine, SeargePromptText, LoadWanVideoT5TextEncoder, WanVideoTorchCompileSettings, WanVideoBlockSwap]
patterns: []
missing: []
---

# 视频生成/文生视频/WAN2.1 万相文生视频_1894738475621482497.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/1894738475621482497.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（16 个）：
- `WanVideoVAELoader`
- `WanVideoTextEncode`
- `WanVideoEmptyEmbeds`
- `easy cleanGpuUsed`
- `WanVideoModelLoader`
- `WanVideoSampler` ★核心
- `WanVideoDecode`
- `ImageUpscaleWithModel`
- `RIFE VFI`
- `UpscaleModelLoader`
- `easy cleanGpuUsed`
- `VHS_VideoCombine`
- `SeargePromptText`
- `LoadWanVideoT5TextEncoder`
- `WanVideoTorchCompileSettings`
- `WanVideoBlockSwap`

## 知识

覆盖率 **100%**（16/16）

**有卡**：`WanVideoVAELoader`、`WanVideoTextEncode`、`WanVideoEmptyEmbeds`、`easy cleanGpuUsed`、`WanVideoModelLoader`、`WanVideoSampler`、`WanVideoDecode`、`ImageUpscaleWithModel`、`RIFE VFI`、`UpscaleModelLoader`、`VHS_VideoCombine`、`SeargePromptText`、`LoadWanVideoT5TextEncoder`、`WanVideoTorchCompileSettings`、`WanVideoBlockSwap`

**用到的条目**：WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、ImageUpscaleWithModel、UpscaleModelLoader、UpscaleModelLoader

---
key: 视频生成/文生视频/WAN2.1 万相文生视频_2012869543177228289.json
name: WAN2.1 万相文生视频_2012869543177228289
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/WAN2.1 万相文生视频_2012869543177228289.json
hash: a7d64be5a605adba
coverage: 1
learned_at: 2026-10-15 22:47:03
nodes: [WanVideoVAELoader, WanVideoEmptyEmbeds, easy cleanGpuUsed, WanVideoModelLoader, WanVideoSampler, WanVideoDecode, WanVideoBlockSwap, LoadWanVideoT5TextEncoder, WanVideoTorchCompileSettings, easy cleanGpuUsed, ImageUpscaleWithModel, UpscaleModelLoader, RIFE VFI, VHS_VideoCombine, SeargePromptText, WanVideoTextEncode]
patterns: []
missing: []
---

# 视频生成/文生视频/WAN2.1 万相文生视频_2012869543177228289.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/WAN2.1 万相文生视频_2012869543177228289.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（16 个）：
- `WanVideoVAELoader`
- `WanVideoEmptyEmbeds`
- `easy cleanGpuUsed`
- `WanVideoModelLoader`
- `WanVideoSampler` ★核心
- `WanVideoDecode`
- `WanVideoBlockSwap`
- `LoadWanVideoT5TextEncoder`
- `WanVideoTorchCompileSettings`
- `easy cleanGpuUsed`
- `ImageUpscaleWithModel`
- `UpscaleModelLoader`
- `RIFE VFI`
- `VHS_VideoCombine`
- `SeargePromptText`
- `WanVideoTextEncode`

## 知识

覆盖率 **100%**（16/16）

**有卡**：`WanVideoVAELoader`、`WanVideoEmptyEmbeds`、`easy cleanGpuUsed`、`WanVideoModelLoader`、`WanVideoSampler`、`WanVideoDecode`、`WanVideoBlockSwap`、`LoadWanVideoT5TextEncoder`、`WanVideoTorchCompileSettings`、`ImageUpscaleWithModel`、`UpscaleModelLoader`、`RIFE VFI`、`VHS_VideoCombine`、`SeargePromptText`、`WanVideoTextEncode`

**用到的条目**：WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、ImageUpscaleWithModel、UpscaleModelLoader、UpscaleModelLoader

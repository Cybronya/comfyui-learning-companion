---
key: 视频生成/文生视频/WAN2.1 万相文生视频_2013157670638850049.json
name: WAN2.1 万相文生视频_2013157670638850049
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/WAN2.1 万相文生视频_2013157670638850049.json
hash: a87e79e5fbfdc747
coverage: 1
learned_at: 2026-10-15 22:47:03
nodes: [WanVideoVAELoader, WanVideoEmptyEmbeds, easy cleanGpuUsed, WanVideoModelLoader, WanVideoSampler, WanVideoDecode, WanVideoBlockSwap, LoadWanVideoT5TextEncoder, WanVideoTorchCompileSettings, easy cleanGpuUsed, ImageUpscaleWithModel, UpscaleModelLoader, RIFE VFI, VHS_VideoCombine, WanVideoTextEncode, SeargePromptText]
patterns: []
missing: []
---

# 视频生成/文生视频/WAN2.1 万相文生视频_2013157670638850049.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/WAN2.1 万相文生视频_2013157670638850049.json`

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
- `WanVideoTextEncode`
- `SeargePromptText`

## 知识

覆盖率 **100%**（16/16）

**有卡**：`WanVideoVAELoader`、`WanVideoEmptyEmbeds`、`easy cleanGpuUsed`、`WanVideoModelLoader`、`WanVideoSampler`、`WanVideoDecode`、`WanVideoBlockSwap`、`LoadWanVideoT5TextEncoder`、`WanVideoTorchCompileSettings`、`ImageUpscaleWithModel`、`UpscaleModelLoader`、`RIFE VFI`、`VHS_VideoCombine`、`WanVideoTextEncode`、`SeargePromptText`

**用到的条目**：WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、ImageUpscaleWithModel、UpscaleModelLoader、UpscaleModelLoader

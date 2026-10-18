---
key: 视频生成/文生视频/Wan2.1最新FusionX LORA  2分钟生视频_1935600068689068033.json
name: Wan2.1最新FusionX LORA  2分钟生视频_1935600068689068033.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/Wan2.1最新FusionX LORA  2分钟生视频_1935600068689068033.json
hash: 3f331a9cb3adacb7
coverage: 1
learned_at: 2026-10-15 22:43:29
nodes: [WanVideoBlockSwap, WanVideoModelLoader, LoadWanVideoT5TextEncoder, WanVideoVAELoader, VHS_VideoCombine, WanVideoTorchCompileSettings, WanVideoModelLoader, WanVideoDecode, WanVideoSampler, WanVideoEmptyEmbeds, WanVideoLoraSelect, WanVideoTextEncode]
patterns: []
missing: []
---

# 视频生成/文生视频/Wan2.1最新FusionX LORA  2分钟生视频_1935600068689068033.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/1935600068689068033.json`

## 结构

**生成流程**：Model → Sampling → Other

**节点**（12 个）：
- `WanVideoBlockSwap`
- `WanVideoModelLoader`
- `LoadWanVideoT5TextEncoder`
- `WanVideoVAELoader`
- `VHS_VideoCombine`
- `WanVideoTorchCompileSettings`
- `WanVideoModelLoader`
- `WanVideoDecode`
- `WanVideoSampler` ★核心
- `WanVideoEmptyEmbeds`
- `WanVideoLoraSelect`
- `WanVideoTextEncode`

## 知识

覆盖率 **100%**（12/12）

**有卡**：`WanVideoBlockSwap`、`WanVideoModelLoader`、`LoadWanVideoT5TextEncoder`、`WanVideoVAELoader`、`VHS_VideoCombine`、`WanVideoTorchCompileSettings`、`WanVideoDecode`、`WanVideoSampler`、`WanVideoEmptyEmbeds`、`WanVideoLoraSelect`、`WanVideoTextEncode`

**用到的条目**：WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoLoraSelect、VHS_VideoCombine、WanVideoBlockSwap

---
key: 视频生成/图生视频/文生视频 Wrapper-SelfForcing-TextToVideo-60FPS_1937763177356509185.json
name: 文生视频 Wrapper-SelfForcing-TextToVideo-60FPS_1937763177356509185.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1937763177356509185.json
hash: a9b7aa19932d6993
coverage: 0.615385
learned_at: 2026-10-15 22:30:29
nodes: [SetNode, Anything Everywhere, Reroute, Reroute, Note, Note, Reroute, Reroute, VHS_VideoCombine, WanVideoEnhanceAVideo, Reroute, WanVideoDecode, easy cleanGpuUsed, Reroute, RIFE VFI, WanVideoVAELoader, WanVideoBlockSwap, WanVideoModelLoader, WanVideoLoraSelect, Reroute, easy clearCacheAll, Int, Text Prompt (JPS), WanVideoSampler, easy cleanGpuUsed, WanVideoTextEncode, easy clearCacheAll, Note, WanVideoLoraSelect, easy cleanGpuUsed, Reroute, easy cleanGpuUsed, UpscaleModelLoader, Reroute, VHS_VideoCombine, WanVideoEmptyEmbeds, LoadWanVideoT5TextEncoder, Note, Text Prompt (JPS)]
patterns: []
missing: []
---

# 视频生成/图生视频/文生视频 Wrapper-SelfForcing-TextToVideo-60FPS_1937763177356509185.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1937763177356509185.json`

## 结构

**生成流程**：Model → Sampling → Other

**节点**（39 个）：
- `SetNode`
- `Anything Everywhere`
- `Reroute`
- `Reroute`
- `Note`
- `Note`
- `Reroute`
- `Reroute`
- `VHS_VideoCombine`
- `WanVideoEnhanceAVideo`
- `Reroute`
- `WanVideoDecode`
- `easy cleanGpuUsed`
- `Reroute`
- `RIFE VFI`
- `WanVideoVAELoader`
- `WanVideoBlockSwap`
- `WanVideoModelLoader`
- `WanVideoLoraSelect`
- `Reroute`
- `easy clearCacheAll`
- `Int`
- `Text Prompt (JPS)`
- `WanVideoSampler` ★核心
- `easy cleanGpuUsed`
- `WanVideoTextEncode`
- `easy clearCacheAll`
- `Note`
- `WanVideoLoraSelect`
- `easy cleanGpuUsed`
- `Reroute`
- `easy cleanGpuUsed`
- `UpscaleModelLoader`
- `Reroute`
- `VHS_VideoCombine`
- `WanVideoEmptyEmbeds`
- `LoadWanVideoT5TextEncoder`
- `Note`
- `Text Prompt (JPS)`

## 知识

覆盖率 **62%**（24/39）

**有卡**：`VHS_VideoCombine`、`WanVideoEnhanceAVideo`、`WanVideoDecode`、`easy cleanGpuUsed`、`RIFE VFI`、`WanVideoVAELoader`、`WanVideoBlockSwap`、`WanVideoModelLoader`、`WanVideoLoraSelect`、`easy clearCacheAll`、`Int`、`Text Prompt (JPS)`、`WanVideoSampler`、`WanVideoTextEncode`、`UpscaleModelLoader`、`WanVideoEmptyEmbeds`、`LoadWanVideoT5TextEncoder`

**用到的条目**：WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoLoraSelect、UpscaleModelLoader、UpscaleModelLoader

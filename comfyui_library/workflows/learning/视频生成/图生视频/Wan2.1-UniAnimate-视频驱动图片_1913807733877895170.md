---
key: 视频生成/图生视频/Wan2.1-UniAnimate-视频驱动图片_1913807733877895170.json
name: Wan2.1-UniAnimate-视频驱动图片_1913807733877895170.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/Wan2.1-UniAnimate-视频驱动图片_1913807733877895170.json
hash: 9478f16a7954efd1
coverage: 0.543478
learned_at: 2026-10-15 22:29:34
nodes: [WanVideoExperimentalArgs, WanVideoTeaCache, WanVideoSLG, SetNode, SetNode, SetNode, SetNode, Florence2ModelLoader, SetNode, SetNode, SetNode, SetNode, SetNode, SetNode, LayerUtility: PurgeVRAM, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, WanVideoEnhanceAVideo, WanVideoTextEncode, GetNode, WanVideoDecode, WanVideoSampler, Florence2Run, ImageResizeKJ, ImageResizeKJ, GetNode, GetNode, WanVideoClipVisionEncode, WanVideoUniAnimateDWPoseDetector, WanVideoUniAnimatePoseInput, WanVideoImageToVideoEncode, LoadImage, WanVideoModelLoader, WanVideoLoraSelect, LoadWanVideoT5TextEncoder, LoadWanVideoClipTextEncoder, WanVideoVAELoader, WanVideoBlockSwap, VHS_LoadVideo, VHS_VideoCombine]
patterns: []
missing: []
---

# 视频生成/图生视频/Wan2.1-UniAnimate-视频驱动图片_1913807733877895170.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1913807733877895170.json`

## 结构

**生成流程**：Model → Condition → Sampling → Process → Other

**节点**（46 个）：
- `WanVideoExperimentalArgs`
- `WanVideoTeaCache`
- `WanVideoSLG`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `Florence2ModelLoader`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `LayerUtility: PurgeVRAM`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `WanVideoEnhanceAVideo`
- `WanVideoTextEncode`
- `GetNode`
- `WanVideoDecode`
- `WanVideoSampler` ★核心
- `Florence2Run`
- `ImageResizeKJ`
- `ImageResizeKJ`
- `GetNode`
- `GetNode`
- `WanVideoClipVisionEncode`
- `WanVideoUniAnimateDWPoseDetector`
- `WanVideoUniAnimatePoseInput`
- `WanVideoImageToVideoEncode`
- `LoadImage`
- `WanVideoModelLoader`
- `WanVideoLoraSelect`
- `LoadWanVideoT5TextEncoder`
- `LoadWanVideoClipTextEncoder` ★核心
- `WanVideoVAELoader`
- `WanVideoBlockSwap`
- `VHS_LoadVideo`
- `VHS_VideoCombine`

## 知识

覆盖率 **54%**（25/46）

**有卡**：`WanVideoExperimentalArgs`、`WanVideoTeaCache`、`WanVideoSLG`、`Florence2ModelLoader`、`LayerUtility: PurgeVRAM`、`WanVideoEnhanceAVideo`、`WanVideoTextEncode`、`WanVideoDecode`、`WanVideoSampler`、`Florence2Run`、`ImageResizeKJ`、`WanVideoClipVisionEncode`、`WanVideoUniAnimateDWPoseDetector`、`WanVideoUniAnimatePoseInput`、`WanVideoImageToVideoEncode`、`LoadImage`、`WanVideoModelLoader`、`WanVideoLoraSelect`、`LoadWanVideoT5TextEncoder`、`LoadWanVideoClipTextEncoder`、`WanVideoVAELoader`、`WanVideoBlockSwap`、`VHS_LoadVideo`、`VHS_VideoCombine`

**用到的条目**：LoadImage、WanVideoSampler、LoadWanVideoClipTextEncoder、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoClipVisionEncode

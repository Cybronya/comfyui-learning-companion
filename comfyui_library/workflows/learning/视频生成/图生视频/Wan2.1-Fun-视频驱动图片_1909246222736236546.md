---
key: 视频生成/图生视频/Wan2.1-Fun-视频驱动图片_1909246222736236546.json
name: Wan2.1-Fun-视频驱动图片_1909246222736236546.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1909246222736236546.json
hash: 3ee05eee3a7dd0ea
coverage: 0.541667
learned_at: 2026-10-15 22:29:29
nodes: [WanVideoExperimentalArgs, WanVideoTeaCache, WanVideoSLG, SetNode, SetNode, SetNode, SetNode, Florence2ModelLoader, SetNode, ImageResizeKJ, ImageResizeKJ, SetNode, SetNode, SetNode, SetNode, LayerUtility: PurgeVRAM, WanVideoEncode, GetNode, GetNode, GetNode, GetNode, GetNode, WanVideoControlEmbeds, GetNode, GetNode, GetNode, WanVideoEnhanceAVideo, WanVideoTextEncode, GetNode, WanVideoImageToVideoEncode, GetNode, WanVideoSampler, WanVideoDecode, PreviewImage, WanVideoModelLoader, LoadWanVideoT5TextEncoder, LoadWanVideoClipTextEncoder, WanVideoVAELoader, SetNode, AIO_Preprocessor, VHS_LoadVideo, Florence2Run, LoadImage, VHS_VideoCombine, VHS_VideoCombine, WanVideoBlockSwap, GetNode, WanVideoClipVisionEncode]
patterns: []
missing: []
---

# 视频生成/图生视频/Wan2.1-Fun-视频驱动图片_1909246222736236546.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1909246222736236546.json`

## 结构

**生成流程**：Model → Condition → Sampling → Process → Output → Other

**节点**（48 个）：
- `WanVideoExperimentalArgs`
- `WanVideoTeaCache`
- `WanVideoSLG`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `Florence2ModelLoader`
- `SetNode`
- `ImageResizeKJ`
- `ImageResizeKJ`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `LayerUtility: PurgeVRAM`
- `WanVideoEncode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `WanVideoControlEmbeds`
- `GetNode`
- `GetNode`
- `GetNode`
- `WanVideoEnhanceAVideo`
- `WanVideoTextEncode`
- `GetNode`
- `WanVideoImageToVideoEncode`
- `GetNode`
- `WanVideoSampler` ★核心
- `WanVideoDecode`
- `PreviewImage`
- `WanVideoModelLoader`
- `LoadWanVideoT5TextEncoder`
- `LoadWanVideoClipTextEncoder` ★核心
- `WanVideoVAELoader`
- `SetNode`
- `AIO_Preprocessor`
- `VHS_LoadVideo`
- `Florence2Run`
- `LoadImage`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `GetNode`
- `WanVideoClipVisionEncode`

## 知识

覆盖率 **54%**（26/48）

**有卡**：`WanVideoExperimentalArgs`、`WanVideoTeaCache`、`WanVideoSLG`、`Florence2ModelLoader`、`ImageResizeKJ`、`LayerUtility: PurgeVRAM`、`WanVideoEncode`、`WanVideoControlEmbeds`、`WanVideoEnhanceAVideo`、`WanVideoTextEncode`、`WanVideoImageToVideoEncode`、`WanVideoSampler`、`WanVideoDecode`、`WanVideoModelLoader`、`LoadWanVideoT5TextEncoder`、`LoadWanVideoClipTextEncoder`、`WanVideoVAELoader`、`AIO_Preprocessor`、`VHS_LoadVideo`、`Florence2Run`、`LoadImage`、`VHS_VideoCombine`、`WanVideoBlockSwap`、`WanVideoClipVisionEncode`

**用到的条目**：LoadImage、WanVideoSampler、LoadWanVideoClipTextEncoder、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoClipVisionEncode

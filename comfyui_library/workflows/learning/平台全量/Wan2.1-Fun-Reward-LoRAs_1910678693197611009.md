---
key: 平台全量/Wan2.1-Fun-Reward-LoRAs_1910678693197611009.json
name: Wan2.1-Fun-Reward-LoRAs_1910678693197611009
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/Wan2.1-Fun-Reward-LoRAs_1910678693197611009.json
hash: 9516f0cf27fd45fd
coverage: 0.588235
learned_at: 2026-11-14 01:04:35
nodes: [WanVideoExperimentalArgs, WanVideoTeaCache, WanVideoSLG, WanVideoBlockSwap, SetNode, SetNode, SetNode, SetNode, AIO_Preprocessor, Florence2ModelLoader, SetNode, VHS_VideoCombine, ImageBlend, ImageResizeKJ, ImageResizeKJ, SetNode, SetNode, SetNode, SetNode, SetNode, LayerUtility: PurgeVRAM, WanVideoEncode, GetNode, GetNode, GetNode, GetNode, GetNode, WanVideoControlEmbeds, GetNode, GetNode, GetNode, WanVideoEnhanceAVideo, WanVideoTextEncode, GetNode, WanVideoImageToVideoEncode, WanVideoClipVisionEncode, WanVideoSampler, WanVideoDecode, VHS_VideoCombine, AIO_Preprocessor, WanVideoLoraSelect, WanVideoLoraSelect, LoadWanVideoT5TextEncoder, LoadWanVideoClipTextEncoder, WanVideoVAELoader, WanVideoModelLoader, Florence2Run, GetNode, GetNode, LoadImage, VHS_LoadVideo]
patterns: []
missing: []
---

# 平台全量/Wan2.1-Fun-Reward-LoRAs_1910678693197611009.json

> 来源文件 `comfyui_library/workflows/平台全量/Wan2.1-Fun-Reward-LoRAs_1910678693197611009.json`

## 结构

**生成流程**：Model → Condition → Sampling → Process → Other

**节点**（51 个）：
- `WanVideoExperimentalArgs`
- `WanVideoTeaCache`
- `WanVideoSLG`
- `WanVideoBlockSwap`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `AIO_Preprocessor`
- `Florence2ModelLoader`
- `SetNode`
- `VHS_VideoCombine`
- `ImageBlend`
- `ImageResizeKJ`
- `ImageResizeKJ`
- `SetNode`
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
- `WanVideoClipVisionEncode`
- `WanVideoSampler` ★核心
- `WanVideoDecode`
- `VHS_VideoCombine`
- `AIO_Preprocessor`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `LoadWanVideoT5TextEncoder`
- `LoadWanVideoClipTextEncoder` ★核心
- `WanVideoVAELoader`
- `WanVideoModelLoader`
- `Florence2Run`
- `GetNode`
- `GetNode`
- `LoadImage`
- `VHS_LoadVideo`

## 知识

覆盖率 **59%**（30/51）

**有卡**：`WanVideoExperimentalArgs`、`WanVideoTeaCache`、`WanVideoSLG`、`WanVideoBlockSwap`、`AIO_Preprocessor`、`Florence2ModelLoader`、`VHS_VideoCombine`、`ImageBlend`、`ImageResizeKJ`、`LayerUtility: PurgeVRAM`、`WanVideoEncode`、`WanVideoControlEmbeds`、`WanVideoEnhanceAVideo`、`WanVideoTextEncode`、`WanVideoImageToVideoEncode`、`WanVideoClipVisionEncode`、`WanVideoSampler`、`WanVideoDecode`、`WanVideoLoraSelect`、`LoadWanVideoT5TextEncoder`、`LoadWanVideoClipTextEncoder`、`WanVideoVAELoader`、`WanVideoModelLoader`、`Florence2Run`、`LoadImage`、`VHS_LoadVideo`

**用到的条目**：LoadImage、WanVideoSampler、LoadWanVideoClipTextEncoder、LoadWanVideoT5TextEncoder、WanVideoClipVisionEncode、WanVideoDecode、WanVideoEncode、WanVideoImageToVideoEncode

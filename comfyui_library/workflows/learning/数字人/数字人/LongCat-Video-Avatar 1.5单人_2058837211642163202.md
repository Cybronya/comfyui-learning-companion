---
key: 数字人/数字人/LongCat-Video-Avatar 1.5单人_2058837211642163202.json
name: LongCat-Video-Avatar 1.5单人_2058837211642163202
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/数字人/数字人/LongCat-Video-Avatar 1.5单人_2058837211642163202.json
hash: 719181d56c7888aa
coverage: 0.923077
learned_at: 2026-10-26 01:56:21
nodes: [WanVideoBlockSwap, LoadWanVideoT5TextEncoder, ImageResizeKJv2, WanVideoSetBlockSwap, WanVideoBlockSwap, WhisperModelLoader, Evaluate Floats, TrimAudioDuration, ComfyNumberConvert, WanVideoVAELoader, WanVideoLongCatAvatarExtendEmbeds, FloatConstant, FloatConstant, WanVideoEncode, LongCatAvatarWhisperEmbeds, WanVideoTextEncode, LoadImage, WanVideoLoraSelect, PrimitiveNode, LoadAudio, easy showAnything, WanVideoSchedulerv2, WanVideoModelLoader, WanVideoSamplerv2, WanVideoDecode, VHS_VideoCombine]
patterns: []
missing: []
---

# 数字人/数字人/LongCat-Video-Avatar 1.5单人_2058837211642163202.json

> 来源文件 `comfyui_library/workflows/数字人/数字人/LongCat-Video-Avatar 1.5单人_2058837211642163202.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（26 个）：
- `WanVideoBlockSwap`
- `LoadWanVideoT5TextEncoder`
- `ImageResizeKJv2`
- `WanVideoSetBlockSwap`
- `WanVideoBlockSwap`
- `WhisperModelLoader`
- `Evaluate Floats`
- `TrimAudioDuration`
- `ComfyNumberConvert`
- `WanVideoVAELoader`
- `WanVideoLongCatAvatarExtendEmbeds`
- `FloatConstant`
- `FloatConstant`
- `WanVideoEncode`
- `LongCatAvatarWhisperEmbeds`
- `WanVideoTextEncode`
- `LoadImage`
- `WanVideoLoraSelect`
- `PrimitiveNode`
- `LoadAudio`
- `easy showAnything`
- `WanVideoSchedulerv2`
- `WanVideoModelLoader`
- `WanVideoSamplerv2` ★核心
- `WanVideoDecode`
- `VHS_VideoCombine`

## 知识

覆盖率 **92%**（24/26）

**有卡**：`WanVideoBlockSwap`、`LoadWanVideoT5TextEncoder`、`ImageResizeKJv2`、`WanVideoSetBlockSwap`、`WhisperModelLoader`、`Evaluate Floats`、`TrimAudioDuration`、`ComfyNumberConvert`、`WanVideoVAELoader`、`WanVideoLongCatAvatarExtendEmbeds`、`FloatConstant`、`WanVideoEncode`、`LongCatAvatarWhisperEmbeds`、`WanVideoTextEncode`、`LoadImage`、`WanVideoLoraSelect`、`LoadAudio`、`WanVideoSchedulerv2`、`WanVideoModelLoader`、`WanVideoSamplerv2`、`WanVideoDecode`、`VHS_VideoCombine`

**用到的条目**：LoadImage、WanVideoSamplerv2、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoEncode、WanVideoLoraSelect

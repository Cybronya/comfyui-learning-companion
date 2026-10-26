---
key: 数字人/数字人/LongCat-Video-Avatar 1.5数字人_2058887899709534210.json
name: LongCat-Video-Avatar 1.5数字人_2058887899709534210
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/数字人/数字人/LongCat-Video-Avatar 1.5数字人_2058887899709534210.json
hash: 506c40229c2062b3
coverage: 1
learned_at: 2026-10-26 01:56:21
nodes: [FloatConstant, FloatConstant, VHS_VideoCombine, WanVideoModelLoader, WanVideoBlockSwap, WanVideoLoraSelect, LoadWanVideoT5TextEncoder, WhisperModelLoader, ComfyNumberConvert, TrimAudioDuration, WanVideoLongCatAvatarExtendEmbeds, WanVideoTextEncode, LoadAudio, WanVideoSchedulerv2, WanVideoVAELoader, ImageResizeKJv2, LongCatAvatarWhisperEmbeds, WanVideoDecode, WanVideoEncode, Evaluate Floats, WanVideoSamplerv2, LoadImage]
patterns: []
missing: []
---

# 数字人/数字人/LongCat-Video-Avatar 1.5数字人_2058887899709534210.json

> 来源文件 `comfyui_library/workflows/数字人/数字人/LongCat-Video-Avatar 1.5数字人_2058887899709534210.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（22 个）：
- `FloatConstant`
- `FloatConstant`
- `VHS_VideoCombine`
- `WanVideoModelLoader`
- `WanVideoBlockSwap`
- `WanVideoLoraSelect`
- `LoadWanVideoT5TextEncoder`
- `WhisperModelLoader`
- `ComfyNumberConvert`
- `TrimAudioDuration`
- `WanVideoLongCatAvatarExtendEmbeds`
- `WanVideoTextEncode`
- `LoadAudio`
- `WanVideoSchedulerv2`
- `WanVideoVAELoader`
- `ImageResizeKJv2`
- `LongCatAvatarWhisperEmbeds`
- `WanVideoDecode`
- `WanVideoEncode`
- `Evaluate Floats`
- `WanVideoSamplerv2` ★核心
- `LoadImage`

## 知识

覆盖率 **100%**（22/22）

**有卡**：`FloatConstant`、`VHS_VideoCombine`、`WanVideoModelLoader`、`WanVideoBlockSwap`、`WanVideoLoraSelect`、`LoadWanVideoT5TextEncoder`、`WhisperModelLoader`、`ComfyNumberConvert`、`TrimAudioDuration`、`WanVideoLongCatAvatarExtendEmbeds`、`WanVideoTextEncode`、`LoadAudio`、`WanVideoSchedulerv2`、`WanVideoVAELoader`、`ImageResizeKJv2`、`LongCatAvatarWhisperEmbeds`、`WanVideoDecode`、`WanVideoEncode`、`Evaluate Floats`、`WanVideoSamplerv2`、`LoadImage`

**用到的条目**：LoadImage、WanVideoSamplerv2、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoEncode、WanVideoLoraSelect

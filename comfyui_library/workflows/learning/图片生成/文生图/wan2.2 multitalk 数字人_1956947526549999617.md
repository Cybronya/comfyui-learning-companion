---
key: 图片生成/文生图/wan2.2 multitalk 数字人_1956947526549999617.json
name: wan2.2 multitalk 数字人_1956947526549999617
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/wan2.2 multitalk 数字人_1956947526549999617.json
hash: 352318c79dfe2ff5
coverage: 0.612245
learned_at: 2026-10-15 22:27:57
nodes: [WanVideoBlockSwap, WanVideoTorchCompileSettings, MultiTalkModelLoader, WanVideoBlockSwap, SetNode, SetNode, GetNode, SetNode, SetNode, DownloadAndLoadWav2VecModel, SetNode, GetNode, GetNode, WanVideoDecode, GetNode, LoadWanVideoT5TextEncoder, GetNode, GetNode, GetNode, WanVideoModelLoader, WanVideoTorchCompileSettings, WanVideoModelLoader, WanVideoLoraSelect, WanVideoLoraSelect, SimpleMath+, GetNode, CLIPVisionLoader, SetNode, WanVideoVAELoader, MultiTalkWav2VecEmbeds, AudioCrop, RH_GetAudioDuration, GetNode, WanVideoClipVisionEncode, WanVideoSampler, ImageResizeKJv2, WanVideoImageToVideoEncode, LoadImage, WanVideoTextEncode, LoadAudio, VHS_VideoCombine, Int, Int, SetNode, SetNode, SetNode, WanVideoSampler, MultiTalkModelLoader, GetNode]
patterns: []
missing: []
---

# 图片生成/文生图/wan2.2 multitalk 数字人_1956947526549999617.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/wan2.2 multitalk 数字人_1956947526549999617.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（49 个）：
- `WanVideoBlockSwap`
- `WanVideoTorchCompileSettings`
- `MultiTalkModelLoader`
- `WanVideoBlockSwap`
- `SetNode`
- `SetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `DownloadAndLoadWav2VecModel`
- `SetNode`
- `GetNode`
- `GetNode`
- `WanVideoDecode`
- `GetNode`
- `LoadWanVideoT5TextEncoder`
- `GetNode`
- `GetNode`
- `GetNode`
- `WanVideoModelLoader`
- `WanVideoTorchCompileSettings`
- `WanVideoModelLoader`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `SimpleMath+`
- `GetNode`
- `CLIPVisionLoader`
- `SetNode`
- `WanVideoVAELoader`
- `MultiTalkWav2VecEmbeds`
- `AudioCrop`
- `RH_GetAudioDuration`
- `GetNode`
- `WanVideoClipVisionEncode`
- `WanVideoSampler` ★核心
- `ImageResizeKJv2`
- `WanVideoImageToVideoEncode`
- `LoadImage`
- `WanVideoTextEncode`
- `LoadAudio`
- `VHS_VideoCombine`
- `Int`
- `Int`
- `SetNode`
- `SetNode`
- `SetNode`
- `WanVideoSampler` ★核心
- `MultiTalkModelLoader`
- `GetNode`

## 知识

覆盖率 **61%**（30/49）

**有卡**：`WanVideoBlockSwap`、`WanVideoTorchCompileSettings`、`MultiTalkModelLoader`、`DownloadAndLoadWav2VecModel`、`WanVideoDecode`、`LoadWanVideoT5TextEncoder`、`WanVideoModelLoader`、`WanVideoLoraSelect`、`SimpleMath+`、`CLIPVisionLoader`、`WanVideoVAELoader`、`MultiTalkWav2VecEmbeds`、`AudioCrop`、`RH_GetAudioDuration`、`WanVideoClipVisionEncode`、`WanVideoSampler`、`ImageResizeKJv2`、`WanVideoImageToVideoEncode`、`LoadImage`、`WanVideoTextEncode`、`LoadAudio`、`VHS_VideoCombine`、`Int`

**用到的条目**：LoadImage、WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoImageToVideoEncode

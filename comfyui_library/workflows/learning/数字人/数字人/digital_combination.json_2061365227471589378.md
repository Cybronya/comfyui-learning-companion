---
key: 数字人/数字人/digital_combination.json_2061365227471589378.json
name: digital_combination.json_2061365227471589378
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/数字人/数字人/digital_combination.json_2061365227471589378.json
hash: ee91725037be83af
coverage: 0.964286
learned_at: 2026-10-26 01:58:30
nodes: [WanVideoDecode, WanVideoImageToVideoMultiTalk, WanVideoVAELoader, LoadWanVideoT5TextEncoder, AudioSeparation, WanVideoModelLoader, easy showAnything, CLIPVisionLoader, MultiTalkWav2VecEmbeds, VHS_VideoCombine, MultiTalkModelLoader, WanVideoTorchCompileSettings, WanVideoLoraSelect, WanVideoBlockSwap, RH_GetAudioDuration, ToInt, Int, SimpleMath+, AudioCrop, DownloadAndLoadWav2VecModel, WanVideoSampler, WanVideoClipVisionEncode, easy int, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, WanVideoTextEncode, ImageResizeKJv2, VHS_LoadAudioUpload]
patterns: []
missing: []
---

# 数字人/数字人/digital_combination.json_2061365227471589378.json

> 来源文件 `comfyui_library/workflows/数字人/数字人/digital_combination.json_2061365227471589378.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（28 个）：
- `WanVideoDecode`
- `WanVideoImageToVideoMultiTalk`
- `WanVideoVAELoader`
- `LoadWanVideoT5TextEncoder`
- `AudioSeparation`
- `WanVideoModelLoader`
- `easy showAnything`
- `CLIPVisionLoader`
- `MultiTalkWav2VecEmbeds`
- `VHS_VideoCombine`
- `MultiTalkModelLoader`
- `WanVideoTorchCompileSettings`
- `WanVideoLoraSelect`
- `WanVideoBlockSwap`
- `RH_GetAudioDuration`
- `ToInt`
- `Int`
- `SimpleMath+`
- `AudioCrop`
- `DownloadAndLoadWav2VecModel`
- `WanVideoSampler` ★核心
- `WanVideoClipVisionEncode`
- `easy int`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `WanVideoTextEncode`
- `ImageResizeKJv2`
- `VHS_LoadAudioUpload`

## 知识

覆盖率 **96%**（27/28）

**有卡**：`WanVideoDecode`、`WanVideoImageToVideoMultiTalk`、`WanVideoVAELoader`、`LoadWanVideoT5TextEncoder`、`AudioSeparation`、`WanVideoModelLoader`、`CLIPVisionLoader`、`MultiTalkWav2VecEmbeds`、`VHS_VideoCombine`、`MultiTalkModelLoader`、`WanVideoTorchCompileSettings`、`WanVideoLoraSelect`、`WanVideoBlockSwap`、`RH_GetAudioDuration`、`ToInt`、`Int`、`SimpleMath+`、`AudioCrop`、`DownloadAndLoadWav2VecModel`、`WanVideoSampler`、`WanVideoClipVisionEncode`、`easy int`、`LayerUtility: ImageScaleByAspectRatio V2`、`LoadImage`、`WanVideoTextEncode`、`ImageResizeKJv2`、`VHS_LoadAudioUpload`

**用到的条目**：LoadImage、LayerUtility: ImageScaleByAspectRatio V2、WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoClipVisionEncode

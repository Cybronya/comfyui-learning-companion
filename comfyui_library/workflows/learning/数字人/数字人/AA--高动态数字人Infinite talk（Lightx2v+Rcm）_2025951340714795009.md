---
key: 数字人/数字人/AA--高动态数字人Infinite talk（Lightx2v+Rcm）_2025951340714795009.json
name: AA--高动态数字人Infinite talk（Lightx2v+Rcm）_2025951340714795009
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/数字人/数字人/AA--高动态数字人Infinite talk（Lightx2v+Rcm）_2025951340714795009.json
hash: 6e043d5823275ffa
coverage: 0.828571
learned_at: 2026-10-26 01:53:34
nodes: [WanVideoLoraSelect, WanVideoBlockSwap, MultiTalkModelLoader, PreviewAny, CLIPVisionLoader, LoadWanVideoT5TextEncoder, VHS_VideoCombine, WanVideoModelLoader, MultiTalkWav2VecEmbeds, LayerUtility: ImageScaleByAspectRatio V2, AudioCrop, WanVideoSampler, WanVideoDecode, WanVideoTextEncode, WanVideoImageToVideoMultiTalk, GetImageSizeAndCount, Note, RH_GetAudioDuration, easy showAnything, JWInteger, CastAnyToIntStringFloat, AudioSeparation, WanVideoLoraSelect, WanVideoClipVisionEncode, WanVideoVAELoader, DownloadAndLoadWav2VecModel, easy mathInt, easy mathInt, Note, easy showAnything, VHS_VideoCombine, LoadImage, LoadAudio, CR Prompt Text, Note]
patterns: []
missing: []
---

# 数字人/数字人/AA--高动态数字人Infinite talk（Lightx2v+Rcm）_2025951340714795009.json

> 来源文件 `comfyui_library/workflows/数字人/数字人/AA--高动态数字人Infinite talk（Lightx2v+Rcm）_2025951340714795009.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（35 个）：
- `WanVideoLoraSelect`
- `WanVideoBlockSwap`
- `MultiTalkModelLoader`
- `PreviewAny`
- `CLIPVisionLoader`
- `LoadWanVideoT5TextEncoder`
- `VHS_VideoCombine`
- `WanVideoModelLoader`
- `MultiTalkWav2VecEmbeds`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `AudioCrop`
- `WanVideoSampler` ★核心
- `WanVideoDecode`
- `WanVideoTextEncode`
- `WanVideoImageToVideoMultiTalk`
- `GetImageSizeAndCount`
- `Note`
- `RH_GetAudioDuration`
- `easy showAnything`
- `JWInteger`
- `CastAnyToIntStringFloat`
- `AudioSeparation`
- `WanVideoLoraSelect`
- `WanVideoClipVisionEncode`
- `WanVideoVAELoader`
- `DownloadAndLoadWav2VecModel`
- `easy mathInt`
- `easy mathInt`
- `Note`
- `easy showAnything`
- `VHS_VideoCombine`
- `LoadImage`
- `LoadAudio`
- `CR Prompt Text`
- `Note`

## 知识

覆盖率 **83%**（29/35）

**有卡**：`WanVideoLoraSelect`、`WanVideoBlockSwap`、`MultiTalkModelLoader`、`CLIPVisionLoader`、`LoadWanVideoT5TextEncoder`、`VHS_VideoCombine`、`WanVideoModelLoader`、`MultiTalkWav2VecEmbeds`、`LayerUtility: ImageScaleByAspectRatio V2`、`AudioCrop`、`WanVideoSampler`、`WanVideoDecode`、`WanVideoTextEncode`、`WanVideoImageToVideoMultiTalk`、`GetImageSizeAndCount`、`RH_GetAudioDuration`、`JWInteger`、`CastAnyToIntStringFloat`、`AudioSeparation`、`WanVideoClipVisionEncode`、`WanVideoVAELoader`、`DownloadAndLoadWav2VecModel`、`easy mathInt`、`LoadImage`、`LoadAudio`、`CR Prompt Text`

**用到的条目**：LoadImage、WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoLoraSelect

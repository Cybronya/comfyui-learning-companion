---
key: 数字人/数字人/视频对口型，无限时长——infinitetalk视频对口型，video2video_1958795663838437378.json
name: 视频对口型，无限时长——infinitetalk视频对口型，video2video_1958795663838437378
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/数字人/数字人/视频对口型，无限时长——infinitetalk视频对口型，video2video_1958795663838437378.json
hash: c5e87ba531cb000c
coverage: 0.931034
learned_at: 2026-10-26 02:05:11
nodes: [WanVideoExperimentalArgs, AudioSeparation, DownloadAndLoadWav2VecModel, LoadWanVideoT5TextEncoder, WanVideoModelLoader, WanVideoBlockSwap, WanVideoImageToVideoMultiTalk, easy showAnything, WanVideoTextEncode, WanVideoDecode, VHS_VideoCombine, WanVideoSampler, PreviewImage, ImageConcatMulti, WanVideoVAELoader, VHS_VideoCombine, WanVideoSLG, WanVideoTeaCache, WanVideoEnhanceAVideo, CLIPVisionLoader, WanVideoLoraSelectMulti, WanVideoTorchCompileSettings, VHS_LoadVideo, MultiTalkModelLoader, MultiTalkWav2VecEmbeds, LayerUtility: ImageScaleByAspectRatio V2, WanVideoEncode, ImageFromBatch, WanVideoClipVisionEncode]
patterns: []
missing: []
---

# 数字人/数字人/视频对口型，无限时长——infinitetalk视频对口型，video2video_1958795663838437378.json

> 来源文件 `comfyui_library/workflows/数字人/数字人/视频对口型，无限时长——infinitetalk视频对口型，video2video_1958795663838437378.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（29 个）：
- `WanVideoExperimentalArgs`
- `AudioSeparation`
- `DownloadAndLoadWav2VecModel`
- `LoadWanVideoT5TextEncoder`
- `WanVideoModelLoader`
- `WanVideoBlockSwap`
- `WanVideoImageToVideoMultiTalk`
- `easy showAnything`
- `WanVideoTextEncode`
- `WanVideoDecode`
- `VHS_VideoCombine`
- `WanVideoSampler` ★核心
- `PreviewImage`
- `ImageConcatMulti`
- `WanVideoVAELoader`
- `VHS_VideoCombine`
- `WanVideoSLG`
- `WanVideoTeaCache`
- `WanVideoEnhanceAVideo`
- `CLIPVisionLoader`
- `WanVideoLoraSelectMulti`
- `WanVideoTorchCompileSettings`
- `VHS_LoadVideo`
- `MultiTalkModelLoader`
- `MultiTalkWav2VecEmbeds`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `WanVideoEncode`
- `ImageFromBatch`
- `WanVideoClipVisionEncode`

## 知识

覆盖率 **93%**（27/29）

**有卡**：`WanVideoExperimentalArgs`、`AudioSeparation`、`DownloadAndLoadWav2VecModel`、`LoadWanVideoT5TextEncoder`、`WanVideoModelLoader`、`WanVideoBlockSwap`、`WanVideoImageToVideoMultiTalk`、`WanVideoTextEncode`、`WanVideoDecode`、`VHS_VideoCombine`、`WanVideoSampler`、`ImageConcatMulti`、`WanVideoVAELoader`、`WanVideoSLG`、`WanVideoTeaCache`、`WanVideoEnhanceAVideo`、`CLIPVisionLoader`、`WanVideoLoraSelectMulti`、`WanVideoTorchCompileSettings`、`VHS_LoadVideo`、`MultiTalkModelLoader`、`MultiTalkWav2VecEmbeds`、`LayerUtility: ImageScaleByAspectRatio V2`、`WanVideoEncode`、`ImageFromBatch`、`WanVideoClipVisionEncode`

**用到的条目**：WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoEncode、WanVideoLoraSelectMulti

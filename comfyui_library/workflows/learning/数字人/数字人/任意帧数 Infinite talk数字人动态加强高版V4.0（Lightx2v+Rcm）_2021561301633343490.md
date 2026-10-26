---
key: 数字人/数字人/任意帧数 Infinite talk数字人动态加强高版V4.0（Lightx2v+Rcm）_2021561301633343490.json
name: 任意帧数 Infinite talk数字人动态加强高版V4.0（Lightx2v+Rcm）_2021561301633343490
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/数字人/数字人/任意帧数 Infinite talk数字人动态加强高版V4.0（Lightx2v+Rcm）_2021561301633343490.json
hash: d185f280c8d2da46
coverage: 0.771429
learned_at: 2026-10-26 02:00:21
nodes: [LoadWanVideoT5TextEncoder, CLIPVisionLoader, PreviewAny, WanVideoVAELoader, WanVideoClipVisionEncode, AudioSeparation, DownloadAndLoadWav2VecModel, Note, WanVideoModelLoader, WanVideoTextEncode, WanVideoSampler, WanVideoImageToVideoMultiTalk, WanVideoLoraSelect, MultiTalkModelLoader, MultiTalkWav2VecEmbeds, AudioCrop, Note, Note, Note, VHS_VideoCombine, WanVideoLoraSelect, JWFloat, Reroute, VHS_VideoCombine, Note, LayerUtility: ImageScaleByAspectRatio V2, WanVideoBlockSwap, Note, WanVideoDecode, LoadAudio, LoadImage, GetImageSizeAndCount, JWInteger, JWInteger, CR Prompt Text]
patterns: []
missing: []
---

# 数字人/数字人/任意帧数 Infinite talk数字人动态加强高版V4.0（Lightx2v+Rcm）_2021561301633343490.json

> 来源文件 `comfyui_library/workflows/数字人/数字人/任意帧数 Infinite talk数字人动态加强高版V4.0（Lightx2v+Rcm）_2021561301633343490.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（35 个）：
- `LoadWanVideoT5TextEncoder`
- `CLIPVisionLoader`
- `PreviewAny`
- `WanVideoVAELoader`
- `WanVideoClipVisionEncode`
- `AudioSeparation`
- `DownloadAndLoadWav2VecModel`
- `Note`
- `WanVideoModelLoader`
- `WanVideoTextEncode`
- `WanVideoSampler` ★核心
- `WanVideoImageToVideoMultiTalk`
- `WanVideoLoraSelect`
- `MultiTalkModelLoader`
- `MultiTalkWav2VecEmbeds`
- `AudioCrop`
- `Note`
- `Note`
- `Note`
- `VHS_VideoCombine`
- `WanVideoLoraSelect`
- `JWFloat`
- `Reroute`
- `VHS_VideoCombine`
- `Note`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `WanVideoBlockSwap`
- `Note`
- `WanVideoDecode`
- `LoadAudio`
- `LoadImage`
- `GetImageSizeAndCount`
- `JWInteger`
- `JWInteger`
- `CR Prompt Text`

## 知识

覆盖率 **77%**（27/35）

**有卡**：`LoadWanVideoT5TextEncoder`、`CLIPVisionLoader`、`WanVideoVAELoader`、`WanVideoClipVisionEncode`、`AudioSeparation`、`DownloadAndLoadWav2VecModel`、`WanVideoModelLoader`、`WanVideoTextEncode`、`WanVideoSampler`、`WanVideoImageToVideoMultiTalk`、`WanVideoLoraSelect`、`MultiTalkModelLoader`、`MultiTalkWav2VecEmbeds`、`AudioCrop`、`VHS_VideoCombine`、`JWFloat`、`LayerUtility: ImageScaleByAspectRatio V2`、`WanVideoBlockSwap`、`WanVideoDecode`、`LoadAudio`、`LoadImage`、`GetImageSizeAndCount`、`JWInteger`、`CR Prompt Text`

**用到的条目**：LoadImage、WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoLoraSelect

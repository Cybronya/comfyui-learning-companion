---
key: 数字人/数字人/(户外)Infinite talk数字人动态加强高版V4（Lightx2v+Rcm）_1991178505719492610.json
name: (户外)Infinite talk数字人动态加强高版V4（Lightx2v+Rcm）_1991178505719492610
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/数字人/数字人/(户外)Infinite talk数字人动态加强高版V4（Lightx2v+Rcm）_1991178505719492610.json
hash: be0f3fd9b0b41db5
coverage: 0.75
learned_at: 2026-10-26 01:53:11
nodes: [MarkdownNote, LayerUtility: ImageScaleByAspectRatio V2, LoadWanVideoT5TextEncoder, CLIPVisionLoader, PreviewAny, WanVideoVAELoader, WanVideoClipVisionEncode, AudioSeparation, DownloadAndLoadWav2VecModel, GetImageSizeAndCount, Note, WanVideoModelLoader, WanVideoTextEncode, WanVideoSampler, WanVideoImageToVideoMultiTalk, WanVideoLoraSelect, WanVideoLoraSelect, MultiTalkModelLoader, JWFloat, MultiTalkWav2VecEmbeds, CR Prompt Text, WanVideoDecode, AudioCrop, WanVideoBlockSwap, Reroute, VHS_VideoCombine, JWInteger, Note, Note, Note, Note, LoadImage, Note, LoadAudio, JWInteger, VHS_VideoCombine]
patterns: []
missing: []
---

# 数字人/数字人/(户外)Infinite talk数字人动态加强高版V4（Lightx2v+Rcm）_1991178505719492610.json

> 来源文件 `comfyui_library/workflows/数字人/数字人/(户外)Infinite talk数字人动态加强高版V4（Lightx2v+Rcm）_1991178505719492610.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（36 个）：
- `MarkdownNote`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadWanVideoT5TextEncoder`
- `CLIPVisionLoader`
- `PreviewAny`
- `WanVideoVAELoader`
- `WanVideoClipVisionEncode`
- `AudioSeparation`
- `DownloadAndLoadWav2VecModel`
- `GetImageSizeAndCount`
- `Note`
- `WanVideoModelLoader`
- `WanVideoTextEncode`
- `WanVideoSampler` ★核心
- `WanVideoImageToVideoMultiTalk`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `MultiTalkModelLoader`
- `JWFloat`
- `MultiTalkWav2VecEmbeds`
- `CR Prompt Text`
- `WanVideoDecode`
- `AudioCrop`
- `WanVideoBlockSwap`
- `Reroute`
- `VHS_VideoCombine`
- `JWInteger`
- `Note`
- `Note`
- `Note`
- `Note`
- `LoadImage`
- `Note`
- `LoadAudio`
- `JWInteger`
- `VHS_VideoCombine`

## 知识

覆盖率 **75%**（27/36）

**有卡**：`LayerUtility: ImageScaleByAspectRatio V2`、`LoadWanVideoT5TextEncoder`、`CLIPVisionLoader`、`WanVideoVAELoader`、`WanVideoClipVisionEncode`、`AudioSeparation`、`DownloadAndLoadWav2VecModel`、`GetImageSizeAndCount`、`WanVideoModelLoader`、`WanVideoTextEncode`、`WanVideoSampler`、`WanVideoImageToVideoMultiTalk`、`WanVideoLoraSelect`、`MultiTalkModelLoader`、`JWFloat`、`MultiTalkWav2VecEmbeds`、`CR Prompt Text`、`WanVideoDecode`、`AudioCrop`、`WanVideoBlockSwap`、`VHS_VideoCombine`、`JWInteger`、`LoadImage`、`LoadAudio`

**用到的条目**：LoadImage、WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoLoraSelect

---
key: 数字人/数字人/(大龙）Infinite+talk数字人动态加强高版V4（Lightx2v+Rcm）-音画同步修复_2039657945738256386.json
name: (大龙）Infinite+talk数字人动态加强高版V4（Lightx2v+Rcm）-音画同步修复_2039657945738256386
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/数字人/数字人/(大龙）Infinite+talk数字人动态加强高版V4（Lightx2v+Rcm）-音画同步修复_2039657945738256386.json
hash: d481564f17baa16c
coverage: 0.785714
learned_at: 2026-10-26 01:53:10
nodes: [CLIPVisionLoader, WanVideoVAELoader, Note, MultiTalkModelLoader, MarkdownNote, WanVideoDecode, WanVideoLoraSelect, Note, AudioCrop, Note, Note, Reroute, Note, Note, VHS_VideoCombine, VHS_VideoCombine, CR Prompt Text, JWFloat, AudioTrim, LayerUtility: ImageScaleByAspectRatio V2, JWInteger, FloatConstant, WanVideoBlockSwap, PreviewAny, WanVideoClipVisionEncode, DownloadAndLoadWav2VecModel, AudioSeparation, WanVideoLoraSelect, WanVideoSampler, JWInteger, WanVideoModelLoader, LoadImage, JWInteger, MultiTalkWav2VecEmbeds, FloatConstant, FloatConstant, LoadWanVideoT5TextEncoder, GetImageSizeAndCount, WanVideoImageToVideoMultiTalk, LoadAudio, CR Text, WanVideoTextEncode]
patterns: []
missing: []
---

# 数字人/数字人/(大龙）Infinite+talk数字人动态加强高版V4（Lightx2v+Rcm）-音画同步修复_2039657945738256386.json

> 来源文件 `comfyui_library/workflows/数字人/数字人/(大龙）Infinite+talk数字人动态加强高版V4（Lightx2v+Rcm）-音画同步修复_2039657945738256386.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（42 个）：
- `CLIPVisionLoader`
- `WanVideoVAELoader`
- `Note`
- `MultiTalkModelLoader`
- `MarkdownNote`
- `WanVideoDecode`
- `WanVideoLoraSelect`
- `Note`
- `AudioCrop`
- `Note`
- `Note`
- `Reroute`
- `Note`
- `Note`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `CR Prompt Text`
- `JWFloat`
- `AudioTrim`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `JWInteger`
- `FloatConstant`
- `WanVideoBlockSwap`
- `PreviewAny`
- `WanVideoClipVisionEncode`
- `DownloadAndLoadWav2VecModel`
- `AudioSeparation`
- `WanVideoLoraSelect`
- `WanVideoSampler` ★核心
- `JWInteger`
- `WanVideoModelLoader`
- `LoadImage`
- `JWInteger`
- `MultiTalkWav2VecEmbeds`
- `FloatConstant`
- `FloatConstant`
- `LoadWanVideoT5TextEncoder`
- `GetImageSizeAndCount`
- `WanVideoImageToVideoMultiTalk`
- `LoadAudio`
- `CR Text`
- `WanVideoTextEncode`

## 知识

覆盖率 **79%**（33/42）

**有卡**：`CLIPVisionLoader`、`WanVideoVAELoader`、`MultiTalkModelLoader`、`WanVideoDecode`、`WanVideoLoraSelect`、`AudioCrop`、`VHS_VideoCombine`、`CR Prompt Text`、`JWFloat`、`AudioTrim`、`LayerUtility: ImageScaleByAspectRatio V2`、`JWInteger`、`FloatConstant`、`WanVideoBlockSwap`、`WanVideoClipVisionEncode`、`DownloadAndLoadWav2VecModel`、`AudioSeparation`、`WanVideoSampler`、`WanVideoModelLoader`、`LoadImage`、`MultiTalkWav2VecEmbeds`、`LoadWanVideoT5TextEncoder`、`GetImageSizeAndCount`、`WanVideoImageToVideoMultiTalk`、`LoadAudio`、`CR Text`、`WanVideoTextEncode`

**用到的条目**：LoadImage、WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoLoraSelect

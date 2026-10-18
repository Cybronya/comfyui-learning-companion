---
key: 视频生成/图生视频/(清雅）Infinite talk数字人动态加强高版V4（Lightx2v+Rcm）_2020847239698063361.json
name: (清雅）Infinite talk数字人动态加强高版V4（Lightx2v+Rcm）_2020847239698063361.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/(清雅）Infinite talk数字人动态加强高版V4（Lightx2v+Rcm）_2020847239698063361.json
hash: c594a2a946daa3ff
coverage: 0.75
learned_at: 2026-10-15 22:35:07
nodes: [LoadWanVideoT5TextEncoder, CLIPVisionLoader, PreviewAny, WanVideoVAELoader, WanVideoClipVisionEncode, AudioSeparation, DownloadAndLoadWav2VecModel, Note, WanVideoModelLoader, WanVideoTextEncode, WanVideoSampler, WanVideoImageToVideoMultiTalk, WanVideoLoraSelect, MultiTalkModelLoader, MultiTalkWav2VecEmbeds, AudioCrop, GetImageSizeAndCount, Note, Note, Note, WanVideoLoraSelect, JWFloat, Reroute, VHS_VideoCombine, Note, JWInteger, CR Prompt Text, LayerUtility: ImageScaleByAspectRatio V2, MarkdownNote, WanVideoBlockSwap, Note, WanVideoDecode, LoadAudio, JWInteger, VHS_VideoCombine, LoadImage]
patterns: []
missing: []
---

# 视频生成/图生视频/(清雅）Infinite talk数字人动态加强高版V4（Lightx2v+Rcm）_2020847239698063361.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2020847239698063361.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（36 个）：
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
- `GetImageSizeAndCount`
- `Note`
- `Note`
- `Note`
- `WanVideoLoraSelect`
- `JWFloat`
- `Reroute`
- `VHS_VideoCombine`
- `Note`
- `JWInteger`
- `CR Prompt Text`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `MarkdownNote`
- `WanVideoBlockSwap`
- `Note`
- `WanVideoDecode`
- `LoadAudio`
- `JWInteger`
- `VHS_VideoCombine`
- `LoadImage`

## 知识

覆盖率 **75%**（27/36）

**有卡**：`LoadWanVideoT5TextEncoder`、`CLIPVisionLoader`、`WanVideoVAELoader`、`WanVideoClipVisionEncode`、`AudioSeparation`、`DownloadAndLoadWav2VecModel`、`WanVideoModelLoader`、`WanVideoTextEncode`、`WanVideoSampler`、`WanVideoImageToVideoMultiTalk`、`WanVideoLoraSelect`、`MultiTalkModelLoader`、`MultiTalkWav2VecEmbeds`、`AudioCrop`、`GetImageSizeAndCount`、`JWFloat`、`VHS_VideoCombine`、`JWInteger`、`CR Prompt Text`、`LayerUtility: ImageScaleByAspectRatio V2`、`WanVideoBlockSwap`、`WanVideoDecode`、`LoadAudio`、`LoadImage`

**用到的条目**：LoadImage、WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoLoraSelect

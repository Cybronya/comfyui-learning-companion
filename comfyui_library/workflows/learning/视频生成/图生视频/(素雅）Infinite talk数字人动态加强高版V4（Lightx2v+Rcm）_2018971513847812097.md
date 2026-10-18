---
key: 视频生成/图生视频/(素雅）Infinite talk数字人动态加强高版V4（Lightx2v+Rcm）_2018971513847812097.json
name: (素雅）Infinite talk数字人动态加强高版V4（Lightx2v+Rcm）_2018971513847812097.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/(素雅）Infinite talk数字人动态加强高版V4（Lightx2v+Rcm）_2018971513847812097.json
hash: 9f62d47422cce91b
coverage: 0.75
learned_at: 2026-10-15 22:34:59
nodes: [LoadWanVideoT5TextEncoder, CLIPVisionLoader, PreviewAny, WanVideoVAELoader, WanVideoClipVisionEncode, AudioSeparation, DownloadAndLoadWav2VecModel, Note, WanVideoModelLoader, WanVideoTextEncode, WanVideoSampler, WanVideoImageToVideoMultiTalk, WanVideoLoraSelect, MultiTalkModelLoader, MultiTalkWav2VecEmbeds, AudioCrop, GetImageSizeAndCount, Note, Note, Note, VHS_VideoCombine, WanVideoDecode, WanVideoLoraSelect, JWFloat, Reroute, VHS_VideoCombine, Note, JWInteger, CR Prompt Text, LayerUtility: ImageScaleByAspectRatio V2, MarkdownNote, WanVideoBlockSwap, Note, LoadImage, LoadAudio, JWInteger]
patterns: []
missing: []
---

# 视频生成/图生视频/(素雅）Infinite talk数字人动态加强高版V4（Lightx2v+Rcm）_2018971513847812097.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2018971513847812097.json`

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
- `VHS_VideoCombine`
- `WanVideoDecode`
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
- `LoadImage`
- `LoadAudio`
- `JWInteger`

## 知识

覆盖率 **75%**（27/36）

**有卡**：`LoadWanVideoT5TextEncoder`、`CLIPVisionLoader`、`WanVideoVAELoader`、`WanVideoClipVisionEncode`、`AudioSeparation`、`DownloadAndLoadWav2VecModel`、`WanVideoModelLoader`、`WanVideoTextEncode`、`WanVideoSampler`、`WanVideoImageToVideoMultiTalk`、`WanVideoLoraSelect`、`MultiTalkModelLoader`、`MultiTalkWav2VecEmbeds`、`AudioCrop`、`GetImageSizeAndCount`、`VHS_VideoCombine`、`WanVideoDecode`、`JWFloat`、`JWInteger`、`CR Prompt Text`、`LayerUtility: ImageScaleByAspectRatio V2`、`WanVideoBlockSwap`、`LoadImage`、`LoadAudio`

**用到的条目**：LoadImage、WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoLoraSelect

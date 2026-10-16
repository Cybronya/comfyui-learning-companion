---
key: 视频生成/图生视频/(阴影)Infinite talk数字人动态加强高版V4（Lightx2v+Rcm）_2003097265713684481.json
name: (阴影)Infinite talk数字人动态加强高版V4（Lightx2v+Rcm）_2003097265713684481.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2003097265713684481.json
hash: a967b63d374e127a
coverage: 0.75
learned_at: 2026-10-15 22:33:50
nodes: [MarkdownNote, LayerUtility: ImageScaleByAspectRatio V2, LoadWanVideoT5TextEncoder, CLIPVisionLoader, PreviewAny, WanVideoVAELoader, WanVideoClipVisionEncode, AudioSeparation, DownloadAndLoadWav2VecModel, Note, WanVideoModelLoader, WanVideoTextEncode, WanVideoSampler, WanVideoImageToVideoMultiTalk, WanVideoLoraSelect, WanVideoLoraSelect, MultiTalkModelLoader, JWFloat, MultiTalkWav2VecEmbeds, WanVideoDecode, AudioCrop, Reroute, Note, Note, VHS_VideoCombine, JWInteger, WanVideoBlockSwap, GetImageSizeAndCount, Note, Note, Note, CR Prompt Text, VHS_VideoCombine, LoadAudio, LoadImage, JWInteger]
patterns: []
missing: []
---

# 视频生成/图生视频/(阴影)Infinite talk数字人动态加强高版V4（Lightx2v+Rcm）_2003097265713684481.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2003097265713684481.json`

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
- `WanVideoDecode`
- `AudioCrop`
- `Reroute`
- `Note`
- `Note`
- `VHS_VideoCombine`
- `JWInteger`
- `WanVideoBlockSwap`
- `GetImageSizeAndCount`
- `Note`
- `Note`
- `Note`
- `CR Prompt Text`
- `VHS_VideoCombine`
- `LoadAudio`
- `LoadImage`
- `JWInteger`

## 知识

覆盖率 **75%**（27/36）

**有卡**：`LayerUtility: ImageScaleByAspectRatio V2`、`LoadWanVideoT5TextEncoder`、`CLIPVisionLoader`、`WanVideoVAELoader`、`WanVideoClipVisionEncode`、`AudioSeparation`、`DownloadAndLoadWav2VecModel`、`WanVideoModelLoader`、`WanVideoTextEncode`、`WanVideoSampler`、`WanVideoImageToVideoMultiTalk`、`WanVideoLoraSelect`、`MultiTalkModelLoader`、`JWFloat`、`MultiTalkWav2VecEmbeds`、`WanVideoDecode`、`AudioCrop`、`VHS_VideoCombine`、`JWInteger`、`WanVideoBlockSwap`、`GetImageSizeAndCount`、`CR Prompt Text`、`LoadAudio`、`LoadImage`

**用到的条目**：LoadImage、WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoLoraSelect

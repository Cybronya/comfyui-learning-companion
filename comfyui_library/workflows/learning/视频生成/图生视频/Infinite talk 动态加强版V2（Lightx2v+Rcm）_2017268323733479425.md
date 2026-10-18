---
key: 视频生成/图生视频/Infinite talk 动态加强版V2（Lightx2v+Rcm）_2017268323733479425.json
name: Infinite talk 动态加强版V2（Lightx2v+Rcm）_2017268323733479425.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/Infinite talk 动态加强版V2（Lightx2v+Rcm）_2017268323733479425.json
hash: b83db34b8d9f9fe3
coverage: 0.896552
learned_at: 2026-10-15 22:34:46
nodes: [WanVideoBlockSwap, MarkdownNote, JWInteger, JWInteger, LoadAudio, CR Prompt Text, LoadImage, WanVideoLoraSelect, MultiTalkModelLoader, CLIPVisionLoader, Note, WanVideoVAELoader, LoadWanVideoT5TextEncoder, LayerUtility: ImageScaleByAspectRatio V2, GetImageSizeAndCount, WanVideoClipVisionEncode, MultiTalkWav2VecEmbeds, DownloadAndLoadWav2VecModel, AudioSeparation, PreviewAny, JWFloat, WanVideoTextEncode, WanVideoImageToVideoMultiTalk, WanVideoSampler, WanVideoDecode, VHS_VideoCombine, AudioCrop, WanVideoModelLoader, WanVideoLoraSelect]
patterns: []
missing: []
---

# 视频生成/图生视频/Infinite talk 动态加强版V2（Lightx2v+Rcm）_2017268323733479425.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2017268323733479425.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（29 个）：
- `WanVideoBlockSwap`
- `MarkdownNote`
- `JWInteger`
- `JWInteger`
- `LoadAudio`
- `CR Prompt Text`
- `LoadImage`
- `WanVideoLoraSelect`
- `MultiTalkModelLoader`
- `CLIPVisionLoader`
- `Note`
- `WanVideoVAELoader`
- `LoadWanVideoT5TextEncoder`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `GetImageSizeAndCount`
- `WanVideoClipVisionEncode`
- `MultiTalkWav2VecEmbeds`
- `DownloadAndLoadWav2VecModel`
- `AudioSeparation`
- `PreviewAny`
- `JWFloat`
- `WanVideoTextEncode`
- `WanVideoImageToVideoMultiTalk`
- `WanVideoSampler` ★核心
- `WanVideoDecode`
- `VHS_VideoCombine`
- `AudioCrop`
- `WanVideoModelLoader`
- `WanVideoLoraSelect`

## 知识

覆盖率 **90%**（26/29）

**有卡**：`WanVideoBlockSwap`、`JWInteger`、`LoadAudio`、`CR Prompt Text`、`LoadImage`、`WanVideoLoraSelect`、`MultiTalkModelLoader`、`CLIPVisionLoader`、`WanVideoVAELoader`、`LoadWanVideoT5TextEncoder`、`LayerUtility: ImageScaleByAspectRatio V2`、`GetImageSizeAndCount`、`WanVideoClipVisionEncode`、`MultiTalkWav2VecEmbeds`、`DownloadAndLoadWav2VecModel`、`AudioSeparation`、`JWFloat`、`WanVideoTextEncode`、`WanVideoImageToVideoMultiTalk`、`WanVideoSampler`、`WanVideoDecode`、`VHS_VideoCombine`、`AudioCrop`、`WanVideoModelLoader`

**用到的条目**：LoadImage、WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoLoraSelect

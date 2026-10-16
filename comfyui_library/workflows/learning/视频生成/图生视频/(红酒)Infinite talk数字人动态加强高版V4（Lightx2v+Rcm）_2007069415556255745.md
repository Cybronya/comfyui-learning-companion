---
key: 视频生成/图生视频/(红酒)Infinite talk数字人动态加强高版V4（Lightx2v+Rcm）_2007069415556255745.json
name: (红酒)Infinite talk数字人动态加强高版V4（Lightx2v+Rcm）_2007069415556255745.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2007069415556255745.json
hash: 6cdf61b4f1f781c2
coverage: 0.75
learned_at: 2026-10-15 22:34:03
nodes: [MarkdownNote, LayerUtility: ImageScaleByAspectRatio V2, LoadWanVideoT5TextEncoder, CLIPVisionLoader, PreviewAny, WanVideoVAELoader, WanVideoClipVisionEncode, AudioSeparation, DownloadAndLoadWav2VecModel, Note, WanVideoModelLoader, WanVideoTextEncode, WanVideoSampler, WanVideoImageToVideoMultiTalk, WanVideoLoraSelect, MultiTalkModelLoader, JWFloat, MultiTalkWav2VecEmbeds, WanVideoDecode, AudioCrop, Reroute, Note, Note, VHS_VideoCombine, JWInteger, GetImageSizeAndCount, Note, Note, Note, CR Prompt Text, VHS_VideoCombine, WanVideoLoraSelect, WanVideoBlockSwap, JWInteger, LoadAudio, LoadImage]
patterns: []
missing: []
---

# 视频生成/图生视频/(红酒)Infinite talk数字人动态加强高版V4（Lightx2v+Rcm）_2007069415556255745.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2007069415556255745.json`

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
- `GetImageSizeAndCount`
- `Note`
- `Note`
- `Note`
- `CR Prompt Text`
- `VHS_VideoCombine`
- `WanVideoLoraSelect`
- `WanVideoBlockSwap`
- `JWInteger`
- `LoadAudio`
- `LoadImage`

## 知识

覆盖率 **75%**（27/36）

**有卡**：`LayerUtility: ImageScaleByAspectRatio V2`、`LoadWanVideoT5TextEncoder`、`CLIPVisionLoader`、`WanVideoVAELoader`、`WanVideoClipVisionEncode`、`AudioSeparation`、`DownloadAndLoadWav2VecModel`、`WanVideoModelLoader`、`WanVideoTextEncode`、`WanVideoSampler`、`WanVideoImageToVideoMultiTalk`、`WanVideoLoraSelect`、`MultiTalkModelLoader`、`JWFloat`、`MultiTalkWav2VecEmbeds`、`WanVideoDecode`、`AudioCrop`、`VHS_VideoCombine`、`JWInteger`、`GetImageSizeAndCount`、`CR Prompt Text`、`WanVideoBlockSwap`、`LoadAudio`、`LoadImage`

**用到的条目**：LoadImage、WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoLoraSelect

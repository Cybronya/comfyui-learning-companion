---
key: 视频生成/图生视频/(落叶)Infinite talk数字人动态加强高版V4（Lightx2v+Rcm）_2001666583061774338.json
name: (落叶)Infinite talk数字人动态加强高版V4（Lightx2v+Rcm）_2001666583061774338.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2001666583061774338.json
hash: dfc5d315bd6ac076
coverage: 0.75
learned_at: 2026-10-15 22:33:46
nodes: [MarkdownNote, LayerUtility: ImageScaleByAspectRatio V2, LoadWanVideoT5TextEncoder, CLIPVisionLoader, WanVideoVAELoader, WanVideoClipVisionEncode, AudioSeparation, DownloadAndLoadWav2VecModel, Note, WanVideoModelLoader, WanVideoTextEncode, WanVideoSampler, WanVideoImageToVideoMultiTalk, WanVideoLoraSelect, WanVideoLoraSelect, MultiTalkModelLoader, JWFloat, MultiTalkWav2VecEmbeds, WanVideoDecode, AudioCrop, Reroute, Note, Note, VHS_VideoCombine, JWInteger, GetImageSizeAndCount, Note, Note, Note, CR Prompt Text, LoadImage, JWInteger, WanVideoBlockSwap, VHS_VideoCombine, LoadAudio, PreviewAny]
patterns: []
missing: []
---

# 视频生成/图生视频/(落叶)Infinite talk数字人动态加强高版V4（Lightx2v+Rcm）_2001666583061774338.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2001666583061774338.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（36 个）：
- `MarkdownNote`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadWanVideoT5TextEncoder`
- `CLIPVisionLoader`
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
- `GetImageSizeAndCount`
- `Note`
- `Note`
- `Note`
- `CR Prompt Text`
- `LoadImage`
- `JWInteger`
- `WanVideoBlockSwap`
- `VHS_VideoCombine`
- `LoadAudio`
- `PreviewAny`

## 知识

覆盖率 **75%**（27/36）

**有卡**：`LayerUtility: ImageScaleByAspectRatio V2`、`LoadWanVideoT5TextEncoder`、`CLIPVisionLoader`、`WanVideoVAELoader`、`WanVideoClipVisionEncode`、`AudioSeparation`、`DownloadAndLoadWav2VecModel`、`WanVideoModelLoader`、`WanVideoTextEncode`、`WanVideoSampler`、`WanVideoImageToVideoMultiTalk`、`WanVideoLoraSelect`、`MultiTalkModelLoader`、`JWFloat`、`MultiTalkWav2VecEmbeds`、`WanVideoDecode`、`AudioCrop`、`VHS_VideoCombine`、`JWInteger`、`GetImageSizeAndCount`、`CR Prompt Text`、`LoadImage`、`WanVideoBlockSwap`、`LoadAudio`

**用到的条目**：LoadImage、WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoLoraSelect

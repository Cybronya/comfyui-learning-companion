---
key: 视频生成/图生视频/(闻花)Infinite talk数字人动态加强高版V4（Lightx2v+Rcm）_2008612127463972865.json
name: (闻花)Infinite talk数字人动态加强高版V4（Lightx2v+Rcm）_2008612127463972865.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/(闻花)Infinite talk数字人动态加强高版V4（Lightx2v+Rcm）_2008612127463972865.json
hash: 23827592af71f487
coverage: 0.75
learned_at: 2026-10-15 22:34:08
nodes: [MarkdownNote, LayerUtility: ImageScaleByAspectRatio V2, LoadWanVideoT5TextEncoder, CLIPVisionLoader, PreviewAny, WanVideoVAELoader, WanVideoClipVisionEncode, AudioSeparation, DownloadAndLoadWav2VecModel, Note, WanVideoModelLoader, WanVideoTextEncode, WanVideoSampler, WanVideoImageToVideoMultiTalk, WanVideoLoraSelect, MultiTalkModelLoader, MultiTalkWav2VecEmbeds, AudioCrop, Reroute, VHS_VideoCombine, JWInteger, GetImageSizeAndCount, Note, Note, Note, WanVideoBlockSwap, Note, Note, VHS_VideoCombine, WanVideoDecode, WanVideoLoraSelect, JWFloat, CR Prompt Text, LoadImage, LoadAudio, JWInteger]
patterns: []
missing: []
---

# 视频生成/图生视频/(闻花)Infinite talk数字人动态加强高版V4（Lightx2v+Rcm）_2008612127463972865.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2008612127463972865.json`

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
- `MultiTalkWav2VecEmbeds`
- `AudioCrop`
- `Reroute`
- `VHS_VideoCombine`
- `JWInteger`
- `GetImageSizeAndCount`
- `Note`
- `Note`
- `Note`
- `WanVideoBlockSwap`
- `Note`
- `Note`
- `VHS_VideoCombine`
- `WanVideoDecode`
- `WanVideoLoraSelect`
- `JWFloat`
- `CR Prompt Text`
- `LoadImage`
- `LoadAudio`
- `JWInteger`

## 知识

覆盖率 **75%**（27/36）

**有卡**：`LayerUtility: ImageScaleByAspectRatio V2`、`LoadWanVideoT5TextEncoder`、`CLIPVisionLoader`、`WanVideoVAELoader`、`WanVideoClipVisionEncode`、`AudioSeparation`、`DownloadAndLoadWav2VecModel`、`WanVideoModelLoader`、`WanVideoTextEncode`、`WanVideoSampler`、`WanVideoImageToVideoMultiTalk`、`WanVideoLoraSelect`、`MultiTalkModelLoader`、`MultiTalkWav2VecEmbeds`、`AudioCrop`、`VHS_VideoCombine`、`JWInteger`、`GetImageSizeAndCount`、`WanVideoBlockSwap`、`WanVideoDecode`、`JWFloat`、`CR Prompt Text`、`LoadImage`、`LoadAudio`

**用到的条目**：LoadImage、WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoLoraSelect

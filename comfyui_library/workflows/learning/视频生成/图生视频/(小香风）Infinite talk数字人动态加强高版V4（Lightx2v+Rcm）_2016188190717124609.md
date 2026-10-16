---
key: 视频生成/图生视频/(小香风）Infinite talk数字人动态加强高版V4（Lightx2v+Rcm）_2016188190717124609.json
name: (小香风）Infinite talk数字人动态加强高版V4（Lightx2v+Rcm）_2016188190717124609.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2016188190717124609.json
hash: 0f1c286ff98e8c65
coverage: 0.75
learned_at: 2026-10-15 22:34:41
nodes: [MarkdownNote, LayerUtility: ImageScaleByAspectRatio V2, LoadWanVideoT5TextEncoder, CLIPVisionLoader, PreviewAny, WanVideoVAELoader, WanVideoClipVisionEncode, AudioSeparation, DownloadAndLoadWav2VecModel, Note, WanVideoModelLoader, WanVideoTextEncode, WanVideoSampler, WanVideoImageToVideoMultiTalk, WanVideoLoraSelect, MultiTalkModelLoader, MultiTalkWav2VecEmbeds, AudioCrop, GetImageSizeAndCount, Note, Note, Note, Note, VHS_VideoCombine, WanVideoDecode, WanVideoLoraSelect, JWFloat, Reroute, WanVideoBlockSwap, CR Prompt Text, VHS_VideoCombine, JWInteger, Note, LoadAudio, LoadImage, JWInteger]
patterns: []
missing: []
---

# 视频生成/图生视频/(小香风）Infinite talk数字人动态加强高版V4（Lightx2v+Rcm）_2016188190717124609.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2016188190717124609.json`

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
- `GetImageSizeAndCount`
- `Note`
- `Note`
- `Note`
- `Note`
- `VHS_VideoCombine`
- `WanVideoDecode`
- `WanVideoLoraSelect`
- `JWFloat`
- `Reroute`
- `WanVideoBlockSwap`
- `CR Prompt Text`
- `VHS_VideoCombine`
- `JWInteger`
- `Note`
- `LoadAudio`
- `LoadImage`
- `JWInteger`

## 知识

覆盖率 **75%**（27/36）

**有卡**：`LayerUtility: ImageScaleByAspectRatio V2`、`LoadWanVideoT5TextEncoder`、`CLIPVisionLoader`、`WanVideoVAELoader`、`WanVideoClipVisionEncode`、`AudioSeparation`、`DownloadAndLoadWav2VecModel`、`WanVideoModelLoader`、`WanVideoTextEncode`、`WanVideoSampler`、`WanVideoImageToVideoMultiTalk`、`WanVideoLoraSelect`、`MultiTalkModelLoader`、`MultiTalkWav2VecEmbeds`、`AudioCrop`、`GetImageSizeAndCount`、`VHS_VideoCombine`、`WanVideoDecode`、`JWFloat`、`WanVideoBlockSwap`、`CR Prompt Text`、`JWInteger`、`LoadAudio`、`LoadImage`

**用到的条目**：LoadImage、WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoLoraSelect

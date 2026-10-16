---
key: 视频生成/图生视频/(蒂芙尼）Infinite talk数字人动态加强高版V4（Lightx2v+Rcm）_2016531749928443905.json
name: (蒂芙尼）Infinite talk数字人动态加强高版V4（Lightx2v+Rcm）_2016531749928443905.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2016531749928443905.json
hash: 48f4d070a66888c4
coverage: 0.75
learned_at: 2026-10-15 22:34:43
nodes: [MarkdownNote, LayerUtility: ImageScaleByAspectRatio V2, LoadWanVideoT5TextEncoder, CLIPVisionLoader, PreviewAny, WanVideoVAELoader, WanVideoClipVisionEncode, AudioSeparation, DownloadAndLoadWav2VecModel, Note, WanVideoModelLoader, WanVideoTextEncode, WanVideoSampler, WanVideoImageToVideoMultiTalk, WanVideoLoraSelect, MultiTalkModelLoader, MultiTalkWav2VecEmbeds, AudioCrop, GetImageSizeAndCount, Note, Note, Note, Note, VHS_VideoCombine, WanVideoDecode, WanVideoLoraSelect, JWFloat, Reroute, WanVideoBlockSwap, CR Prompt Text, VHS_VideoCombine, Note, JWInteger, JWInteger, LoadAudio, LoadImage]
patterns: []
missing: []
---

# 视频生成/图生视频/(蒂芙尼）Infinite talk数字人动态加强高版V4（Lightx2v+Rcm）_2016531749928443905.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2016531749928443905.json`

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
- `Note`
- `JWInteger`
- `JWInteger`
- `LoadAudio`
- `LoadImage`

## 知识

覆盖率 **75%**（27/36）

**有卡**：`LayerUtility: ImageScaleByAspectRatio V2`、`LoadWanVideoT5TextEncoder`、`CLIPVisionLoader`、`WanVideoVAELoader`、`WanVideoClipVisionEncode`、`AudioSeparation`、`DownloadAndLoadWav2VecModel`、`WanVideoModelLoader`、`WanVideoTextEncode`、`WanVideoSampler`、`WanVideoImageToVideoMultiTalk`、`WanVideoLoraSelect`、`MultiTalkModelLoader`、`MultiTalkWav2VecEmbeds`、`AudioCrop`、`GetImageSizeAndCount`、`VHS_VideoCombine`、`WanVideoDecode`、`JWFloat`、`WanVideoBlockSwap`、`CR Prompt Text`、`JWInteger`、`LoadAudio`、`LoadImage`

**用到的条目**：LoadImage、WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoLoraSelect

---
key: 视频生成/图生视频/(制服)Infinite talk数字人动态加强高版V4（Lightx2v+Rcm）_1997612991061405697.json
name: (制服)Infinite talk数字人动态加强高版V4（Lightx2v+Rcm）_1997612991061405697.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1997612991061405697.json
hash: 10e205de8f424f7c
coverage: 0.75
learned_at: 2026-10-15 22:33:30
nodes: [MarkdownNote, LayerUtility: ImageScaleByAspectRatio V2, LoadWanVideoT5TextEncoder, CLIPVisionLoader, PreviewAny, WanVideoVAELoader, WanVideoClipVisionEncode, Note, AudioSeparation, DownloadAndLoadWav2VecModel, GetImageSizeAndCount, Note, WanVideoModelLoader, WanVideoTextEncode, WanVideoSampler, WanVideoImageToVideoMultiTalk, WanVideoLoraSelect, WanVideoLoraSelect, MultiTalkModelLoader, JWFloat, MultiTalkWav2VecEmbeds, WanVideoDecode, AudioCrop, Reroute, Note, CR Prompt Text, Note, Note, Note, JWInteger, VHS_VideoCombine, VHS_VideoCombine, WanVideoBlockSwap, LoadAudio, JWInteger, LoadImage]
patterns: []
missing: []
---

# 视频生成/图生视频/(制服)Infinite talk数字人动态加强高版V4（Lightx2v+Rcm）_1997612991061405697.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1997612991061405697.json`

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
- `Note`
- `AudioSeparation`
- `DownloadAndLoadWav2VecModel`
- `GetImageSizeAndCount`
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
- `CR Prompt Text`
- `Note`
- `Note`
- `Note`
- `JWInteger`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `LoadAudio`
- `JWInteger`
- `LoadImage`

## 知识

覆盖率 **75%**（27/36）

**有卡**：`LayerUtility: ImageScaleByAspectRatio V2`、`LoadWanVideoT5TextEncoder`、`CLIPVisionLoader`、`WanVideoVAELoader`、`WanVideoClipVisionEncode`、`AudioSeparation`、`DownloadAndLoadWav2VecModel`、`GetImageSizeAndCount`、`WanVideoModelLoader`、`WanVideoTextEncode`、`WanVideoSampler`、`WanVideoImageToVideoMultiTalk`、`WanVideoLoraSelect`、`MultiTalkModelLoader`、`JWFloat`、`MultiTalkWav2VecEmbeds`、`WanVideoDecode`、`AudioCrop`、`CR Prompt Text`、`JWInteger`、`VHS_VideoCombine`、`WanVideoBlockSwap`、`LoadAudio`、`LoadImage`

**用到的条目**：LoadImage、WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoLoraSelect

---
key: 视频生成/图生视频/(运动装)Infinite talk数字人动态加强高版V4（Lightx2v+Rcm）_1994427374332747777.json
name: (运动装)Infinite talk数字人动态加强高版V4（Lightx2v+Rcm）_1994427374332747777.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1994427374332747777.json
hash: 18cc353bbffb39cc
coverage: 0.75
learned_at: 2026-10-15 22:33:21
nodes: [MarkdownNote, LayerUtility: ImageScaleByAspectRatio V2, LoadWanVideoT5TextEncoder, CLIPVisionLoader, PreviewAny, WanVideoVAELoader, WanVideoClipVisionEncode, Note, Note, AudioSeparation, DownloadAndLoadWav2VecModel, GetImageSizeAndCount, Note, WanVideoModelLoader, WanVideoTextEncode, WanVideoSampler, WanVideoImageToVideoMultiTalk, WanVideoLoraSelect, WanVideoLoraSelect, MultiTalkModelLoader, JWFloat, MultiTalkWav2VecEmbeds, WanVideoDecode, AudioCrop, WanVideoBlockSwap, Reroute, VHS_VideoCombine, Note, JWInteger, VHS_VideoCombine, CR Prompt Text, Note, Note, LoadImage, JWInteger, LoadAudio]
patterns: []
missing: []
---

# 视频生成/图生视频/(运动装)Infinite talk数字人动态加强高版V4（Lightx2v+Rcm）_1994427374332747777.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1994427374332747777.json`

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
- `WanVideoBlockSwap`
- `Reroute`
- `VHS_VideoCombine`
- `Note`
- `JWInteger`
- `VHS_VideoCombine`
- `CR Prompt Text`
- `Note`
- `Note`
- `LoadImage`
- `JWInteger`
- `LoadAudio`

## 知识

覆盖率 **75%**（27/36）

**有卡**：`LayerUtility: ImageScaleByAspectRatio V2`、`LoadWanVideoT5TextEncoder`、`CLIPVisionLoader`、`WanVideoVAELoader`、`WanVideoClipVisionEncode`、`AudioSeparation`、`DownloadAndLoadWav2VecModel`、`GetImageSizeAndCount`、`WanVideoModelLoader`、`WanVideoTextEncode`、`WanVideoSampler`、`WanVideoImageToVideoMultiTalk`、`WanVideoLoraSelect`、`MultiTalkModelLoader`、`JWFloat`、`MultiTalkWav2VecEmbeds`、`WanVideoDecode`、`AudioCrop`、`WanVideoBlockSwap`、`VHS_VideoCombine`、`JWInteger`、`CR Prompt Text`、`LoadImage`、`LoadAudio`

**用到的条目**：LoadImage、WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoLoraSelect

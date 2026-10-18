---
key: 视频生成/图生视频/(难过)Infinite talk数字人动态加强高版V4（Lightx2v+Rcm）_2002782100631764994.json
name: (难过)Infinite talk数字人动态加强高版V4（Lightx2v+Rcm）_2002782100631764994.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/(难过)Infinite talk数字人动态加强高版V4（Lightx2v+Rcm）_2002782100631764994.json
hash: c2f1d1b2bf9ab305
coverage: 0.75
learned_at: 2026-10-15 22:33:49
nodes: [MarkdownNote, LayerUtility: ImageScaleByAspectRatio V2, LoadWanVideoT5TextEncoder, CLIPVisionLoader, PreviewAny, WanVideoVAELoader, WanVideoClipVisionEncode, AudioSeparation, DownloadAndLoadWav2VecModel, Note, WanVideoModelLoader, WanVideoTextEncode, WanVideoSampler, WanVideoImageToVideoMultiTalk, WanVideoLoraSelect, WanVideoLoraSelect, MultiTalkModelLoader, JWFloat, MultiTalkWav2VecEmbeds, WanVideoDecode, AudioCrop, Reroute, Note, Note, VHS_VideoCombine, JWInteger, GetImageSizeAndCount, VHS_VideoCombine, Note, Note, Note, CR Prompt Text, LoadImage, JWInteger, WanVideoBlockSwap, LoadAudio]
patterns: []
missing: []
---

# 视频生成/图生视频/(难过)Infinite talk数字人动态加强高版V4（Lightx2v+Rcm）_2002782100631764994.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2002782100631764994.json`

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
- `GetImageSizeAndCount`
- `VHS_VideoCombine`
- `Note`
- `Note`
- `Note`
- `CR Prompt Text`
- `LoadImage`
- `JWInteger`
- `WanVideoBlockSwap`
- `LoadAudio`

## 知识

覆盖率 **75%**（27/36）

**有卡**：`LayerUtility: ImageScaleByAspectRatio V2`、`LoadWanVideoT5TextEncoder`、`CLIPVisionLoader`、`WanVideoVAELoader`、`WanVideoClipVisionEncode`、`AudioSeparation`、`DownloadAndLoadWav2VecModel`、`WanVideoModelLoader`、`WanVideoTextEncode`、`WanVideoSampler`、`WanVideoImageToVideoMultiTalk`、`WanVideoLoraSelect`、`MultiTalkModelLoader`、`JWFloat`、`MultiTalkWav2VecEmbeds`、`WanVideoDecode`、`AudioCrop`、`VHS_VideoCombine`、`JWInteger`、`GetImageSizeAndCount`、`CR Prompt Text`、`LoadImage`、`WanVideoBlockSwap`、`LoadAudio`

**用到的条目**：LoadImage、WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoLoraSelect

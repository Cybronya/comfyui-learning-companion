---
key: 视频生成/图生视频/(黑丝贞贞)Infinite talk数字人动态加强高版V4（Lightx2v+Rcm）_1995775197665955841.json
name: (黑丝贞贞)Infinite talk数字人动态加强高版V4（Lightx2v+Rcm）_1995775197665955841.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1995775197665955841.json
hash: 4dcd91eae6e048d7
coverage: 0.75
learned_at: 2026-10-15 22:33:24
nodes: [MarkdownNote, LayerUtility: ImageScaleByAspectRatio V2, LoadWanVideoT5TextEncoder, CLIPVisionLoader, PreviewAny, WanVideoVAELoader, WanVideoClipVisionEncode, Note, AudioSeparation, DownloadAndLoadWav2VecModel, GetImageSizeAndCount, Note, WanVideoModelLoader, WanVideoTextEncode, WanVideoImageToVideoMultiTalk, WanVideoLoraSelect, WanVideoLoraSelect, MultiTalkModelLoader, JWFloat, MultiTalkWav2VecEmbeds, WanVideoDecode, AudioCrop, Reroute, VHS_VideoCombine, Note, CR Prompt Text, Note, Note, Note, WanVideoBlockSwap, JWInteger, LoadImage, LoadAudio, JWInteger, WanVideoSampler, VHS_VideoCombine]
patterns: []
missing: []
---

# 视频生成/图生视频/(黑丝贞贞)Infinite talk数字人动态加强高版V4（Lightx2v+Rcm）_1995775197665955841.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1995775197665955841.json`

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
- `WanVideoImageToVideoMultiTalk`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `MultiTalkModelLoader`
- `JWFloat`
- `MultiTalkWav2VecEmbeds`
- `WanVideoDecode`
- `AudioCrop`
- `Reroute`
- `VHS_VideoCombine`
- `Note`
- `CR Prompt Text`
- `Note`
- `Note`
- `Note`
- `WanVideoBlockSwap`
- `JWInteger`
- `LoadImage`
- `LoadAudio`
- `JWInteger`
- `WanVideoSampler` ★核心
- `VHS_VideoCombine`

## 知识

覆盖率 **75%**（27/36）

**有卡**：`LayerUtility: ImageScaleByAspectRatio V2`、`LoadWanVideoT5TextEncoder`、`CLIPVisionLoader`、`WanVideoVAELoader`、`WanVideoClipVisionEncode`、`AudioSeparation`、`DownloadAndLoadWav2VecModel`、`GetImageSizeAndCount`、`WanVideoModelLoader`、`WanVideoTextEncode`、`WanVideoImageToVideoMultiTalk`、`WanVideoLoraSelect`、`MultiTalkModelLoader`、`JWFloat`、`MultiTalkWav2VecEmbeds`、`WanVideoDecode`、`AudioCrop`、`VHS_VideoCombine`、`CR Prompt Text`、`WanVideoBlockSwap`、`JWInteger`、`LoadImage`、`LoadAudio`、`WanVideoSampler`

**用到的条目**：LoadImage、WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoLoraSelect

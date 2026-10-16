---
key: 视频生成/图生视频/(扎发)Infinite talk数字人动态加强高版V4（Lightx2v+Rcm）_1986470586845167617.json
name: (扎发)Infinite talk数字人动态加强高版V4（Lightx2v+Rcm）_1986470586845167617.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1986470586845167617.json
hash: 49beea521a824588
coverage: 0.75
learned_at: 2026-10-15 22:32:55
nodes: [MarkdownNote, LayerUtility: ImageScaleByAspectRatio V2, LoadWanVideoT5TextEncoder, CLIPVisionLoader, PreviewAny, WanVideoVAELoader, WanVideoClipVisionEncode, Note, Note, Note, Note, Note, AudioSeparation, DownloadAndLoadWav2VecModel, GetImageSizeAndCount, Note, WanVideoModelLoader, WanVideoTextEncode, WanVideoSampler, WanVideoImageToVideoMultiTalk, WanVideoLoraSelect, WanVideoLoraSelect, MultiTalkModelLoader, JWFloat, MultiTalkWav2VecEmbeds, JWInteger, CR Prompt Text, LoadAudio, JWInteger, VHS_VideoCombine, VHS_VideoCombine, LoadImage, WanVideoDecode, AudioCrop, Reroute, WanVideoBlockSwap]
patterns: []
missing: []
---

# 视频生成/图生视频/(扎发)Infinite talk数字人动态加强高版V4（Lightx2v+Rcm）_1986470586845167617.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1986470586845167617.json`

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
- `Note`
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
- `JWInteger`
- `CR Prompt Text`
- `LoadAudio`
- `JWInteger`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `LoadImage`
- `WanVideoDecode`
- `AudioCrop`
- `Reroute`
- `WanVideoBlockSwap`

## 知识

覆盖率 **75%**（27/36）

**有卡**：`LayerUtility: ImageScaleByAspectRatio V2`、`LoadWanVideoT5TextEncoder`、`CLIPVisionLoader`、`WanVideoVAELoader`、`WanVideoClipVisionEncode`、`AudioSeparation`、`DownloadAndLoadWav2VecModel`、`GetImageSizeAndCount`、`WanVideoModelLoader`、`WanVideoTextEncode`、`WanVideoSampler`、`WanVideoImageToVideoMultiTalk`、`WanVideoLoraSelect`、`MultiTalkModelLoader`、`JWFloat`、`MultiTalkWav2VecEmbeds`、`JWInteger`、`CR Prompt Text`、`LoadAudio`、`VHS_VideoCombine`、`LoadImage`、`WanVideoDecode`、`AudioCrop`、`WanVideoBlockSwap`

**用到的条目**：LoadImage、WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoLoraSelect

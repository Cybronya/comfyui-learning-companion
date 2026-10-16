---
key: 视频生成/图生视频/Infinite talk数字人V4（Lightx2v+Rcm） 浮云12.11_1999018182650290177.json
name: Infinite talk数字人V4（Lightx2v+Rcm） 浮云12.11_1999018182650290177.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1999018182650290177.json
hash: da879e68b810692c
coverage: 0.896552
learned_at: 2026-10-15 22:33:35
nodes: [LayerUtility: ImageScaleByAspectRatio V2, LoadWanVideoT5TextEncoder, CLIPVisionLoader, PreviewAny, WanVideoVAELoader, WanVideoClipVisionEncode, AudioSeparation, DownloadAndLoadWav2VecModel, GetImageSizeAndCount, Note, WanVideoModelLoader, WanVideoSampler, WanVideoImageToVideoMultiTalk, WanVideoLoraSelect, MultiTalkModelLoader, JWFloat, MultiTalkWav2VecEmbeds, AudioCrop, WanVideoTextEncode, WanVideoDecode, Reroute, LoadImage, JWInteger, LoadAudio, CR Prompt Text, WanVideoBlockSwap, WanVideoLoraSelect, JWInteger, VHS_VideoCombine]
patterns: []
missing: []
---

# 视频生成/图生视频/Infinite talk数字人V4（Lightx2v+Rcm） 浮云12.11_1999018182650290177.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1999018182650290177.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（29 个）：
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadWanVideoT5TextEncoder`
- `CLIPVisionLoader`
- `PreviewAny`
- `WanVideoVAELoader`
- `WanVideoClipVisionEncode`
- `AudioSeparation`
- `DownloadAndLoadWav2VecModel`
- `GetImageSizeAndCount`
- `Note`
- `WanVideoModelLoader`
- `WanVideoSampler` ★核心
- `WanVideoImageToVideoMultiTalk`
- `WanVideoLoraSelect`
- `MultiTalkModelLoader`
- `JWFloat`
- `MultiTalkWav2VecEmbeds`
- `AudioCrop`
- `WanVideoTextEncode`
- `WanVideoDecode`
- `Reroute`
- `LoadImage`
- `JWInteger`
- `LoadAudio`
- `CR Prompt Text`
- `WanVideoBlockSwap`
- `WanVideoLoraSelect`
- `JWInteger`
- `VHS_VideoCombine`

## 知识

覆盖率 **90%**（26/29）

**有卡**：`LayerUtility: ImageScaleByAspectRatio V2`、`LoadWanVideoT5TextEncoder`、`CLIPVisionLoader`、`WanVideoVAELoader`、`WanVideoClipVisionEncode`、`AudioSeparation`、`DownloadAndLoadWav2VecModel`、`GetImageSizeAndCount`、`WanVideoModelLoader`、`WanVideoSampler`、`WanVideoImageToVideoMultiTalk`、`WanVideoLoraSelect`、`MultiTalkModelLoader`、`JWFloat`、`MultiTalkWav2VecEmbeds`、`AudioCrop`、`WanVideoTextEncode`、`WanVideoDecode`、`LoadImage`、`JWInteger`、`LoadAudio`、`CR Prompt Text`、`WanVideoBlockSwap`、`VHS_VideoCombine`

**用到的条目**：LoadImage、WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoLoraSelect

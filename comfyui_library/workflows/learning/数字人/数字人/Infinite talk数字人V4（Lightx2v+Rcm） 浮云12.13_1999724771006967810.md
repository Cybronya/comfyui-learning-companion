---
key: 数字人/数字人/Infinite talk数字人V4（Lightx2v+Rcm） 浮云12.13_1999724771006967810.json
name: Infinite talk数字人V4（Lightx2v+Rcm） 浮云12.13_1999724771006967810
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/数字人/数字人/Infinite talk数字人V4（Lightx2v+Rcm） 浮云12.13_1999724771006967810.json
hash: b0e80c46cb42fa93
coverage: 0.896552
learned_at: 2026-10-26 01:54:55
nodes: [LayerUtility: ImageScaleByAspectRatio V2, LoadWanVideoT5TextEncoder, CLIPVisionLoader, PreviewAny, WanVideoVAELoader, WanVideoClipVisionEncode, AudioSeparation, DownloadAndLoadWav2VecModel, GetImageSizeAndCount, Note, WanVideoModelLoader, WanVideoImageToVideoMultiTalk, WanVideoLoraSelect, MultiTalkModelLoader, JWFloat, MultiTalkWav2VecEmbeds, AudioCrop, WanVideoTextEncode, WanVideoDecode, Reroute, LoadImage, JWInteger, LoadAudio, JWInteger, CR Prompt Text, WanVideoBlockSwap, WanVideoLoraSelect, WanVideoSampler, VHS_VideoCombine]
patterns: []
missing: []
---

# 数字人/数字人/Infinite talk数字人V4（Lightx2v+Rcm） 浮云12.13_1999724771006967810.json

> 来源文件 `comfyui_library/workflows/数字人/数字人/Infinite talk数字人V4（Lightx2v+Rcm） 浮云12.13_1999724771006967810.json`

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
- `JWInteger`
- `CR Prompt Text`
- `WanVideoBlockSwap`
- `WanVideoLoraSelect`
- `WanVideoSampler` ★核心
- `VHS_VideoCombine`

## 知识

覆盖率 **90%**（26/29）

**有卡**：`LayerUtility: ImageScaleByAspectRatio V2`、`LoadWanVideoT5TextEncoder`、`CLIPVisionLoader`、`WanVideoVAELoader`、`WanVideoClipVisionEncode`、`AudioSeparation`、`DownloadAndLoadWav2VecModel`、`GetImageSizeAndCount`、`WanVideoModelLoader`、`WanVideoImageToVideoMultiTalk`、`WanVideoLoraSelect`、`MultiTalkModelLoader`、`JWFloat`、`MultiTalkWav2VecEmbeds`、`AudioCrop`、`WanVideoTextEncode`、`WanVideoDecode`、`LoadImage`、`JWInteger`、`LoadAudio`、`CR Prompt Text`、`WanVideoBlockSwap`、`WanVideoSampler`、`VHS_VideoCombine`

**用到的条目**：LoadImage、WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoLoraSelect

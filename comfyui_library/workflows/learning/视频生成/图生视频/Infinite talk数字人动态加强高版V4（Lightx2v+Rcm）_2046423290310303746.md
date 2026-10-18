---
key: 视频生成/图生视频/Infinite talk数字人动态加强高版V4（Lightx2v+Rcm）_2046423290310303746.json
name: Infinite talk数字人动态加强高版V4（Lightx2v+Rcm）_2046423290310303746.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/Infinite talk数字人动态加强高版V4（Lightx2v+Rcm）_2046423290310303746.json
hash: dc228996a1fc862f
coverage: 0.931034
learned_at: 2026-10-15 22:36:57
nodes: [WanVideoModelLoader, WanVideoLoraSelect, WanVideoLoraSelect, MultiTalkModelLoader, JWFloat, WanVideoBlockSwap, CLIPVisionLoader, LoadWanVideoT5TextEncoder, WanVideoVAELoader, WanVideoTextEncode, WanVideoImageToVideoMultiTalk, WanVideoSampler, WanVideoDecode, Reroute, VHS_VideoCombine, VHS_VideoCombine, WanVideoClipVisionEncode, AudioSeparation, JWInteger, MultiTalkWav2VecEmbeds, AudioCrop, DownloadAndLoadWav2VecModel, LoadAudio, LoadImage, CR Prompt Text, GetImageSizeAndCount, JWInteger, LayerUtility: ImageScaleByAspectRatio V2, PreviewAny]
patterns: []
missing: []
---

# 视频生成/图生视频/Infinite talk数字人动态加强高版V4（Lightx2v+Rcm）_2046423290310303746.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2046423290310303746.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（29 个）：
- `WanVideoModelLoader`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `MultiTalkModelLoader`
- `JWFloat`
- `WanVideoBlockSwap`
- `CLIPVisionLoader`
- `LoadWanVideoT5TextEncoder`
- `WanVideoVAELoader`
- `WanVideoTextEncode`
- `WanVideoImageToVideoMultiTalk`
- `WanVideoSampler` ★核心
- `WanVideoDecode`
- `Reroute`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `WanVideoClipVisionEncode`
- `AudioSeparation`
- `JWInteger`
- `MultiTalkWav2VecEmbeds`
- `AudioCrop`
- `DownloadAndLoadWav2VecModel`
- `LoadAudio`
- `LoadImage`
- `CR Prompt Text`
- `GetImageSizeAndCount`
- `JWInteger`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `PreviewAny`

## 知识

覆盖率 **93%**（27/29）

**有卡**：`WanVideoModelLoader`、`WanVideoLoraSelect`、`MultiTalkModelLoader`、`JWFloat`、`WanVideoBlockSwap`、`CLIPVisionLoader`、`LoadWanVideoT5TextEncoder`、`WanVideoVAELoader`、`WanVideoTextEncode`、`WanVideoImageToVideoMultiTalk`、`WanVideoSampler`、`WanVideoDecode`、`VHS_VideoCombine`、`WanVideoClipVisionEncode`、`AudioSeparation`、`JWInteger`、`MultiTalkWav2VecEmbeds`、`AudioCrop`、`DownloadAndLoadWav2VecModel`、`LoadAudio`、`LoadImage`、`CR Prompt Text`、`GetImageSizeAndCount`、`LayerUtility: ImageScaleByAspectRatio V2`

**用到的条目**：LoadImage、WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoLoraSelect

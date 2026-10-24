---
key: 图片生成/图生图/(白衣黑丝)Infinite talk数字人动态加强高版V4（Lightx2v+Rcm）_1995530159656722434.json
name: (白衣黑丝)Infinite talk数字人动态加强高版V4（Lightx2v+Rcm）_1995530159656722434
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/(白衣黑丝)Infinite talk数字人动态加强高版V4（Lightx2v+Rcm）_1995530159656722434.json
hash: caee2abdf999b077
coverage: 0.75
learned_at: 2026-10-23 10:46:50
nodes: [MarkdownNote, LayerUtility: ImageScaleByAspectRatio V2, LoadWanVideoT5TextEncoder, CLIPVisionLoader, PreviewAny, WanVideoVAELoader, WanVideoClipVisionEncode, Note, AudioSeparation, DownloadAndLoadWav2VecModel, GetImageSizeAndCount, Note, WanVideoModelLoader, WanVideoTextEncode, WanVideoSampler, WanVideoImageToVideoMultiTalk, WanVideoLoraSelect, WanVideoLoraSelect, MultiTalkModelLoader, JWFloat, MultiTalkWav2VecEmbeds, WanVideoDecode, AudioCrop, Reroute, CR Prompt Text, Note, Note, Note, JWInteger, VHS_VideoCombine, VHS_VideoCombine, LoadAudio, JWInteger, Note, LoadImage, WanVideoBlockSwap]
patterns: []
missing: []
---

# 图片生成/图生图/(白衣黑丝)Infinite talk数字人动态加强高版V4（Lightx2v+Rcm）_1995530159656722434.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/(白衣黑丝)Infinite talk数字人动态加强高版V4（Lightx2v+Rcm）_1995530159656722434.json`

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
- `CR Prompt Text`
- `Note`
- `Note`
- `Note`
- `JWInteger`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `LoadAudio`
- `JWInteger`
- `Note`
- `LoadImage`
- `WanVideoBlockSwap`

## 知识

覆盖率 **75%**（27/36）

**有卡**：`LayerUtility: ImageScaleByAspectRatio V2`、`LoadWanVideoT5TextEncoder`、`CLIPVisionLoader`、`WanVideoVAELoader`、`WanVideoClipVisionEncode`、`AudioSeparation`、`DownloadAndLoadWav2VecModel`、`GetImageSizeAndCount`、`WanVideoModelLoader`、`WanVideoTextEncode`、`WanVideoSampler`、`WanVideoImageToVideoMultiTalk`、`WanVideoLoraSelect`、`MultiTalkModelLoader`、`JWFloat`、`MultiTalkWav2VecEmbeds`、`WanVideoDecode`、`AudioCrop`、`CR Prompt Text`、`JWInteger`、`VHS_VideoCombine`、`LoadAudio`、`LoadImage`、`WanVideoBlockSwap`

**用到的条目**：LoadImage、WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoLoraSelect

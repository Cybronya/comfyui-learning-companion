---
key: 图片生成/图生图/(蓝马甲)Infinite talk数字人动态加强高版V4（Lightx2v+Rcm）_1998121724271058945.json
name: (蓝马甲)Infinite talk数字人动态加强高版V4（Lightx2v+Rcm）_1998121724271058945
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/(蓝马甲)Infinite talk数字人动态加强高版V4（Lightx2v+Rcm）_1998121724271058945.json
hash: d1263dc4d5aa307b
coverage: 0.75
learned_at: 2026-10-23 10:46:51
nodes: [MarkdownNote, LayerUtility: ImageScaleByAspectRatio V2, LoadWanVideoT5TextEncoder, CLIPVisionLoader, PreviewAny, WanVideoVAELoader, WanVideoClipVisionEncode, Note, AudioSeparation, DownloadAndLoadWav2VecModel, GetImageSizeAndCount, Note, WanVideoModelLoader, WanVideoTextEncode, WanVideoSampler, WanVideoImageToVideoMultiTalk, WanVideoLoraSelect, WanVideoLoraSelect, MultiTalkModelLoader, JWFloat, MultiTalkWav2VecEmbeds, WanVideoDecode, AudioCrop, Reroute, Note, CR Prompt Text, Note, Note, Note, JWInteger, VHS_VideoCombine, VHS_VideoCombine, WanVideoBlockSwap, LoadImage, LoadAudio, JWInteger]
patterns: []
missing: []
---

# 图片生成/图生图/(蓝马甲)Infinite talk数字人动态加强高版V4（Lightx2v+Rcm）_1998121724271058945.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/(蓝马甲)Infinite talk数字人动态加强高版V4（Lightx2v+Rcm）_1998121724271058945.json`

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
- `LoadImage`
- `LoadAudio`
- `JWInteger`

## 知识

覆盖率 **75%**（27/36）

**有卡**：`LayerUtility: ImageScaleByAspectRatio V2`、`LoadWanVideoT5TextEncoder`、`CLIPVisionLoader`、`WanVideoVAELoader`、`WanVideoClipVisionEncode`、`AudioSeparation`、`DownloadAndLoadWav2VecModel`、`GetImageSizeAndCount`、`WanVideoModelLoader`、`WanVideoTextEncode`、`WanVideoSampler`、`WanVideoImageToVideoMultiTalk`、`WanVideoLoraSelect`、`MultiTalkModelLoader`、`JWFloat`、`MultiTalkWav2VecEmbeds`、`WanVideoDecode`、`AudioCrop`、`CR Prompt Text`、`JWInteger`、`VHS_VideoCombine`、`WanVideoBlockSwap`、`LoadImage`、`LoadAudio`

**用到的条目**：LoadImage、WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoLoraSelect

---
key: 视频生成/图生视频/(茶餐厅)Infinite talk数字人动态加强高版V4（Lightx2v+Rcm）_1994792318651785217.json
name: (茶餐厅)Infinite talk数字人动态加强高版V4（Lightx2v+Rcm）_1994792318651785217.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1994792318651785217.json
hash: c56e231674237bda
coverage: 0.75
learned_at: 2026-10-15 22:33:21
nodes: [MarkdownNote, LayerUtility: ImageScaleByAspectRatio V2, LoadWanVideoT5TextEncoder, CLIPVisionLoader, PreviewAny, WanVideoVAELoader, WanVideoClipVisionEncode, Note, AudioSeparation, DownloadAndLoadWav2VecModel, GetImageSizeAndCount, Note, WanVideoModelLoader, WanVideoTextEncode, WanVideoSampler, WanVideoImageToVideoMultiTalk, WanVideoLoraSelect, WanVideoLoraSelect, MultiTalkModelLoader, JWFloat, MultiTalkWav2VecEmbeds, WanVideoDecode, AudioCrop, Reroute, VHS_VideoCombine, Note, VHS_VideoCombine, CR Prompt Text, Note, Note, JWInteger, Note, WanVideoBlockSwap, LoadAudio, LoadImage, JWInteger]
patterns: []
missing: []
---

# 视频生成/图生视频/(茶餐厅)Infinite talk数字人动态加强高版V4（Lightx2v+Rcm）_1994792318651785217.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1994792318651785217.json`

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
- `VHS_VideoCombine`
- `Note`
- `VHS_VideoCombine`
- `CR Prompt Text`
- `Note`
- `Note`
- `JWInteger`
- `Note`
- `WanVideoBlockSwap`
- `LoadAudio`
- `LoadImage`
- `JWInteger`

## 知识

覆盖率 **75%**（27/36）

**有卡**：`LayerUtility: ImageScaleByAspectRatio V2`、`LoadWanVideoT5TextEncoder`、`CLIPVisionLoader`、`WanVideoVAELoader`、`WanVideoClipVisionEncode`、`AudioSeparation`、`DownloadAndLoadWav2VecModel`、`GetImageSizeAndCount`、`WanVideoModelLoader`、`WanVideoTextEncode`、`WanVideoSampler`、`WanVideoImageToVideoMultiTalk`、`WanVideoLoraSelect`、`MultiTalkModelLoader`、`JWFloat`、`MultiTalkWav2VecEmbeds`、`WanVideoDecode`、`AudioCrop`、`VHS_VideoCombine`、`CR Prompt Text`、`JWInteger`、`WanVideoBlockSwap`、`LoadAudio`、`LoadImage`

**用到的条目**：LoadImage、WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoLoraSelect

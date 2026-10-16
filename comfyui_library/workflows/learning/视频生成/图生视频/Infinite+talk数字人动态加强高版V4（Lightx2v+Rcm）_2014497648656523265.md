---
key: 视频生成/图生视频/Infinite+talk数字人动态加强高版V4（Lightx2v+Rcm）_2014497648656523265.json
name: Infinite+talk数字人动态加强高版V4（Lightx2v+Rcm）_2014497648656523265.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2014497648656523265.json
hash: 513022f127d79159
coverage: 0.764706
learned_at: 2026-10-15 22:34:35
nodes: [WanVideoLoraSelect, Note, CLIPVisionLoader, WanVideoVAELoader, WanVideoModelLoader, MultiTalkModelLoader, WanVideoBlockSwap, WanVideoLoraSelect, JWFloat, Reroute, MarkdownNote, MarkdownNote, LayerUtility: ImageScaleByAspectRatio V2, LoadWanVideoT5TextEncoder, GetImageSizeAndCount, WanVideoTextEncode, WanVideoImageToVideoMultiTalk, WanVideoClipVisionEncode, DownloadAndLoadWav2VecModel, AudioCrop, AudioSeparation, MultiTalkWav2VecEmbeds, PreviewAny, WanVideoSampler, WanVideoDecode, LoadImage, LoadAudio, JWInteger, MarkdownNote, MarkdownNote, JWInteger, MarkdownNote, CR Prompt Text, VHS_VideoCombine]
patterns: []
missing: []
---

# 视频生成/图生视频/Infinite+talk数字人动态加强高版V4（Lightx2v+Rcm）_2014497648656523265.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2014497648656523265.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（34 个）：
- `WanVideoLoraSelect`
- `Note`
- `CLIPVisionLoader`
- `WanVideoVAELoader`
- `WanVideoModelLoader`
- `MultiTalkModelLoader`
- `WanVideoBlockSwap`
- `WanVideoLoraSelect`
- `JWFloat`
- `Reroute`
- `MarkdownNote`
- `MarkdownNote`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadWanVideoT5TextEncoder`
- `GetImageSizeAndCount`
- `WanVideoTextEncode`
- `WanVideoImageToVideoMultiTalk`
- `WanVideoClipVisionEncode`
- `DownloadAndLoadWav2VecModel`
- `AudioCrop`
- `AudioSeparation`
- `MultiTalkWav2VecEmbeds`
- `PreviewAny`
- `WanVideoSampler` ★核心
- `WanVideoDecode`
- `LoadImage`
- `LoadAudio`
- `JWInteger`
- `MarkdownNote`
- `MarkdownNote`
- `JWInteger`
- `MarkdownNote`
- `CR Prompt Text`
- `VHS_VideoCombine`

## 知识

覆盖率 **76%**（26/34）

**有卡**：`WanVideoLoraSelect`、`CLIPVisionLoader`、`WanVideoVAELoader`、`WanVideoModelLoader`、`MultiTalkModelLoader`、`WanVideoBlockSwap`、`JWFloat`、`LayerUtility: ImageScaleByAspectRatio V2`、`LoadWanVideoT5TextEncoder`、`GetImageSizeAndCount`、`WanVideoTextEncode`、`WanVideoImageToVideoMultiTalk`、`WanVideoClipVisionEncode`、`DownloadAndLoadWav2VecModel`、`AudioCrop`、`AudioSeparation`、`MultiTalkWav2VecEmbeds`、`WanVideoSampler`、`WanVideoDecode`、`LoadImage`、`LoadAudio`、`JWInteger`、`CR Prompt Text`、`VHS_VideoCombine`

**用到的条目**：LoadImage、WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoLoraSelect

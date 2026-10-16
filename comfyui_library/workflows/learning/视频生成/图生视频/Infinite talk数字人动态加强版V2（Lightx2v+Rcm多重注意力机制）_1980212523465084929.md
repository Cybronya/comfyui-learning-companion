---
key: 视频生成/图生视频/Infinite talk数字人动态加强版V2（Lightx2v+Rcm多重注意力机制）_1980212523465084929.json
name: Infinite talk数字人动态加强版V2（Lightx2v+Rcm多重注意力机制）_1980212523465084929.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1980212523465084929.json
hash: e6825752cee8a3f7
coverage: 0.672727
learned_at: 2026-10-15 22:32:29
nodes: [MarkdownNote, MultiTalkWav2VecEmbeds, LayerUtility: ImageScaleByAspectRatio V2, LoadWanVideoT5TextEncoder, CLIPVisionLoader, PreviewAny, MultiTalkModelLoader, WanVideoImageToVideoMultiTalk, WanVideoVAELoader, WanVideoClipVisionEncode, Note, Note, Note, Note, WanVideoBlockSwap, Note, AudioSeparation, AudioCrop, WanVideoDecode, CR Prompt Text, DownloadAndLoadWav2VecModel, GetImageSizeAndCount, LoadAudio, LoadImage, JWInteger, VHS_VideoCombine, VHS_VideoCombine, VHS_VideoCombine, Note, VHS_VideoCombine, Note, VHS_VideoCombine, VHS_VideoCombine, JWInteger, VHS_VideoCombine, VHS_VideoCombine, VHS_VideoCombine, VHS_VideoCombine, Note, Note, VHS_VideoCombine, Note, Note, Note, Note, Note, Note, WanVideoTextEncode, WanVideoSampler, Note, VHS_VideoCombine, WanVideoModelLoader, WanVideoLoraSelect, WanVideoLoraSelect, JWFloat]
patterns: []
missing: []
---

# 视频生成/图生视频/Infinite talk数字人动态加强版V2（Lightx2v+Rcm多重注意力机制）_1980212523465084929.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1980212523465084929.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（55 个）：
- `MarkdownNote`
- `MultiTalkWav2VecEmbeds`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadWanVideoT5TextEncoder`
- `CLIPVisionLoader`
- `PreviewAny`
- `MultiTalkModelLoader`
- `WanVideoImageToVideoMultiTalk`
- `WanVideoVAELoader`
- `WanVideoClipVisionEncode`
- `Note`
- `Note`
- `Note`
- `Note`
- `WanVideoBlockSwap`
- `Note`
- `AudioSeparation`
- `AudioCrop`
- `WanVideoDecode`
- `CR Prompt Text`
- `DownloadAndLoadWav2VecModel`
- `GetImageSizeAndCount`
- `LoadAudio`
- `LoadImage`
- `JWInteger`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `Note`
- `VHS_VideoCombine`
- `Note`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `JWInteger`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `Note`
- `Note`
- `VHS_VideoCombine`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `WanVideoTextEncode`
- `WanVideoSampler` ★核心
- `Note`
- `VHS_VideoCombine`
- `WanVideoModelLoader`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `JWFloat`

## 知识

覆盖率 **67%**（37/55）

**有卡**：`MultiTalkWav2VecEmbeds`、`LayerUtility: ImageScaleByAspectRatio V2`、`LoadWanVideoT5TextEncoder`、`CLIPVisionLoader`、`MultiTalkModelLoader`、`WanVideoImageToVideoMultiTalk`、`WanVideoVAELoader`、`WanVideoClipVisionEncode`、`WanVideoBlockSwap`、`AudioSeparation`、`AudioCrop`、`WanVideoDecode`、`CR Prompt Text`、`DownloadAndLoadWav2VecModel`、`GetImageSizeAndCount`、`LoadAudio`、`LoadImage`、`JWInteger`、`VHS_VideoCombine`、`WanVideoTextEncode`、`WanVideoSampler`、`WanVideoModelLoader`、`WanVideoLoraSelect`、`JWFloat`

**用到的条目**：LoadImage、WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoLoraSelect

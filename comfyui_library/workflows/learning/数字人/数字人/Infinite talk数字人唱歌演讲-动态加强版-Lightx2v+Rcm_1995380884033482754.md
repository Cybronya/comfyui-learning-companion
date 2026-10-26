---
key: 数字人/数字人/Infinite talk数字人唱歌演讲-动态加强版-Lightx2v+Rcm_1995380884033482754.json
name: Infinite talk数字人唱歌演讲-动态加强版-Lightx2v+Rcm_1995380884033482754
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/数字人/数字人/Infinite talk数字人唱歌演讲-动态加强版-Lightx2v+Rcm_1995380884033482754.json
hash: 453615632c56f031
coverage: 0.702703
learned_at: 2026-10-26 01:54:56
nodes: [CLIPVisionLoader, PreviewAny, WanVideoVAELoader, WanVideoModelLoader, Note, WanVideoTextEncode, AudioSeparation, Note, Note, WanVideoClipVisionEncode, Note, DownloadAndLoadWav2VecModel, LoadImage, WanVideoImageToVideoMultiTalk, WanVideoSampler, WanVideoDecode, Reroute, WanVideoBlockSwap, WanVideoLoraSelect, Note, Note, GetImageSizeAndCount, MultiTalkWav2VecEmbeds, LayerUtility: ImageScaleByAspectRatio V2, JWInteger, LoadWanVideoT5TextEncoder, Note, MarkdownNote, MarkdownNote, VHS_VideoCombine, JWInteger, AudioCrop, JWFloat, MultiTalkModelLoader, WanVideoLoraSelect, LoadAudio, CR Prompt Text]
patterns: []
missing: []
---

# 数字人/数字人/Infinite talk数字人唱歌演讲-动态加强版-Lightx2v+Rcm_1995380884033482754.json

> 来源文件 `comfyui_library/workflows/数字人/数字人/Infinite talk数字人唱歌演讲-动态加强版-Lightx2v+Rcm_1995380884033482754.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（37 个）：
- `CLIPVisionLoader`
- `PreviewAny`
- `WanVideoVAELoader`
- `WanVideoModelLoader`
- `Note`
- `WanVideoTextEncode`
- `AudioSeparation`
- `Note`
- `Note`
- `WanVideoClipVisionEncode`
- `Note`
- `DownloadAndLoadWav2VecModel`
- `LoadImage`
- `WanVideoImageToVideoMultiTalk`
- `WanVideoSampler` ★核心
- `WanVideoDecode`
- `Reroute`
- `WanVideoBlockSwap`
- `WanVideoLoraSelect`
- `Note`
- `Note`
- `GetImageSizeAndCount`
- `MultiTalkWav2VecEmbeds`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `JWInteger`
- `LoadWanVideoT5TextEncoder`
- `Note`
- `MarkdownNote`
- `MarkdownNote`
- `VHS_VideoCombine`
- `JWInteger`
- `AudioCrop`
- `JWFloat`
- `MultiTalkModelLoader`
- `WanVideoLoraSelect`
- `LoadAudio`
- `CR Prompt Text`

## 知识

覆盖率 **70%**（26/37）

**有卡**：`CLIPVisionLoader`、`WanVideoVAELoader`、`WanVideoModelLoader`、`WanVideoTextEncode`、`AudioSeparation`、`WanVideoClipVisionEncode`、`DownloadAndLoadWav2VecModel`、`LoadImage`、`WanVideoImageToVideoMultiTalk`、`WanVideoSampler`、`WanVideoDecode`、`WanVideoBlockSwap`、`WanVideoLoraSelect`、`GetImageSizeAndCount`、`MultiTalkWav2VecEmbeds`、`LayerUtility: ImageScaleByAspectRatio V2`、`JWInteger`、`LoadWanVideoT5TextEncoder`、`VHS_VideoCombine`、`AudioCrop`、`JWFloat`、`MultiTalkModelLoader`、`LoadAudio`、`CR Prompt Text`

**用到的条目**：LoadImage、WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoLoraSelect

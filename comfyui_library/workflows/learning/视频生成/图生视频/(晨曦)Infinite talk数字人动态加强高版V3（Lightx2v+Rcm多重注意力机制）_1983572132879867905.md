---
key: 视频生成/图生视频/(晨曦)Infinite talk数字人动态加强高版V3（Lightx2v+Rcm多重注意力机制）_1983572132879867905.json
name: (晨曦)Infinite talk数字人动态加强高版V3（Lightx2v+Rcm多重注意力机制）_1983572132879867905.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1983572132879867905.json
hash: c2f9d9da4439ff89
coverage: 0.771429
learned_at: 2026-10-15 22:32:45
nodes: [MarkdownNote, MultiTalkWav2VecEmbeds, LayerUtility: ImageScaleByAspectRatio V2, LoadWanVideoT5TextEncoder, CLIPVisionLoader, PreviewAny, WanVideoVAELoader, WanVideoClipVisionEncode, Note, Note, Note, Note, Note, AudioSeparation, CR Prompt Text, DownloadAndLoadWav2VecModel, GetImageSizeAndCount, Note, WanVideoModelLoader, WanVideoTextEncode, WanVideoSampler, WanVideoImageToVideoMultiTalk, JWInteger, AudioCrop, WanVideoLoraSelect, WanVideoLoraSelect, MultiTalkModelLoader, JWFloat, WanVideoBlockSwap, WanVideoDecode, LoadAudio, JWInteger, LoadImage, VHS_VideoCombine, VHS_VideoCombine]
patterns: []
missing: []
---

# 视频生成/图生视频/(晨曦)Infinite talk数字人动态加强高版V3（Lightx2v+Rcm多重注意力机制）_1983572132879867905.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1983572132879867905.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（35 个）：
- `MarkdownNote`
- `MultiTalkWav2VecEmbeds`
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
- `CR Prompt Text`
- `DownloadAndLoadWav2VecModel`
- `GetImageSizeAndCount`
- `Note`
- `WanVideoModelLoader`
- `WanVideoTextEncode`
- `WanVideoSampler` ★核心
- `WanVideoImageToVideoMultiTalk`
- `JWInteger`
- `AudioCrop`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `MultiTalkModelLoader`
- `JWFloat`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `LoadAudio`
- `JWInteger`
- `LoadImage`
- `VHS_VideoCombine`
- `VHS_VideoCombine`

## 知识

覆盖率 **77%**（27/35）

**有卡**：`MultiTalkWav2VecEmbeds`、`LayerUtility: ImageScaleByAspectRatio V2`、`LoadWanVideoT5TextEncoder`、`CLIPVisionLoader`、`WanVideoVAELoader`、`WanVideoClipVisionEncode`、`AudioSeparation`、`CR Prompt Text`、`DownloadAndLoadWav2VecModel`、`GetImageSizeAndCount`、`WanVideoModelLoader`、`WanVideoTextEncode`、`WanVideoSampler`、`WanVideoImageToVideoMultiTalk`、`JWInteger`、`AudioCrop`、`WanVideoLoraSelect`、`MultiTalkModelLoader`、`JWFloat`、`WanVideoBlockSwap`、`WanVideoDecode`、`LoadAudio`、`LoadImage`、`VHS_VideoCombine`

**用到的条目**：LoadImage、WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoLoraSelect

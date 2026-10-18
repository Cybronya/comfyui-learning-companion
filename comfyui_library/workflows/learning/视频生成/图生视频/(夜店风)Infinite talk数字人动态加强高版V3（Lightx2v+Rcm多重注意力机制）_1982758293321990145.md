---
key: 视频生成/图生视频/(夜店风)Infinite talk数字人动态加强高版V3（Lightx2v+Rcm多重注意力机制）_1982758293321990145.json
name: (夜店风)Infinite talk数字人动态加强高版V3（Lightx2v+Rcm多重注意力机制）_1982758293321990145.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/(夜店风)Infinite talk数字人动态加强高版V3（Lightx2v+Rcm多重注意力机制）_1982758293321990145.json
hash: 6b3a80df79d1d6ff
coverage: 0.771429
learned_at: 2026-10-15 22:32:42
nodes: [MarkdownNote, MultiTalkWav2VecEmbeds, LayerUtility: ImageScaleByAspectRatio V2, LoadWanVideoT5TextEncoder, CLIPVisionLoader, PreviewAny, WanVideoVAELoader, WanVideoClipVisionEncode, Note, Note, Note, Note, WanVideoBlockSwap, Note, AudioSeparation, CR Prompt Text, DownloadAndLoadWav2VecModel, GetImageSizeAndCount, Note, WanVideoModelLoader, WanVideoTextEncode, WanVideoImageToVideoMultiTalk, AudioCrop, WanVideoLoraSelect, WanVideoLoraSelect, MultiTalkModelLoader, JWFloat, JWInteger, JWInteger, LoadImage, LoadAudio, WanVideoSampler, WanVideoDecode, VHS_VideoCombine, VHS_VideoCombine]
patterns: []
missing: []
---

# 视频生成/图生视频/(夜店风)Infinite talk数字人动态加强高版V3（Lightx2v+Rcm多重注意力机制）_1982758293321990145.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1982758293321990145.json`

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
- `WanVideoBlockSwap`
- `Note`
- `AudioSeparation`
- `CR Prompt Text`
- `DownloadAndLoadWav2VecModel`
- `GetImageSizeAndCount`
- `Note`
- `WanVideoModelLoader`
- `WanVideoTextEncode`
- `WanVideoImageToVideoMultiTalk`
- `AudioCrop`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `MultiTalkModelLoader`
- `JWFloat`
- `JWInteger`
- `JWInteger`
- `LoadImage`
- `LoadAudio`
- `WanVideoSampler` ★核心
- `WanVideoDecode`
- `VHS_VideoCombine`
- `VHS_VideoCombine`

## 知识

覆盖率 **77%**（27/35）

**有卡**：`MultiTalkWav2VecEmbeds`、`LayerUtility: ImageScaleByAspectRatio V2`、`LoadWanVideoT5TextEncoder`、`CLIPVisionLoader`、`WanVideoVAELoader`、`WanVideoClipVisionEncode`、`WanVideoBlockSwap`、`AudioSeparation`、`CR Prompt Text`、`DownloadAndLoadWav2VecModel`、`GetImageSizeAndCount`、`WanVideoModelLoader`、`WanVideoTextEncode`、`WanVideoImageToVideoMultiTalk`、`AudioCrop`、`WanVideoLoraSelect`、`MultiTalkModelLoader`、`JWFloat`、`JWInteger`、`LoadImage`、`LoadAudio`、`WanVideoSampler`、`WanVideoDecode`、`VHS_VideoCombine`

**用到的条目**：LoadImage、WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoLoraSelect

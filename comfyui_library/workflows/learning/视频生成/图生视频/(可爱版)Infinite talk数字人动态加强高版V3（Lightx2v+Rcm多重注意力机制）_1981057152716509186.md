---
key: 视频生成/图生视频/(可爱版)Infinite talk数字人动态加强高版V3（Lightx2v+Rcm多重注意力机制）_1981057152716509186.json
name: (可爱版)Infinite talk数字人动态加强高版V3（Lightx2v+Rcm多重注意力机制）_1981057152716509186.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/(可爱版)Infinite talk数字人动态加强高版V3（Lightx2v+Rcm多重注意力机制）_1981057152716509186.json
hash: 76a9fe78a9405de0
coverage: 0.771429
learned_at: 2026-10-15 22:32:36
nodes: [MarkdownNote, MultiTalkWav2VecEmbeds, LayerUtility: ImageScaleByAspectRatio V2, LoadWanVideoT5TextEncoder, CLIPVisionLoader, PreviewAny, MultiTalkModelLoader, WanVideoVAELoader, WanVideoClipVisionEncode, Note, Note, Note, Note, WanVideoBlockSwap, Note, AudioSeparation, CR Prompt Text, DownloadAndLoadWav2VecModel, GetImageSizeAndCount, Note, WanVideoModelLoader, WanVideoLoraSelect, WanVideoLoraSelect, WanVideoTextEncode, WanVideoSampler, WanVideoImageToVideoMultiTalk, JWInteger, VHS_VideoCombine, WanVideoDecode, VHS_VideoCombine, AudioCrop, LoadAudio, JWInteger, JWFloat, LoadImage]
patterns: []
missing: []
---

# 视频生成/图生视频/(可爱版)Infinite talk数字人动态加强高版V3（Lightx2v+Rcm多重注意力机制）_1981057152716509186.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1981057152716509186.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（35 个）：
- `MarkdownNote`
- `MultiTalkWav2VecEmbeds`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadWanVideoT5TextEncoder`
- `CLIPVisionLoader`
- `PreviewAny`
- `MultiTalkModelLoader`
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
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `WanVideoTextEncode`
- `WanVideoSampler` ★核心
- `WanVideoImageToVideoMultiTalk`
- `JWInteger`
- `VHS_VideoCombine`
- `WanVideoDecode`
- `VHS_VideoCombine`
- `AudioCrop`
- `LoadAudio`
- `JWInteger`
- `JWFloat`
- `LoadImage`

## 知识

覆盖率 **77%**（27/35）

**有卡**：`MultiTalkWav2VecEmbeds`、`LayerUtility: ImageScaleByAspectRatio V2`、`LoadWanVideoT5TextEncoder`、`CLIPVisionLoader`、`MultiTalkModelLoader`、`WanVideoVAELoader`、`WanVideoClipVisionEncode`、`WanVideoBlockSwap`、`AudioSeparation`、`CR Prompt Text`、`DownloadAndLoadWav2VecModel`、`GetImageSizeAndCount`、`WanVideoModelLoader`、`WanVideoLoraSelect`、`WanVideoTextEncode`、`WanVideoSampler`、`WanVideoImageToVideoMultiTalk`、`JWInteger`、`VHS_VideoCombine`、`WanVideoDecode`、`AudioCrop`、`LoadAudio`、`JWFloat`、`LoadImage`

**用到的条目**：LoadImage、WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoLoraSelect

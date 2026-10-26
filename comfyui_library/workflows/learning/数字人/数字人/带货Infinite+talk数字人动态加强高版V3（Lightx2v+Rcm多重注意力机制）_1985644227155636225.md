---
key: 数字人/数字人/带货Infinite+talk数字人动态加强高版V3（Lightx2v+Rcm多重注意力机制）_1985644227155636225.json
name: 带货Infinite+talk数字人动态加强高版V3（Lightx2v+Rcm多重注意力机制）_1985644227155636225
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/数字人/数字人/带货Infinite+talk数字人动态加强高版V3（Lightx2v+Rcm多重注意力机制）_1985644227155636225.json
hash: 63120a427819c26f
coverage: 0.771429
learned_at: 2026-10-26 02:02:02
nodes: [MarkdownNote, LayerUtility: ImageScaleByAspectRatio V2, CLIPVisionLoader, PreviewAny, WanVideoVAELoader, Note, AudioSeparation, CR Prompt Text, DownloadAndLoadWav2VecModel, GetImageSizeAndCount, Note, WanVideoModelLoader, WanVideoLoraSelect, MultiTalkModelLoader, MultiTalkWav2VecEmbeds, JWInteger, WanVideoBlockSwap, WanVideoTextEncode, WanVideoDecode, WanVideoClipVisionEncode, Note, AudioCrop, LoadAudio, Note, Note, Note, JWInteger, WanVideoLoraSelect, JWFloat, LoadImage, WanVideoImageToVideoMultiTalk, WanVideoSampler, VHS_VideoCombine, LoadWanVideoT5TextEncoder, VHS_VideoCombine]
patterns: []
missing: []
---

# 数字人/数字人/带货Infinite+talk数字人动态加强高版V3（Lightx2v+Rcm多重注意力机制）_1985644227155636225.json

> 来源文件 `comfyui_library/workflows/数字人/数字人/带货Infinite+talk数字人动态加强高版V3（Lightx2v+Rcm多重注意力机制）_1985644227155636225.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（35 个）：
- `MarkdownNote`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `CLIPVisionLoader`
- `PreviewAny`
- `WanVideoVAELoader`
- `Note`
- `AudioSeparation`
- `CR Prompt Text`
- `DownloadAndLoadWav2VecModel`
- `GetImageSizeAndCount`
- `Note`
- `WanVideoModelLoader`
- `WanVideoLoraSelect`
- `MultiTalkModelLoader`
- `MultiTalkWav2VecEmbeds`
- `JWInteger`
- `WanVideoBlockSwap`
- `WanVideoTextEncode`
- `WanVideoDecode`
- `WanVideoClipVisionEncode`
- `Note`
- `AudioCrop`
- `LoadAudio`
- `Note`
- `Note`
- `Note`
- `JWInteger`
- `WanVideoLoraSelect`
- `JWFloat`
- `LoadImage`
- `WanVideoImageToVideoMultiTalk`
- `WanVideoSampler` ★核心
- `VHS_VideoCombine`
- `LoadWanVideoT5TextEncoder`
- `VHS_VideoCombine`

## 知识

覆盖率 **77%**（27/35）

**有卡**：`LayerUtility: ImageScaleByAspectRatio V2`、`CLIPVisionLoader`、`WanVideoVAELoader`、`AudioSeparation`、`CR Prompt Text`、`DownloadAndLoadWav2VecModel`、`GetImageSizeAndCount`、`WanVideoModelLoader`、`WanVideoLoraSelect`、`MultiTalkModelLoader`、`MultiTalkWav2VecEmbeds`、`JWInteger`、`WanVideoBlockSwap`、`WanVideoTextEncode`、`WanVideoDecode`、`WanVideoClipVisionEncode`、`AudioCrop`、`LoadAudio`、`JWFloat`、`LoadImage`、`WanVideoImageToVideoMultiTalk`、`WanVideoSampler`、`VHS_VideoCombine`、`LoadWanVideoT5TextEncoder`

**用到的条目**：LoadImage、WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoLoraSelect

---
key: 图片生成/图生图/(KJ装)Infinite talk数字人动态加强高版V3（Lightx2v+Rcm多重注意力机制）_1983138457956589570.json
name: (KJ装)Infinite talk数字人动态加强高版V3（Lightx2v+Rcm多重注意力机制）_1983138457956589570
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/(KJ装)Infinite talk数字人动态加强高版V3（Lightx2v+Rcm多重注意力机制）_1983138457956589570.json
hash: cad9a5d6d91388cb
coverage: 0.771429
learned_at: 2026-10-23 10:46:42
nodes: [MarkdownNote, MultiTalkWav2VecEmbeds, LayerUtility: ImageScaleByAspectRatio V2, LoadWanVideoT5TextEncoder, CLIPVisionLoader, PreviewAny, WanVideoVAELoader, WanVideoClipVisionEncode, Note, Note, Note, Note, Note, AudioSeparation, CR Prompt Text, DownloadAndLoadWav2VecModel, GetImageSizeAndCount, Note, WanVideoModelLoader, WanVideoTextEncode, WanVideoImageToVideoMultiTalk, WanVideoLoraSelect, WanVideoLoraSelect, MultiTalkModelLoader, JWFloat, JWInteger, JWInteger, WanVideoSampler, WanVideoDecode, VHS_VideoCombine, VHS_VideoCombine, LoadAudio, LoadImage, WanVideoBlockSwap, AudioCrop]
patterns: []
missing: []
---

# 图片生成/图生图/(KJ装)Infinite talk数字人动态加强高版V3（Lightx2v+Rcm多重注意力机制）_1983138457956589570.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/(KJ装)Infinite talk数字人动态加强高版V3（Lightx2v+Rcm多重注意力机制）_1983138457956589570.json`

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
- `WanVideoImageToVideoMultiTalk`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `MultiTalkModelLoader`
- `JWFloat`
- `JWInteger`
- `JWInteger`
- `WanVideoSampler` ★核心
- `WanVideoDecode`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `LoadAudio`
- `LoadImage`
- `WanVideoBlockSwap`
- `AudioCrop`

## 知识

覆盖率 **77%**（27/35）

**有卡**：`MultiTalkWav2VecEmbeds`、`LayerUtility: ImageScaleByAspectRatio V2`、`LoadWanVideoT5TextEncoder`、`CLIPVisionLoader`、`WanVideoVAELoader`、`WanVideoClipVisionEncode`、`AudioSeparation`、`CR Prompt Text`、`DownloadAndLoadWav2VecModel`、`GetImageSizeAndCount`、`WanVideoModelLoader`、`WanVideoTextEncode`、`WanVideoImageToVideoMultiTalk`、`WanVideoLoraSelect`、`MultiTalkModelLoader`、`JWFloat`、`JWInteger`、`WanVideoSampler`、`WanVideoDecode`、`VHS_VideoCombine`、`LoadAudio`、`LoadImage`、`WanVideoBlockSwap`、`AudioCrop`

**用到的条目**：LoadImage、WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoLoraSelect

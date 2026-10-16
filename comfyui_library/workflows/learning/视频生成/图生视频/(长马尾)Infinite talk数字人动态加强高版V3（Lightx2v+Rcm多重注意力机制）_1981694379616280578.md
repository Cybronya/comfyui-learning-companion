---
key: 视频生成/图生视频/(长马尾)Infinite talk数字人动态加强高版V3（Lightx2v+Rcm多重注意力机制）_1981694379616280578.json
name: (长马尾)Infinite talk数字人动态加强高版V3（Lightx2v+Rcm多重注意力机制）_1981694379616280578.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1981694379616280578.json
hash: 2c2ba2f0f06e0e65
coverage: 0.771429
learned_at: 2026-10-15 22:32:38
nodes: [MarkdownNote, MultiTalkWav2VecEmbeds, LayerUtility: ImageScaleByAspectRatio V2, LoadWanVideoT5TextEncoder, CLIPVisionLoader, PreviewAny, WanVideoVAELoader, WanVideoClipVisionEncode, Note, Note, Note, Note, WanVideoBlockSwap, Note, AudioSeparation, CR Prompt Text, DownloadAndLoadWav2VecModel, GetImageSizeAndCount, Note, WanVideoModelLoader, WanVideoTextEncode, WanVideoSampler, WanVideoImageToVideoMultiTalk, JWInteger, VHS_VideoCombine, WanVideoDecode, VHS_VideoCombine, AudioCrop, LoadAudio, JWInteger, LoadImage, WanVideoLoraSelect, WanVideoLoraSelect, MultiTalkModelLoader, JWFloat]
patterns: []
missing: []
---

# 视频生成/图生视频/(长马尾)Infinite talk数字人动态加强高版V3（Lightx2v+Rcm多重注意力机制）_1981694379616280578.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1981694379616280578.json`

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
- `WanVideoSampler` ★核心
- `WanVideoImageToVideoMultiTalk`
- `JWInteger`
- `VHS_VideoCombine`
- `WanVideoDecode`
- `VHS_VideoCombine`
- `AudioCrop`
- `LoadAudio`
- `JWInteger`
- `LoadImage`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `MultiTalkModelLoader`
- `JWFloat`

## 知识

覆盖率 **77%**（27/35）

**有卡**：`MultiTalkWav2VecEmbeds`、`LayerUtility: ImageScaleByAspectRatio V2`、`LoadWanVideoT5TextEncoder`、`CLIPVisionLoader`、`WanVideoVAELoader`、`WanVideoClipVisionEncode`、`WanVideoBlockSwap`、`AudioSeparation`、`CR Prompt Text`、`DownloadAndLoadWav2VecModel`、`GetImageSizeAndCount`、`WanVideoModelLoader`、`WanVideoTextEncode`、`WanVideoSampler`、`WanVideoImageToVideoMultiTalk`、`JWInteger`、`VHS_VideoCombine`、`WanVideoDecode`、`AudioCrop`、`LoadAudio`、`LoadImage`、`WanVideoLoraSelect`、`MultiTalkModelLoader`、`JWFloat`

**用到的条目**：LoadImage、WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoLoraSelect

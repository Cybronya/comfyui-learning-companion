---
key: 视频生成/文生视频/Infinite+talk数字人动态加强高版V3.5_1991175069309448194.json
name: Infinite+talk数字人动态加强高版V3.5_1991175069309448194
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/Infinite+talk数字人动态加强高版V3.5_1991175069309448194.json
hash: f852f2bc0511470b
coverage: 0.771429
learned_at: 2026-10-15 22:44:28
nodes: [MarkdownNote, LayerUtility: ImageScaleByAspectRatio V2, LoadWanVideoT5TextEncoder, CLIPVisionLoader, PreviewAny, WanVideoVAELoader, WanVideoClipVisionEncode, Note, Note, Note, Note, Note, AudioSeparation, GetImageSizeAndCount, Note, WanVideoModelLoader, WanVideoTextEncode, WanVideoSampler, WanVideoImageToVideoMultiTalk, WanVideoLoraSelect, MultiTalkModelLoader, JWFloat, MultiTalkWav2VecEmbeds, WanVideoBlockSwap, JWInteger, WanVideoDecode, VHS_VideoCombine, VHS_VideoCombine, CR Prompt Text, LoadImage, LoadAudio, WanVideoLoraSelect, AudioCrop, JWInteger, DownloadAndLoadWav2VecModel]
patterns: []
missing: []
---

# 视频生成/文生视频/Infinite+talk数字人动态加强高版V3.5_1991175069309448194.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/Infinite+talk数字人动态加强高版V3.5_1991175069309448194.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（35 个）：
- `MarkdownNote`
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
- `GetImageSizeAndCount`
- `Note`
- `WanVideoModelLoader`
- `WanVideoTextEncode`
- `WanVideoSampler` ★核心
- `WanVideoImageToVideoMultiTalk`
- `WanVideoLoraSelect`
- `MultiTalkModelLoader`
- `JWFloat`
- `MultiTalkWav2VecEmbeds`
- `WanVideoBlockSwap`
- `JWInteger`
- `WanVideoDecode`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `CR Prompt Text`
- `LoadImage`
- `LoadAudio`
- `WanVideoLoraSelect`
- `AudioCrop`
- `JWInteger`
- `DownloadAndLoadWav2VecModel`

## 知识

覆盖率 **77%**（27/35）

**有卡**：`LayerUtility: ImageScaleByAspectRatio V2`、`LoadWanVideoT5TextEncoder`、`CLIPVisionLoader`、`WanVideoVAELoader`、`WanVideoClipVisionEncode`、`AudioSeparation`、`GetImageSizeAndCount`、`WanVideoModelLoader`、`WanVideoTextEncode`、`WanVideoSampler`、`WanVideoImageToVideoMultiTalk`、`WanVideoLoraSelect`、`MultiTalkModelLoader`、`JWFloat`、`MultiTalkWav2VecEmbeds`、`WanVideoBlockSwap`、`JWInteger`、`WanVideoDecode`、`VHS_VideoCombine`、`CR Prompt Text`、`LoadImage`、`LoadAudio`、`AudioCrop`、`DownloadAndLoadWav2VecModel`

**用到的条目**：LoadImage、WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoLoraSelect

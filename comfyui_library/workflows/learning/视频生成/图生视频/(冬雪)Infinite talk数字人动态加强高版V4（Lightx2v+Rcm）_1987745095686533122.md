---
key: 视频生成/图生视频/(冬雪)Infinite talk数字人动态加强高版V4（Lightx2v+Rcm）_1987745095686533122.json
name: (冬雪)Infinite talk数字人动态加强高版V4（Lightx2v+Rcm）_1987745095686533122.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1987745095686533122.json
hash: 52a87d093d510fd5
coverage: 0.75
learned_at: 2026-10-15 22:33:00
nodes: [MarkdownNote, LayerUtility: ImageScaleByAspectRatio V2, LoadWanVideoT5TextEncoder, CLIPVisionLoader, PreviewAny, WanVideoVAELoader, WanVideoClipVisionEncode, Note, Note, Note, Note, Note, AudioSeparation, DownloadAndLoadWav2VecModel, GetImageSizeAndCount, Note, WanVideoModelLoader, WanVideoTextEncode, WanVideoSampler, WanVideoImageToVideoMultiTalk, WanVideoLoraSelect, WanVideoLoraSelect, MultiTalkModelLoader, JWFloat, MultiTalkWav2VecEmbeds, JWInteger, CR Prompt Text, VHS_VideoCombine, VHS_VideoCombine, WanVideoDecode, AudioCrop, Reroute, WanVideoBlockSwap, LoadAudio, JWInteger, LoadImage]
patterns: []
missing: []
---

# 视频生成/图生视频/(冬雪)Infinite talk数字人动态加强高版V4（Lightx2v+Rcm）_1987745095686533122.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1987745095686533122.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（36 个）：
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
- `DownloadAndLoadWav2VecModel`
- `GetImageSizeAndCount`
- `Note`
- `WanVideoModelLoader`
- `WanVideoTextEncode`
- `WanVideoSampler` ★核心
- `WanVideoImageToVideoMultiTalk`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `MultiTalkModelLoader`
- `JWFloat`
- `MultiTalkWav2VecEmbeds`
- `JWInteger`
- `CR Prompt Text`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `WanVideoDecode`
- `AudioCrop`
- `Reroute`
- `WanVideoBlockSwap`
- `LoadAudio`
- `JWInteger`
- `LoadImage`

## 知识

覆盖率 **75%**（27/36）

**有卡**：`LayerUtility: ImageScaleByAspectRatio V2`、`LoadWanVideoT5TextEncoder`、`CLIPVisionLoader`、`WanVideoVAELoader`、`WanVideoClipVisionEncode`、`AudioSeparation`、`DownloadAndLoadWav2VecModel`、`GetImageSizeAndCount`、`WanVideoModelLoader`、`WanVideoTextEncode`、`WanVideoSampler`、`WanVideoImageToVideoMultiTalk`、`WanVideoLoraSelect`、`MultiTalkModelLoader`、`JWFloat`、`MultiTalkWav2VecEmbeds`、`JWInteger`、`CR Prompt Text`、`VHS_VideoCombine`、`WanVideoDecode`、`AudioCrop`、`WanVideoBlockSwap`、`LoadAudio`、`LoadImage`

**用到的条目**：LoadImage、WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoLoraSelect

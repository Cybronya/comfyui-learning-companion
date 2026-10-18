---
key: 视频生成/图生视频/（荷花灯）Infinite talk数字人动态加强高版V4（Lightx2v+Rcm）_2026180704601645057.json
name: （荷花灯）Infinite talk数字人动态加强高版V4（Lightx2v+Rcm）_2026180704601645057.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/（荷花灯）Infinite talk数字人动态加强高版V4（Lightx2v+Rcm）_2026180704601645057.json
hash: ad498f9edac459f2
coverage: 0.75
learned_at: 2026-10-15 22:35:13
nodes: [LoadWanVideoT5TextEncoder, CLIPVisionLoader, PreviewAny, WanVideoVAELoader, WanVideoClipVisionEncode, AudioSeparation, DownloadAndLoadWav2VecModel, Note, WanVideoModelLoader, WanVideoLoraSelect, MultiTalkModelLoader, MultiTalkWav2VecEmbeds, GetImageSizeAndCount, Note, Reroute, JWInteger, CR Prompt Text, LayerUtility: ImageScaleByAspectRatio V2, MarkdownNote, WanVideoBlockSwap, Note, WanVideoDecode, WanVideoSampler, WanVideoLoraSelect, JWFloat, VHS_VideoCombine, VHS_VideoCombine, WanVideoTextEncode, WanVideoImageToVideoMultiTalk, Note, Note, Note, AudioCrop, LoadAudio, JWInteger, LoadImage]
patterns: []
missing: []
---

# 视频生成/图生视频/（荷花灯）Infinite talk数字人动态加强高版V4（Lightx2v+Rcm）_2026180704601645057.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2026180704601645057.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（36 个）：
- `LoadWanVideoT5TextEncoder`
- `CLIPVisionLoader`
- `PreviewAny`
- `WanVideoVAELoader`
- `WanVideoClipVisionEncode`
- `AudioSeparation`
- `DownloadAndLoadWav2VecModel`
- `Note`
- `WanVideoModelLoader`
- `WanVideoLoraSelect`
- `MultiTalkModelLoader`
- `MultiTalkWav2VecEmbeds`
- `GetImageSizeAndCount`
- `Note`
- `Reroute`
- `JWInteger`
- `CR Prompt Text`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `MarkdownNote`
- `WanVideoBlockSwap`
- `Note`
- `WanVideoDecode`
- `WanVideoSampler` ★核心
- `WanVideoLoraSelect`
- `JWFloat`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `WanVideoTextEncode`
- `WanVideoImageToVideoMultiTalk`
- `Note`
- `Note`
- `Note`
- `AudioCrop`
- `LoadAudio`
- `JWInteger`
- `LoadImage`

## 知识

覆盖率 **75%**（27/36）

**有卡**：`LoadWanVideoT5TextEncoder`、`CLIPVisionLoader`、`WanVideoVAELoader`、`WanVideoClipVisionEncode`、`AudioSeparation`、`DownloadAndLoadWav2VecModel`、`WanVideoModelLoader`、`WanVideoLoraSelect`、`MultiTalkModelLoader`、`MultiTalkWav2VecEmbeds`、`GetImageSizeAndCount`、`JWInteger`、`CR Prompt Text`、`LayerUtility: ImageScaleByAspectRatio V2`、`WanVideoBlockSwap`、`WanVideoDecode`、`WanVideoSampler`、`JWFloat`、`VHS_VideoCombine`、`WanVideoTextEncode`、`WanVideoImageToVideoMultiTalk`、`AudioCrop`、`LoadAudio`、`LoadImage`

**用到的条目**：LoadImage、WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoLoraSelect

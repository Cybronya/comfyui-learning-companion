---
key: 视频生成/图生视频/(红色睡衣)Infinite talk数字人动态加强高版V4（Lightx2v+Rcm）_2004565109903163393.json
name: (红色睡衣)Infinite talk数字人动态加强高版V4（Lightx2v+Rcm）_2004565109903163393.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2004565109903163393.json
hash: 4b743e66786919ad
coverage: 0.75
learned_at: 2026-10-15 22:33:55
nodes: [MarkdownNote, LayerUtility: ImageScaleByAspectRatio V2, LoadWanVideoT5TextEncoder, CLIPVisionLoader, PreviewAny, WanVideoVAELoader, WanVideoClipVisionEncode, AudioSeparation, DownloadAndLoadWav2VecModel, Note, WanVideoModelLoader, WanVideoSampler, WanVideoLoraSelect, WanVideoLoraSelect, MultiTalkModelLoader, JWFloat, MultiTalkWav2VecEmbeds, WanVideoDecode, AudioCrop, Reroute, Note, VHS_VideoCombine, JWInteger, GetImageSizeAndCount, Note, Note, Note, CR Prompt Text, VHS_VideoCombine, Note, WanVideoTextEncode, WanVideoImageToVideoMultiTalk, LoadAudio, JWInteger, LoadImage, WanVideoBlockSwap]
patterns: []
missing: []
---

# 视频生成/图生视频/(红色睡衣)Infinite talk数字人动态加强高版V4（Lightx2v+Rcm）_2004565109903163393.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2004565109903163393.json`

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
- `AudioSeparation`
- `DownloadAndLoadWav2VecModel`
- `Note`
- `WanVideoModelLoader`
- `WanVideoSampler` ★核心
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `MultiTalkModelLoader`
- `JWFloat`
- `MultiTalkWav2VecEmbeds`
- `WanVideoDecode`
- `AudioCrop`
- `Reroute`
- `Note`
- `VHS_VideoCombine`
- `JWInteger`
- `GetImageSizeAndCount`
- `Note`
- `Note`
- `Note`
- `CR Prompt Text`
- `VHS_VideoCombine`
- `Note`
- `WanVideoTextEncode`
- `WanVideoImageToVideoMultiTalk`
- `LoadAudio`
- `JWInteger`
- `LoadImage`
- `WanVideoBlockSwap`

## 知识

覆盖率 **75%**（27/36）

**有卡**：`LayerUtility: ImageScaleByAspectRatio V2`、`LoadWanVideoT5TextEncoder`、`CLIPVisionLoader`、`WanVideoVAELoader`、`WanVideoClipVisionEncode`、`AudioSeparation`、`DownloadAndLoadWav2VecModel`、`WanVideoModelLoader`、`WanVideoSampler`、`WanVideoLoraSelect`、`MultiTalkModelLoader`、`JWFloat`、`MultiTalkWav2VecEmbeds`、`WanVideoDecode`、`AudioCrop`、`VHS_VideoCombine`、`JWInteger`、`GetImageSizeAndCount`、`CR Prompt Text`、`WanVideoTextEncode`、`WanVideoImageToVideoMultiTalk`、`LoadAudio`、`LoadImage`、`WanVideoBlockSwap`

**用到的条目**：LoadImage、WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoLoraSelect

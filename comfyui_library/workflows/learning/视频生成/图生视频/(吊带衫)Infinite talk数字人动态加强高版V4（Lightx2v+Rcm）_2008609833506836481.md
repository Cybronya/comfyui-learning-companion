---
key: 视频生成/图生视频/(吊带衫)Infinite talk数字人动态加强高版V4（Lightx2v+Rcm）_2008609833506836481.json
name: (吊带衫)Infinite talk数字人动态加强高版V4（Lightx2v+Rcm）_2008609833506836481.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/(吊带衫)Infinite talk数字人动态加强高版V4（Lightx2v+Rcm）_2008609833506836481.json
hash: b1c83315f4d09652
coverage: 0.75
learned_at: 2026-10-15 22:34:08
nodes: [MarkdownNote, LayerUtility: ImageScaleByAspectRatio V2, LoadWanVideoT5TextEncoder, CLIPVisionLoader, PreviewAny, WanVideoVAELoader, WanVideoClipVisionEncode, AudioSeparation, DownloadAndLoadWav2VecModel, Note, WanVideoModelLoader, WanVideoTextEncode, WanVideoSampler, WanVideoImageToVideoMultiTalk, WanVideoLoraSelect, MultiTalkModelLoader, MultiTalkWav2VecEmbeds, AudioCrop, Reroute, JWInteger, GetImageSizeAndCount, Note, Note, Note, WanVideoBlockSwap, Note, VHS_VideoCombine, WanVideoDecode, WanVideoLoraSelect, JWFloat, CR Prompt Text, LoadAudio, JWInteger, LoadImage, Note, VHS_VideoCombine]
patterns: []
missing: []
---

# 视频生成/图生视频/(吊带衫)Infinite talk数字人动态加强高版V4（Lightx2v+Rcm）_2008609833506836481.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2008609833506836481.json`

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
- `WanVideoTextEncode`
- `WanVideoSampler` ★核心
- `WanVideoImageToVideoMultiTalk`
- `WanVideoLoraSelect`
- `MultiTalkModelLoader`
- `MultiTalkWav2VecEmbeds`
- `AudioCrop`
- `Reroute`
- `JWInteger`
- `GetImageSizeAndCount`
- `Note`
- `Note`
- `Note`
- `WanVideoBlockSwap`
- `Note`
- `VHS_VideoCombine`
- `WanVideoDecode`
- `WanVideoLoraSelect`
- `JWFloat`
- `CR Prompt Text`
- `LoadAudio`
- `JWInteger`
- `LoadImage`
- `Note`
- `VHS_VideoCombine`

## 知识

覆盖率 **75%**（27/36）

**有卡**：`LayerUtility: ImageScaleByAspectRatio V2`、`LoadWanVideoT5TextEncoder`、`CLIPVisionLoader`、`WanVideoVAELoader`、`WanVideoClipVisionEncode`、`AudioSeparation`、`DownloadAndLoadWav2VecModel`、`WanVideoModelLoader`、`WanVideoTextEncode`、`WanVideoSampler`、`WanVideoImageToVideoMultiTalk`、`WanVideoLoraSelect`、`MultiTalkModelLoader`、`MultiTalkWav2VecEmbeds`、`AudioCrop`、`JWInteger`、`GetImageSizeAndCount`、`WanVideoBlockSwap`、`VHS_VideoCombine`、`WanVideoDecode`、`JWFloat`、`CR Prompt Text`、`LoadAudio`、`LoadImage`

**用到的条目**：LoadImage、WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoLoraSelect

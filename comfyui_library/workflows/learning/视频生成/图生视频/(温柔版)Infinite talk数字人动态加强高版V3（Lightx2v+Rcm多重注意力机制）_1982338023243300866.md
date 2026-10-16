---
key: 视频生成/图生视频/(温柔版)Infinite talk数字人动态加强高版V3（Lightx2v+Rcm多重注意力机制）_1982338023243300866.json
name: (温柔版)Infinite talk数字人动态加强高版V3（Lightx2v+Rcm多重注意力机制）_1982338023243300866.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1982338023243300866.json
hash: 62af3bfe0eb7f8c8
coverage: 0.771429
learned_at: 2026-10-15 22:32:41
nodes: [MarkdownNote, MultiTalkWav2VecEmbeds, LayerUtility: ImageScaleByAspectRatio V2, LoadWanVideoT5TextEncoder, CLIPVisionLoader, PreviewAny, WanVideoVAELoader, WanVideoClipVisionEncode, Note, Note, Note, Note, WanVideoBlockSwap, Note, AudioSeparation, CR Prompt Text, DownloadAndLoadWav2VecModel, GetImageSizeAndCount, Note, WanVideoModelLoader, WanVideoTextEncode, WanVideoSampler, WanVideoImageToVideoMultiTalk, VHS_VideoCombine, AudioCrop, WanVideoLoraSelect, WanVideoLoraSelect, MultiTalkModelLoader, JWFloat, JWInteger, JWInteger, LoadImage, LoadAudio, WanVideoDecode, VHS_VideoCombine]
patterns: []
missing: []
---

# 视频生成/图生视频/(温柔版)Infinite talk数字人动态加强高版V3（Lightx2v+Rcm多重注意力机制）_1982338023243300866.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1982338023243300866.json`

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
- `VHS_VideoCombine`
- `AudioCrop`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `MultiTalkModelLoader`
- `JWFloat`
- `JWInteger`
- `JWInteger`
- `LoadImage`
- `LoadAudio`
- `WanVideoDecode`
- `VHS_VideoCombine`

## 知识

覆盖率 **77%**（27/35）

**有卡**：`MultiTalkWav2VecEmbeds`、`LayerUtility: ImageScaleByAspectRatio V2`、`LoadWanVideoT5TextEncoder`、`CLIPVisionLoader`、`WanVideoVAELoader`、`WanVideoClipVisionEncode`、`WanVideoBlockSwap`、`AudioSeparation`、`CR Prompt Text`、`DownloadAndLoadWav2VecModel`、`GetImageSizeAndCount`、`WanVideoModelLoader`、`WanVideoTextEncode`、`WanVideoSampler`、`WanVideoImageToVideoMultiTalk`、`VHS_VideoCombine`、`AudioCrop`、`WanVideoLoraSelect`、`MultiTalkModelLoader`、`JWFloat`、`JWInteger`、`LoadImage`、`LoadAudio`、`WanVideoDecode`

**用到的条目**：LoadImage、WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoLoraSelect

---
key: 视频生成/图生视频/（紫衫）)Infinite talk数字人动态加强高版V4（Lightx2v+Rcm）_1988918406697070593.json
name: （紫衫）)Infinite talk数字人动态加强高版V4（Lightx2v+Rcm）_1988918406697070593.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/（紫衫）)Infinite talk数字人动态加强高版V4（Lightx2v+Rcm）_1988918406697070593.json
hash: dba166ba4aae05bb
coverage: 0.75
learned_at: 2026-10-15 22:33:04
nodes: [MarkdownNote, LayerUtility: ImageScaleByAspectRatio V2, LoadWanVideoT5TextEncoder, CLIPVisionLoader, PreviewAny, WanVideoVAELoader, WanVideoClipVisionEncode, Note, Note, Note, Note, AudioSeparation, DownloadAndLoadWav2VecModel, GetImageSizeAndCount, Note, WanVideoModelLoader, WanVideoTextEncode, WanVideoSampler, WanVideoImageToVideoMultiTalk, WanVideoLoraSelect, WanVideoLoraSelect, MultiTalkModelLoader, JWFloat, MultiTalkWav2VecEmbeds, CR Prompt Text, WanVideoDecode, AudioCrop, VHS_VideoCombine, Reroute, VHS_VideoCombine, JWInteger, Note, LoadAudio, JWInteger, LoadImage, WanVideoBlockSwap]
patterns: []
missing: []
---

# 视频生成/图生视频/（紫衫）)Infinite talk数字人动态加强高版V4（Lightx2v+Rcm）_1988918406697070593.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1988918406697070593.json`

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
- `CR Prompt Text`
- `WanVideoDecode`
- `AudioCrop`
- `VHS_VideoCombine`
- `Reroute`
- `VHS_VideoCombine`
- `JWInteger`
- `Note`
- `LoadAudio`
- `JWInteger`
- `LoadImage`
- `WanVideoBlockSwap`

## 知识

覆盖率 **75%**（27/36）

**有卡**：`LayerUtility: ImageScaleByAspectRatio V2`、`LoadWanVideoT5TextEncoder`、`CLIPVisionLoader`、`WanVideoVAELoader`、`WanVideoClipVisionEncode`、`AudioSeparation`、`DownloadAndLoadWav2VecModel`、`GetImageSizeAndCount`、`WanVideoModelLoader`、`WanVideoTextEncode`、`WanVideoSampler`、`WanVideoImageToVideoMultiTalk`、`WanVideoLoraSelect`、`MultiTalkModelLoader`、`JWFloat`、`MultiTalkWav2VecEmbeds`、`CR Prompt Text`、`WanVideoDecode`、`AudioCrop`、`VHS_VideoCombine`、`JWInteger`、`LoadAudio`、`LoadImage`、`WanVideoBlockSwap`

**用到的条目**：LoadImage、WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoLoraSelect

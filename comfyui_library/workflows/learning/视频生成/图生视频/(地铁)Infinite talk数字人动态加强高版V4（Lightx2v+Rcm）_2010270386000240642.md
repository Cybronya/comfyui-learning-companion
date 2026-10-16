---
key: 视频生成/图生视频/(地铁)Infinite talk数字人动态加强高版V4（Lightx2v+Rcm）_2010270386000240642.json
name: (地铁)Infinite talk数字人动态加强高版V4（Lightx2v+Rcm）_2010270386000240642.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2010270386000240642.json
hash: 2e36193d568dfb74
coverage: 0.756757
learned_at: 2026-10-15 22:34:16
nodes: [MarkdownNote, LayerUtility: ImageScaleByAspectRatio V2, LoadWanVideoT5TextEncoder, CLIPVisionLoader, PreviewAny, WanVideoVAELoader, WanVideoClipVisionEncode, AudioSeparation, DownloadAndLoadWav2VecModel, Note, WanVideoModelLoader, WanVideoTextEncode, WanVideoSampler, WanVideoImageToVideoMultiTalk, WanVideoLoraSelect, MultiTalkModelLoader, MultiTalkWav2VecEmbeds, AudioCrop, VHS_VideoCombine, GetImageSizeAndCount, Note, Note, Note, Note, VHS_VideoCombine, WanVideoDecode, WanVideoLoraSelect, JWFloat, CR Prompt Text, WanVideoBlockSwap, Reroute, JWInteger, LoadAudio, JWInteger, Note, LoadImage, HAIGC_LoadImagesFromZip]
patterns: []
missing: []
---

# 视频生成/图生视频/(地铁)Infinite talk数字人动态加强高版V4（Lightx2v+Rcm）_2010270386000240642.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2010270386000240642.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（37 个）：
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
- `VHS_VideoCombine`
- `GetImageSizeAndCount`
- `Note`
- `Note`
- `Note`
- `Note`
- `VHS_VideoCombine`
- `WanVideoDecode`
- `WanVideoLoraSelect`
- `JWFloat`
- `CR Prompt Text`
- `WanVideoBlockSwap`
- `Reroute`
- `JWInteger`
- `LoadAudio`
- `JWInteger`
- `Note`
- `LoadImage`
- `HAIGC_LoadImagesFromZip`

## 知识

覆盖率 **76%**（28/37）

**有卡**：`LayerUtility: ImageScaleByAspectRatio V2`、`LoadWanVideoT5TextEncoder`、`CLIPVisionLoader`、`WanVideoVAELoader`、`WanVideoClipVisionEncode`、`AudioSeparation`、`DownloadAndLoadWav2VecModel`、`WanVideoModelLoader`、`WanVideoTextEncode`、`WanVideoSampler`、`WanVideoImageToVideoMultiTalk`、`WanVideoLoraSelect`、`MultiTalkModelLoader`、`MultiTalkWav2VecEmbeds`、`AudioCrop`、`VHS_VideoCombine`、`GetImageSizeAndCount`、`WanVideoDecode`、`JWFloat`、`CR Prompt Text`、`WanVideoBlockSwap`、`JWInteger`、`LoadAudio`、`LoadImage`、`HAIGC_LoadImagesFromZip`

**用到的条目**：LoadImage、WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoLoraSelect

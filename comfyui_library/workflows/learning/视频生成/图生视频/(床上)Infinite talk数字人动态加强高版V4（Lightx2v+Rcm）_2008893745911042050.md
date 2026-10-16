---
key: 视频生成/图生视频/(床上)Infinite talk数字人动态加强高版V4（Lightx2v+Rcm）_2008893745911042050.json
name: (床上)Infinite talk数字人动态加强高版V4（Lightx2v+Rcm）_2008893745911042050.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2008893745911042050.json
hash: bad0e3343cfb5ec9
coverage: 0.75
learned_at: 2026-10-15 22:34:10
nodes: [MarkdownNote, LayerUtility: ImageScaleByAspectRatio V2, LoadWanVideoT5TextEncoder, CLIPVisionLoader, PreviewAny, WanVideoVAELoader, WanVideoClipVisionEncode, AudioSeparation, DownloadAndLoadWav2VecModel, Note, WanVideoModelLoader, WanVideoTextEncode, WanVideoSampler, WanVideoImageToVideoMultiTalk, WanVideoLoraSelect, MultiTalkModelLoader, MultiTalkWav2VecEmbeds, AudioCrop, Reroute, VHS_VideoCombine, JWInteger, GetImageSizeAndCount, Note, Note, Note, Note, Note, VHS_VideoCombine, WanVideoDecode, WanVideoLoraSelect, JWFloat, CR Prompt Text, LoadAudio, JWInteger, LoadImage, WanVideoBlockSwap]
patterns: []
missing: []
---

# 视频生成/图生视频/(床上)Infinite talk数字人动态加强高版V4（Lightx2v+Rcm）_2008893745911042050.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2008893745911042050.json`

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
- `VHS_VideoCombine`
- `JWInteger`
- `GetImageSizeAndCount`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `VHS_VideoCombine`
- `WanVideoDecode`
- `WanVideoLoraSelect`
- `JWFloat`
- `CR Prompt Text`
- `LoadAudio`
- `JWInteger`
- `LoadImage`
- `WanVideoBlockSwap`

## 知识

覆盖率 **75%**（27/36）

**有卡**：`LayerUtility: ImageScaleByAspectRatio V2`、`LoadWanVideoT5TextEncoder`、`CLIPVisionLoader`、`WanVideoVAELoader`、`WanVideoClipVisionEncode`、`AudioSeparation`、`DownloadAndLoadWav2VecModel`、`WanVideoModelLoader`、`WanVideoTextEncode`、`WanVideoSampler`、`WanVideoImageToVideoMultiTalk`、`WanVideoLoraSelect`、`MultiTalkModelLoader`、`MultiTalkWav2VecEmbeds`、`AudioCrop`、`VHS_VideoCombine`、`JWInteger`、`GetImageSizeAndCount`、`WanVideoDecode`、`JWFloat`、`CR Prompt Text`、`LoadAudio`、`LoadImage`、`WanVideoBlockSwap`

**用到的条目**：LoadImage、WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoLoraSelect

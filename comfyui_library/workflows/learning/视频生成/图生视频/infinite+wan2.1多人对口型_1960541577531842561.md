---
key: 视频生成/图生视频/infinite+wan2.1多人对口型_1960541577531842561.json
name: infinite+wan2.1多人对口型_1960541577531842561.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1960541577531842561.json
hash: 487677951df52d43
coverage: 0.961538
learned_at: 2026-10-15 22:31:26
nodes: [WanVideoDecode, UpscaleModelLoader, ImageScaleToMegapixels, AudioCrop, LoadImage, LayerUtility: ImageScaleByAspectRatio V2, DownloadAndLoadWav2VecModel, AudioSeparation, AudioSeparation, VHS_VideoCombine, PreviewImage, MultiTalkWav2VecEmbeds, WanVideoLoraSelect, WanVideoImageToVideoMultiTalk, SeparateMasks, WanVideoModelLoader, WanVideoSampler, WanVideoTorchCompileSettings, WanVideoBlockSwap, MultiTalkModelLoader, WanVideoTextEncode, WanVideoVAELoader, LoadWanVideoT5TextEncoder, PreviewAudio, LoadAudio, AudioCrop]
patterns: []
missing: []
---

# 视频生成/图生视频/infinite+wan2.1多人对口型_1960541577531842561.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1960541577531842561.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（26 个）：
- `WanVideoDecode`
- `UpscaleModelLoader`
- `ImageScaleToMegapixels`
- `AudioCrop`
- `LoadImage`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `DownloadAndLoadWav2VecModel`
- `AudioSeparation`
- `AudioSeparation`
- `VHS_VideoCombine`
- `PreviewImage`
- `MultiTalkWav2VecEmbeds`
- `WanVideoLoraSelect`
- `WanVideoImageToVideoMultiTalk`
- `SeparateMasks`
- `WanVideoModelLoader`
- `WanVideoSampler` ★核心
- `WanVideoTorchCompileSettings`
- `WanVideoBlockSwap`
- `MultiTalkModelLoader`
- `WanVideoTextEncode`
- `WanVideoVAELoader`
- `LoadWanVideoT5TextEncoder`
- `PreviewAudio`
- `LoadAudio`
- `AudioCrop`

## 知识

覆盖率 **96%**（25/26）

**有卡**：`WanVideoDecode`、`UpscaleModelLoader`、`ImageScaleToMegapixels`、`AudioCrop`、`LoadImage`、`LayerUtility: ImageScaleByAspectRatio V2`、`DownloadAndLoadWav2VecModel`、`AudioSeparation`、`VHS_VideoCombine`、`MultiTalkWav2VecEmbeds`、`WanVideoLoraSelect`、`WanVideoImageToVideoMultiTalk`、`SeparateMasks`、`WanVideoModelLoader`、`WanVideoSampler`、`WanVideoTorchCompileSettings`、`WanVideoBlockSwap`、`MultiTalkModelLoader`、`WanVideoTextEncode`、`WanVideoVAELoader`、`LoadWanVideoT5TextEncoder`、`PreviewAudio`、`LoadAudio`

**用到的条目**：LoadImage、WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoLoraSelect、UpscaleModelLoader

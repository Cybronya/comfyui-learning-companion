---
key: 视频生成/图生视频/Wan2.1单人对口型_2064352779824623618.json
name: Wan2.1单人对口型_2064352779824623618.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/Wan2.1单人对口型_2064352779824623618.json
hash: 289508746797bf10
coverage: 0.977778
learned_at: 2026-10-15 22:39:23
nodes: [WanVideoBlockSwap, easy setNode, CLIPVisionLoader, easy setNode, easy setNode, WanVideoLoraSelect, easy setNode, easy setNode, WanVideoTorchCompileSettings, Wav2VecModelLoader, DownloadAndLoadWav2VecModel, easy setNode, easy setNode, easy setNode, AudioSeparation, easy getNode, easy getNode, MultiTalkWav2VecEmbeds, easy getNode, ImageResizeKJv2, PreviewAny, GetImageSizeAndCount, easy getNode, easy getNode, WanVideoClipVisionEncode, WanVideoImageToVideoMultiTalk, FancyTimerNode, easy getNode, easy getNode, easy getNode, easy getNode, WanVideoModelLoader, WanVideoTextEncodeCached, easy setNode, easy setNode, easy getNode, WanVideoSampler, WanVideoPassImagesFromSamples, ImageScale, VHS_VideoCombine, LoadImage, LoadAudio, CR Text, MultiTalkModelLoader, WanVideoVAELoader]
patterns: []
missing: []
---

# 视频生成/图生视频/Wan2.1单人对口型_2064352779824623618.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2064352779824623618.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（45 个）：
- `WanVideoBlockSwap`
- `easy setNode`
- `CLIPVisionLoader`
- `easy setNode`
- `easy setNode`
- `WanVideoLoraSelect`
- `easy setNode`
- `easy setNode`
- `WanVideoTorchCompileSettings`
- `Wav2VecModelLoader`
- `DownloadAndLoadWav2VecModel`
- `easy setNode`
- `easy setNode`
- `easy setNode`
- `AudioSeparation`
- `easy getNode`
- `easy getNode`
- `MultiTalkWav2VecEmbeds`
- `easy getNode`
- `ImageResizeKJv2`
- `PreviewAny`
- `GetImageSizeAndCount`
- `easy getNode`
- `easy getNode`
- `WanVideoClipVisionEncode`
- `WanVideoImageToVideoMultiTalk`
- `FancyTimerNode`
- `easy getNode`
- `easy getNode`
- `easy getNode`
- `easy getNode`
- `WanVideoModelLoader`
- `WanVideoTextEncodeCached`
- `easy setNode`
- `easy setNode`
- `easy getNode`
- `WanVideoSampler` ★核心
- `WanVideoPassImagesFromSamples`
- `ImageScale`
- `VHS_VideoCombine`
- `LoadImage`
- `LoadAudio`
- `CR Text`
- `MultiTalkModelLoader`
- `WanVideoVAELoader`

## 知识

覆盖率 **98%**（44/45）

**有卡**：`WanVideoBlockSwap`、`easy setNode`、`CLIPVisionLoader`、`WanVideoLoraSelect`、`WanVideoTorchCompileSettings`、`Wav2VecModelLoader`、`DownloadAndLoadWav2VecModel`、`AudioSeparation`、`easy getNode`、`MultiTalkWav2VecEmbeds`、`ImageResizeKJv2`、`GetImageSizeAndCount`、`WanVideoClipVisionEncode`、`WanVideoImageToVideoMultiTalk`、`FancyTimerNode`、`WanVideoModelLoader`、`WanVideoTextEncodeCached`、`WanVideoSampler`、`WanVideoPassImagesFromSamples`、`ImageScale`、`VHS_VideoCombine`、`LoadImage`、`LoadAudio`、`CR Text`、`MultiTalkModelLoader`、`WanVideoVAELoader`

**用到的条目**：LoadImage、WanVideoSampler、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoTextEncodeCached、WanVideoLoraSelect、CLIPVisionLoader、GetImageSizeAndCount

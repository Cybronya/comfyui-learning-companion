---
key: 数字人/数字人/Wan2.1单人对口型_2096760991131455490.json
name: Wan2.1单人对口型_2096760991131455490
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/数字人/数字人/Wan2.1单人对口型_2096760991131455490.json
hash: 9a70e2762d424e12
coverage: 0.97619
learned_at: 2026-10-19 00:19:14
nodes: [WanVideoBlockSwap, easy setNode, CLIPVisionLoader, easy setNode, easy setNode, WanVideoLoraSelect, easy setNode, easy setNode, WanVideoTorchCompileSettings, Wav2VecModelLoader, DownloadAndLoadWav2VecModel, easy setNode, easy setNode, easy setNode, easy getNode, MultiTalkWav2VecEmbeds, easy getNode, ImageResizeKJv2, PreviewAny, GetImageSizeAndCount, easy getNode, easy getNode, WanVideoClipVisionEncode, WanVideoImageToVideoMultiTalk, FancyTimerNode, easy getNode, easy getNode, easy getNode, easy getNode, WanVideoModelLoader, WanVideoTextEncodeCached, easy setNode, easy getNode, WanVideoSampler, WanVideoPassImagesFromSamples, ImageScale, VHS_VideoCombine, LoadImage, CR Text, MultiTalkModelLoader, WanVideoVAELoader, LoadAudio]
patterns: []
missing: []
---

# 数字人/数字人/Wan2.1单人对口型_2096760991131455490.json

> 来源文件 `comfyui_library/workflows/数字人/数字人/Wan2.1单人对口型_2096760991131455490.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（42 个）：
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
- `easy getNode`
- `WanVideoSampler` ★核心
- `WanVideoPassImagesFromSamples`
- `ImageScale`
- `VHS_VideoCombine`
- `LoadImage`
- `CR Text`
- `MultiTalkModelLoader`
- `WanVideoVAELoader`
- `LoadAudio`

## 知识

覆盖率 **98%**（41/42）

**有卡**：`WanVideoBlockSwap`、`easy setNode`、`CLIPVisionLoader`、`WanVideoLoraSelect`、`WanVideoTorchCompileSettings`、`Wav2VecModelLoader`、`DownloadAndLoadWav2VecModel`、`easy getNode`、`MultiTalkWav2VecEmbeds`、`ImageResizeKJv2`、`GetImageSizeAndCount`、`WanVideoClipVisionEncode`、`WanVideoImageToVideoMultiTalk`、`FancyTimerNode`、`WanVideoModelLoader`、`WanVideoTextEncodeCached`、`WanVideoSampler`、`WanVideoPassImagesFromSamples`、`ImageScale`、`VHS_VideoCombine`、`LoadImage`、`CR Text`、`MultiTalkModelLoader`、`WanVideoVAELoader`、`LoadAudio`

**用到的条目**：LoadImage、WanVideoSampler、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoTextEncodeCached、WanVideoLoraSelect、CLIPVisionLoader、GetImageSizeAndCount

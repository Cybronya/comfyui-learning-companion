---
key: 数字人/数字人/InfiniteTalk-GGUF.自用_1961661222749978625.json
name: InfiniteTalk-GGUF.自用_1961661222749978625
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/数字人/数字人/InfiniteTalk-GGUF.自用_1961661222749978625.json
hash: 27a5d29b4f4a1dfd
coverage: 0.545455
learned_at: 2026-10-26 01:55:05
nodes: [MarkdownNote, SetNode, SetNode, SetNode, SetNode, AudioCrop, AudioSeparation, DownloadAndLoadWav2VecModel, SetNode, GetNode, GetNode, WanVideoBlockSwap, WanVideoClipVisionEncode, GetNode, GetNode, SetNode, PreviewAny, SetNode, MultiTalkWav2VecEmbeds, Note, GetNode, WanVideoDecode, GetNode, GetImageSizeAndCount, GetNode, GetNode, ImageResizeKJv2, Note, WanVideoTorchCompileSettings, WanVideoLoraSelect, WanVideoModelLoader, CLIPVisionLoader, WanVideoImageToVideoMultiTalk, INTConstant, INTConstant, INTConstant, VHS_VideoCombine, WanVideoTextEncodeCached, LoadImage, LoadAudio, MultiTalkModelLoader, WanVideoVAELoader, WanVideoSampler, SetNode]
patterns: []
missing: []
---

# 数字人/数字人/InfiniteTalk-GGUF.自用_1961661222749978625.json

> 来源文件 `comfyui_library/workflows/数字人/数字人/InfiniteTalk-GGUF.自用_1961661222749978625.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（44 个）：
- `MarkdownNote`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `AudioCrop`
- `AudioSeparation`
- `DownloadAndLoadWav2VecModel`
- `SetNode`
- `GetNode`
- `GetNode`
- `WanVideoBlockSwap`
- `WanVideoClipVisionEncode`
- `GetNode`
- `GetNode`
- `SetNode`
- `PreviewAny`
- `SetNode`
- `MultiTalkWav2VecEmbeds`
- `Note`
- `GetNode`
- `WanVideoDecode`
- `GetNode`
- `GetImageSizeAndCount`
- `GetNode`
- `GetNode`
- `ImageResizeKJv2`
- `Note`
- `WanVideoTorchCompileSettings`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `CLIPVisionLoader`
- `WanVideoImageToVideoMultiTalk`
- `INTConstant`
- `INTConstant`
- `INTConstant`
- `VHS_VideoCombine`
- `WanVideoTextEncodeCached`
- `LoadImage`
- `LoadAudio`
- `MultiTalkModelLoader`
- `WanVideoVAELoader`
- `WanVideoSampler` ★核心
- `SetNode`

## 知识

覆盖率 **55%**（24/44）

**有卡**：`AudioCrop`、`AudioSeparation`、`DownloadAndLoadWav2VecModel`、`WanVideoBlockSwap`、`WanVideoClipVisionEncode`、`MultiTalkWav2VecEmbeds`、`WanVideoDecode`、`GetImageSizeAndCount`、`ImageResizeKJv2`、`WanVideoTorchCompileSettings`、`WanVideoLoraSelect`、`WanVideoModelLoader`、`CLIPVisionLoader`、`WanVideoImageToVideoMultiTalk`、`INTConstant`、`VHS_VideoCombine`、`WanVideoTextEncodeCached`、`LoadImage`、`LoadAudio`、`MultiTalkModelLoader`、`WanVideoVAELoader`、`WanVideoSampler`

**用到的条目**：LoadImage、WanVideoSampler、WanVideoDecode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoTextEncodeCached、WanVideoLoraSelect、CLIPVisionLoader

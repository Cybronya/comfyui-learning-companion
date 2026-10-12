---
key: 视频生成/图生视频/Wan2.1 InfiniTetalk 图像数字人配口型 KJ节点版_2044728496185937922.json
name: Wan2.1 InfiniTetalk 图像数字人配口型 KJ节点版_2044728496185937922
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/Wan2.1 InfiniTetalk 图像数字人配口型 KJ节点版_2044728496185937922.json
hash: 992c1a828773026a
coverage: 0.75
learned_at: 2026-10-13 01:36:54
nodes: [WanVideoBlockSwap, AudioSeparation, WanVideoTorchCompileSettings, WanVideoClipVisionEncode, Note, LoadImage, LoadImage, WanVideoLoraSelect, WanVideoSampler, DownloadAndLoadWav2VecModel, LoadWanVideoT5TextEncoder, Note, Note, SetNode, AudioCrop, WanVideoTextEncode, VHS_VideoCombine, MarkdownNote, INTConstant, LoadAudio, PixaromaResolution, ImageResizeKJv2, MultiTalkModelLoader, WanVideoModelLoader, WanVideoVAELoader, CLIPVisionLoader, WanVideoImageToVideoMultiTalk, GetNode, MultiTalkWav2VecEmbeds, SetNode, PixaromaLabel, PixaromaLabel, PlaySound|pysssss, WanVideoDecode, LoadImage, PreviewAny]
patterns: []
missing: [PlaySound|pysssss]
discoveries: [次要节点 `PlaySound|pysssss` 知识库中没有该节点类型的任何知识]
---

# 视频生成/图生视频/Wan2.1 InfiniTetalk 图像数字人配口型 KJ节点版_2044728496185937922.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/Wan2.1 InfiniTetalk 图像数字人配口型 KJ节点版_2044728496185937922.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（36 个）：
- `WanVideoBlockSwap`
- `AudioSeparation`
- `WanVideoTorchCompileSettings`
- `WanVideoClipVisionEncode`
- `Note`
- `LoadImage`
- `LoadImage`
- `WanVideoLoraSelect`
- `WanVideoSampler` ★核心
- `DownloadAndLoadWav2VecModel`
- `LoadWanVideoT5TextEncoder`
- `Note`
- `Note`
- `SetNode`
- `AudioCrop`
- `WanVideoTextEncode`
- `VHS_VideoCombine`
- `MarkdownNote`
- `INTConstant`
- `LoadAudio`
- `PixaromaResolution`
- `ImageResizeKJv2`
- `MultiTalkModelLoader`
- `WanVideoModelLoader`
- `WanVideoVAELoader`
- `CLIPVisionLoader`
- `WanVideoImageToVideoMultiTalk`
- `GetNode`
- `MultiTalkWav2VecEmbeds`
- `SetNode`
- `PixaromaLabel`
- `PixaromaLabel`
- `PlaySound|pysssss`
- `WanVideoDecode`
- `LoadImage`
- `PreviewAny`

## 知识

覆盖率 **75%**（27/36）

**有卡**：`WanVideoBlockSwap`、`AudioSeparation`、`WanVideoTorchCompileSettings`、`WanVideoClipVisionEncode`、`LoadImage`、`WanVideoLoraSelect`、`WanVideoSampler`、`DownloadAndLoadWav2VecModel`、`LoadWanVideoT5TextEncoder`、`AudioCrop`、`WanVideoTextEncode`、`VHS_VideoCombine`、`INTConstant`、`LoadAudio`、`PixaromaResolution`、`ImageResizeKJv2`、`MultiTalkModelLoader`、`WanVideoModelLoader`、`WanVideoVAELoader`、`CLIPVisionLoader`、`WanVideoImageToVideoMultiTalk`、`MultiTalkWav2VecEmbeds`、`PixaromaLabel`、`WanVideoDecode`

**缺卡**（1）：`PlaySound|pysssss`

**用到的条目**：LoadImage、WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoLoraSelect

## 学习发现

- 次要节点 `PlaySound|pysssss` 知识库中没有该节点类型的任何知识

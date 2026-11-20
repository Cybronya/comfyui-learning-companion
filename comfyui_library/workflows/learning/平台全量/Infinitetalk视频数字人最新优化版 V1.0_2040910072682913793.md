---
key: 平台全量/Infinitetalk视频数字人最新优化版 V1.0_2040910072682913793.json
name: Infinitetalk视频数字人最新优化版 V1.0_2040910072682913793
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/Infinitetalk视频数字人最新优化版 V1.0_2040910072682913793.json
hash: db52a3bf72c574c1
coverage: 0.928571
learned_at: 2026-11-14 00:32:44
nodes: [MultiTalkWav2VecEmbeds, VHS_VideoCombine, WanVideoImageToVideoMultiTalk, AudioSeparation, DownloadAndLoadWav2VecModel, GetImageRangeFromBatch, Audio Duration (mtb), WanVideoSampler, MathExpression|pysssss, MathExpression|pysssss, WanVideoTextEncodeCached, AudioCrop, CLIPVisionLoader, ImageResizeKJv2, WanVideoDecode, WanVideoEncode, MarkdownNote, MarkdownNote, WanVideoTorchCompileSettings, WanVideoBlockSwap, WanVideoLoraSelectMulti, MultiTalkModelLoader, WanVideoVAELoader, WanVideoModelLoader, WanVideoClipVisionEncode, VHS_LoadVideo, LoadAudio, VHS_VideoInfo]
patterns: []
missing: []
---

# 平台全量/Infinitetalk视频数字人最新优化版 V1.0_2040910072682913793.json

> 来源文件 `comfyui_library/workflows/平台全量/Infinitetalk视频数字人最新优化版 V1.0_2040910072682913793.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（28 个）：
- `MultiTalkWav2VecEmbeds`
- `VHS_VideoCombine`
- `WanVideoImageToVideoMultiTalk`
- `AudioSeparation`
- `DownloadAndLoadWav2VecModel`
- `GetImageRangeFromBatch`
- `Audio Duration (mtb)`
- `WanVideoSampler` ★核心
- `MathExpression|pysssss`
- `MathExpression|pysssss`
- `WanVideoTextEncodeCached`
- `AudioCrop`
- `CLIPVisionLoader`
- `ImageResizeKJv2`
- `WanVideoDecode`
- `WanVideoEncode`
- `MarkdownNote`
- `MarkdownNote`
- `WanVideoTorchCompileSettings`
- `WanVideoBlockSwap`
- `WanVideoLoraSelectMulti`
- `MultiTalkModelLoader`
- `WanVideoVAELoader`
- `WanVideoModelLoader`
- `WanVideoClipVisionEncode`
- `VHS_LoadVideo`
- `LoadAudio`
- `VHS_VideoInfo`

## 知识

覆盖率 **93%**（26/28）

**有卡**：`MultiTalkWav2VecEmbeds`、`VHS_VideoCombine`、`WanVideoImageToVideoMultiTalk`、`AudioSeparation`、`DownloadAndLoadWav2VecModel`、`GetImageRangeFromBatch`、`Audio Duration (mtb)`、`WanVideoSampler`、`MathExpression|pysssss`、`WanVideoTextEncodeCached`、`AudioCrop`、`CLIPVisionLoader`、`ImageResizeKJv2`、`WanVideoDecode`、`WanVideoEncode`、`WanVideoTorchCompileSettings`、`WanVideoBlockSwap`、`WanVideoLoraSelectMulti`、`MultiTalkModelLoader`、`WanVideoVAELoader`、`WanVideoModelLoader`、`WanVideoClipVisionEncode`、`VHS_LoadVideo`、`LoadAudio`、`VHS_VideoInfo`

**用到的条目**：WanVideoSampler、WanVideoClipVisionEncode、WanVideoDecode、WanVideoEncode、WanVideoTextEncodeCached、WanVideoVAELoader、WanVideoLoraSelectMulti、CLIPVisionLoader

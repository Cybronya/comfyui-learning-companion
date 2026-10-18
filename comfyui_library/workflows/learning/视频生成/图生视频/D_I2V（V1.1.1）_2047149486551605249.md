---
key: 视频生成/图生视频/D_I2V（V1.1.1）_2047149486551605249.json
name: D_I2V（V1.1.1）_2047149486551605249.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/D_I2V（V1.1.1）_2047149486551605249.json
hash: 021b3be5693628de
coverage: 0.736842
learned_at: 2026-10-15 22:37:03
nodes: [DownloadAndLoadWav2VecModel, WanVideoBlockSwap, Note, MarkdownNote, WanVideoTorchCompileSettings, MarkdownNote, WanVideoVAELoader, MarkdownNote, WanVideoLoraSelect, MultiTalkModelLoader, MelBandRoFormerModelLoader, SetNode, PreviewAny, GetNode, INTConstant, SetNode, ResizeImagesByLongerEdge, CLIPVisionLoader, Wav2VecModelLoader, LoadAudio, GetImageSize, ImageResizeKJv2, FB_Qwen3TTSVoiceClone, PreviewAudio, MelBandRoFormerSampler, MultiTalkWav2VecEmbeds, SetNode, GetImageSizeAndCount, VHS_VideoCombine, WanVideoImageToVideoMultiTalk, WanVideoPassImagesFromSamples, WanVideoClipVisionEncode, Note, WanVideoSampler, WanVideoModelLoader, Text, LoadImage, WanVideoTextEncodeCached]
patterns: []
missing: []
---

# 视频生成/图生视频/D_I2V（V1.1.1）_2047149486551605249.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2047149486551605249.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（38 个）：
- `DownloadAndLoadWav2VecModel`
- `WanVideoBlockSwap`
- `Note`
- `MarkdownNote`
- `WanVideoTorchCompileSettings`
- `MarkdownNote`
- `WanVideoVAELoader`
- `MarkdownNote`
- `WanVideoLoraSelect`
- `MultiTalkModelLoader`
- `MelBandRoFormerModelLoader`
- `SetNode`
- `PreviewAny`
- `GetNode`
- `INTConstant`
- `SetNode`
- `ResizeImagesByLongerEdge`
- `CLIPVisionLoader`
- `Wav2VecModelLoader`
- `LoadAudio`
- `GetImageSize`
- `ImageResizeKJv2`
- `FB_Qwen3TTSVoiceClone`
- `PreviewAudio`
- `MelBandRoFormerSampler` ★核心
- `MultiTalkWav2VecEmbeds`
- `SetNode`
- `GetImageSizeAndCount`
- `VHS_VideoCombine`
- `WanVideoImageToVideoMultiTalk`
- `WanVideoPassImagesFromSamples`
- `WanVideoClipVisionEncode`
- `Note`
- `WanVideoSampler` ★核心
- `WanVideoModelLoader`
- `Text`
- `LoadImage`
- `WanVideoTextEncodeCached`

## 知识

覆盖率 **74%**（28/38）

**有卡**：`DownloadAndLoadWav2VecModel`、`WanVideoBlockSwap`、`WanVideoTorchCompileSettings`、`WanVideoVAELoader`、`WanVideoLoraSelect`、`MultiTalkModelLoader`、`MelBandRoFormerModelLoader`、`INTConstant`、`ResizeImagesByLongerEdge`、`CLIPVisionLoader`、`Wav2VecModelLoader`、`LoadAudio`、`GetImageSize`、`ImageResizeKJv2`、`FB_Qwen3TTSVoiceClone`、`PreviewAudio`、`MelBandRoFormerSampler`、`MultiTalkWav2VecEmbeds`、`GetImageSizeAndCount`、`VHS_VideoCombine`、`WanVideoImageToVideoMultiTalk`、`WanVideoPassImagesFromSamples`、`WanVideoClipVisionEncode`、`WanVideoSampler`、`WanVideoModelLoader`、`Text`、`LoadImage`、`WanVideoTextEncodeCached`

**用到的条目**：LoadImage、WanVideoSampler、MelBandRoFormerSampler、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoTextEncodeCached、WanVideoLoraSelect、CLIPVisionLoader

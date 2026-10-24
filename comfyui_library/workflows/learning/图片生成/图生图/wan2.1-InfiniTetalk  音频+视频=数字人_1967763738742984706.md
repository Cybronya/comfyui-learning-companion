---
key: 图片生成/图生图/wan2.1-InfiniTetalk  音频+视频=数字人_1967763738742984706.json
name: wan2.1-InfiniTetalk  音频+视频=数字人_1967763738742984706
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/wan2.1-InfiniTetalk  音频+视频=数字人_1967763738742984706.json
hash: 3172b4074f1b97e0
coverage: 0.916667
learned_at: 2026-10-23 11:45:49
nodes: [WanVideoBlockSwap, WanVideoTorchCompileSettings, WanVideoModelLoader, MultiTalkModelLoader, WanVideoLoraSelect, MultiTalkWav2VecEmbeds, DownloadAndLoadWav2VecModel, AudioSeparation, WanVideoTextEncodeCached, WanVideoSampler, SetNode, PreviewAny, PreviewImage, VHS_VideoCombine, Wav2VecModelLoader, MelBandRoFormerSampler, MelBandRoFormerModelLoader, PreviewAudio, WanVideoVAELoader, WanVideoDecode, GetImageSizeAndCount, GetImageRangeFromBatch, ImageConcatMulti, AudioCrop, INTConstant, GetImageRangeFromBatch, LayerUtility: ImageScaleByAspectRatio V2, WanVideoEncode, GetImageSizeAndCount, WanVideoImageToVideoMultiTalk, CLIPVisionLoader, WanVideoClipVisionEncode, VHS_LoadVideo, Int, LoadAudio, Fast Bypasser (rgthree)]
patterns: []
missing: []
---

# 图片生成/图生图/wan2.1-InfiniTetalk  音频+视频=数字人_1967763738742984706.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/wan2.1-InfiniTetalk  音频+视频=数字人_1967763738742984706.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（36 个）：
- `WanVideoBlockSwap`
- `WanVideoTorchCompileSettings`
- `WanVideoModelLoader`
- `MultiTalkModelLoader`
- `WanVideoLoraSelect`
- `MultiTalkWav2VecEmbeds`
- `DownloadAndLoadWav2VecModel`
- `AudioSeparation`
- `WanVideoTextEncodeCached`
- `WanVideoSampler` ★核心
- `SetNode`
- `PreviewAny`
- `PreviewImage`
- `VHS_VideoCombine`
- `Wav2VecModelLoader`
- `MelBandRoFormerSampler` ★核心
- `MelBandRoFormerModelLoader`
- `PreviewAudio`
- `WanVideoVAELoader`
- `WanVideoDecode`
- `GetImageSizeAndCount`
- `GetImageRangeFromBatch`
- `ImageConcatMulti`
- `AudioCrop`
- `INTConstant`
- `GetImageRangeFromBatch`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `WanVideoEncode`
- `GetImageSizeAndCount`
- `WanVideoImageToVideoMultiTalk`
- `CLIPVisionLoader`
- `WanVideoClipVisionEncode`
- `VHS_LoadVideo`
- `Int`
- `LoadAudio`
- `Fast Bypasser (rgthree)`

## 知识

覆盖率 **92%**（33/36）

**有卡**：`WanVideoBlockSwap`、`WanVideoTorchCompileSettings`、`WanVideoModelLoader`、`MultiTalkModelLoader`、`WanVideoLoraSelect`、`MultiTalkWav2VecEmbeds`、`DownloadAndLoadWav2VecModel`、`AudioSeparation`、`WanVideoTextEncodeCached`、`WanVideoSampler`、`VHS_VideoCombine`、`Wav2VecModelLoader`、`MelBandRoFormerSampler`、`MelBandRoFormerModelLoader`、`PreviewAudio`、`WanVideoVAELoader`、`WanVideoDecode`、`GetImageSizeAndCount`、`GetImageRangeFromBatch`、`ImageConcatMulti`、`AudioCrop`、`INTConstant`、`LayerUtility: ImageScaleByAspectRatio V2`、`WanVideoEncode`、`WanVideoImageToVideoMultiTalk`、`CLIPVisionLoader`、`WanVideoClipVisionEncode`、`VHS_LoadVideo`、`Int`、`LoadAudio`、`Fast Bypasser (rgthree)`

**用到的条目**：WanVideoSampler、MelBandRoFormerSampler、WanVideoDecode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoTextEncodeCached、WanVideoEncode、WanVideoLoraSelect

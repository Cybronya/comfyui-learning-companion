---
key: 视频生成/图生视频/wan2.1-InfiniTetalk-音频+图像=数字人_1967501356460335105.json
name: wan2.1-InfiniTetalk-音频+图像=数字人_1967501356460335105.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1967501356460335105.json
hash: 94875272e822cc59
coverage: 0.935484
learned_at: 2026-10-15 22:31:41
nodes: [PreviewAny, MultiTalkWav2VecEmbeds, WanVideoSampler, WanVideoDecode, VHS_VideoCombine, WanVideoImageToVideoMultiTalk, WanVideoModelLoader, WanVideoBlockSwap, WanVideoTorchCompileSettings, WanVideoVAELoader, DownloadAndLoadWav2VecModel, SetNode, CLIPVisionLoader, LoadImage, WanVideoTextEncodeCached, GetImageSizeAndCount, Switch any [Crystools], WanVideoLoraSelect, WanVideoClipVisionEncode, MultiTalkModelLoader, MelBandRoFormerModelLoader, MelBandRoFormerSampler, Fast Bypasser (rgthree), AudioCrop, LoadAudio, Wav2VecModelLoader, PreviewAudio, AudioSeparation, INTConstant, LayerUtility: ImageScaleByAspectRatio V2, ImageResizeKJv2]
patterns: []
missing: []
---

# 视频生成/图生视频/wan2.1-InfiniTetalk-音频+图像=数字人_1967501356460335105.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1967501356460335105.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（31 个）：
- `PreviewAny`
- `MultiTalkWav2VecEmbeds`
- `WanVideoSampler` ★核心
- `WanVideoDecode`
- `VHS_VideoCombine`
- `WanVideoImageToVideoMultiTalk`
- `WanVideoModelLoader`
- `WanVideoBlockSwap`
- `WanVideoTorchCompileSettings`
- `WanVideoVAELoader`
- `DownloadAndLoadWav2VecModel`
- `SetNode`
- `CLIPVisionLoader`
- `LoadImage`
- `WanVideoTextEncodeCached`
- `GetImageSizeAndCount`
- `Switch any [Crystools]`
- `WanVideoLoraSelect`
- `WanVideoClipVisionEncode`
- `MultiTalkModelLoader`
- `MelBandRoFormerModelLoader`
- `MelBandRoFormerSampler` ★核心
- `Fast Bypasser (rgthree)`
- `AudioCrop`
- `LoadAudio`
- `Wav2VecModelLoader`
- `PreviewAudio`
- `AudioSeparation`
- `INTConstant`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `ImageResizeKJv2`

## 知识

覆盖率 **94%**（29/31）

**有卡**：`MultiTalkWav2VecEmbeds`、`WanVideoSampler`、`WanVideoDecode`、`VHS_VideoCombine`、`WanVideoImageToVideoMultiTalk`、`WanVideoModelLoader`、`WanVideoBlockSwap`、`WanVideoTorchCompileSettings`、`WanVideoVAELoader`、`DownloadAndLoadWav2VecModel`、`CLIPVisionLoader`、`LoadImage`、`WanVideoTextEncodeCached`、`GetImageSizeAndCount`、`Switch any [Crystools]`、`WanVideoLoraSelect`、`WanVideoClipVisionEncode`、`MultiTalkModelLoader`、`MelBandRoFormerModelLoader`、`MelBandRoFormerSampler`、`Fast Bypasser (rgthree)`、`AudioCrop`、`LoadAudio`、`Wav2VecModelLoader`、`PreviewAudio`、`AudioSeparation`、`INTConstant`、`LayerUtility: ImageScaleByAspectRatio V2`、`ImageResizeKJv2`

**用到的条目**：LoadImage、LayerUtility: ImageScaleByAspectRatio V2、WanVideoSampler、MelBandRoFormerSampler、WanVideoDecode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoTextEncodeCached

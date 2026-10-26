---
key: 数字人/数字人/超级数字人Infinite Talk+SteadyDancer_2017063651705884674.json
name: 超级数字人Infinite Talk+SteadyDancer_2017063651705884674
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/数字人/数字人/超级数字人Infinite Talk+SteadyDancer_2017063651705884674.json
hash: 89c8e3a380770e17
coverage: 0.932203
learned_at: 2026-10-26 02:05:39
nodes: [ImageConcatMulti, WanVideoDecode, WanVideoSetBlockSwap, Reroute, LoadImage, WanVideoBlockSwap, WanVideoLoraSelect, VHS_VideoCombine, VHS_VideoCombine, VHS_VideoCombine, LoadImage, WanVideoModelLoader, MultiTalkModelLoader, WanVideoTorchCompileSettings, WanVideoSetLoRAs, WanVideoContextOptions, WanVideoEncode, VHS_LoadVideo, WanVideoClipVisionEncode, WanVideoSampler, WanVideoVAELoader, WanVideoClipVisionEncode, CLIPVisionLoader, WanVideoTextEncodeCached, ImageResizeKJv2, ImageResizeKJv2, LayerUtility: ImageScaleByAspectRatio V2, GetImageSizeAndCount, GetImageRangeFromBatch, PreviewImage, PreviewImage, VHS_VideoCombine, ImageConcatMulti, LoadImage, LoadImage, PrimitiveFloat, easy convertAnything, ImageFromBatch, VHS_VideoCombine, VHS_VideoCombine, VHS_VideoCombine, VHS_VideoCombine, VHS_VideoCombine, VHS_VideoCombine, VHS_VideoCombine, OnnxDetectionModelLoader, PoseDetectionOneToAllAnimation, WanVideoAddSteadyDancerEmbeds, MelBandRoFormerModelLoader, MultiTalkWav2VecEmbeds, MelBandRoFormerSampler, Wav2VecModelLoader, VHS_LoadVideo, WanVideoImageToVideoEncode, VHS_LoadVideo, easy imageBatchToImageList, ImageListToBatch+, VHS_VideoCombine, VHS_VideoInfo]
patterns: []
missing: []
---

# 数字人/数字人/超级数字人Infinite Talk+SteadyDancer_2017063651705884674.json

> 来源文件 `comfyui_library/workflows/数字人/数字人/超级数字人Infinite Talk+SteadyDancer_2017063651705884674.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（59 个）：
- `ImageConcatMulti`
- `WanVideoDecode`
- `WanVideoSetBlockSwap`
- `Reroute`
- `LoadImage`
- `WanVideoBlockSwap`
- `WanVideoLoraSelect`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `LoadImage`
- `WanVideoModelLoader`
- `MultiTalkModelLoader`
- `WanVideoTorchCompileSettings`
- `WanVideoSetLoRAs`
- `WanVideoContextOptions`
- `WanVideoEncode`
- `VHS_LoadVideo`
- `WanVideoClipVisionEncode`
- `WanVideoSampler` ★核心
- `WanVideoVAELoader`
- `WanVideoClipVisionEncode`
- `CLIPVisionLoader`
- `WanVideoTextEncodeCached`
- `ImageResizeKJv2`
- `ImageResizeKJv2`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `GetImageSizeAndCount`
- `GetImageRangeFromBatch`
- `PreviewImage`
- `PreviewImage`
- `VHS_VideoCombine`
- `ImageConcatMulti`
- `LoadImage`
- `LoadImage`
- `PrimitiveFloat`
- `easy convertAnything`
- `ImageFromBatch`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `OnnxDetectionModelLoader`
- `PoseDetectionOneToAllAnimation`
- `WanVideoAddSteadyDancerEmbeds`
- `MelBandRoFormerModelLoader`
- `MultiTalkWav2VecEmbeds`
- `MelBandRoFormerSampler` ★核心
- `Wav2VecModelLoader`
- `VHS_LoadVideo`
- `WanVideoImageToVideoEncode`
- `VHS_LoadVideo`
- `easy imageBatchToImageList`
- `ImageListToBatch+`
- `VHS_VideoCombine`
- `VHS_VideoInfo`

## 知识

覆盖率 **93%**（55/59）

**有卡**：`ImageConcatMulti`、`WanVideoDecode`、`WanVideoSetBlockSwap`、`LoadImage`、`WanVideoBlockSwap`、`WanVideoLoraSelect`、`VHS_VideoCombine`、`WanVideoModelLoader`、`MultiTalkModelLoader`、`WanVideoTorchCompileSettings`、`WanVideoSetLoRAs`、`WanVideoContextOptions`、`WanVideoEncode`、`VHS_LoadVideo`、`WanVideoClipVisionEncode`、`WanVideoSampler`、`WanVideoVAELoader`、`CLIPVisionLoader`、`WanVideoTextEncodeCached`、`ImageResizeKJv2`、`LayerUtility: ImageScaleByAspectRatio V2`、`GetImageSizeAndCount`、`GetImageRangeFromBatch`、`easy convertAnything`、`ImageFromBatch`、`OnnxDetectionModelLoader`、`PoseDetectionOneToAllAnimation`、`WanVideoAddSteadyDancerEmbeds`、`MelBandRoFormerModelLoader`、`MultiTalkWav2VecEmbeds`、`MelBandRoFormerSampler`、`Wav2VecModelLoader`、`WanVideoImageToVideoEncode`、`easy imageBatchToImageList`、`ImageListToBatch+`、`VHS_VideoInfo`

**用到的条目**：LoadImage、LayerUtility: ImageScaleByAspectRatio V2、WanVideoSampler、MelBandRoFormerSampler、WanVideoDecode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoImageToVideoEncode

---
key: 平台全量/视频-视频对音频口型-wan2.1-InfiniteTalk-KJ_1973968886301331458.json
name: 视频-视频对音频口型-wan2.1-InfiniteTalk-KJ_1973968886301331458
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/视频-视频对音频口型-wan2.1-InfiniteTalk-KJ_1973968886301331458.json
hash: b6321b917f8c0735
coverage: 0.825397
learned_at: 2026-11-14 02:34:32
nodes: [CLIPVisionLoader, MultiTalkModelLoader, WanVideoLoraSelect, WanVideoVAELoader, WanVideoClipVisionEncode, CM_FloatBinaryOperation, Reroute, VHS_VideoInfo, Int, Int, LayerUtility: ImageScaleByAspectRatio V2, CM_FloatToInt, easy showAnything, SetNode, GetImageSizeAndCount, CM_IntUnaryOperation, easy showAnything, GetImageSizeAndCount, CR Prompt Text, WanVideoBlockSwap, GetImageRangeFromBatch, ImageBatchMulti, WanVideoImageToVideoMultiTalk, WanVideoTextEncodeCached, WanVideoModelLoader, easy showAnything, ImageBatchRepeatInterleaving, GetImageRangeFromBatch, Reroute, WanVideoVACEStartToEndFrame, Reroute, WanVideoEncode, DownloadAndLoadWav2VecModel, AudioSeparation, GetNode, MultiTalkWav2VecEmbeds, Reroute, VHS_LoadVideo, SoundFlow_GetLength, LoadAudio, WanVideoEncode, MaskPreview+, VHS_VideoCombine, WanVideoSampler, WanVideoSampler, MultiTalkWav2VecEmbeds, GetImageRangeFromBatch, WanVideoDecode, PreviewImage, GetImageRangeFromBatch, GetImageSizeAndCount, WanVideoDecode, VHS_VideoCombine, VHS_VideoCombine, ImageConcanate, GetImageSizeAndCount, easy anythingIndexSwitch, easy showAnything, CM_BoolToInt, CM_IntBinaryCondition JK, GetImageSizeAndCount, CM_IntBinaryOperation, AudioCrop]
patterns: []
missing: []
---

# 平台全量/视频-视频对音频口型-wan2.1-InfiniteTalk-KJ_1973968886301331458.json

> 来源文件 `comfyui_library/workflows/平台全量/视频-视频对音频口型-wan2.1-InfiniteTalk-KJ_1973968886301331458.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（63 个）：
- `CLIPVisionLoader`
- `MultiTalkModelLoader`
- `WanVideoLoraSelect`
- `WanVideoVAELoader`
- `WanVideoClipVisionEncode`
- `CM_FloatBinaryOperation`
- `Reroute`
- `VHS_VideoInfo`
- `Int`
- `Int`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `CM_FloatToInt`
- `easy showAnything`
- `SetNode`
- `GetImageSizeAndCount`
- `CM_IntUnaryOperation`
- `easy showAnything`
- `GetImageSizeAndCount`
- `CR Prompt Text`
- `WanVideoBlockSwap`
- `GetImageRangeFromBatch`
- `ImageBatchMulti`
- `WanVideoImageToVideoMultiTalk`
- `WanVideoTextEncodeCached`
- `WanVideoModelLoader`
- `easy showAnything`
- `ImageBatchRepeatInterleaving`
- `GetImageRangeFromBatch`
- `Reroute`
- `WanVideoVACEStartToEndFrame`
- `Reroute`
- `WanVideoEncode`
- `DownloadAndLoadWav2VecModel`
- `AudioSeparation`
- `GetNode`
- `MultiTalkWav2VecEmbeds`
- `Reroute`
- `VHS_LoadVideo`
- `SoundFlow_GetLength`
- `LoadAudio`
- `WanVideoEncode`
- `MaskPreview+`
- `VHS_VideoCombine`
- `WanVideoSampler` ★核心
- `WanVideoSampler` ★核心
- `MultiTalkWav2VecEmbeds`
- `GetImageRangeFromBatch`
- `WanVideoDecode`
- `PreviewImage`
- `GetImageRangeFromBatch`
- `GetImageSizeAndCount`
- `WanVideoDecode`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `ImageConcanate`
- `GetImageSizeAndCount`
- `easy anythingIndexSwitch`
- `easy showAnything`
- `CM_BoolToInt`
- `CM_IntBinaryCondition JK`
- `GetImageSizeAndCount`
- `CM_IntBinaryOperation`
- `AudioCrop`

## 知识

覆盖率 **83%**（52/63）

**有卡**：`CLIPVisionLoader`、`MultiTalkModelLoader`、`WanVideoLoraSelect`、`WanVideoVAELoader`、`WanVideoClipVisionEncode`、`CM_FloatBinaryOperation`、`VHS_VideoInfo`、`Int`、`LayerUtility: ImageScaleByAspectRatio V2`、`CM_FloatToInt`、`GetImageSizeAndCount`、`CM_IntUnaryOperation`、`CR Prompt Text`、`WanVideoBlockSwap`、`GetImageRangeFromBatch`、`ImageBatchMulti`、`WanVideoImageToVideoMultiTalk`、`WanVideoTextEncodeCached`、`WanVideoModelLoader`、`ImageBatchRepeatInterleaving`、`WanVideoVACEStartToEndFrame`、`WanVideoEncode`、`DownloadAndLoadWav2VecModel`、`AudioSeparation`、`MultiTalkWav2VecEmbeds`、`VHS_LoadVideo`、`SoundFlow_GetLength`、`LoadAudio`、`MaskPreview+`、`VHS_VideoCombine`、`WanVideoSampler`、`WanVideoDecode`、`ImageConcanate`、`easy anythingIndexSwitch`、`CM_BoolToInt`、`CM_IntBinaryCondition JK`、`CM_IntBinaryOperation`、`AudioCrop`

**用到的条目**：WanVideoSampler、WanVideoClipVisionEncode、WanVideoDecode、WanVideoEncode、WanVideoTextEncodeCached、WanVideoVAELoader、WanVideoLoraSelect、CLIPVisionLoader

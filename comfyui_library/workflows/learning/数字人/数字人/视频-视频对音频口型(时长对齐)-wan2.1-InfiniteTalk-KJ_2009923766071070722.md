---
key: 数字人/数字人/视频-视频对音频口型(时长对齐)-wan2.1-InfiniteTalk-KJ_2009923766071070722.json
name: 视频-视频对音频口型(时长对齐)-wan2.1-InfiniteTalk-KJ_2009923766071070722
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/数字人/数字人/视频-视频对音频口型(时长对齐)-wan2.1-InfiniteTalk-KJ_2009923766071070722.json
hash: da68a292f236c9b4
coverage: 0.822581
learned_at: 2026-10-26 02:04:45
nodes: [CLIPVisionLoader, MultiTalkModelLoader, WanVideoLoraSelect, WanVideoVAELoader, WanVideoClipVisionEncode, CM_FloatBinaryOperation, Reroute, VHS_VideoInfo, Int, Int, LayerUtility: ImageScaleByAspectRatio V2, easy showAnything, SetNode, GetImageSizeAndCount, easy showAnything, GetImageSizeAndCount, CR Prompt Text, WanVideoBlockSwap, GetImageRangeFromBatch, ImageBatchMulti, WanVideoTextEncodeCached, WanVideoModelLoader, easy showAnything, Reroute, Reroute, GetNode, VHS_LoadVideo, SoundFlow_GetLength, LoadAudio, WanVideoEncode, WanVideoSampler, VHS_VideoCombine, VHS_VideoCombine, easy showAnything, CM_BoolToInt, CM_IntBinaryCondition JK, AudioCrop, easy anythingIndexSwitch, WanVideoDecode, Reroute, GetImageSizeAndCount, WanVideoImageToVideoMultiTalk, VHS_VideoCombine, GetImageSizeAndCount, MultiTalkWav2VecEmbeds, CM_FloatToInt, CM_IntBinaryOperation, ImageConcanate, MultiTalkWav2VecEmbeds, DownloadAndLoadWav2VecModel, AudioSeparation, WanVideoEncode, GetImageRangeFromBatch, PreviewImage, MaskPreview+, WanVideoSampler, GetImageRangeFromBatch, WanVideoDecode, GetImageRangeFromBatch, GetImageSizeAndCount, GetImageSizeAndCount, WanVideoVACEStartToEndFrame]
patterns: []
missing: []
---

# 数字人/数字人/视频-视频对音频口型(时长对齐)-wan2.1-InfiniteTalk-KJ_2009923766071070722.json

> 来源文件 `comfyui_library/workflows/数字人/数字人/视频-视频对音频口型(时长对齐)-wan2.1-InfiniteTalk-KJ_2009923766071070722.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（62 个）：
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
- `easy showAnything`
- `SetNode`
- `GetImageSizeAndCount`
- `easy showAnything`
- `GetImageSizeAndCount`
- `CR Prompt Text`
- `WanVideoBlockSwap`
- `GetImageRangeFromBatch`
- `ImageBatchMulti`
- `WanVideoTextEncodeCached`
- `WanVideoModelLoader`
- `easy showAnything`
- `Reroute`
- `Reroute`
- `GetNode`
- `VHS_LoadVideo`
- `SoundFlow_GetLength`
- `LoadAudio`
- `WanVideoEncode`
- `WanVideoSampler` ★核心
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `easy showAnything`
- `CM_BoolToInt`
- `CM_IntBinaryCondition JK`
- `AudioCrop`
- `easy anythingIndexSwitch`
- `WanVideoDecode`
- `Reroute`
- `GetImageSizeAndCount`
- `WanVideoImageToVideoMultiTalk`
- `VHS_VideoCombine`
- `GetImageSizeAndCount`
- `MultiTalkWav2VecEmbeds`
- `CM_FloatToInt`
- `CM_IntBinaryOperation`
- `ImageConcanate`
- `MultiTalkWav2VecEmbeds`
- `DownloadAndLoadWav2VecModel`
- `AudioSeparation`
- `WanVideoEncode`
- `GetImageRangeFromBatch`
- `PreviewImage`
- `MaskPreview+`
- `WanVideoSampler` ★核心
- `GetImageRangeFromBatch`
- `WanVideoDecode`
- `GetImageRangeFromBatch`
- `GetImageSizeAndCount`
- `GetImageSizeAndCount`
- `WanVideoVACEStartToEndFrame`

## 知识

覆盖率 **82%**（51/62）

**有卡**：`CLIPVisionLoader`、`MultiTalkModelLoader`、`WanVideoLoraSelect`、`WanVideoVAELoader`、`WanVideoClipVisionEncode`、`CM_FloatBinaryOperation`、`VHS_VideoInfo`、`Int`、`LayerUtility: ImageScaleByAspectRatio V2`、`GetImageSizeAndCount`、`CR Prompt Text`、`WanVideoBlockSwap`、`GetImageRangeFromBatch`、`ImageBatchMulti`、`WanVideoTextEncodeCached`、`WanVideoModelLoader`、`VHS_LoadVideo`、`SoundFlow_GetLength`、`LoadAudio`、`WanVideoEncode`、`WanVideoSampler`、`VHS_VideoCombine`、`CM_BoolToInt`、`CM_IntBinaryCondition JK`、`AudioCrop`、`easy anythingIndexSwitch`、`WanVideoDecode`、`WanVideoImageToVideoMultiTalk`、`MultiTalkWav2VecEmbeds`、`CM_FloatToInt`、`CM_IntBinaryOperation`、`ImageConcanate`、`DownloadAndLoadWav2VecModel`、`AudioSeparation`、`MaskPreview+`、`WanVideoVACEStartToEndFrame`

**用到的条目**：WanVideoSampler、WanVideoDecode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoTextEncodeCached、WanVideoEncode、WanVideoLoraSelect、CLIPVisionLoader

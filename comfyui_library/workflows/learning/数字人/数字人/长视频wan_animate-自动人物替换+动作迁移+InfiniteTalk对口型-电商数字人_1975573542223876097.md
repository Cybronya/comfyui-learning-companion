---
key: 数字人/数字人/长视频wan_animate-自动人物替换+动作迁移+InfiniteTalk对口型-电商数字人_1975573542223876097.json
name: 长视频wan_animate-自动人物替换+动作迁移+InfiniteTalk对口型-电商数字人_1975573542223876097
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/数字人/数字人/长视频wan_animate-自动人物替换+动作迁移+InfiniteTalk对口型-电商数字人_1975573542223876097.json
hash: 3f8f9ff2bac8ddec
coverage: 0.53719
learned_at: 2026-10-26 02:05:52
nodes: [ImageConcatMulti, GetNode, GetNode, ImageConcatMulti, GetNode, SetNode, SetNode, SetNode, SetNode, SetNode, GetNode, ImageResizeKJv2, WanVideoDecode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, easy int, easy int, WanVideoLoraSelectMulti, GetNode, WanVideoVAELoader, SetNode, WanVideoModelLoader, WanVideoBlockSwap, WanVideoAnimateEmbeds, easy float, ImageResizeKJv2, GetImageRangeFromBatch, VHS_VideoInfoLoaded, SetNode, easy int, SetNode, easy int, VHS_VideoCombine, GetNode, GetNode, DrawViTPose, DrawMaskOnImage, SetNode, GetNode, GetNode, PoseAndFaceDetection, SetNode, LayerUtility: ImageBlend, Sam2Segmentation, OnnxDetectionModelLoader, VHS_VideoCombine, DownloadAndLoadSAM2Model, GetNode, GetNode, VHS_VideoCombine, WanVideoSampler, GetNode, WanVideoClipVisionEncode, CLIPVisionLoader, GetNode, WanVideoTextEncodeCached, SetNode, GetNode, SetNode, SetNode, BlockifyMask, GrowMask, easy int, SetNode, SetNode, SetNode, DownloadAndLoadWav2VecModel, WanVideoTorchCompileSettings, WanVideoVAELoader, CLIPVisionLoader, AudioSeparation, WanVideoLoraSelect, PreviewAudio, WanVideoBlockSwap, MultiTalkModelLoader, WanVideoModelLoader, WanVideoSampler, GetImageRangeFromBatch, GetImageSizeAndCount, WanVideoEncode, WanVideoClipVisionEncode, WanVideoImageToVideoMultiTalk, WanVideoDecode, GetNode, ConvertAny2Int, SoundFlow_TrimAudio, SetNode, MathExpression|pysssss, MathExpression|pysssss, GetNode, GetNode, SetNode, GetImageSizeAndCount, SetNode, VHS_VideoCombine, GetNode, VHS_LoadVideo, LoadImage, WanVideoTextEncodeCached, MultiTalkWav2VecEmbeds, GetNode, GetNode, GetNode, GetNode, AudioCrop, Note, GetNode, SetNode, GetNode, GetNode, GetNode, VHS_VideoCombine, CR Text, GetImageRangeFromBatch, SetNode, GetNode]
patterns: []
missing: []
---

# 数字人/数字人/长视频wan_animate-自动人物替换+动作迁移+InfiniteTalk对口型-电商数字人_1975573542223876097.json

> 来源文件 `comfyui_library/workflows/数字人/数字人/长视频wan_animate-自动人物替换+动作迁移+InfiniteTalk对口型-电商数字人_1975573542223876097.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（121 个）：
- `ImageConcatMulti`
- `GetNode`
- `GetNode`
- `ImageConcatMulti`
- `GetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `ImageResizeKJv2`
- `WanVideoDecode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `easy int`
- `easy int`
- `WanVideoLoraSelectMulti`
- `GetNode`
- `WanVideoVAELoader`
- `SetNode`
- `WanVideoModelLoader`
- `WanVideoBlockSwap`
- `WanVideoAnimateEmbeds`
- `easy float`
- `ImageResizeKJv2`
- `GetImageRangeFromBatch`
- `VHS_VideoInfoLoaded`
- `SetNode`
- `easy int`
- `SetNode`
- `easy int`
- `VHS_VideoCombine`
- `GetNode`
- `GetNode`
- `DrawViTPose`
- `DrawMaskOnImage`
- `SetNode`
- `GetNode`
- `GetNode`
- `PoseAndFaceDetection`
- `SetNode`
- `LayerUtility: ImageBlend`
- `Sam2Segmentation`
- `OnnxDetectionModelLoader`
- `VHS_VideoCombine`
- `DownloadAndLoadSAM2Model`
- `GetNode`
- `GetNode`
- `VHS_VideoCombine`
- `WanVideoSampler` ★核心
- `GetNode`
- `WanVideoClipVisionEncode`
- `CLIPVisionLoader`
- `GetNode`
- `WanVideoTextEncodeCached`
- `SetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `BlockifyMask`
- `GrowMask`
- `easy int`
- `SetNode`
- `SetNode`
- `SetNode`
- `DownloadAndLoadWav2VecModel`
- `WanVideoTorchCompileSettings`
- `WanVideoVAELoader`
- `CLIPVisionLoader`
- `AudioSeparation`
- `WanVideoLoraSelect`
- `PreviewAudio`
- `WanVideoBlockSwap`
- `MultiTalkModelLoader`
- `WanVideoModelLoader`
- `WanVideoSampler` ★核心
- `GetImageRangeFromBatch`
- `GetImageSizeAndCount`
- `WanVideoEncode`
- `WanVideoClipVisionEncode`
- `WanVideoImageToVideoMultiTalk`
- `WanVideoDecode`
- `GetNode`
- `ConvertAny2Int`
- `SoundFlow_TrimAudio`
- `SetNode`
- `MathExpression|pysssss`
- `MathExpression|pysssss`
- `GetNode`
- `GetNode`
- `SetNode`
- `GetImageSizeAndCount`
- `SetNode`
- `VHS_VideoCombine`
- `GetNode`
- `VHS_LoadVideo`
- `LoadImage`
- `WanVideoTextEncodeCached`
- `MultiTalkWav2VecEmbeds`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `AudioCrop`
- `Note`
- `GetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `VHS_VideoCombine`
- `CR Text`
- `GetImageRangeFromBatch`
- `SetNode`
- `GetNode`

## 知识

覆盖率 **54%**（65/121）

**有卡**：`ImageConcatMulti`、`ImageResizeKJv2`、`WanVideoDecode`、`easy int`、`WanVideoLoraSelectMulti`、`WanVideoVAELoader`、`WanVideoModelLoader`、`WanVideoBlockSwap`、`WanVideoAnimateEmbeds`、`easy float`、`GetImageRangeFromBatch`、`VHS_VideoInfoLoaded`、`VHS_VideoCombine`、`DrawViTPose`、`DrawMaskOnImage`、`PoseAndFaceDetection`、`LayerUtility: ImageBlend`、`Sam2Segmentation`、`OnnxDetectionModelLoader`、`DownloadAndLoadSAM2Model`、`WanVideoSampler`、`WanVideoClipVisionEncode`、`CLIPVisionLoader`、`WanVideoTextEncodeCached`、`BlockifyMask`、`GrowMask`、`DownloadAndLoadWav2VecModel`、`WanVideoTorchCompileSettings`、`AudioSeparation`、`WanVideoLoraSelect`、`PreviewAudio`、`MultiTalkModelLoader`、`GetImageSizeAndCount`、`WanVideoEncode`、`WanVideoImageToVideoMultiTalk`、`ConvertAny2Int`、`SoundFlow_TrimAudio`、`MathExpression|pysssss`、`VHS_LoadVideo`、`LoadImage`、`MultiTalkWav2VecEmbeds`、`AudioCrop`、`CR Text`

**用到的条目**：LoadImage、WanVideoSampler、WanVideoDecode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoTextEncodeCached、WanVideoEncode、WanVideoLoraSelect

---
key: 视频生成/文生视频/10s+图生视频+时间加长版 人物舞蹈+美女跳舞 动作迁移+++SteadDancer+2.0（支持_2045730540698996738.json
name: 10s+图生视频+时间加长版 人物舞蹈+美女跳舞 动作迁移+++SteadDancer+2.0（支持_2045730540698996738
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/10s+图生视频+时间加长版 人物舞蹈+美女跳舞 动作迁移+++SteadDancer+2.0（支持_2045730540698996738.json
hash: c9f5af1df6f94ea1
coverage: 0.632353
learned_at: 2026-10-15 22:43:18
nodes: [ImageConcatMulti, WanVideoSetBlockSwap, SetNode, WanVideoEncode, GetNode, SetNode, SetNode, DrawViTPose, ImageResizeKJv2, WanVideoAddSteadyDancerEmbeds, ImageConcatMulti, WanVideoSamplerSettings, OnnxDetectionModelLoader, CLIPVisionLoader, WanVideoDecode, WanVideoVAELoader, GetNode, WanVideoModelLoader, GetNode, GetNode, GetImageSizeAndCount, GetNode, GetNode, WanVideoTorchCompileSettings, WanVideoBlockSwap, SetNode, WanVideoSetLoRAs, SetNode, WanVideoSamplerFromSettings, PoseAndFaceDetection, WanVideoScheduler, GetNode, GetNode, WanVideoClipVisionEncode, WanVideoLoraSelect, WanVideoTextEncodeCached, WanVideoContextOptions, PrimitiveNode, PrimitiveNode, SetNode, WanVideoImageToVideoEncode, PreviewImage, RH_Sora2_I2V, VHS_VideoCombine, GetNode, GetNode, GetNode, GetNode, ImageResizeKJv2, GetImageRangeFromBatch, GetNode, Note, WanVideoClipVisionEncode, LayerUtility: ImageScaleByAspectRatio V2, Int, MathExpression|pysssss, Int, Int, DF_Int_to_Float, easy setNode, SetNode, VHS_VideoCombine, easy getNode, GetNode, VHS_VideoCombine, Text, VHS_LoadVideo, LoadImage]
patterns: []
missing: []
---

# 视频生成/文生视频/10s+图生视频+时间加长版 人物舞蹈+美女跳舞 动作迁移+++SteadDancer+2.0（支持_2045730540698996738.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/10s+图生视频+时间加长版 人物舞蹈+美女跳舞 动作迁移+++SteadDancer+2.0（支持_2045730540698996738.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（68 个）：
- `ImageConcatMulti`
- `WanVideoSetBlockSwap`
- `SetNode`
- `WanVideoEncode`
- `GetNode`
- `SetNode`
- `SetNode`
- `DrawViTPose`
- `ImageResizeKJv2`
- `WanVideoAddSteadyDancerEmbeds`
- `ImageConcatMulti`
- `WanVideoSamplerSettings` ★核心
- `OnnxDetectionModelLoader`
- `CLIPVisionLoader`
- `WanVideoDecode`
- `WanVideoVAELoader`
- `GetNode`
- `WanVideoModelLoader`
- `GetNode`
- `GetNode`
- `GetImageSizeAndCount`
- `GetNode`
- `GetNode`
- `WanVideoTorchCompileSettings`
- `WanVideoBlockSwap`
- `SetNode`
- `WanVideoSetLoRAs`
- `SetNode`
- `WanVideoSamplerFromSettings` ★核心
- `PoseAndFaceDetection`
- `WanVideoScheduler`
- `GetNode`
- `GetNode`
- `WanVideoClipVisionEncode`
- `WanVideoLoraSelect`
- `WanVideoTextEncodeCached`
- `WanVideoContextOptions`
- `PrimitiveNode`
- `PrimitiveNode`
- `SetNode`
- `WanVideoImageToVideoEncode`
- `PreviewImage`
- `RH_Sora2_I2V`
- `VHS_VideoCombine`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `ImageResizeKJv2`
- `GetImageRangeFromBatch`
- `GetNode`
- `Note`
- `WanVideoClipVisionEncode`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `Int`
- `MathExpression|pysssss`
- `Int`
- `Int`
- `DF_Int_to_Float`
- `easy setNode`
- `SetNode`
- `VHS_VideoCombine`
- `easy getNode`
- `GetNode`
- `VHS_VideoCombine`
- `Text`
- `VHS_LoadVideo`
- `LoadImage`

## 知识

覆盖率 **63%**（43/68）

**有卡**：`ImageConcatMulti`、`WanVideoSetBlockSwap`、`WanVideoEncode`、`DrawViTPose`、`ImageResizeKJv2`、`WanVideoAddSteadyDancerEmbeds`、`WanVideoSamplerSettings`、`OnnxDetectionModelLoader`、`CLIPVisionLoader`、`WanVideoDecode`、`WanVideoVAELoader`、`WanVideoModelLoader`、`GetImageSizeAndCount`、`WanVideoTorchCompileSettings`、`WanVideoBlockSwap`、`WanVideoSetLoRAs`、`WanVideoSamplerFromSettings`、`PoseAndFaceDetection`、`WanVideoScheduler`、`WanVideoClipVisionEncode`、`WanVideoLoraSelect`、`WanVideoTextEncodeCached`、`WanVideoContextOptions`、`WanVideoImageToVideoEncode`、`RH_Sora2_I2V`、`VHS_VideoCombine`、`GetImageRangeFromBatch`、`LayerUtility: ImageScaleByAspectRatio V2`、`Int`、`MathExpression|pysssss`、`DF_Int_to_Float`、`easy setNode`、`easy getNode`、`Text`、`VHS_LoadVideo`、`LoadImage`

**用到的条目**：LoadImage、LayerUtility: ImageScaleByAspectRatio V2、WanVideoSamplerFromSettings、WanVideoSamplerSettings、WanVideoDecode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoImageToVideoEncode

---
key: 视频生成/图生视频/（10s+时间加长版）动作迁移 人物舞蹈 美女跳舞 SteadDancer 2.0（支持动漫人物）_2041680923317506050.json
name: （10s+时间加长版）动作迁移 人物舞蹈 美女跳舞 SteadDancer 2.0（支持动漫人物）_2041680923317506050.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2041680923317506050.json
hash: f33f286e2c81e65b
coverage: 0.632353
learned_at: 2026-10-15 22:36:21
nodes: [ImageConcatMulti, WanVideoSetBlockSwap, SetNode, WanVideoEncode, GetNode, SetNode, SetNode, DrawViTPose, ImageResizeKJv2, WanVideoAddSteadyDancerEmbeds, ImageConcatMulti, WanVideoSamplerSettings, OnnxDetectionModelLoader, CLIPVisionLoader, WanVideoDecode, WanVideoVAELoader, GetNode, WanVideoModelLoader, GetNode, GetNode, GetImageSizeAndCount, GetNode, GetNode, WanVideoTorchCompileSettings, WanVideoBlockSwap, SetNode, WanVideoSetLoRAs, SetNode, WanVideoSamplerFromSettings, PoseAndFaceDetection, WanVideoScheduler, GetNode, GetNode, WanVideoClipVisionEncode, WanVideoLoraSelect, WanVideoTextEncodeCached, WanVideoContextOptions, PrimitiveNode, PrimitiveNode, SetNode, WanVideoImageToVideoEncode, PreviewImage, RH_Sora2_I2V, VHS_VideoCombine, GetNode, GetNode, GetNode, GetNode, ImageResizeKJv2, GetImageRangeFromBatch, GetNode, VHS_LoadVideo, Note, WanVideoClipVisionEncode, LayerUtility: ImageScaleByAspectRatio V2, Int, MathExpression|pysssss, Int, Int, DF_Int_to_Float, easy setNode, SetNode, Text, VHS_VideoCombine, easy getNode, GetNode, VHS_VideoCombine, LoadImage]
patterns: []
missing: []
---

# 视频生成/图生视频/（10s+时间加长版）动作迁移 人物舞蹈 美女跳舞 SteadDancer 2.0（支持动漫人物）_2041680923317506050.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2041680923317506050.json`

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
- `VHS_LoadVideo`
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
- `Text`
- `VHS_VideoCombine`
- `easy getNode`
- `GetNode`
- `VHS_VideoCombine`
- `LoadImage`

## 知识

覆盖率 **63%**（43/68）

**有卡**：`ImageConcatMulti`、`WanVideoSetBlockSwap`、`WanVideoEncode`、`DrawViTPose`、`ImageResizeKJv2`、`WanVideoAddSteadyDancerEmbeds`、`WanVideoSamplerSettings`、`OnnxDetectionModelLoader`、`CLIPVisionLoader`、`WanVideoDecode`、`WanVideoVAELoader`、`WanVideoModelLoader`、`GetImageSizeAndCount`、`WanVideoTorchCompileSettings`、`WanVideoBlockSwap`、`WanVideoSetLoRAs`、`WanVideoSamplerFromSettings`、`PoseAndFaceDetection`、`WanVideoScheduler`、`WanVideoClipVisionEncode`、`WanVideoLoraSelect`、`WanVideoTextEncodeCached`、`WanVideoContextOptions`、`WanVideoImageToVideoEncode`、`RH_Sora2_I2V`、`VHS_VideoCombine`、`GetImageRangeFromBatch`、`VHS_LoadVideo`、`LayerUtility: ImageScaleByAspectRatio V2`、`Int`、`MathExpression|pysssss`、`DF_Int_to_Float`、`easy setNode`、`Text`、`easy getNode`、`LoadImage`

**用到的条目**：LoadImage、LayerUtility: ImageScaleByAspectRatio V2、WanVideoSamplerFromSettings、WanVideoSamplerSettings、WanVideoDecode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoImageToVideoEncode

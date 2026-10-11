---
key: 视频生成/文生视频/10s+图生视频+时间加长版 人物舞蹈+美女跳舞 动作迁移+++SteadDancer+2.0（支持_2045733887124447234.json
name: 10s+图生视频+时间加长版 人物舞蹈+美女跳舞 动作迁移+++SteadDancer+2.0（支持_2045733887124447234
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/10s+图生视频+时间加长版 人物舞蹈+美女跳舞 动作迁移+++SteadDancer+2.0（支持_2045733887124447234.json
hash: 29fa1d0a45e32660
coverage: 0.573529
learned_at: 2026-10-11 19:49:33
nodes: [ImageConcatMulti, WanVideoSetBlockSwap, SetNode, WanVideoEncode, GetNode, SetNode, SetNode, DrawViTPose, ImageResizeKJv2, WanVideoAddSteadyDancerEmbeds, ImageConcatMulti, WanVideoSamplerSettings, OnnxDetectionModelLoader, CLIPVisionLoader, WanVideoDecode, WanVideoVAELoader, GetNode, WanVideoModelLoader, GetNode, GetNode, GetImageSizeAndCount, GetNode, GetNode, WanVideoTorchCompileSettings, WanVideoBlockSwap, SetNode, WanVideoSetLoRAs, SetNode, WanVideoSamplerFromSettings, PoseAndFaceDetection, WanVideoScheduler, GetNode, GetNode, WanVideoClipVisionEncode, WanVideoLoraSelect, WanVideoTextEncodeCached, WanVideoContextOptions, PrimitiveNode, PrimitiveNode, SetNode, WanVideoImageToVideoEncode, PreviewImage, RH_Sora2_I2V, VHS_VideoCombine, GetNode, GetNode, GetNode, GetNode, ImageResizeKJv2, GetImageRangeFromBatch, GetNode, Note, WanVideoClipVisionEncode, LayerUtility: ImageScaleByAspectRatio V2, Int, MathExpression|pysssss, Int, Int, DF_Int_to_Float, easy setNode, SetNode, VHS_VideoCombine, easy getNode, GetNode, VHS_VideoCombine, Text, VHS_LoadVideo, LoadImage]
patterns: []
missing: [LayerUtility: ImageScaleByAspectRatio V2, MathExpression|pysssss, easy getNode, easy setNode]
discoveries: [次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识, 次要节点 `MathExpression|pysssss` 知识库中没有该节点类型的任何知识, 次要节点 `easy getNode` 知识库中没有该节点类型的任何知识, 次要节点 `easy setNode` 知识库中没有该节点类型的任何知识]
---

# 视频生成/文生视频/10s+图生视频+时间加长版 人物舞蹈+美女跳舞 动作迁移+++SteadDancer+2.0（支持_2045733887124447234.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/10s+图生视频+时间加长版 人物舞蹈+美女跳舞 动作迁移+++SteadDancer+2.0（支持_2045733887124447234.json`

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

覆盖率 **57%**（39/68）

**有卡**：`ImageConcatMulti`、`WanVideoSetBlockSwap`、`WanVideoEncode`、`DrawViTPose`、`ImageResizeKJv2`、`WanVideoAddSteadyDancerEmbeds`、`WanVideoSamplerSettings`、`OnnxDetectionModelLoader`、`CLIPVisionLoader`、`WanVideoDecode`、`WanVideoVAELoader`、`WanVideoModelLoader`、`GetImageSizeAndCount`、`WanVideoTorchCompileSettings`、`WanVideoBlockSwap`、`WanVideoSetLoRAs`、`WanVideoSamplerFromSettings`、`PoseAndFaceDetection`、`WanVideoScheduler`、`WanVideoClipVisionEncode`、`WanVideoLoraSelect`、`WanVideoTextEncodeCached`、`WanVideoContextOptions`、`WanVideoImageToVideoEncode`、`RH_Sora2_I2V`、`VHS_VideoCombine`、`GetImageRangeFromBatch`、`Int`、`DF_Int_to_Float`、`Text`、`VHS_LoadVideo`、`LoadImage`

**缺卡**（4）：`LayerUtility: ImageScaleByAspectRatio V2`、`MathExpression|pysssss`、`easy getNode`、`easy setNode`

**用到的条目**：LoadImage、WanVideoSamplerFromSettings、WanVideoSamplerSettings、WanVideoDecode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoImageToVideoEncode、WanVideoTextEncodeCached

## 学习发现

- 次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识
- 次要节点 `MathExpression|pysssss` 知识库中没有该节点类型的任何知识
- 次要节点 `easy getNode` 知识库中没有该节点类型的任何知识
- 次要节点 `easy setNode` 知识库中没有该节点类型的任何知识

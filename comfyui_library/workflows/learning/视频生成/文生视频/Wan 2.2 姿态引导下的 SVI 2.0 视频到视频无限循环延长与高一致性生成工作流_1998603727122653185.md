---
key: 视频生成/文生视频/Wan 2.2 姿态引导下的 SVI 2.0 视频到视频无限循环延长与高一致性生成工作流_1998603727122653185.json
name: Wan 2.2 姿态引导下的 SVI 2.0 视频到视频无限循环延长与高一致性生成工作流_1998603727122653185
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/Wan 2.2 姿态引导下的 SVI 2.0 视频到视频无限循环延长与高一致性生成工作流_1998603727122653185.json
hash: 67e73b92b092809a
coverage: 0.775862
learned_at: 2026-10-11 02:57:38
nodes: [DWPreprocessor, GetImageSizeAndCount, ImageResizeKJv2, GetNode, ImageResizeKJv2, GetNode, GetNode, JWInteger, GetImageRangeFromBatch, GetImageRangeFromBatch, DWPreprocessor, ImageBatch, GetNode, GetImageSizeAndCount, SimpleMath+, GetImageRangeFromBatch, GetImageRangeFromBatch, SetNode, INTConstant, VHS_BatchManager, easy seed, GetImageRangeFromBatch, MathExpression|pysssss, Note, WanVideoSetBlockSwap, Note, WanVideoDecode, WanVideoSetBlockSwap, WanVideoSampler, WanVideoSetLoRAs, WanVideoSetLoRAs, easy globalSeed, WanVideoScheduler, easy seed, Note, WanVideoSetBlockSwap, Note, WanVideoSetBlockSwap, easy globalSeed, WanVideoSampler, WanVideoSampler, WanVideoBlockSwap, LoadLynxResampler, LynxInsightFaceCrop, LynxEncodeFaceIP, LoadLynxResampler, LynxInsightFaceCrop, WanVideoBlockSwap, WanVideoLoraSelect, WanVideoVACEStartToEndFrame, VHS_VideoCombine, ImageResizeKJv2, VHS_LoadVideo, WanVideoVACEEncode, LynxEncodeFaceIP, LayerUtility: PurgeVRAM V2, WanVideoSampler, PrimitiveNode, WanVideoVACEModelSelect, WanVideoVACEModelSelect, WanVideoExtraModelSelect, WanVideoExtraModelSelect, WanVideoScheduler, WanVideoModelLoader, WanVideoModelLoader, WanVideoLoraSelect, RH_Captioner, WanVideoLoraSelect, WanVideoLoraSelect, PrimitiveNode, PrimitiveNode, WanVideoSigmaToStep, easy forLoopEnd, easy batchAnything, VHS_VideoCombine, WanVideoVACEModelSelect, WanVideoScheduler, easy seed, WanVideoScheduler, WanVideoDecode, ImageResizeKJv2, MathExpression|pysssss, VHS_LoadVideo, VHS_VideoCombine, VHS_VideoCombine, WanVideoVACEStartToEndFrame, WanVideoVACEModelSelect, WanVideoExtraModelSelect, WanVideoExtraModelSelect, WanVideoModelLoader, WanVideoLoraSelect, WanVideoSetLoRAs, WanVideoSetLoRAs, GetImageSizeAndCount, WanVideoVACEEncode, LoadWanVideoT5TextEncoder, LoadWanVideoT5TextEncoder, RH_Captioner, PrimitiveNode, WanVideoSigmaToStep, VHS_VideoCombine, WanVideoVAELoader, VHS_VideoCombine, WanVideoTextEncode, WanVideoAddLynxEmbeds, WanVideoAddLynxEmbeds, WanVideoModelLoader, WanVideoLoraSelect, WanVideoLoraSelect, String Literal, LoadImage, WanVideoTextEncode, RH_Captioner, easy forLoopStart, VHS_VideoCombine, Int]
patterns: []
missing: [LayerUtility: PurgeVRAM V2, MathExpression|pysssss, MathExpression|pysssss, SimpleMath+, String Literal, easy batchAnything, easy forLoopEnd, easy forLoopStart, easy globalSeed, easy globalSeed, easy seed, easy seed, easy seed]
discoveries: [次要节点 `LayerUtility: PurgeVRAM V2` 知识库中没有该节点类型的任何知识, 次要节点 `MathExpression|pysssss` 知识库中没有该节点类型的任何知识, 次要节点 `MathExpression|pysssss` 知识库中没有该节点类型的任何知识, 次要节点 `SimpleMath+` 知识库中没有该节点类型的任何知识, 次要节点 `String Literal` 知识库中没有该节点类型的任何知识, 次要节点 `easy batchAnything` 知识库中没有该节点类型的任何知识, 次要节点 `easy forLoopEnd` 知识库中没有该节点类型的任何知识, 次要节点 `easy forLoopStart` 知识库中没有该节点类型的任何知识, 次要节点 `easy globalSeed` 仅有 KSampler 的通用知识，没有该节点自己的说明, 次要节点 `easy globalSeed` 仅有 KSampler 的通用知识，没有该节点自己的说明, 次要节点 `easy seed` 仅有 KSampler 的通用知识，没有该节点自己的说明, 次要节点 `easy seed` 仅有 KSampler 的通用知识，没有该节点自己的说明, 次要节点 `easy seed` 仅有 KSampler 的通用知识，没有该节点自己的说明]
---

# 视频生成/文生视频/Wan 2.2 姿态引导下的 SVI 2.0 视频到视频无限循环延长与高一致性生成工作流_1998603727122653185.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/Wan 2.2 姿态引导下的 SVI 2.0 视频到视频无限循环延长与高一致性生成工作流_1998603727122653185.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（116 个）：
- `DWPreprocessor`
- `GetImageSizeAndCount`
- `ImageResizeKJv2`
- `GetNode`
- `ImageResizeKJv2`
- `GetNode`
- `GetNode`
- `JWInteger`
- `GetImageRangeFromBatch`
- `GetImageRangeFromBatch`
- `DWPreprocessor`
- `ImageBatch`
- `GetNode`
- `GetImageSizeAndCount`
- `SimpleMath+`
- `GetImageRangeFromBatch`
- `GetImageRangeFromBatch`
- `SetNode`
- `INTConstant`
- `VHS_BatchManager`
- `easy seed`
- `GetImageRangeFromBatch`
- `MathExpression|pysssss`
- `Note`
- `WanVideoSetBlockSwap`
- `Note`
- `WanVideoDecode`
- `WanVideoSetBlockSwap`
- `WanVideoSampler` ★核心
- `WanVideoSetLoRAs`
- `WanVideoSetLoRAs`
- `easy globalSeed`
- `WanVideoScheduler`
- `easy seed`
- `Note`
- `WanVideoSetBlockSwap`
- `Note`
- `WanVideoSetBlockSwap`
- `easy globalSeed`
- `WanVideoSampler` ★核心
- `WanVideoSampler` ★核心
- `WanVideoBlockSwap`
- `LoadLynxResampler` ★核心
- `LynxInsightFaceCrop`
- `LynxEncodeFaceIP`
- `LoadLynxResampler` ★核心
- `LynxInsightFaceCrop`
- `WanVideoBlockSwap`
- `WanVideoLoraSelect`
- `WanVideoVACEStartToEndFrame`
- `VHS_VideoCombine`
- `ImageResizeKJv2`
- `VHS_LoadVideo`
- `WanVideoVACEEncode`
- `LynxEncodeFaceIP`
- `LayerUtility: PurgeVRAM V2`
- `WanVideoSampler` ★核心
- `PrimitiveNode`
- `WanVideoVACEModelSelect`
- `WanVideoVACEModelSelect`
- `WanVideoExtraModelSelect`
- `WanVideoExtraModelSelect`
- `WanVideoScheduler`
- `WanVideoModelLoader`
- `WanVideoModelLoader`
- `WanVideoLoraSelect`
- `RH_Captioner`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `PrimitiveNode`
- `PrimitiveNode`
- `WanVideoSigmaToStep`
- `easy forLoopEnd`
- `easy batchAnything`
- `VHS_VideoCombine`
- `WanVideoVACEModelSelect`
- `WanVideoScheduler`
- `easy seed`
- `WanVideoScheduler`
- `WanVideoDecode`
- `ImageResizeKJv2`
- `MathExpression|pysssss`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `WanVideoVACEStartToEndFrame`
- `WanVideoVACEModelSelect`
- `WanVideoExtraModelSelect`
- `WanVideoExtraModelSelect`
- `WanVideoModelLoader`
- `WanVideoLoraSelect`
- `WanVideoSetLoRAs`
- `WanVideoSetLoRAs`
- `GetImageSizeAndCount`
- `WanVideoVACEEncode`
- `LoadWanVideoT5TextEncoder`
- `LoadWanVideoT5TextEncoder`
- `RH_Captioner`
- `PrimitiveNode`
- `WanVideoSigmaToStep`
- `VHS_VideoCombine`
- `WanVideoVAELoader`
- `VHS_VideoCombine`
- `WanVideoTextEncode`
- `WanVideoAddLynxEmbeds`
- `WanVideoAddLynxEmbeds`
- `WanVideoModelLoader`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `String Literal`
- `LoadImage`
- `WanVideoTextEncode`
- `RH_Captioner`
- `easy forLoopStart`
- `VHS_VideoCombine`
- `Int`

## 知识

覆盖率 **78%**（90/116）

**有卡**：`DWPreprocessor`、`GetImageSizeAndCount`、`ImageResizeKJv2`、`JWInteger`、`GetImageRangeFromBatch`、`ImageBatch`、`INTConstant`、`VHS_BatchManager`、`WanVideoSetBlockSwap`、`WanVideoDecode`、`WanVideoSampler`、`WanVideoSetLoRAs`、`WanVideoScheduler`、`WanVideoBlockSwap`、`LoadLynxResampler`、`LynxInsightFaceCrop`、`LynxEncodeFaceIP`、`WanVideoLoraSelect`、`WanVideoVACEStartToEndFrame`、`VHS_VideoCombine`、`VHS_LoadVideo`、`WanVideoVACEEncode`、`WanVideoVACEModelSelect`、`WanVideoExtraModelSelect`、`WanVideoModelLoader`、`RH_Captioner`、`WanVideoSigmaToStep`、`LoadWanVideoT5TextEncoder`、`WanVideoVAELoader`、`WanVideoTextEncode`、`WanVideoAddLynxEmbeds`、`LoadImage`、`Int`

**缺卡**（13）：`LayerUtility: PurgeVRAM V2`、`MathExpression|pysssss`、`MathExpression|pysssss`、`SimpleMath+`、`String Literal`、`easy batchAnything`、`easy forLoopEnd`、`easy forLoopStart`、`easy globalSeed`、`easy globalSeed`、`easy seed`、`easy seed`、`easy seed`

**用到的条目**：LoadImage、WanVideoSampler、LoadLynxResampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoVACEEncode

## 学习发现

- 次要节点 `LayerUtility: PurgeVRAM V2` 知识库中没有该节点类型的任何知识
- 次要节点 `MathExpression|pysssss` 知识库中没有该节点类型的任何知识
- 次要节点 `MathExpression|pysssss` 知识库中没有该节点类型的任何知识
- 次要节点 `SimpleMath+` 知识库中没有该节点类型的任何知识
- 次要节点 `String Literal` 知识库中没有该节点类型的任何知识
- 次要节点 `easy batchAnything` 知识库中没有该节点类型的任何知识
- 次要节点 `easy forLoopEnd` 知识库中没有该节点类型的任何知识
- 次要节点 `easy forLoopStart` 知识库中没有该节点类型的任何知识
- 次要节点 `easy globalSeed` 仅有 KSampler 的通用知识，没有该节点自己的说明
- 次要节点 `easy globalSeed` 仅有 KSampler 的通用知识，没有该节点自己的说明
- 次要节点 `easy seed` 仅有 KSampler 的通用知识，没有该节点自己的说明
- 次要节点 `easy seed` 仅有 KSampler 的通用知识，没有该节点自己的说明
- 次要节点 `easy seed` 仅有 KSampler 的通用知识，没有该节点自己的说明

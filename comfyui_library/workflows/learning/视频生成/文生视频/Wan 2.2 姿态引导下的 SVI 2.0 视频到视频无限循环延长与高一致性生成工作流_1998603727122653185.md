---
key: 视频生成/文生视频/Wan 2.2 姿态引导下的 SVI 2.0 视频到视频无限循环延长与高一致性生成工作流_1998603727122653185.json
name: Wan 2.2 姿态引导下的 SVI 2.0 视频到视频无限循环延长与高一致性生成工作流_1998603727122653185
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/Wan 2.2 姿态引导下的 SVI 2.0 视频到视频无限循环延长与高一致性生成工作流_1998603727122653185.json
hash: 67e73b92b092809a
coverage: 0.887931
learned_at: 2026-10-15 22:47:05
nodes: [DWPreprocessor, GetImageSizeAndCount, ImageResizeKJv2, GetNode, ImageResizeKJv2, GetNode, GetNode, JWInteger, GetImageRangeFromBatch, GetImageRangeFromBatch, DWPreprocessor, ImageBatch, GetNode, GetImageSizeAndCount, SimpleMath+, GetImageRangeFromBatch, GetImageRangeFromBatch, SetNode, INTConstant, VHS_BatchManager, easy seed, GetImageRangeFromBatch, MathExpression|pysssss, Note, WanVideoSetBlockSwap, Note, WanVideoDecode, WanVideoSetBlockSwap, WanVideoSampler, WanVideoSetLoRAs, WanVideoSetLoRAs, easy globalSeed, WanVideoScheduler, easy seed, Note, WanVideoSetBlockSwap, Note, WanVideoSetBlockSwap, easy globalSeed, WanVideoSampler, WanVideoSampler, WanVideoBlockSwap, LoadLynxResampler, LynxInsightFaceCrop, LynxEncodeFaceIP, LoadLynxResampler, LynxInsightFaceCrop, WanVideoBlockSwap, WanVideoLoraSelect, WanVideoVACEStartToEndFrame, VHS_VideoCombine, ImageResizeKJv2, VHS_LoadVideo, WanVideoVACEEncode, LynxEncodeFaceIP, LayerUtility: PurgeVRAM V2, WanVideoSampler, PrimitiveNode, WanVideoVACEModelSelect, WanVideoVACEModelSelect, WanVideoExtraModelSelect, WanVideoExtraModelSelect, WanVideoScheduler, WanVideoModelLoader, WanVideoModelLoader, WanVideoLoraSelect, RH_Captioner, WanVideoLoraSelect, WanVideoLoraSelect, PrimitiveNode, PrimitiveNode, WanVideoSigmaToStep, easy forLoopEnd, easy batchAnything, VHS_VideoCombine, WanVideoVACEModelSelect, WanVideoScheduler, easy seed, WanVideoScheduler, WanVideoDecode, ImageResizeKJv2, MathExpression|pysssss, VHS_LoadVideo, VHS_VideoCombine, VHS_VideoCombine, WanVideoVACEStartToEndFrame, WanVideoVACEModelSelect, WanVideoExtraModelSelect, WanVideoExtraModelSelect, WanVideoModelLoader, WanVideoLoraSelect, WanVideoSetLoRAs, WanVideoSetLoRAs, GetImageSizeAndCount, WanVideoVACEEncode, LoadWanVideoT5TextEncoder, LoadWanVideoT5TextEncoder, RH_Captioner, PrimitiveNode, WanVideoSigmaToStep, VHS_VideoCombine, WanVideoVAELoader, VHS_VideoCombine, WanVideoTextEncode, WanVideoAddLynxEmbeds, WanVideoAddLynxEmbeds, WanVideoModelLoader, WanVideoLoraSelect, WanVideoLoraSelect, String Literal, LoadImage, WanVideoTextEncode, RH_Captioner, easy forLoopStart, VHS_VideoCombine, Int]
patterns: []
missing: []
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

覆盖率 **89%**（103/116）

**有卡**：`DWPreprocessor`、`GetImageSizeAndCount`、`ImageResizeKJv2`、`JWInteger`、`GetImageRangeFromBatch`、`ImageBatch`、`SimpleMath+`、`INTConstant`、`VHS_BatchManager`、`easy seed`、`MathExpression|pysssss`、`WanVideoSetBlockSwap`、`WanVideoDecode`、`WanVideoSampler`、`WanVideoSetLoRAs`、`easy globalSeed`、`WanVideoScheduler`、`WanVideoBlockSwap`、`LoadLynxResampler`、`LynxInsightFaceCrop`、`LynxEncodeFaceIP`、`WanVideoLoraSelect`、`WanVideoVACEStartToEndFrame`、`VHS_VideoCombine`、`VHS_LoadVideo`、`WanVideoVACEEncode`、`LayerUtility: PurgeVRAM V2`、`WanVideoVACEModelSelect`、`WanVideoExtraModelSelect`、`WanVideoModelLoader`、`RH_Captioner`、`WanVideoSigmaToStep`、`easy forLoopEnd`、`easy batchAnything`、`LoadWanVideoT5TextEncoder`、`WanVideoVAELoader`、`WanVideoTextEncode`、`WanVideoAddLynxEmbeds`、`String Literal`、`LoadImage`、`easy forLoopStart`、`Int`

**用到的条目**：LoadImage、WanVideoSampler、LoadLynxResampler、easy globalSeed、easy seed、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode

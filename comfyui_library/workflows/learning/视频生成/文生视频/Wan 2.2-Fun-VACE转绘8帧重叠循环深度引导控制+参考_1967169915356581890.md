---
key: 视频生成/文生视频/Wan 2.2-Fun-VACE转绘8帧重叠循环深度引导控制+参考_1967169915356581890.json
name: Wan 2.2-Fun-VACE转绘8帧重叠循环深度引导控制+参考_1967169915356581890
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/Wan 2.2-Fun-VACE转绘8帧重叠循环深度引导控制+参考_1967169915356581890.json
hash: 44aebc1adf15f87c
coverage: 0.747826
learned_at: 2026-10-10 23:06:14
nodes: [Int, ImageResizeKJv2, GetImageSizeAndCount, WanVideoVACEStartToEndFrame, GetImageSizeAndCount, VHS_VideoCombine, ImageResizeKJv2, ImageResizeKJv2, VHS_VideoCombine, easy forLoopEnd, GetImageRangeFromBatch, easy forLoopStart, GetImageRangeFromBatch, Int, WanVideoVACEStartToEndFrame, ImageResizeKJv2, easy batchAnything, GetImageSizeAndCount, SimpleMath+, GetImageRangeFromBatch, GetImageRangeFromBatch, SetNode, INTConstant, VHS_BatchManager, VHS_VideoCombine, VHS_VideoCombine, easy seed, GetImageRangeFromBatch, MathExpression|pysssss, Note, WanVideoSetBlockSwap, Note, WanVideoDecode, WanVideoSetBlockSwap, WanVideoSampler, WanVideoTextEncode, WanVideoSetLoRAs, WanVideoSetLoRAs, LoadWanVideoT5TextEncoder, easy globalSeed, PrimitiveNode, WanVideoSigmaToStep, WanVideoScheduler, WanVideoScheduler, easy seed, WanVideoVAELoader, WanVideoBlockSwap, WanVideoLoraSelect, WanVideoModelLoader, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, PrimitiveNode, WanVideoVACEEncode, SetNode, Note, WanVideoSetBlockSwap, Note, WanVideoDecode, WanVideoSetBlockSwap, WanVideoTextEncode, WanVideoSetLoRAs, WanVideoSetLoRAs, LoadWanVideoT5TextEncoder, easy globalSeed, PrimitiveNode, WanVideoSigmaToStep, WanVideoScheduler, VHS_VideoCombine, WanVideoScheduler, easy seed, WanVideoVAELoader, WanVideoBlockSwap, WanVideoLoraSelect, WanVideoModelLoader, WanVideoLoraSelect, WanVideoLoraSelect, WanVideoModelLoader, WanVideoLoraSelect, WanVideoSampler, PrimitiveNode, WanVideoSampler, WanVideoVACEEncode, WanVideoLoraSelect, WanVideoLoraSelect, WanVideoVACEModelSelect, WanVideoVACEModelSelect, WanVideoVACEModelSelect, WanVideoVACEModelSelect, String Literal, JWInteger, LoadImage, VHS_VideoCombine, SetNode, GetNode, GetNode, DepthCrafter, MathExpression|pysssss, VHS_LoadVideo, GetNode, GetNode, GetNode, GetNode, VHS_LoadVideo, DownloadAndLoadDepthCrafterModel, ImageBatch, DownloadAndLoadDepthCrafterModel, DepthCrafter, ImageResizeKJv2, DWPreprocessor, VHS_VideoCombine, VHS_VideoCombine, VHS_LoadVideo, VHS_VideoCombine, VHS_VideoCombine]
patterns: []
missing: [MathExpression|pysssss, MathExpression|pysssss, SimpleMath+, String Literal, easy batchAnything, easy forLoopEnd, easy forLoopStart, easy globalSeed, easy globalSeed, easy seed, easy seed, easy seed]
discoveries: [次要节点 `MathExpression|pysssss` 知识库中没有该节点类型的任何知识, 次要节点 `MathExpression|pysssss` 知识库中没有该节点类型的任何知识, 次要节点 `SimpleMath+` 知识库中没有该节点类型的任何知识, 次要节点 `String Literal` 知识库中没有该节点类型的任何知识, 次要节点 `easy batchAnything` 知识库中没有该节点类型的任何知识, 次要节点 `easy forLoopEnd` 知识库中没有该节点类型的任何知识, 次要节点 `easy forLoopStart` 知识库中没有该节点类型的任何知识, 次要节点 `easy globalSeed` 仅有 KSampler 的通用知识，没有该节点自己的说明, 次要节点 `easy globalSeed` 仅有 KSampler 的通用知识，没有该节点自己的说明, 次要节点 `easy seed` 仅有 KSampler 的通用知识，没有该节点自己的说明, 次要节点 `easy seed` 仅有 KSampler 的通用知识，没有该节点自己的说明, 次要节点 `easy seed` 仅有 KSampler 的通用知识，没有该节点自己的说明]
---

# 视频生成/文生视频/Wan 2.2-Fun-VACE转绘8帧重叠循环深度引导控制+参考_1967169915356581890.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/Wan 2.2-Fun-VACE转绘8帧重叠循环深度引导控制+参考_1967169915356581890.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（115 个）：
- `Int`
- `ImageResizeKJv2`
- `GetImageSizeAndCount`
- `WanVideoVACEStartToEndFrame`
- `GetImageSizeAndCount`
- `VHS_VideoCombine`
- `ImageResizeKJv2`
- `ImageResizeKJv2`
- `VHS_VideoCombine`
- `easy forLoopEnd`
- `GetImageRangeFromBatch`
- `easy forLoopStart`
- `GetImageRangeFromBatch`
- `Int`
- `WanVideoVACEStartToEndFrame`
- `ImageResizeKJv2`
- `easy batchAnything`
- `GetImageSizeAndCount`
- `SimpleMath+`
- `GetImageRangeFromBatch`
- `GetImageRangeFromBatch`
- `SetNode`
- `INTConstant`
- `VHS_BatchManager`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `easy seed`
- `GetImageRangeFromBatch`
- `MathExpression|pysssss`
- `Note`
- `WanVideoSetBlockSwap`
- `Note`
- `WanVideoDecode`
- `WanVideoSetBlockSwap`
- `WanVideoSampler` ★核心
- `WanVideoTextEncode`
- `WanVideoSetLoRAs`
- `WanVideoSetLoRAs`
- `LoadWanVideoT5TextEncoder`
- `easy globalSeed`
- `PrimitiveNode`
- `WanVideoSigmaToStep`
- `WanVideoScheduler`
- `WanVideoScheduler`
- `easy seed`
- `WanVideoVAELoader`
- `WanVideoBlockSwap`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSampler` ★核心
- `PrimitiveNode`
- `WanVideoVACEEncode`
- `SetNode`
- `Note`
- `WanVideoSetBlockSwap`
- `Note`
- `WanVideoDecode`
- `WanVideoSetBlockSwap`
- `WanVideoTextEncode`
- `WanVideoSetLoRAs`
- `WanVideoSetLoRAs`
- `LoadWanVideoT5TextEncoder`
- `easy globalSeed`
- `PrimitiveNode`
- `WanVideoSigmaToStep`
- `WanVideoScheduler`
- `VHS_VideoCombine`
- `WanVideoScheduler`
- `easy seed`
- `WanVideoVAELoader`
- `WanVideoBlockSwap`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoLoraSelect`
- `WanVideoSampler` ★核心
- `PrimitiveNode`
- `WanVideoSampler` ★核心
- `WanVideoVACEEncode`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `WanVideoVACEModelSelect`
- `WanVideoVACEModelSelect`
- `WanVideoVACEModelSelect`
- `WanVideoVACEModelSelect`
- `String Literal`
- `JWInteger`
- `LoadImage`
- `VHS_VideoCombine`
- `SetNode`
- `GetNode`
- `GetNode`
- `DepthCrafter`
- `MathExpression|pysssss`
- `VHS_LoadVideo`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `VHS_LoadVideo`
- `DownloadAndLoadDepthCrafterModel`
- `ImageBatch`
- `DownloadAndLoadDepthCrafterModel`
- `DepthCrafter`
- `ImageResizeKJv2`
- `DWPreprocessor`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `VHS_VideoCombine`

## 知识

覆盖率 **75%**（86/115）

**有卡**：`Int`、`ImageResizeKJv2`、`GetImageSizeAndCount`、`WanVideoVACEStartToEndFrame`、`VHS_VideoCombine`、`GetImageRangeFromBatch`、`INTConstant`、`VHS_BatchManager`、`WanVideoSetBlockSwap`、`WanVideoDecode`、`WanVideoSampler`、`WanVideoTextEncode`、`WanVideoSetLoRAs`、`LoadWanVideoT5TextEncoder`、`WanVideoSigmaToStep`、`WanVideoScheduler`、`WanVideoVAELoader`、`WanVideoBlockSwap`、`WanVideoLoraSelect`、`WanVideoModelLoader`、`WanVideoVACEEncode`、`WanVideoVACEModelSelect`、`JWInteger`、`LoadImage`、`DepthCrafter`、`VHS_LoadVideo`、`DownloadAndLoadDepthCrafterModel`、`ImageBatch`、`DWPreprocessor`

**缺卡**（12）：`MathExpression|pysssss`、`MathExpression|pysssss`、`SimpleMath+`、`String Literal`、`easy batchAnything`、`easy forLoopEnd`、`easy forLoopStart`、`easy globalSeed`、`easy globalSeed`、`easy seed`、`easy seed`、`easy seed`

**用到的条目**：LoadImage、DepthCrafter、DownloadAndLoadDepthCrafterModel、WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader

## 学习发现

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

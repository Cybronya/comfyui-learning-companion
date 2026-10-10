---
key: 视频生成/文生视频/Wan 2.2-Fun-VACE转绘8帧重叠循环姿态引导控制+参考_1967140300189786113.json
name: Wan 2.2-Fun-VACE转绘8帧重叠循环姿态引导控制+参考_1967140300189786113
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/Wan 2.2-Fun-VACE转绘8帧重叠循环姿态引导控制+参考_1967140300189786113.json
hash: 9ab91623115ad4e4
coverage: 0.728972
learned_at: 2026-10-10 23:06:13
nodes: [Int, ImageResizeKJv2, DWPreprocessor, GetImageSizeAndCount, GetImageSizeAndCount, VHS_VideoCombine, ImageResizeKJv2, GetNode, ImageResizeKJv2, VHS_VideoCombine, easy forLoopEnd, GetNode, GetNode, JWInteger, GetImageRangeFromBatch, easy forLoopStart, GetImageRangeFromBatch, Int, DWPreprocessor, WanVideoVACEStartToEndFrame, ImageResizeKJv2, easy batchAnything, ImageBatch, GetNode, GetImageSizeAndCount, SimpleMath+, GetImageRangeFromBatch, GetImageRangeFromBatch, SetNode, INTConstant, LoadImage, VHS_LoadVideo, VHS_BatchManager, VHS_VideoCombine, VHS_VideoCombine, VHS_LoadVideo, easy seed, GetImageRangeFromBatch, MathExpression|pysssss, GetNode, SetNode, Note, WanVideoSetBlockSwap, Note, WanVideoDecode, WanVideoSetBlockSwap, WanVideoSampler, WanVideoTextEncode, WanVideoSetLoRAs, WanVideoSetLoRAs, LoadWanVideoT5TextEncoder, easy globalSeed, PrimitiveNode, WanVideoSigmaToStep, WanVideoScheduler, WanVideoScheduler, easy seed, WanVideoVAELoader, WanVideoBlockSwap, WanVideoLoraSelect, WanVideoModelLoader, WanVideoModelLoader, WanVideoSampler, PrimitiveNode, WanVideoVACEEncode, VHS_VideoCombine, GetNode, SetNode, Note, WanVideoSetBlockSwap, Note, WanVideoDecode, WanVideoSetBlockSwap, WanVideoTextEncode, WanVideoSetLoRAs, WanVideoSetLoRAs, LoadWanVideoT5TextEncoder, easy globalSeed, PrimitiveNode, WanVideoSigmaToStep, WanVideoScheduler, VHS_VideoCombine, WanVideoScheduler, easy seed, WanVideoVAELoader, WanVideoBlockSwap, WanVideoLoraSelect, WanVideoModelLoader, WanVideoLoraSelect, WanVideoLoraSelect, WanVideoModelLoader, WanVideoLoraSelect, WanVideoSampler, PrimitiveNode, WanVideoSampler, WanVideoVACEEncode, WanVideoLoraSelect, WanVideoLoraSelect, WanVideoVACEModelSelect, WanVideoVACEModelSelect, String Literal, WanVideoVACEModelSelect, WanVideoVACEModelSelect, MathExpression|pysssss, WanVideoVACEStartToEndFrame, WanVideoLoraSelect, VHS_VideoCombine]
patterns: []
missing: [MathExpression|pysssss, MathExpression|pysssss, SimpleMath+, String Literal, easy batchAnything, easy forLoopEnd, easy forLoopStart, easy globalSeed, easy globalSeed, easy seed, easy seed, easy seed]
discoveries: [次要节点 `MathExpression|pysssss` 知识库中没有该节点类型的任何知识, 次要节点 `MathExpression|pysssss` 知识库中没有该节点类型的任何知识, 次要节点 `SimpleMath+` 知识库中没有该节点类型的任何知识, 次要节点 `String Literal` 知识库中没有该节点类型的任何知识, 次要节点 `easy batchAnything` 知识库中没有该节点类型的任何知识, 次要节点 `easy forLoopEnd` 知识库中没有该节点类型的任何知识, 次要节点 `easy forLoopStart` 知识库中没有该节点类型的任何知识, 次要节点 `easy globalSeed` 仅有 KSampler 的通用知识，没有该节点自己的说明, 次要节点 `easy globalSeed` 仅有 KSampler 的通用知识，没有该节点自己的说明, 次要节点 `easy seed` 仅有 KSampler 的通用知识，没有该节点自己的说明, 次要节点 `easy seed` 仅有 KSampler 的通用知识，没有该节点自己的说明, 次要节点 `easy seed` 仅有 KSampler 的通用知识，没有该节点自己的说明]
---

# 视频生成/文生视频/Wan 2.2-Fun-VACE转绘8帧重叠循环姿态引导控制+参考_1967140300189786113.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/Wan 2.2-Fun-VACE转绘8帧重叠循环姿态引导控制+参考_1967140300189786113.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（107 个）：
- `Int`
- `ImageResizeKJv2`
- `DWPreprocessor`
- `GetImageSizeAndCount`
- `GetImageSizeAndCount`
- `VHS_VideoCombine`
- `ImageResizeKJv2`
- `GetNode`
- `ImageResizeKJv2`
- `VHS_VideoCombine`
- `easy forLoopEnd`
- `GetNode`
- `GetNode`
- `JWInteger`
- `GetImageRangeFromBatch`
- `easy forLoopStart`
- `GetImageRangeFromBatch`
- `Int`
- `DWPreprocessor`
- `WanVideoVACEStartToEndFrame`
- `ImageResizeKJv2`
- `easy batchAnything`
- `ImageBatch`
- `GetNode`
- `GetImageSizeAndCount`
- `SimpleMath+`
- `GetImageRangeFromBatch`
- `GetImageRangeFromBatch`
- `SetNode`
- `INTConstant`
- `LoadImage`
- `VHS_LoadVideo`
- `VHS_BatchManager`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `VHS_LoadVideo`
- `easy seed`
- `GetImageRangeFromBatch`
- `MathExpression|pysssss`
- `GetNode`
- `SetNode`
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
- `WanVideoModelLoader`
- `WanVideoSampler` ★核心
- `PrimitiveNode`
- `WanVideoVACEEncode`
- `VHS_VideoCombine`
- `GetNode`
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
- `String Literal`
- `WanVideoVACEModelSelect`
- `WanVideoVACEModelSelect`
- `MathExpression|pysssss`
- `WanVideoVACEStartToEndFrame`
- `WanVideoLoraSelect`
- `VHS_VideoCombine`

## 知识

覆盖率 **73%**（78/107）

**有卡**：`Int`、`ImageResizeKJv2`、`DWPreprocessor`、`GetImageSizeAndCount`、`VHS_VideoCombine`、`JWInteger`、`GetImageRangeFromBatch`、`WanVideoVACEStartToEndFrame`、`ImageBatch`、`INTConstant`、`LoadImage`、`VHS_LoadVideo`、`VHS_BatchManager`、`WanVideoSetBlockSwap`、`WanVideoDecode`、`WanVideoSampler`、`WanVideoTextEncode`、`WanVideoSetLoRAs`、`LoadWanVideoT5TextEncoder`、`WanVideoSigmaToStep`、`WanVideoScheduler`、`WanVideoVAELoader`、`WanVideoBlockSwap`、`WanVideoLoraSelect`、`WanVideoModelLoader`、`WanVideoVACEEncode`、`WanVideoVACEModelSelect`

**缺卡**（12）：`MathExpression|pysssss`、`MathExpression|pysssss`、`SimpleMath+`、`String Literal`、`easy batchAnything`、`easy forLoopEnd`、`easy forLoopStart`、`easy globalSeed`、`easy globalSeed`、`easy seed`、`easy seed`、`easy seed`

**用到的条目**：LoadImage、WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoVACEEncode、WanVideoLoraSelect

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

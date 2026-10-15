---
key: 视频生成/文生视频/Wan 2.2-Fun-VACE转绘8帧重叠循环姿态引导控制+参考_1967140300189786113.json
name: Wan 2.2-Fun-VACE转绘8帧重叠循环姿态引导控制+参考_1967140300189786113
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/Wan 2.2-Fun-VACE转绘8帧重叠循环姿态引导控制+参考_1967140300189786113.json
hash: 9ab91623115ad4e4
coverage: 0.841121
learned_at: 2026-10-15 22:47:05
nodes: [Int, ImageResizeKJv2, DWPreprocessor, GetImageSizeAndCount, GetImageSizeAndCount, VHS_VideoCombine, ImageResizeKJv2, GetNode, ImageResizeKJv2, VHS_VideoCombine, easy forLoopEnd, GetNode, GetNode, JWInteger, GetImageRangeFromBatch, easy forLoopStart, GetImageRangeFromBatch, Int, DWPreprocessor, WanVideoVACEStartToEndFrame, ImageResizeKJv2, easy batchAnything, ImageBatch, GetNode, GetImageSizeAndCount, SimpleMath+, GetImageRangeFromBatch, GetImageRangeFromBatch, SetNode, INTConstant, LoadImage, VHS_LoadVideo, VHS_BatchManager, VHS_VideoCombine, VHS_VideoCombine, VHS_LoadVideo, easy seed, GetImageRangeFromBatch, MathExpression|pysssss, GetNode, SetNode, Note, WanVideoSetBlockSwap, Note, WanVideoDecode, WanVideoSetBlockSwap, WanVideoSampler, WanVideoTextEncode, WanVideoSetLoRAs, WanVideoSetLoRAs, LoadWanVideoT5TextEncoder, easy globalSeed, PrimitiveNode, WanVideoSigmaToStep, WanVideoScheduler, WanVideoScheduler, easy seed, WanVideoVAELoader, WanVideoBlockSwap, WanVideoLoraSelect, WanVideoModelLoader, WanVideoModelLoader, WanVideoSampler, PrimitiveNode, WanVideoVACEEncode, VHS_VideoCombine, GetNode, SetNode, Note, WanVideoSetBlockSwap, Note, WanVideoDecode, WanVideoSetBlockSwap, WanVideoTextEncode, WanVideoSetLoRAs, WanVideoSetLoRAs, LoadWanVideoT5TextEncoder, easy globalSeed, PrimitiveNode, WanVideoSigmaToStep, WanVideoScheduler, VHS_VideoCombine, WanVideoScheduler, easy seed, WanVideoVAELoader, WanVideoBlockSwap, WanVideoLoraSelect, WanVideoModelLoader, WanVideoLoraSelect, WanVideoLoraSelect, WanVideoModelLoader, WanVideoLoraSelect, WanVideoSampler, PrimitiveNode, WanVideoSampler, WanVideoVACEEncode, WanVideoLoraSelect, WanVideoLoraSelect, WanVideoVACEModelSelect, WanVideoVACEModelSelect, String Literal, WanVideoVACEModelSelect, WanVideoVACEModelSelect, MathExpression|pysssss, WanVideoVACEStartToEndFrame, WanVideoLoraSelect, VHS_VideoCombine]
patterns: []
missing: []
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

覆盖率 **84%**（90/107）

**有卡**：`Int`、`ImageResizeKJv2`、`DWPreprocessor`、`GetImageSizeAndCount`、`VHS_VideoCombine`、`easy forLoopEnd`、`JWInteger`、`GetImageRangeFromBatch`、`easy forLoopStart`、`WanVideoVACEStartToEndFrame`、`easy batchAnything`、`ImageBatch`、`SimpleMath+`、`INTConstant`、`LoadImage`、`VHS_LoadVideo`、`VHS_BatchManager`、`easy seed`、`MathExpression|pysssss`、`WanVideoSetBlockSwap`、`WanVideoDecode`、`WanVideoSampler`、`WanVideoTextEncode`、`WanVideoSetLoRAs`、`LoadWanVideoT5TextEncoder`、`easy globalSeed`、`WanVideoSigmaToStep`、`WanVideoScheduler`、`WanVideoVAELoader`、`WanVideoBlockSwap`、`WanVideoLoraSelect`、`WanVideoModelLoader`、`WanVideoVACEEncode`、`WanVideoVACEModelSelect`、`String Literal`

**用到的条目**：LoadImage、WanVideoSampler、easy globalSeed、easy seed、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader

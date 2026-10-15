---
key: 视频生成/文生视频/Wan 2.2-Fun-VACE转绘8帧重叠循环深度引导控制+参考_2072999578032709632.json
name: Wan 2.2-Fun-VACE转绘8帧重叠循环深度引导控制+参考_2072999578032709632
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/Wan 2.2-Fun-VACE转绘8帧重叠循环深度引导控制+参考_2072999578032709632.json
hash: 4fb9aa1badbbd750
coverage: 0.852174
learned_at: 2026-10-15 22:47:06
nodes: [Int, ImageResizeKJv2, GetImageSizeAndCount, WanVideoVACEStartToEndFrame, GetImageSizeAndCount, VHS_VideoCombine, ImageResizeKJv2, ImageResizeKJv2, VHS_VideoCombine, easy forLoopEnd, GetImageRangeFromBatch, easy forLoopStart, GetImageRangeFromBatch, Int, WanVideoVACEStartToEndFrame, ImageResizeKJv2, easy batchAnything, GetImageSizeAndCount, SimpleMath+, GetImageRangeFromBatch, GetImageRangeFromBatch, SetNode, INTConstant, VHS_BatchManager, VHS_VideoCombine, VHS_VideoCombine, easy seed, GetImageRangeFromBatch, MathExpression|pysssss, Note, WanVideoSetBlockSwap, Note, WanVideoDecode, WanVideoSetBlockSwap, WanVideoSampler, WanVideoTextEncode, WanVideoSetLoRAs, WanVideoSetLoRAs, LoadWanVideoT5TextEncoder, easy globalSeed, PrimitiveNode, WanVideoSigmaToStep, WanVideoScheduler, WanVideoScheduler, easy seed, WanVideoVAELoader, WanVideoBlockSwap, WanVideoLoraSelect, WanVideoModelLoader, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, PrimitiveNode, WanVideoVACEEncode, SetNode, Note, WanVideoSetBlockSwap, Note, WanVideoDecode, WanVideoSetBlockSwap, WanVideoTextEncode, WanVideoSetLoRAs, WanVideoSetLoRAs, LoadWanVideoT5TextEncoder, easy globalSeed, PrimitiveNode, WanVideoSigmaToStep, WanVideoScheduler, VHS_VideoCombine, WanVideoScheduler, easy seed, WanVideoVAELoader, WanVideoBlockSwap, WanVideoLoraSelect, WanVideoModelLoader, WanVideoLoraSelect, WanVideoLoraSelect, WanVideoModelLoader, WanVideoLoraSelect, WanVideoSampler, PrimitiveNode, WanVideoSampler, WanVideoVACEEncode, WanVideoLoraSelect, WanVideoLoraSelect, WanVideoVACEModelSelect, WanVideoVACEModelSelect, WanVideoVACEModelSelect, WanVideoVACEModelSelect, String Literal, JWInteger, LoadImage, VHS_VideoCombine, SetNode, GetNode, GetNode, DepthCrafter, MathExpression|pysssss, VHS_LoadVideo, GetNode, GetNode, GetNode, GetNode, VHS_LoadVideo, DownloadAndLoadDepthCrafterModel, ImageBatch, DownloadAndLoadDepthCrafterModel, DepthCrafter, ImageResizeKJv2, DWPreprocessor, VHS_VideoCombine, VHS_VideoCombine, VHS_LoadVideo, VHS_VideoCombine, VHS_VideoCombine]
patterns: []
missing: []
---

# 视频生成/文生视频/Wan 2.2-Fun-VACE转绘8帧重叠循环深度引导控制+参考_2072999578032709632.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/Wan 2.2-Fun-VACE转绘8帧重叠循环深度引导控制+参考_2072999578032709632.json`

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

覆盖率 **85%**（98/115）

**有卡**：`Int`、`ImageResizeKJv2`、`GetImageSizeAndCount`、`WanVideoVACEStartToEndFrame`、`VHS_VideoCombine`、`easy forLoopEnd`、`GetImageRangeFromBatch`、`easy forLoopStart`、`easy batchAnything`、`SimpleMath+`、`INTConstant`、`VHS_BatchManager`、`easy seed`、`MathExpression|pysssss`、`WanVideoSetBlockSwap`、`WanVideoDecode`、`WanVideoSampler`、`WanVideoTextEncode`、`WanVideoSetLoRAs`、`LoadWanVideoT5TextEncoder`、`easy globalSeed`、`WanVideoSigmaToStep`、`WanVideoScheduler`、`WanVideoVAELoader`、`WanVideoBlockSwap`、`WanVideoLoraSelect`、`WanVideoModelLoader`、`WanVideoVACEEncode`、`WanVideoVACEModelSelect`、`String Literal`、`JWInteger`、`LoadImage`、`DepthCrafter`、`VHS_LoadVideo`、`DownloadAndLoadDepthCrafterModel`、`ImageBatch`、`DWPreprocessor`

**用到的条目**：LoadImage、DepthCrafter、DownloadAndLoadDepthCrafterModel、WanVideoSampler、easy globalSeed、easy seed、LoadWanVideoT5TextEncoder、WanVideoDecode

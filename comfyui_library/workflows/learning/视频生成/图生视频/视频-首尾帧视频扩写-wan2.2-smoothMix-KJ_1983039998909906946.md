---
key: 视频生成/图生视频/视频-首尾帧视频扩写-wan2.2-smoothMix-KJ_1983039998909906946.json
name: 视频-首尾帧视频扩写-wan2.2-smoothMix-KJ_1983039998909906946.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/视频-首尾帧视频扩写-wan2.2-smoothMix-KJ_1983039998909906946.json
hash: 168a463538477467
coverage: 0.64
learned_at: 2026-10-15 22:32:43
nodes: [easy showAnything, easy imageSize, GetImageSizeAndCount, GetNode, GetImageSizeAndCount, Reroute, WanVideoDecode, WanVideoSampler, ImpactFloat, easy showAnything, easy showAnything, WanVideoSigmaToStep, WanVideoSampler, CreateCFGScheduleFloatList, ImageResizeKJ, SetNode, GetNode, GetNode, WanVideoImageToVideoEncode, GetImageSizeAndCount, GetImageSizeAndCount, GetNode, GetNode, VHS_VideoCombine, GetNode, ImageFromBatch, PreviewImage, PreviewImage, GetImageSizeAndCount, SetNode, SetNode, SetNode, GetNode, GetImageSizeAndCount, VHS_VideoCombine, easy seed, GetNode, GetImageSizeAndCount, WanVideoTextEncodeCached, GetNode, WanVideoBlockSwap, WanVideoVAELoader, WanVideoSetBlockSwap, WanVideoSetBlockSwap, INTConstant, StringFunction|pysssss, GetNode, StringFunction|pysssss, SetNode, ImageLoader, LayerUtility: ImageScaleByAspectRatio V2, GetImageSizeAndCount, easy positive, GetImageSizeAndCount, MultiplePathsInput, ImageLoader, WanVideoScheduler, WanVideoScheduler, easy int, WanVideoModelLoader, WanVideoModelLoader, easy showAnything, MemoryCleaner, easy anythingIndexSwitch, GetImageSizeAndCount, SetNode, SetNode, PrimitiveFloat, SetNode, MathExpression|pysssss, ImpactFloat, SetNode, easy int, easy positive, Qwen3_VQA]
patterns: []
missing: []
---

# 视频生成/图生视频/视频-首尾帧视频扩写-wan2.2-smoothMix-KJ_1983039998909906946.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1983039998909906946.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（75 个）：
- `easy showAnything`
- `easy imageSize`
- `GetImageSizeAndCount`
- `GetNode`
- `GetImageSizeAndCount`
- `Reroute`
- `WanVideoDecode`
- `WanVideoSampler` ★核心
- `ImpactFloat`
- `easy showAnything`
- `easy showAnything`
- `WanVideoSigmaToStep`
- `WanVideoSampler` ★核心
- `CreateCFGScheduleFloatList`
- `ImageResizeKJ`
- `SetNode`
- `GetNode`
- `GetNode`
- `WanVideoImageToVideoEncode`
- `GetImageSizeAndCount`
- `GetImageSizeAndCount`
- `GetNode`
- `GetNode`
- `VHS_VideoCombine`
- `GetNode`
- `ImageFromBatch`
- `PreviewImage`
- `PreviewImage`
- `GetImageSizeAndCount`
- `SetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetImageSizeAndCount`
- `VHS_VideoCombine`
- `easy seed`
- `GetNode`
- `GetImageSizeAndCount`
- `WanVideoTextEncodeCached`
- `GetNode`
- `WanVideoBlockSwap`
- `WanVideoVAELoader`
- `WanVideoSetBlockSwap`
- `WanVideoSetBlockSwap`
- `INTConstant`
- `StringFunction|pysssss`
- `GetNode`
- `StringFunction|pysssss`
- `SetNode`
- `ImageLoader`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `GetImageSizeAndCount`
- `easy positive`
- `GetImageSizeAndCount`
- `MultiplePathsInput`
- `ImageLoader`
- `WanVideoScheduler`
- `WanVideoScheduler`
- `easy int`
- `WanVideoModelLoader`
- `WanVideoModelLoader`
- `easy showAnything`
- `MemoryCleaner`
- `easy anythingIndexSwitch`
- `GetImageSizeAndCount`
- `SetNode`
- `SetNode`
- `PrimitiveFloat`
- `SetNode`
- `MathExpression|pysssss`
- `ImpactFloat`
- `SetNode`
- `easy int`
- `easy positive`
- `Qwen3_VQA`

## 知识

覆盖率 **64%**（48/75）

**有卡**：`easy imageSize`、`GetImageSizeAndCount`、`WanVideoDecode`、`WanVideoSampler`、`ImpactFloat`、`WanVideoSigmaToStep`、`CreateCFGScheduleFloatList`、`ImageResizeKJ`、`WanVideoImageToVideoEncode`、`VHS_VideoCombine`、`ImageFromBatch`、`easy seed`、`WanVideoTextEncodeCached`、`WanVideoBlockSwap`、`WanVideoVAELoader`、`WanVideoSetBlockSwap`、`INTConstant`、`StringFunction|pysssss`、`ImageLoader`、`LayerUtility: ImageScaleByAspectRatio V2`、`easy positive`、`MultiplePathsInput`、`WanVideoScheduler`、`easy int`、`WanVideoModelLoader`、`MemoryCleaner`、`easy anythingIndexSwitch`、`MathExpression|pysssss`、`Qwen3_VQA`

**用到的条目**：LayerUtility: ImageScaleByAspectRatio V2、WanVideoSampler、CreateCFGScheduleFloatList、easy seed、WanVideoDecode、WanVideoVAELoader、WanVideoImageToVideoEncode、WanVideoTextEncodeCached

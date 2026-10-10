---
key: 视频生成/文生视频/【超清版】WAN2.2--图生视频（超清极速版）_1973229498395136001.json
name: 【超清版】WAN2.2--图生视频（超清极速版）_1973229498395136001
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/【超清版】WAN2.2--图生视频（超清极速版）_1973229498395136001.json
hash: 6b2577e45d872f3e
coverage: 0.818182
learned_at: 2026-10-10 23:10:18
nodes: [LoadWanVideoT5TextEncoder, WanVideoVAELoader, WanVideoBlockSwap, WanVideoBlockSwap, LoadImage, easy int, WanVideoBlockSwap, WanVideoSetBlockSwap, WanVideoImageToVideoEncode, MathExpression|pysssss, INTConstant, GetImageSizeAndCount, WanVideoSetLoRAs, WanVideoSetLoRAs, WanVideoLoraSelect, DF_Integer, JjkText, WanVideoSampler, WanVideoSampler, WanVideoTextEncode, SimpleMath+, WanVideoLoraSelect, JWInteger, WanVideoDecode, WanVideoSetBlockSwap, LayerUtility: ImageScaleByAspectRatio V2, CreateCFGScheduleFloatList, WanVideoLoraSelect, VHS_VideoCombine, WanVideoModelLoader, WanVideoModelLoader, PrimitiveNode, WanVideoLoraSelect]
patterns: []
missing: [LayerUtility: ImageScaleByAspectRatio V2, MathExpression|pysssss, SimpleMath+, easy int]
discoveries: [次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识, 次要节点 `MathExpression|pysssss` 知识库中没有该节点类型的任何知识, 次要节点 `SimpleMath+` 知识库中没有该节点类型的任何知识, 次要节点 `easy int` 知识库中没有该节点类型的任何知识]
---

# 视频生成/文生视频/【超清版】WAN2.2--图生视频（超清极速版）_1973229498395136001.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/【超清版】WAN2.2--图生视频（超清极速版）_1973229498395136001.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（33 个）：
- `LoadWanVideoT5TextEncoder`
- `WanVideoVAELoader`
- `WanVideoBlockSwap`
- `WanVideoBlockSwap`
- `LoadImage`
- `easy int`
- `WanVideoBlockSwap`
- `WanVideoSetBlockSwap`
- `WanVideoImageToVideoEncode`
- `MathExpression|pysssss`
- `INTConstant`
- `GetImageSizeAndCount`
- `WanVideoSetLoRAs`
- `WanVideoSetLoRAs`
- `WanVideoLoraSelect`
- `DF_Integer`
- `JjkText`
- `WanVideoSampler` ★核心
- `WanVideoSampler` ★核心
- `WanVideoTextEncode`
- `SimpleMath+`
- `WanVideoLoraSelect`
- `JWInteger`
- `WanVideoDecode`
- `WanVideoSetBlockSwap`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `CreateCFGScheduleFloatList`
- `WanVideoLoraSelect`
- `VHS_VideoCombine`
- `WanVideoModelLoader`
- `WanVideoModelLoader`
- `PrimitiveNode`
- `WanVideoLoraSelect`

## 知识

覆盖率 **82%**（27/33）

**有卡**：`LoadWanVideoT5TextEncoder`、`WanVideoVAELoader`、`WanVideoBlockSwap`、`LoadImage`、`WanVideoSetBlockSwap`、`WanVideoImageToVideoEncode`、`INTConstant`、`GetImageSizeAndCount`、`WanVideoSetLoRAs`、`WanVideoLoraSelect`、`DF_Integer`、`WanVideoSampler`、`WanVideoTextEncode`、`JWInteger`、`WanVideoDecode`、`CreateCFGScheduleFloatList`、`VHS_VideoCombine`、`WanVideoModelLoader`

**缺卡**（4）：`LayerUtility: ImageScaleByAspectRatio V2`、`MathExpression|pysssss`、`SimpleMath+`、`easy int`

**用到的条目**：LoadImage、WanVideoSampler、CreateCFGScheduleFloatList、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoImageToVideoEncode

## 学习发现

- 次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识
- 次要节点 `MathExpression|pysssss` 知识库中没有该节点类型的任何知识
- 次要节点 `SimpleMath+` 知识库中没有该节点类型的任何知识
- 次要节点 `easy int` 知识库中没有该节点类型的任何知识

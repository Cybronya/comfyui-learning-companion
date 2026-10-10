---
key: 视频生成/文生视频/视频-文生视频自动扩写-wan2.2-KJ_1972719438250332161.json
name: 视频-文生视频自动扩写-wan2.2-KJ_1972719438250332161
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/视频-文生视频自动扩写-wan2.2-KJ_1972719438250332161.json
hash: e7f987344779f1bb
coverage: 0.484848
learned_at: 2026-10-10 23:13:53
nodes: [easy showAnything, easy imageSize, GetImageSizeAndCount, GetImageSizeAndCount, GetNode, WanVideoDecode, VHS_VideoCombine, WanVideoSetBlockSwap, WanVideoSetLoRAs, GetNode, Reroute, SetNode, QwenLoader, WanVideoSampler, ImpactFloat, CreateCFGScheduleFloatList, GetNode, WanVideoEmptyEmbeds, WanVideoSampler, WanVideoSigmaToStep, easy showAnything, easy showAnything, GetNode, SetNode, StringFunction|pysssss, GetNode, SetNode, GetNode, GetImageSizeAndCount, GetNode, StringFunction|pysssss, GetNode, GetImageSizeAndCount, WanVideoPromptExtender, SetNode, StringFunction|pysssss, GetImageSizeAndCount, GetNode, GetImageSizeAndCount, VHS_VideoCombine, WanVideoSetBlockSwap, WanVideoBlockSwap, WanVideoLoraSelect, INTConstant, WanVideoVAELoader, WanVideoTextEncodeCached, WanVideoLoraSelectMulti, WanVideoScheduler, WanVideoScheduler, WanVideoModelLoader, WanVideoModelLoader, easy anythingIndexSwitch, easy positive, easy int, easy int, easy positive, easy int, ImpactFloat, SetNode, easy seed, SetNode, PrimitiveFloat, SetNode, EmptyImage, SetNode, MathExpression|pysssss]
patterns: []
missing: [MathExpression|pysssss, StringFunction|pysssss, StringFunction|pysssss, StringFunction|pysssss, easy anythingIndexSwitch, easy int, easy int, easy int, easy positive, easy positive, easy imageSize, easy seed]
discoveries: [次要节点 `MathExpression|pysssss` 知识库中没有该节点类型的任何知识, 次要节点 `StringFunction|pysssss` 知识库中没有该节点类型的任何知识, 次要节点 `StringFunction|pysssss` 知识库中没有该节点类型的任何知识, 次要节点 `StringFunction|pysssss` 知识库中没有该节点类型的任何知识, 次要节点 `easy anythingIndexSwitch` 知识库中没有该节点类型的任何知识, 次要节点 `easy int` 知识库中没有该节点类型的任何知识, 次要节点 `easy int` 知识库中没有该节点类型的任何知识, 次要节点 `easy int` 知识库中没有该节点类型的任何知识, 次要节点 `easy positive` 知识库中没有该节点类型的任何知识, 次要节点 `easy positive` 知识库中没有该节点类型的任何知识, 次要节点 `easy imageSize` 仅有 Resolution 的通用知识，没有该节点自己的说明, 次要节点 `easy seed` 仅有 KSampler 的通用知识，没有该节点自己的说明]
---

# 视频生成/文生视频/视频-文生视频自动扩写-wan2.2-KJ_1972719438250332161.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/视频-文生视频自动扩写-wan2.2-KJ_1972719438250332161.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（66 个）：
- `easy showAnything`
- `easy imageSize`
- `GetImageSizeAndCount`
- `GetImageSizeAndCount`
- `GetNode`
- `WanVideoDecode`
- `VHS_VideoCombine`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `GetNode`
- `Reroute`
- `SetNode`
- `QwenLoader`
- `WanVideoSampler` ★核心
- `ImpactFloat`
- `CreateCFGScheduleFloatList`
- `GetNode`
- `WanVideoEmptyEmbeds`
- `WanVideoSampler` ★核心
- `WanVideoSigmaToStep`
- `easy showAnything`
- `easy showAnything`
- `GetNode`
- `SetNode`
- `StringFunction|pysssss`
- `GetNode`
- `SetNode`
- `GetNode`
- `GetImageSizeAndCount`
- `GetNode`
- `StringFunction|pysssss`
- `GetNode`
- `GetImageSizeAndCount`
- `WanVideoPromptExtender`
- `SetNode`
- `StringFunction|pysssss`
- `GetImageSizeAndCount`
- `GetNode`
- `GetImageSizeAndCount`
- `VHS_VideoCombine`
- `WanVideoSetBlockSwap`
- `WanVideoBlockSwap`
- `WanVideoLoraSelect`
- `INTConstant`
- `WanVideoVAELoader`
- `WanVideoTextEncodeCached`
- `WanVideoLoraSelectMulti`
- `WanVideoScheduler`
- `WanVideoScheduler`
- `WanVideoModelLoader`
- `WanVideoModelLoader`
- `easy anythingIndexSwitch`
- `easy positive`
- `easy int`
- `easy int`
- `easy positive`
- `easy int`
- `ImpactFloat`
- `SetNode`
- `easy seed`
- `SetNode`
- `PrimitiveFloat`
- `SetNode`
- `EmptyImage`
- `SetNode`
- `MathExpression|pysssss`

## 知识

覆盖率 **48%**（32/66）

**有卡**：`GetImageSizeAndCount`、`WanVideoDecode`、`VHS_VideoCombine`、`WanVideoSetBlockSwap`、`WanVideoSetLoRAs`、`QwenLoader`、`WanVideoSampler`、`ImpactFloat`、`CreateCFGScheduleFloatList`、`WanVideoEmptyEmbeds`、`WanVideoSigmaToStep`、`WanVideoPromptExtender`、`WanVideoBlockSwap`、`WanVideoLoraSelect`、`INTConstant`、`WanVideoVAELoader`、`WanVideoTextEncodeCached`、`WanVideoLoraSelectMulti`、`WanVideoScheduler`、`WanVideoModelLoader`、`EmptyImage`

**缺卡**（12）：`MathExpression|pysssss`、`StringFunction|pysssss`、`StringFunction|pysssss`、`StringFunction|pysssss`、`easy anythingIndexSwitch`、`easy int`、`easy int`、`easy int`、`easy positive`、`easy positive`、`easy imageSize`、`easy seed`

**用到的条目**：WanVideoSampler、CreateCFGScheduleFloatList、WanVideoDecode、WanVideoVAELoader、WanVideoTextEncodeCached、WanVideoLoraSelect、WanVideoSetLoRAs、WanVideoLoraSelectMulti

## 学习发现

- 次要节点 `MathExpression|pysssss` 知识库中没有该节点类型的任何知识
- 次要节点 `StringFunction|pysssss` 知识库中没有该节点类型的任何知识
- 次要节点 `StringFunction|pysssss` 知识库中没有该节点类型的任何知识
- 次要节点 `StringFunction|pysssss` 知识库中没有该节点类型的任何知识
- 次要节点 `easy anythingIndexSwitch` 知识库中没有该节点类型的任何知识
- 次要节点 `easy int` 知识库中没有该节点类型的任何知识
- 次要节点 `easy int` 知识库中没有该节点类型的任何知识
- 次要节点 `easy int` 知识库中没有该节点类型的任何知识
- 次要节点 `easy positive` 知识库中没有该节点类型的任何知识
- 次要节点 `easy positive` 知识库中没有该节点类型的任何知识
- 次要节点 `easy imageSize` 仅有 Resolution 的通用知识，没有该节点自己的说明
- 次要节点 `easy seed` 仅有 KSampler 的通用知识，没有该节点自己的说明

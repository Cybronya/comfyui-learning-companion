---
key: 视频生成/文生视频/视频-文生视频扩写-wan2.2-smoothMix-KJ_1982718916021624834.json
name: 视频-文生视频扩写-wan2.2-smoothMix-KJ_1982718916021624834
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/视频-文生视频扩写-wan2.2-smoothMix-KJ_1982718916021624834.json
hash: e1436bcbcc710646
coverage: 0.476923
learned_at: 2026-10-11 02:45:05
nodes: [easy showAnything, easy imageSize, GetImageSizeAndCount, GetImageSizeAndCount, GetNode, WanVideoDecode, VHS_VideoCombine, GetNode, SetNode, WanVideoSampler, ImpactFloat, CreateCFGScheduleFloatList, GetNode, WanVideoEmptyEmbeds, WanVideoSampler, WanVideoSigmaToStep, easy showAnything, easy showAnything, GetNode, SetNode, StringFunction|pysssss, GetNode, SetNode, GetNode, GetImageSizeAndCount, GetNode, StringFunction|pysssss, GetNode, SetNode, easy seed, WanVideoPromptExtender, SetNode, StringFunction|pysssss, GetImageSizeAndCount, GetNode, GetImageSizeAndCount, VHS_VideoCombine, WanVideoSetBlockSwap, WanVideoBlockSwap, INTConstant, WanVideoVAELoader, WanVideoTextEncodeCached, WanVideoLoraSelectMulti, WanVideoScheduler, WanVideoScheduler, WanVideoModelLoader, Reroute, WanVideoSetBlockSwap, WanVideoLoraSelect, WanVideoModelLoader, EmptyImage, SetNode, ImpactFloat, GetImageSizeAndCount, SetNode, SetNode, MathExpression|pysssss, easy int, PrimitiveFloat, easy int, easy int, easy anythingIndexSwitch, easy positive, QwenLoader, easy positive]
patterns: []
missing: [MathExpression|pysssss, StringFunction|pysssss, StringFunction|pysssss, StringFunction|pysssss, easy anythingIndexSwitch, easy int, easy int, easy int, easy positive, easy positive, easy imageSize, easy seed]
discoveries: [次要节点 `MathExpression|pysssss` 知识库中没有该节点类型的任何知识, 次要节点 `StringFunction|pysssss` 知识库中没有该节点类型的任何知识, 次要节点 `StringFunction|pysssss` 知识库中没有该节点类型的任何知识, 次要节点 `StringFunction|pysssss` 知识库中没有该节点类型的任何知识, 次要节点 `easy anythingIndexSwitch` 知识库中没有该节点类型的任何知识, 次要节点 `easy int` 知识库中没有该节点类型的任何知识, 次要节点 `easy int` 知识库中没有该节点类型的任何知识, 次要节点 `easy int` 知识库中没有该节点类型的任何知识, 次要节点 `easy positive` 知识库中没有该节点类型的任何知识, 次要节点 `easy positive` 知识库中没有该节点类型的任何知识, 次要节点 `easy imageSize` 仅有 Resolution 的通用知识，没有该节点自己的说明, 次要节点 `easy seed` 仅有 KSampler 的通用知识，没有该节点自己的说明]
---

# 视频生成/文生视频/视频-文生视频扩写-wan2.2-smoothMix-KJ_1982718916021624834.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/视频-文生视频扩写-wan2.2-smoothMix-KJ_1982718916021624834.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（65 个）：
- `easy showAnything`
- `easy imageSize`
- `GetImageSizeAndCount`
- `GetImageSizeAndCount`
- `GetNode`
- `WanVideoDecode`
- `VHS_VideoCombine`
- `GetNode`
- `SetNode`
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
- `SetNode`
- `easy seed`
- `WanVideoPromptExtender`
- `SetNode`
- `StringFunction|pysssss`
- `GetImageSizeAndCount`
- `GetNode`
- `GetImageSizeAndCount`
- `VHS_VideoCombine`
- `WanVideoSetBlockSwap`
- `WanVideoBlockSwap`
- `INTConstant`
- `WanVideoVAELoader`
- `WanVideoTextEncodeCached`
- `WanVideoLoraSelectMulti`
- `WanVideoScheduler`
- `WanVideoScheduler`
- `WanVideoModelLoader`
- `Reroute`
- `WanVideoSetBlockSwap`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `EmptyImage`
- `SetNode`
- `ImpactFloat`
- `GetImageSizeAndCount`
- `SetNode`
- `SetNode`
- `MathExpression|pysssss`
- `easy int`
- `PrimitiveFloat`
- `easy int`
- `easy int`
- `easy anythingIndexSwitch`
- `easy positive`
- `QwenLoader`
- `easy positive`

## 知识

覆盖率 **48%**（31/65）

**有卡**：`GetImageSizeAndCount`、`WanVideoDecode`、`VHS_VideoCombine`、`WanVideoSampler`、`ImpactFloat`、`CreateCFGScheduleFloatList`、`WanVideoEmptyEmbeds`、`WanVideoSigmaToStep`、`WanVideoPromptExtender`、`WanVideoSetBlockSwap`、`WanVideoBlockSwap`、`INTConstant`、`WanVideoVAELoader`、`WanVideoTextEncodeCached`、`WanVideoLoraSelectMulti`、`WanVideoScheduler`、`WanVideoModelLoader`、`WanVideoLoraSelect`、`EmptyImage`、`QwenLoader`

**缺卡**（12）：`MathExpression|pysssss`、`StringFunction|pysssss`、`StringFunction|pysssss`、`StringFunction|pysssss`、`easy anythingIndexSwitch`、`easy int`、`easy int`、`easy int`、`easy positive`、`easy positive`、`easy imageSize`、`easy seed`

**用到的条目**：WanVideoSampler、CreateCFGScheduleFloatList、WanVideoDecode、WanVideoVAELoader、WanVideoTextEncodeCached、WanVideoLoraSelect、WanVideoLoraSelectMulti、WanVideoPromptExtender

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

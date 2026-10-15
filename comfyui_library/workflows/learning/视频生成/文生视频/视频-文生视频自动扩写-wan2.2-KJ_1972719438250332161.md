---
key: 视频生成/文生视频/视频-文生视频自动扩写-wan2.2-KJ_1972719438250332161.json
name: 视频-文生视频自动扩写-wan2.2-KJ_1972719438250332161
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/视频-文生视频自动扩写-wan2.2-KJ_1972719438250332161.json
hash: e7f987344779f1bb
coverage: 0.666667
learned_at: 2026-10-15 22:49:00
nodes: [easy showAnything, easy imageSize, GetImageSizeAndCount, GetImageSizeAndCount, GetNode, WanVideoDecode, VHS_VideoCombine, WanVideoSetBlockSwap, WanVideoSetLoRAs, GetNode, Reroute, SetNode, QwenLoader, WanVideoSampler, ImpactFloat, CreateCFGScheduleFloatList, GetNode, WanVideoEmptyEmbeds, WanVideoSampler, WanVideoSigmaToStep, easy showAnything, easy showAnything, GetNode, SetNode, StringFunction|pysssss, GetNode, SetNode, GetNode, GetImageSizeAndCount, GetNode, StringFunction|pysssss, GetNode, GetImageSizeAndCount, WanVideoPromptExtender, SetNode, StringFunction|pysssss, GetImageSizeAndCount, GetNode, GetImageSizeAndCount, VHS_VideoCombine, WanVideoSetBlockSwap, WanVideoBlockSwap, WanVideoLoraSelect, INTConstant, WanVideoVAELoader, WanVideoTextEncodeCached, WanVideoLoraSelectMulti, WanVideoScheduler, WanVideoScheduler, WanVideoModelLoader, WanVideoModelLoader, easy anythingIndexSwitch, easy positive, easy int, easy int, easy positive, easy int, ImpactFloat, SetNode, easy seed, SetNode, PrimitiveFloat, SetNode, EmptyImage, SetNode, MathExpression|pysssss]
patterns: []
missing: []
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

覆盖率 **67%**（44/66）

**有卡**：`easy imageSize`、`GetImageSizeAndCount`、`WanVideoDecode`、`VHS_VideoCombine`、`WanVideoSetBlockSwap`、`WanVideoSetLoRAs`、`QwenLoader`、`WanVideoSampler`、`ImpactFloat`、`CreateCFGScheduleFloatList`、`WanVideoEmptyEmbeds`、`WanVideoSigmaToStep`、`StringFunction|pysssss`、`WanVideoPromptExtender`、`WanVideoBlockSwap`、`WanVideoLoraSelect`、`INTConstant`、`WanVideoVAELoader`、`WanVideoTextEncodeCached`、`WanVideoLoraSelectMulti`、`WanVideoScheduler`、`WanVideoModelLoader`、`easy anythingIndexSwitch`、`easy positive`、`easy int`、`easy seed`、`EmptyImage`、`MathExpression|pysssss`

**用到的条目**：WanVideoSampler、CreateCFGScheduleFloatList、easy seed、WanVideoDecode、WanVideoVAELoader、WanVideoTextEncodeCached、WanVideoLoraSelect、WanVideoSetLoRAs

---
key: 视频生成/文生视频/视频-文生视频扩写-wan2.2-smoothMix-官方_1982718924657704961.json
name: 视频-文生视频扩写-wan2.2-smoothMix-官方_1982718924657704961
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/视频-文生视频扩写-wan2.2-smoothMix-官方_1982718924657704961.json
hash: 14f530578397b826
coverage: 0.453125
learned_at: 2026-10-11 02:45:05
nodes: [easy showAnything, easy imageSize, GetImageSizeAndCount, GetImageSizeAndCount, GetNode, SetNode, GetNode, PathchSageAttentionKJ, PathchSageAttentionKJ, WanMoeKSampler, VAEDecodeTiled, GetImageSizeAndCount, GetNode, CLIPLoader, Reroute, GetNode, SetNode, GetNode, SetNode, WanVideoVACEStartToEndFrame, VAELoader, GetImageSizeAndCount, CLIPTextEncode, CLIPTextEncode, EmptyHunyuanLatentVideo, GetImageSizeAndCount, GetNode, GetNode, GetImageSizeAndCount, VHS_VideoCombine, VHS_VideoCombine, LoraLoaderModelOnly, LoraLoaderModelOnly, UNETLoader, UNETLoader, LoraLoaderModelOnly, EmptyImage, easy int, ImpactFloat, SetNode, MathExpression|pysssss, GetImageSizeAndCount, SetNode, SetNode, SetNode, easy seed, GetNode, easy int, easy int, INTConstant, StringFunction|pysssss, easy positive, JWFloatToString, PrimitiveFloat, easy positive, GetNode, easy showAnything, easy positive, StringFunction|pysssss, RH_LLMAPI_NODE, StringFunction|pysssss, SetNode, easy anythingIndexSwitch, easy saveText]
patterns: []
missing: [MathExpression|pysssss, StringFunction|pysssss, StringFunction|pysssss, StringFunction|pysssss, easy anythingIndexSwitch, easy int, easy int, easy int, easy positive, easy positive, easy positive, easy imageSize, easy saveText, easy seed]
parameters: {"cfg": 20, "denoise": "sa_solver", "sampler_name": 1.5, "scheduler": 1, "seed": 0.875, "steps": "randomize"}
discoveries: [次要节点 `MathExpression|pysssss` 知识库中没有该节点类型的任何知识, 次要节点 `StringFunction|pysssss` 知识库中没有该节点类型的任何知识, 次要节点 `StringFunction|pysssss` 知识库中没有该节点类型的任何知识, 次要节点 `StringFunction|pysssss` 知识库中没有该节点类型的任何知识, 次要节点 `easy anythingIndexSwitch` 知识库中没有该节点类型的任何知识, 次要节点 `easy int` 知识库中没有该节点类型的任何知识, 次要节点 `easy int` 知识库中没有该节点类型的任何知识, 次要节点 `easy int` 知识库中没有该节点类型的任何知识, 次要节点 `easy positive` 知识库中没有该节点类型的任何知识, 次要节点 `easy positive` 知识库中没有该节点类型的任何知识, 次要节点 `easy positive` 知识库中没有该节点类型的任何知识, 次要节点 `easy imageSize` 仅有 Resolution 的通用知识，没有该节点自己的说明, 次要节点 `easy saveText` 仅有 SaveImage 的通用知识，没有该节点自己的说明, 次要节点 `easy seed` 仅有 KSampler 的通用知识，没有该节点自己的说明]
---

# 视频生成/文生视频/视频-文生视频扩写-wan2.2-smoothMix-官方_1982718924657704961.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/视频-文生视频扩写-wan2.2-smoothMix-官方_1982718924657704961.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（64 个）：
- `easy showAnything`
- `easy imageSize`
- `GetImageSizeAndCount`
- `GetImageSizeAndCount`
- `GetNode`
- `SetNode`
- `GetNode`
- `PathchSageAttentionKJ`
- `PathchSageAttentionKJ`
- `WanMoeKSampler` ★核心
- `VAEDecodeTiled` ★核心
- `GetImageSizeAndCount`
- `GetNode`
- `CLIPLoader`
- `Reroute`
- `GetNode`
- `SetNode`
- `GetNode`
- `SetNode`
- `WanVideoVACEStartToEndFrame`
- `VAELoader`
- `GetImageSizeAndCount`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `EmptyHunyuanLatentVideo`
- `GetImageSizeAndCount`
- `GetNode`
- `GetNode`
- `GetImageSizeAndCount`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `EmptyImage`
- `easy int`
- `ImpactFloat`
- `SetNode`
- `MathExpression|pysssss`
- `GetImageSizeAndCount`
- `SetNode`
- `SetNode`
- `SetNode`
- `easy seed`
- `GetNode`
- `easy int`
- `easy int`
- `INTConstant`
- `StringFunction|pysssss`
- `easy positive`
- `JWFloatToString`
- `PrimitiveFloat`
- `easy positive`
- `GetNode`
- `easy showAnything`
- `easy positive`
- `StringFunction|pysssss`
- `RH_LLMAPI_NODE`
- `StringFunction|pysssss`
- `SetNode`
- `easy anythingIndexSwitch`
- `easy saveText`

## 关键参数

- `seed` = `0.875`
- `steps` = `randomize`
- `cfg` = `20`
- `sampler_name` = `1.5`
- `scheduler` = `1`
- `denoise` = `sa_solver`

## 知识

覆盖率 **45%**（29/64）

**有卡**：`GetImageSizeAndCount`、`PathchSageAttentionKJ`、`WanMoeKSampler`、`VAEDecodeTiled`、`CLIPLoader`、`WanVideoVACEStartToEndFrame`、`VAELoader`、`CLIPTextEncode`、`EmptyHunyuanLatentVideo`、`VHS_VideoCombine`、`LoraLoaderModelOnly`、`UNETLoader`、`EmptyImage`、`ImpactFloat`、`INTConstant`、`JWFloatToString`、`RH_LLMAPI_NODE`

**缺卡**（14）：`MathExpression|pysssss`、`StringFunction|pysssss`、`StringFunction|pysssss`、`StringFunction|pysssss`、`easy anythingIndexSwitch`、`easy int`、`easy int`、`easy int`、`easy positive`、`easy positive`、`easy positive`、`easy imageSize`、`easy saveText`、`easy seed`

**用到的条目**：VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、UNETLoader、WanMoeKSampler、VAEDecodeTiled、EmptyHunyuanLatentVideo

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
- 次要节点 `easy positive` 知识库中没有该节点类型的任何知识
- 次要节点 `easy imageSize` 仅有 Resolution 的通用知识，没有该节点自己的说明
- 次要节点 `easy saveText` 仅有 SaveImage 的通用知识，没有该节点自己的说明
- 次要节点 `easy seed` 仅有 KSampler 的通用知识，没有该节点自己的说明

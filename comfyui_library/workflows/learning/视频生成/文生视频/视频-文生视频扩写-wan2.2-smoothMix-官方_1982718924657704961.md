---
key: 视频生成/文生视频/视频-文生视频扩写-wan2.2-smoothMix-官方_1982718924657704961.json
name: 视频-文生视频扩写-wan2.2-smoothMix-官方_1982718924657704961
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/视频-文生视频扩写-wan2.2-smoothMix-官方_1982718924657704961.json
hash: 14f530578397b826
coverage: 0.671875
learned_at: 2026-10-15 22:49:00
nodes: [easy showAnything, easy imageSize, GetImageSizeAndCount, GetImageSizeAndCount, GetNode, SetNode, GetNode, PathchSageAttentionKJ, PathchSageAttentionKJ, WanMoeKSampler, VAEDecodeTiled, GetImageSizeAndCount, GetNode, CLIPLoader, Reroute, GetNode, SetNode, GetNode, SetNode, WanVideoVACEStartToEndFrame, VAELoader, GetImageSizeAndCount, CLIPTextEncode, CLIPTextEncode, EmptyHunyuanLatentVideo, GetImageSizeAndCount, GetNode, GetNode, GetImageSizeAndCount, VHS_VideoCombine, VHS_VideoCombine, LoraLoaderModelOnly, LoraLoaderModelOnly, UNETLoader, UNETLoader, LoraLoaderModelOnly, EmptyImage, easy int, ImpactFloat, SetNode, MathExpression|pysssss, GetImageSizeAndCount, SetNode, SetNode, SetNode, easy seed, GetNode, easy int, easy int, INTConstant, StringFunction|pysssss, easy positive, JWFloatToString, PrimitiveFloat, easy positive, GetNode, easy showAnything, easy positive, StringFunction|pysssss, RH_LLMAPI_NODE, StringFunction|pysssss, SetNode, easy anythingIndexSwitch, easy saveText]
patterns: []
missing: []
parameters: {"cfg": 20, "denoise": "sa_solver", "sampler_name": 1.5, "scheduler": 1, "seed": 0.875, "steps": "randomize"}
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

覆盖率 **67%**（43/64）

**有卡**：`easy imageSize`、`GetImageSizeAndCount`、`PathchSageAttentionKJ`、`WanMoeKSampler`、`VAEDecodeTiled`、`CLIPLoader`、`WanVideoVACEStartToEndFrame`、`VAELoader`、`CLIPTextEncode`、`EmptyHunyuanLatentVideo`、`VHS_VideoCombine`、`LoraLoaderModelOnly`、`UNETLoader`、`EmptyImage`、`easy int`、`ImpactFloat`、`MathExpression|pysssss`、`easy seed`、`INTConstant`、`StringFunction|pysssss`、`easy positive`、`JWFloatToString`、`RH_LLMAPI_NODE`、`easy anythingIndexSwitch`、`easy saveText`

**用到的条目**：VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、UNETLoader、WanMoeKSampler、easy seed、VAEDecodeTiled

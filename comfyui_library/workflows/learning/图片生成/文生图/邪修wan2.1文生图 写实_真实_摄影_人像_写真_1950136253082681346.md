---
key: 图片生成/文生图/邪修wan2.1文生图 写实_真实_摄影_人像_写真_1950136253082681346.json
name: 邪修wan2.1文生图 写实_真实_摄影_人像_写真_1950136253082681346.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/邪修wan2.1文生图 写实_真实_摄影_人像_写真_1950136253082681346.json
hash: 7c383cb95150fab9
coverage: 0.462963
learned_at: 2026-10-07 22:58:19
nodes: [VAELoader, UNETLoader, SetNode, SetNode, SetNode, VAEDecode, Anything Everywhere, VAEDecode, GetNode, GetNode, GetNode, GetNode, GetNode, VAEDecode, GetNode, GetNode, GetNode, GetNode, GetNode, VAEDecode, GetNode, GetNode, GetNode, GetNode, GetNode, KSampler, easy cleanGpuUsed, KSampler, easy cleanGpuUsed, easy cleanGpuUsed, KSampler, KSampler, SaveImage, CLIPTextEncode, CLIPTextEncode, SaveImage, SaveImage, LoraLoaderModelOnly, SaveImage, LoraLoaderModelOnly, WanVideoNAG, CFGZeroStarAndInit, ModelSamplingSD3, CLIPLoader, easy cleanGpuUsed, SetNode, easy seed, Note, Note, SetNode, EmptyHunyuanLatentVideo, Fast Groups Bypasser (rgthree), JWInteger, JWInteger]
patterns: []
missing: [easy cleanGpuUsed, easy cleanGpuUsed, easy cleanGpuUsed, easy cleanGpuUsed, easy seed]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "res_2s", "scheduler": "bong_tangent", "seed": 556545841742232, "steps": 10}
discoveries: [次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识, 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识, 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识, 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识, 次要节点 `easy seed` 仅有 KSampler 的通用知识，没有该节点自己的说明]
---

# 图片生成/文生图/邪修wan2.1文生图 写实_真实_摄影_人像_写真_1950136253082681346.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/1950136253082681346.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Output → Other

**节点**（54 个）：
- `VAELoader`
- `UNETLoader` ★核心
- `SetNode`
- `SetNode`
- `SetNode`
- `VAEDecode` ★核心
- `Anything Everywhere`
- `VAEDecode` ★核心
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `VAEDecode` ★核心
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `VAEDecode` ★核心
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `KSampler` ★核心
- `easy cleanGpuUsed`
- `KSampler` ★核心
- `easy cleanGpuUsed`
- `easy cleanGpuUsed`
- `KSampler` ★核心
- `KSampler` ★核心
- `SaveImage`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `SaveImage`
- `SaveImage`
- `LoraLoaderModelOnly` ★核心
- `SaveImage`
- `LoraLoaderModelOnly` ★核心
- `WanVideoNAG`
- `CFGZeroStarAndInit`
- `ModelSamplingSD3`
- `CLIPLoader`
- `easy cleanGpuUsed`
- `SetNode`
- `easy seed`
- `Note`
- `Note`
- `SetNode`
- `EmptyHunyuanLatentVideo`
- `Fast Groups Bypasser (rgthree)`
- `JWInteger`
- `JWInteger`

## 关键参数

- `seed` = `556545841742232`
- `steps` = `10`
- `cfg` = `1`
- `sampler_name` = `res_2s`
- `scheduler` = `bong_tangent`
- `denoise` = `1`

## 知识

覆盖率 **46%**（25/54）

**有卡**：`VAELoader`、`UNETLoader`、`VAEDecode`、`KSampler`、`SaveImage`、`CLIPTextEncode`、`LoraLoaderModelOnly`、`WanVideoNAG`、`CFGZeroStarAndInit`、`ModelSamplingSD3`、`CLIPLoader`、`EmptyHunyuanLatentVideo`、`JWInteger`

**缺卡**（5）：`easy cleanGpuUsed`、`easy cleanGpuUsed`、`easy cleanGpuUsed`、`easy cleanGpuUsed`、`easy seed`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、UNETLoader、CFGZeroStarAndInit

## 学习发现

- 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识
- 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识
- 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识
- 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识
- 次要节点 `easy seed` 仅有 KSampler 的通用知识，没有该节点自己的说明

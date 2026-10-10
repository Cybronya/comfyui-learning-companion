---
key: 视频生成/文生视频/wan2.2-14B 文生视频，提示词优化_2012816369728888834.json
name: wan2.2-14B 文生视频，提示词优化_2012816369728888834
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/wan2.2-14B 文生视频，提示词优化_2012816369728888834.json
hash: fbf970c3c330b8bf
coverage: 0.62069
learned_at: 2026-10-11 03:07:13
nodes: [KSamplerAdvanced, VAEDecode, LayerUtility: PurgeVRAM, ModelSamplingSD3, VAELoader, EmptyHunyuanLatentVideo, SimpleMath+, SimpleMath+, UNETLoader, UNETLoader, KSamplerAdvanced, SimpleMath+, SimpleMath+, easy imageSize, SimpleMath+, VHS_VideoCombine, ModelSamplingSD3, CLIPLoader, easy showAnything, CR Text Replace, RH_Prompter, TextBox, DF_Integer, CLIPTextEncode, CLIPTextEncode, easy cleanGpuUsed, TextBox, easy showAnything, EmptyImage]
patterns: []
missing: [CR Text Replace, LayerUtility: PurgeVRAM, SimpleMath+, SimpleMath+, SimpleMath+, SimpleMath+, SimpleMath+, easy cleanGpuUsed, easy imageSize]
parameters: {"cfg": 20, "denoise": "simple", "sampler_name": 3.5, "scheduler": "euler", "seed": "disable", "steps": "fixed"}
discoveries: [次要节点 `CR Text Replace` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: PurgeVRAM` 知识库中没有该节点类型的任何知识, 次要节点 `SimpleMath+` 知识库中没有该节点类型的任何知识, 次要节点 `SimpleMath+` 知识库中没有该节点类型的任何知识, 次要节点 `SimpleMath+` 知识库中没有该节点类型的任何知识, 次要节点 `SimpleMath+` 知识库中没有该节点类型的任何知识, 次要节点 `SimpleMath+` 知识库中没有该节点类型的任何知识, 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识, 次要节点 `easy imageSize` 仅有 Resolution 的通用知识，没有该节点自己的说明]
---

# 视频生成/文生视频/wan2.2-14B 文生视频，提示词优化_2012816369728888834.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/wan2.2-14B 文生视频，提示词优化_2012816369728888834.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（29 个）：
- `KSamplerAdvanced` ★核心
- `VAEDecode` ★核心
- `LayerUtility: PurgeVRAM`
- `ModelSamplingSD3`
- `VAELoader`
- `EmptyHunyuanLatentVideo`
- `SimpleMath+`
- `SimpleMath+`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `KSamplerAdvanced` ★核心
- `SimpleMath+`
- `SimpleMath+`
- `easy imageSize`
- `SimpleMath+`
- `VHS_VideoCombine`
- `ModelSamplingSD3`
- `CLIPLoader`
- `easy showAnything`
- `CR Text Replace`
- `RH_Prompter`
- `TextBox`
- `DF_Integer`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `easy cleanGpuUsed`
- `TextBox`
- `easy showAnything`
- `EmptyImage`

## 关键参数

- `seed` = `disable`
- `steps` = `fixed`
- `cfg` = `20`
- `sampler_name` = `3.5`
- `scheduler` = `euler`
- `denoise` = `simple`

## 知识

覆盖率 **62%**（18/29）

**有卡**：`KSamplerAdvanced`、`VAEDecode`、`ModelSamplingSD3`、`VAELoader`、`EmptyHunyuanLatentVideo`、`UNETLoader`、`VHS_VideoCombine`、`CLIPLoader`、`RH_Prompter`、`TextBox`、`DF_Integer`、`CLIPTextEncode`、`EmptyImage`

**缺卡**（9）：`CR Text Replace`、`LayerUtility: PurgeVRAM`、`SimpleMath+`、`SimpleMath+`、`SimpleMath+`、`SimpleMath+`、`SimpleMath+`、`easy cleanGpuUsed`、`easy imageSize`

**用到的条目**：VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、UNETLoader、KSamplerAdvanced、EmptyHunyuanLatentVideo、RH_Prompter

## 学习发现

- 次要节点 `CR Text Replace` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: PurgeVRAM` 知识库中没有该节点类型的任何知识
- 次要节点 `SimpleMath+` 知识库中没有该节点类型的任何知识
- 次要节点 `SimpleMath+` 知识库中没有该节点类型的任何知识
- 次要节点 `SimpleMath+` 知识库中没有该节点类型的任何知识
- 次要节点 `SimpleMath+` 知识库中没有该节点类型的任何知识
- 次要节点 `SimpleMath+` 知识库中没有该节点类型的任何知识
- 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识
- 次要节点 `easy imageSize` 仅有 Resolution 的通用知识，没有该节点自己的说明

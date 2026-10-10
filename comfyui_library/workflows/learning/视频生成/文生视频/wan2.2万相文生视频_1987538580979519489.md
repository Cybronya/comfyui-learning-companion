---
key: 视频生成/文生视频/wan2.2万相文生视频_1987538580979519489.json
name: wan2.2万相文生视频_1987538580979519489
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/wan2.2万相文生视频_1987538580979519489.json
hash: 9b5fe6cb5bf312d6
coverage: 0.761905
learned_at: 2026-10-11 02:57:39
nodes: [easy int, CLIPLoader, CLIPTextEncode, KSamplerAdvanced, KSamplerAdvanced, CM_IntToFloat, SimpleMath+, VHS_VideoCombine, ModelSamplingSD3, ModelSamplingSD3, PathchSageAttentionKJ, PathchSageAttentionKJ, UNETLoader, UNETLoader, VAEDecode, VAELoader, easy int, CLIPTextEncode, EmptyHunyuanLatentVideo, easy int, easy int]
patterns: []
missing: [SimpleMath+, easy int, easy int, easy int, easy int]
parameters: {"cfg": 20, "denoise": "simple", "sampler_name": 3.5, "scheduler": "euler", "seed": "disable", "steps": "randomize"}
discoveries: [次要节点 `SimpleMath+` 知识库中没有该节点类型的任何知识, 次要节点 `easy int` 知识库中没有该节点类型的任何知识, 次要节点 `easy int` 知识库中没有该节点类型的任何知识, 次要节点 `easy int` 知识库中没有该节点类型的任何知识, 次要节点 `easy int` 知识库中没有该节点类型的任何知识]
---

# 视频生成/文生视频/wan2.2万相文生视频_1987538580979519489.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/wan2.2万相文生视频_1987538580979519489.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Other

**节点**（21 个）：
- `easy int`
- `CLIPLoader`
- `CLIPTextEncode` ★核心
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `CM_IntToFloat`
- `SimpleMath+`
- `VHS_VideoCombine`
- `ModelSamplingSD3`
- `ModelSamplingSD3`
- `PathchSageAttentionKJ`
- `PathchSageAttentionKJ`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `VAEDecode` ★核心
- `VAELoader`
- `easy int`
- `CLIPTextEncode` ★核心
- `EmptyHunyuanLatentVideo`
- `easy int`
- `easy int`

## 关键参数

- `seed` = `disable`
- `steps` = `randomize`
- `cfg` = `20`
- `sampler_name` = `3.5`
- `scheduler` = `euler`
- `denoise` = `simple`

## 知识

覆盖率 **76%**（16/21）

**有卡**：`CLIPLoader`、`CLIPTextEncode`、`KSamplerAdvanced`、`CM_IntToFloat`、`VHS_VideoCombine`、`ModelSamplingSD3`、`PathchSageAttentionKJ`、`UNETLoader`、`VAEDecode`、`VAELoader`、`EmptyHunyuanLatentVideo`

**缺卡**（5）：`SimpleMath+`、`easy int`、`easy int`、`easy int`、`easy int`

**用到的条目**：VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、UNETLoader、KSamplerAdvanced、EmptyHunyuanLatentVideo、CM_IntToFloat

## 学习发现

- 次要节点 `SimpleMath+` 知识库中没有该节点类型的任何知识
- 次要节点 `easy int` 知识库中没有该节点类型的任何知识
- 次要节点 `easy int` 知识库中没有该节点类型的任何知识
- 次要节点 `easy int` 知识库中没有该节点类型的任何知识
- 次要节点 `easy int` 知识库中没有该节点类型的任何知识

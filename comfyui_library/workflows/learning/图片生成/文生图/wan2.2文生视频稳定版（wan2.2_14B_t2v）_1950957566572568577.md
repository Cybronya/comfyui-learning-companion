---
key: 图片生成/文生图/wan2.2文生视频稳定版（wan2.2_14B_t2v）_1950957566572568577.json
name: wan2.2文生视频稳定版（wan2.2_14B_t2v）_1950957566572568577
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/wan2.2文生视频稳定版（wan2.2_14B_t2v）_1950957566572568577.json
hash: bc5e65a10ca2d964
coverage: 0.809524
learned_at: 2026-10-10 20:59:27
nodes: [MathExpression|pysssss, ModelSamplingSD3, ModelSamplingSD3, CLIPTextEncode, INTConstant, EmptyHunyuanLatentVideo, easy cleanGpuUsed, KSamplerAdvanced, VAEDecode, easy cleanGpuUsed, CreateVideo, KSamplerAdvanced, Note, INTConstant, INTConstant, CLIPTextEncode, UNETLoader, UNETLoader, CLIPLoader, VAELoader, SaveVideo]
patterns: []
missing: [MathExpression|pysssss, easy cleanGpuUsed, easy cleanGpuUsed]
parameters: {"cfg": 20, "denoise": "simple", "sampler_name": 3.5, "scheduler": "euler", "seed": "disable", "steps": "fixed"}
discoveries: [次要节点 `MathExpression|pysssss` 知识库中没有该节点类型的任何知识, 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识, 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识]
---

# 图片生成/文生图/wan2.2文生视频稳定版（wan2.2_14B_t2v）_1950957566572568577.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/wan2.2文生视频稳定版（wan2.2_14B_t2v）_1950957566572568577.json`

## 结构

**节点**（21 个）：
- `MathExpression|pysssss`
- `ModelSamplingSD3`
- `ModelSamplingSD3`
- `CLIPTextEncode`
- `INTConstant`
- `EmptyHunyuanLatentVideo`
- `easy cleanGpuUsed`
- `KSamplerAdvanced`
- `VAEDecode`
- `easy cleanGpuUsed`
- `CreateVideo`
- `KSamplerAdvanced`
- `Note`
- `INTConstant`
- `INTConstant`
- `CLIPTextEncode`
- `UNETLoader`
- `UNETLoader`
- `CLIPLoader`
- `VAELoader`
- `SaveVideo`

## 关键参数

- `cfg` = `20`
- `denoise` = `simple`
- `sampler_name` = `3.5`
- `scheduler` = `euler`
- `seed` = `disable`
- `steps` = `fixed`

## 知识

覆盖率 **81%**（17/21）

**有卡**：`MathExpression|pysssss`、`ModelSamplingSD3`、`CLIPTextEncode`、`INTConstant`、`EmptyHunyuanLatentVideo`、`easy cleanGpuUsed`、`KSamplerAdvanced`、`VAEDecode`、`CreateVideo`、`Note`、`UNETLoader`

**缺卡**（3）：`MathExpression|pysssss`、`easy cleanGpuUsed`、`easy cleanGpuUsed`

## 学习发现

- 次要节点 `MathExpression|pysssss` 知识库中没有该节点类型的任何知识
- 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识
- 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识

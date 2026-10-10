---
key: 视频生成/文生视频/文生视频wan2.2最新加速dyno_1972639381158862850.json
name: 文生视频wan2.2最新加速dyno_1972639381158862850
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/文生视频wan2.2最新加速dyno_1972639381158862850.json
hash: 939c48b65a6a05a2
coverage: 0.833333
learned_at: 2026-10-10 23:13:11
nodes: [VAEDecode, EmptyHunyuanLatentVideo, KSamplerAdvanced, KSamplerAdvanced, UNETLoader, UNETLoader, CLIPLoader, VAELoader, MarkdownNote, Note, Note, CLIPTextEncode, ModelSamplingSD3, LoraLoaderModelOnly, ModelSamplingSD3, CLIPTextEncode, SaveVideo, CreateVideo, Int, DF_Int_to_Float, MathExpression|pysssss, Int, Int, Int]
patterns: []
missing: [MathExpression|pysssss]
parameters: {"cfg": 4, "denoise": "simple", "sampler_name": 1, "scheduler": "euler", "seed": "disable", "steps": "fixed"}
discoveries: [次要节点 `MathExpression|pysssss` 知识库中没有该节点类型的任何知识]
---

# 视频生成/文生视频/文生视频wan2.2最新加速dyno_1972639381158862850.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/文生视频wan2.2最新加速dyno_1972639381158862850.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Output → Other

**节点**（24 个）：
- `VAEDecode` ★核心
- `EmptyHunyuanLatentVideo`
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `MarkdownNote`
- `Note`
- `Note`
- `CLIPTextEncode` ★核心
- `ModelSamplingSD3`
- `LoraLoaderModelOnly` ★核心
- `ModelSamplingSD3`
- `CLIPTextEncode` ★核心
- `SaveVideo`
- `CreateVideo`
- `Int`
- `DF_Int_to_Float`
- `MathExpression|pysssss`
- `Int`
- `Int`
- `Int`

## 关键参数

- `seed` = `disable`
- `steps` = `fixed`
- `cfg` = `4`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `simple`

## 知识

覆盖率 **83%**（20/24）

**有卡**：`VAEDecode`、`EmptyHunyuanLatentVideo`、`KSamplerAdvanced`、`UNETLoader`、`CLIPLoader`、`VAELoader`、`CLIPTextEncode`、`ModelSamplingSD3`、`LoraLoaderModelOnly`、`SaveVideo`、`CreateVideo`、`Int`、`DF_Int_to_Float`

**缺卡**（1）：`MathExpression|pysssss`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、UNETLoader、KSamplerAdvanced、EmptyHunyuanLatentVideo

## 学习发现

- 次要节点 `MathExpression|pysssss` 知识库中没有该节点类型的任何知识

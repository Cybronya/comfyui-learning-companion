---
key: 视频生成/文生视频/wan2.2 文生视频 (加速版)+ 提示词自动润色_1950000551498006530.json
name: wan2.2 文生视频 (加速版)+ 提示词自动润色_1950000551498006530
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/wan2.2 文生视频 (加速版)+ 提示词自动润色_1950000551498006530.json
hash: 5d8a2279a767820a
coverage: 0.804878
learned_at: 2026-10-15 22:47:34
nodes: [VAEDecode, RH_Translator, VAELoader, UNETLoader, UNETLoader, LoraLoaderModelOnly, PathchSageAttentionKJ, ModelSamplingSD3, LoraLoaderModelOnly, PathchSageAttentionKJ, ModelSamplingSD3, CLIPTextEncode, CLIPTextEncode, Note, Note, Note, Note, CLIPLoader, KSamplerAdvanced, KSamplerAdvanced, PrimitiveBoolean, Note, INTConstant, INTConstant, SimpleMath+, VHS_VideoCombine, EmptyHunyuanLatentVideo, MathExpression|pysssss, MathExpression|pysssss, ShowText|pysssss, DF_Integer, DF_Integer, MathExpression|pysssss, MathExpression|pysssss, DF_Integer, CR Text Concatenate, CR Text, RH_Prompter, easy ifElse, ShowText|pysssss, Text Multiline]
patterns: []
missing: []
parameters: {"cfg": 8, "denoise": "simple", "sampler_name": 3.5, "scheduler": "euler", "seed": "disable", "steps": "fixed"}
---

# 视频生成/文生视频/wan2.2 文生视频 (加速版)+ 提示词自动润色_1950000551498006530.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/wan2.2 文生视频 (加速版)+ 提示词自动润色_1950000551498006530.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Other

**节点**（41 个）：
- `VAEDecode` ★核心
- `RH_Translator`
- `VAELoader`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `PathchSageAttentionKJ`
- `ModelSamplingSD3`
- `LoraLoaderModelOnly` ★核心
- `PathchSageAttentionKJ`
- `ModelSamplingSD3`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `Note`
- `Note`
- `Note`
- `Note`
- `CLIPLoader`
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `PrimitiveBoolean`
- `Note`
- `INTConstant`
- `INTConstant`
- `SimpleMath+`
- `VHS_VideoCombine`
- `EmptyHunyuanLatentVideo`
- `MathExpression|pysssss`
- `MathExpression|pysssss`
- `ShowText|pysssss`
- `DF_Integer`
- `DF_Integer`
- `MathExpression|pysssss`
- `MathExpression|pysssss`
- `DF_Integer`
- `CR Text Concatenate`
- `CR Text`
- `RH_Prompter`
- `easy ifElse`
- `ShowText|pysssss`
- `Text Multiline`

## 关键参数

- `seed` = `disable`
- `steps` = `fixed`
- `cfg` = `8`
- `sampler_name` = `3.5`
- `scheduler` = `euler`
- `denoise` = `simple`

## 知识

覆盖率 **80%**（33/41）

**有卡**：`VAEDecode`、`RH_Translator`、`VAELoader`、`UNETLoader`、`LoraLoaderModelOnly`、`PathchSageAttentionKJ`、`ModelSamplingSD3`、`CLIPTextEncode`、`CLIPLoader`、`KSamplerAdvanced`、`PrimitiveBoolean`、`INTConstant`、`SimpleMath+`、`VHS_VideoCombine`、`EmptyHunyuanLatentVideo`、`MathExpression|pysssss`、`DF_Integer`、`CR Text Concatenate`、`CR Text`、`RH_Prompter`、`Text Multiline`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、UNETLoader、KSamplerAdvanced、EmptyHunyuanLatentVideo

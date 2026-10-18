---
key: 视频生成/文生视频/wan2.2文生视频（kj模型加速版）_1949875835437236226.json
name: wan2.2文生视频（kj模型加速版）_1949875835437236226.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/wan2.2文生视频（kj模型加速版）_1949875835437236226.json
hash: a7da193954efc6a1
coverage: 1
learned_at: 2026-10-15 22:43:33
nodes: [VAEDecode, LoraLoaderModelOnly, PathchSageAttentionKJ, ModelSamplingSD3, CLIPLoader, VAELoader, LoraLoaderModelOnly, PathchSageAttentionKJ, ModelSamplingSD3, CreateVideo, SaveVideo, KSamplerAdvanced, UNETLoader, UNETLoader, CLIPTextEncode, Int, Int, Int, MathExpression|pysssss, CLIPTextEncode, EmptyHunyuanLatentVideo, KSamplerAdvanced]
patterns: []
missing: []
parameters: {"cfg": 8, "denoise": "simple", "sampler_name": 1, "scheduler": "uni_pc", "seed": "disable", "steps": "randomize"}
---

# 视频生成/文生视频/wan2.2文生视频（kj模型加速版）_1949875835437236226.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/1949875835437236226.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Output → Other

**节点**（22 个）：
- `VAEDecode` ★核心
- `LoraLoaderModelOnly` ★核心
- `PathchSageAttentionKJ`
- `ModelSamplingSD3`
- `CLIPLoader`
- `VAELoader`
- `LoraLoaderModelOnly` ★核心
- `PathchSageAttentionKJ`
- `ModelSamplingSD3`
- `CreateVideo`
- `SaveVideo`
- `KSamplerAdvanced` ★核心
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `CLIPTextEncode` ★核心
- `Int`
- `Int`
- `Int`
- `MathExpression|pysssss`
- `CLIPTextEncode` ★核心
- `EmptyHunyuanLatentVideo`
- `KSamplerAdvanced` ★核心

## 关键参数

- `seed` = `disable`
- `steps` = `randomize`
- `cfg` = `8`
- `sampler_name` = `1`
- `scheduler` = `uni_pc`
- `denoise` = `simple`

## 知识

覆盖率 **100%**（22/22）

**有卡**：`VAEDecode`、`LoraLoaderModelOnly`、`PathchSageAttentionKJ`、`ModelSamplingSD3`、`CLIPLoader`、`VAELoader`、`CreateVideo`、`SaveVideo`、`KSamplerAdvanced`、`UNETLoader`、`CLIPTextEncode`、`Int`、`MathExpression|pysssss`、`EmptyHunyuanLatentVideo`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、UNETLoader、KSamplerAdvanced、EmptyHunyuanLatentVideo

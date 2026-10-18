---
key: 视频生成/图生视频/wan2.2图生视频（kj模型加速版）_1950053385758269442.json
name: wan2.2图生视频（kj模型加速版）_1950053385758269442.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/wan2.2图生视频（kj模型加速版）_1950053385758269442.json
hash: 9ed2cb17b00d1f06
coverage: 1
learned_at: 2026-10-15 22:30:52
nodes: [VAEDecode, PathchSageAttentionKJ, ModelSamplingSD3, CLIPLoader, LoraLoaderModelOnly, PathchSageAttentionKJ, ModelSamplingSD3, CreateVideo, SaveVideo, KSamplerAdvanced, CLIPTextEncode, VAELoader, MathExpression|pysssss, Int, Int, LoadImage, Int, CLIPTextEncode, UNETLoader, WanImageToVideo, UNETLoader, KSamplerAdvanced, LoraLoaderModelOnly]
patterns: []
missing: []
parameters: {"cfg": 8, "denoise": "simple", "sampler_name": 1, "scheduler": "uni_pc", "seed": "disable", "steps": "randomize"}
---

# 视频生成/图生视频/wan2.2图生视频（kj模型加速版）_1950053385758269442.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1950053385758269442.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Output → Other

**节点**（23 个）：
- `VAEDecode` ★核心
- `PathchSageAttentionKJ`
- `ModelSamplingSD3`
- `CLIPLoader`
- `LoraLoaderModelOnly` ★核心
- `PathchSageAttentionKJ`
- `ModelSamplingSD3`
- `CreateVideo`
- `SaveVideo`
- `KSamplerAdvanced` ★核心
- `CLIPTextEncode` ★核心
- `VAELoader`
- `MathExpression|pysssss`
- `Int`
- `Int`
- `LoadImage`
- `Int`
- `CLIPTextEncode` ★核心
- `UNETLoader` ★核心
- `WanImageToVideo`
- `UNETLoader` ★核心
- `KSamplerAdvanced` ★核心
- `LoraLoaderModelOnly` ★核心

## 关键参数

- `seed` = `disable`
- `steps` = `randomize`
- `cfg` = `8`
- `sampler_name` = `1`
- `scheduler` = `uni_pc`
- `denoise` = `simple`

## 知识

覆盖率 **100%**（23/23）

**有卡**：`VAEDecode`、`PathchSageAttentionKJ`、`ModelSamplingSD3`、`CLIPLoader`、`LoraLoaderModelOnly`、`CreateVideo`、`SaveVideo`、`KSamplerAdvanced`、`CLIPTextEncode`、`VAELoader`、`MathExpression|pysssss`、`Int`、`LoadImage`、`UNETLoader`、`WanImageToVideo`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerAdvanced

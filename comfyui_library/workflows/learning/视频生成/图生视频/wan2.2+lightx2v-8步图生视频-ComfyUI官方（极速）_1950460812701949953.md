---
key: 视频生成/图生视频/wan2.2+lightx2v-8步图生视频-ComfyUI官方（极速）_1950460812701949953.json
name: wan2.2+lightx2v-8步图生视频-ComfyUI官方（极速）_1950460812701949953.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1950460812701949953.json
hash: 6c4a34cad006ffdb
coverage: 0.892857
learned_at: 2026-10-15 22:30:55
nodes: [CLIPTextEncode, WanImageToVideo, VAEDecode, ImageResizeKJv2, UNETLoader, VAELoader, LoraLoaderModelOnly, PathchSageAttentionKJ, Note, Note, Note, CLIPLoader, LoraLoaderModelOnly, UNETLoader, PathchSageAttentionKJ, ModelSamplingSD3, ModelSamplingSD3, CLIPTextEncode, CreateVideo, KSamplerAdvanced, KSamplerAdvanced, Primitive integer [Crystools], MathExpression|pysssss, LoadImage, Text Multiline, Primitive integer [Crystools], Primitive integer [Crystools], SaveVideo]
patterns: []
missing: []
parameters: {"cfg": 8, "denoise": "simple", "sampler_name": 1, "scheduler": "uni_pc", "seed": "enable", "steps": "randomize"}
---

# 视频生成/图生视频/wan2.2+lightx2v-8步图生视频-ComfyUI官方（极速）_1950460812701949953.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1950460812701949953.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（28 个）：
- `CLIPTextEncode` ★核心
- `WanImageToVideo`
- `VAEDecode` ★核心
- `ImageResizeKJv2`
- `UNETLoader` ★核心
- `VAELoader`
- `LoraLoaderModelOnly` ★核心
- `PathchSageAttentionKJ`
- `Note`
- `Note`
- `Note`
- `CLIPLoader`
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `PathchSageAttentionKJ`
- `ModelSamplingSD3`
- `ModelSamplingSD3`
- `CLIPTextEncode` ★核心
- `CreateVideo`
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `Primitive integer [Crystools]`
- `MathExpression|pysssss`
- `LoadImage`
- `Text Multiline`
- `Primitive integer [Crystools]`
- `Primitive integer [Crystools]`
- `SaveVideo`

## 关键参数

- `seed` = `enable`
- `steps` = `randomize`
- `cfg` = `8`
- `sampler_name` = `1`
- `scheduler` = `uni_pc`
- `denoise` = `simple`

## 知识

覆盖率 **89%**（25/28）

**有卡**：`CLIPTextEncode`、`WanImageToVideo`、`VAEDecode`、`ImageResizeKJv2`、`UNETLoader`、`VAELoader`、`LoraLoaderModelOnly`、`PathchSageAttentionKJ`、`CLIPLoader`、`ModelSamplingSD3`、`CreateVideo`、`KSamplerAdvanced`、`Primitive integer [Crystools]`、`MathExpression|pysssss`、`LoadImage`、`Text Multiline`、`SaveVideo`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerAdvanced

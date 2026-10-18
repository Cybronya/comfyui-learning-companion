---
key: 视频生成/图生视频/wan2.2+lightx2v-4步图生视频-ComfyUI官方_1950054777926369282.json
name: wan2.2+lightx2v-4步图生视频-ComfyUI官方_1950054777926369282.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/wan2.2+lightx2v-4步图生视频-ComfyUI官方_1950054777926369282.json
hash: 40f5dbd2f47b9286
coverage: 1
learned_at: 2026-10-15 22:30:52
nodes: [ModelSamplingSD3, MathExpression|pysssss, Primitive integer [Crystools], Primitive integer [Crystools], Primitive integer [Crystools], Text Multiline, ImageResizeKJv2, WanImageToVideo, CLIPLoader, VAELoader, CLIPTextEncode, CLIPTextEncode, ModelSamplingSD3, VAEDecode, CreateVideo, LoraLoaderModelOnly, UNETLoader, UNETLoader, LoadImage, KSamplerAdvanced, KSamplerAdvanced, SaveVideo, PathchSageAttentionKJ, PathchSageAttentionKJ, LoraLoaderModelOnly]
patterns: []
missing: []
parameters: {"cfg": 4, "denoise": "simple", "sampler_name": 1, "scheduler": "lcm", "seed": "disable", "steps": "fixed"}
---

# 视频生成/图生视频/wan2.2+lightx2v-4步图生视频-ComfyUI官方_1950054777926369282.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1950054777926369282.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（25 个）：
- `ModelSamplingSD3`
- `MathExpression|pysssss`
- `Primitive integer [Crystools]`
- `Primitive integer [Crystools]`
- `Primitive integer [Crystools]`
- `Text Multiline`
- `ImageResizeKJv2`
- `WanImageToVideo`
- `CLIPLoader`
- `VAELoader`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `ModelSamplingSD3`
- `VAEDecode` ★核心
- `CreateVideo`
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `LoadImage`
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `SaveVideo`
- `PathchSageAttentionKJ`
- `PathchSageAttentionKJ`
- `LoraLoaderModelOnly` ★核心

## 关键参数

- `seed` = `disable`
- `steps` = `fixed`
- `cfg` = `4`
- `sampler_name` = `1`
- `scheduler` = `lcm`
- `denoise` = `simple`

## 知识

覆盖率 **100%**（25/25）

**有卡**：`ModelSamplingSD3`、`MathExpression|pysssss`、`Primitive integer [Crystools]`、`Text Multiline`、`ImageResizeKJv2`、`WanImageToVideo`、`CLIPLoader`、`VAELoader`、`CLIPTextEncode`、`VAEDecode`、`CreateVideo`、`LoraLoaderModelOnly`、`UNETLoader`、`LoadImage`、`KSamplerAdvanced`、`SaveVideo`、`PathchSageAttentionKJ`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerAdvanced

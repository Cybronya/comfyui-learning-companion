---
key: 视频生成/图生视频/wan2.2+lightx2v-4步图生视频-ComfyUI官方_1949988822005235714.json
name: wan2.2+lightx2v-4步图生视频-ComfyUI官方_1949988822005235714.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1949988822005235714.json
hash: 43826d81ee19dca6
coverage: 0.892857
learned_at: 2026-10-15 22:30:50
nodes: [SaveVideo, CLIPTextEncode, CLIPTextEncode, CLIPLoader, WanImageToVideo, VAEDecode, CreateVideo, Primitive integer [Crystools], Primitive integer [Crystools], ImageResizeKJv2, Note, Note, Note, Primitive integer [Crystools], MathExpression|pysssss, UNETLoader, ModelSamplingSD3, VAELoader, LoraLoaderModelOnly, ModelSamplingSD3, UNETLoader, LoraLoaderModelOnly, PathchSageAttentionKJ, PathchSageAttentionKJ, LoadImage, Text Multiline, KSamplerAdvanced, KSamplerAdvanced]
patterns: []
missing: []
parameters: {"cfg": 4, "denoise": "simple", "sampler_name": 1, "scheduler": "lcm", "seed": "disable", "steps": "fixed"}
---

# 视频生成/图生视频/wan2.2+lightx2v-4步图生视频-ComfyUI官方_1949988822005235714.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1949988822005235714.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（28 个）：
- `SaveVideo`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `CLIPLoader`
- `WanImageToVideo`
- `VAEDecode` ★核心
- `CreateVideo`
- `Primitive integer [Crystools]`
- `Primitive integer [Crystools]`
- `ImageResizeKJv2`
- `Note`
- `Note`
- `Note`
- `Primitive integer [Crystools]`
- `MathExpression|pysssss`
- `UNETLoader` ★核心
- `ModelSamplingSD3`
- `VAELoader`
- `LoraLoaderModelOnly` ★核心
- `ModelSamplingSD3`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `PathchSageAttentionKJ`
- `PathchSageAttentionKJ`
- `LoadImage`
- `Text Multiline`
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心

## 关键参数

- `seed` = `disable`
- `steps` = `fixed`
- `cfg` = `4`
- `sampler_name` = `1`
- `scheduler` = `lcm`
- `denoise` = `simple`

## 知识

覆盖率 **89%**（25/28）

**有卡**：`SaveVideo`、`CLIPTextEncode`、`CLIPLoader`、`WanImageToVideo`、`VAEDecode`、`CreateVideo`、`Primitive integer [Crystools]`、`ImageResizeKJv2`、`MathExpression|pysssss`、`UNETLoader`、`ModelSamplingSD3`、`VAELoader`、`LoraLoaderModelOnly`、`PathchSageAttentionKJ`、`LoadImage`、`Text Multiline`、`KSamplerAdvanced`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerAdvanced

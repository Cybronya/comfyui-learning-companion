---
key: 图片生成/图生图/Wan2.2 写实美女（图生图）_1993170303243190274.json
name: Wan2.2 写实美女（图生图）_1993170303243190274
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Wan2.2 写实美女（图生图）_1993170303243190274.json
hash: 3ef7c6b96c87217c
coverage: 0.888889
learned_at: 2026-10-23 11:28:02
nodes: [Anything Everywhere, CLIPLoader, VAELoader, Anything Everywhere, CLIPTextEncode, CLIPTextEncode, Note, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, PathchSageAttentionKJ, easy cleanGpuUsed, LoraLoaderModelOnly, PathchSageAttentionKJ, easy cleanGpuUsed, UNETLoader, LoraLoaderModelOnly, KSamplerAdvanced, VAEEncode, KSamplerAdvanced, VAEDecode, ImageCASharpening+, ColorCorrectOfUtils, ImageScale, RHHiddenNodes, LoadImage, SaveImage]
patterns: []
missing: []
parameters: {"cfg": 16, "denoise": "bong_tangent", "sampler_name": 2, "scheduler": "euler", "seed": "disable", "steps": "randomize"}
---

# 图片生成/图生图/Wan2.2 写实美女（图生图）_1993170303243190274.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Wan2.2 写实美女（图生图）_1993170303243190274.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（27 个）：
- `Anything Everywhere`
- `CLIPLoader`
- `VAELoader`
- `Anything Everywhere`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `Note`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `PathchSageAttentionKJ`
- `easy cleanGpuUsed`
- `LoraLoaderModelOnly` ★核心
- `PathchSageAttentionKJ`
- `easy cleanGpuUsed`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `KSamplerAdvanced` ★核心
- `VAEEncode` ★核心
- `KSamplerAdvanced` ★核心
- `VAEDecode` ★核心
- `ImageCASharpening+`
- `ColorCorrectOfUtils`
- `ImageScale`
- `RHHiddenNodes`
- `LoadImage`
- `SaveImage`

## 关键参数

- `seed` = `disable`
- `steps` = `randomize`
- `cfg` = `16`
- `sampler_name` = `2`
- `scheduler` = `euler`
- `denoise` = `bong_tangent`

## 知识

覆盖率 **89%**（24/27）

**有卡**：`CLIPLoader`、`VAELoader`、`CLIPTextEncode`、`UNETLoader`、`LoraLoaderModelOnly`、`PathchSageAttentionKJ`、`easy cleanGpuUsed`、`KSamplerAdvanced`、`VAEEncode`、`VAEDecode`、`ImageCASharpening+`、`ColorCorrectOfUtils`、`ImageScale`、`RHHiddenNodes`、`LoadImage`、`SaveImage`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerAdvanced

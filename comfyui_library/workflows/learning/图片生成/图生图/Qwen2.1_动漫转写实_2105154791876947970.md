---
key: 图片生成/图生图/Qwen2.1_动漫转写实_2105154791876947970.json
name: Qwen2.1_动漫转写实_2105154791876947970
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen2.1_动漫转写实_2105154791876947970.json
hash: d0eb3125b99a2ea9
coverage: 0.75
learned_at: 2026-10-21 00:43:36
nodes: [QwenImage21Cache, UNETLoader, CLIPLoader, VAELoader, PrimitiveInt, TextEncodeQwenImage21, KSampler, VAEDecode, PlaySound|pysssss, SaveImage, LoadImage, Image Comparer (rgthree), PrimitiveStringMultiline, MarkdownNote, Label (rgthree), LoraLoaderModelOnly]
patterns: []
missing: []
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 727168274598936, "steps": 40}
---

# 图片生成/图生图/Qwen2.1_动漫转写实_2105154791876947970.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen2.1_动漫转写实_2105154791876947970.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Output → Other

**节点**（16 个）：
- `QwenImage21Cache`
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `PrimitiveInt`
- `TextEncodeQwenImage21`
- `KSampler` ★核心
- `VAEDecode` ★核心
- `PlaySound|pysssss`
- `SaveImage`
- `LoadImage`
- `Image Comparer (rgthree)`
- `PrimitiveStringMultiline`
- `MarkdownNote`
- `Label (rgthree)`
- `LoraLoaderModelOnly` ★核心

## 关键参数

- `seed` = `727168274598936`
- `steps` = `40`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **75%**（12/16）

**有卡**：`QwenImage21Cache`、`UNETLoader`、`CLIPLoader`、`VAELoader`、`TextEncodeQwenImage21`、`KSampler`、`VAEDecode`、`PlaySound|pysssss`、`SaveImage`、`LoadImage`、`Label (rgthree)`、`LoraLoaderModelOnly`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、CLIPLoader、LoadImage、QwenImage21Cache

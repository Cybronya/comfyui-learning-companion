---
key: 图片生成/图生图/Qwen Image 2.1 Fix修复图像编辑_2103711535771250690.json
name: Qwen Image 2.1 Fix修复图像编辑_2103711535771250690
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen Image 2.1 Fix修复图像编辑_2103711535771250690.json
hash: cb273c2daeb2ffdf
coverage: 0.857143
learned_at: 2026-10-21 00:42:05
nodes: [MarkdownNote, MarkdownNote, JWDatetimeString, FreSca, EmptyLatentImage, easy showAnything, LoadImage, VAEDecode, APG, QwenPERewriteT8, CR Prompt Text, UNETLoader, CLIPLoader, VAELoader, SeedNode, ResolutionSelector, LoraLoaderModelOnly, TextEncodeQwenImage21, LoadImage, SaveImage, KSampler]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 3, "denoise": 1, "height": 1600, "sampler_name": "seeds_2", "scheduler": "sgm_uniform", "seed": 53, "steps": 40, "width": 1200}
---

# 图片生成/图生图/Qwen Image 2.1 Fix修复图像编辑_2103711535771250690.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen Image 2.1 Fix修复图像编辑_2103711535771250690.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（21 个）：
- `MarkdownNote`
- `MarkdownNote`
- `JWDatetimeString`
- `FreSca`
- `EmptyLatentImage` ★核心
- `easy showAnything`
- `LoadImage`
- `VAEDecode` ★核心
- `APG`
- `QwenPERewriteT8`
- `CR Prompt Text`
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `SeedNode`
- `ResolutionSelector`
- `LoraLoaderModelOnly` ★核心
- `TextEncodeQwenImage21`
- `LoadImage`
- `SaveImage`
- `KSampler` ★核心

## 关键参数

- `width` = `1200`
- `height` = `1600`
- `batch_size` = `1`
- `seed` = `53`
- `steps` = `40`
- `cfg` = `3`
- `sampler_name` = `seeds_2`
- `scheduler` = `sgm_uniform`
- `denoise` = `1`

## 知识

覆盖率 **86%**（18/21）

**有卡**：`JWDatetimeString`、`FreSca`、`EmptyLatentImage`、`LoadImage`、`VAEDecode`、`APG`、`QwenPERewriteT8`、`CR Prompt Text`、`UNETLoader`、`CLIPLoader`、`VAELoader`、`SeedNode`、`ResolutionSelector`、`LoraLoaderModelOnly`、`TextEncodeQwenImage21`、`SaveImage`、`KSampler`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、CLIPLoader、EmptyLatentImage、ResolutionSelector

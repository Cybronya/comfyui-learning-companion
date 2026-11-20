---
key: 图片生成/文生图/Qwen+Image+2.1 PE  文生图+图像编辑_两用_2116426276004261889.json
name: Qwen+Image+2.1 PE  文生图+图像编辑_两用_2116426276004261889
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Qwen+Image+2.1 PE  文生图+图像编辑_两用_2116426276004261889.json
hash: 03c6beefab927bf9
coverage: 0.72
learned_at: 2026-11-02 19:15:48
nodes: [LoadImage, LoadImage, LoadImage, LoadImage, KSampler, CLIPLoader, ComfySwitchNode, UNETLoader, easy showAnything, QwenImage21Cache, VAEDecode, VAELoader, easy cleanGpuUsed, SaveImage, 孤海注释, EmptyLatentImage, 孤海注释, ResolutionSelector, Note, 孤海注释, Int, TextEncodeQwenImage21, QwenPERewriteT8, MarkdownNote, CR Prompt Text]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 318294014446432, "steps": 40, "width": 1024}
---

# 图片生成/文生图/Qwen+Image+2.1 PE  文生图+图像编辑_两用_2116426276004261889.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Qwen+Image+2.1 PE  文生图+图像编辑_两用_2116426276004261889.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（25 个）：
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `KSampler` ★核心
- `CLIPLoader`
- `ComfySwitchNode`
- `UNETLoader` ★核心
- `easy showAnything`
- `QwenImage21Cache`
- `VAEDecode` ★核心
- `VAELoader`
- `easy cleanGpuUsed`
- `SaveImage`
- `孤海注释`
- `EmptyLatentImage` ★核心
- `孤海注释`
- `ResolutionSelector`
- `Note`
- `孤海注释`
- `Int`
- `TextEncodeQwenImage21`
- `QwenPERewriteT8`
- `MarkdownNote`
- `CR Prompt Text`

## 关键参数

- `seed` = `318294014446432`
- `steps` = `40`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`
- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`

## 知识

覆盖率 **72%**（18/25）

**有卡**：`LoadImage`、`KSampler`、`CLIPLoader`、`UNETLoader`、`QwenImage21Cache`、`VAEDecode`、`VAELoader`、`easy cleanGpuUsed`、`SaveImage`、`EmptyLatentImage`、`ResolutionSelector`、`Int`、`TextEncodeQwenImage21`、`QwenPERewriteT8`、`CR Prompt Text`

**用到的条目**：KSampler、TextEncodeQwenImage21、VAEDecode、VAELoader、CLIPLoader、EmptyLatentImage、ResolutionSelector、LoadImage

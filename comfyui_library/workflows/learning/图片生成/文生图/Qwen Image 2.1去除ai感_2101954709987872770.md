---
key: 图片生成/文生图/Qwen Image 2.1去除ai感_2101954709987872770.json
name: Qwen Image 2.1去除ai感_2101954709987872770
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Qwen Image 2.1去除ai感_2101954709987872770.json
hash: 8454b23afb68dd6a
coverage: 0.823529
learned_at: 2026-10-20 01:50:55
nodes: [MarkdownNote, CLIPLoader, VAELoader, UNETLoader, LoadImage, ResolutionSelector, QwenImage21Cache, ComfySwitchNode, EmptyLatentImage, VAEDecode, ImageStitch, KSampler, SaveImage, Note, TextEncodeQwenImage21, SaveImage, LoraLoaderModelOnly]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 279407165180065, "steps": 25, "width": 1024}
---

# 图片生成/文生图/Qwen Image 2.1去除ai感_2101954709987872770.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Qwen Image 2.1去除ai感_2101954709987872770.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（17 个）：
- `MarkdownNote`
- `CLIPLoader`
- `VAELoader`
- `UNETLoader` ★核心
- `LoadImage`
- `ResolutionSelector`
- `QwenImage21Cache`
- `ComfySwitchNode`
- `EmptyLatentImage` ★核心
- `VAEDecode` ★核心
- `ImageStitch`
- `KSampler` ★核心
- `SaveImage`
- `Note`
- `TextEncodeQwenImage21`
- `SaveImage`
- `LoraLoaderModelOnly` ★核心

## 关键参数

- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`
- `seed` = `279407165180065`
- `steps` = `25`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **82%**（14/17）

**有卡**：`CLIPLoader`、`VAELoader`、`UNETLoader`、`LoadImage`、`ResolutionSelector`、`QwenImage21Cache`、`EmptyLatentImage`、`VAEDecode`、`ImageStitch`、`KSampler`、`SaveImage`、`TextEncodeQwenImage21`、`LoraLoaderModelOnly`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、CLIPLoader、EmptyLatentImage、ResolutionSelector

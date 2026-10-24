---
key: 图片生成/图生图/Qwen Image 2.1 Turbo 人物角色替换_2108901380495859713.json
name: Qwen Image 2.1 Turbo 人物角色替换_2108901380495859713
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen Image 2.1 Turbo 人物角色替换_2108901380495859713.json
hash: ccaf1955325a453d
coverage: 0.764706
learned_at: 2026-10-23 11:12:35
nodes: [UNETLoader, Note, MarkdownNote, Image Comparer (rgthree), ResolutionSelector, EmptyLatentImage, QwenImage21Cache, KSampler, VAEDecode, ComfySwitchNode, LoraLoaderModelOnly, SaveImage, LoadImage, LoadImage, CLIPLoader, VAELoader, TextEncodeQwenImage21]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 452003132594248, "steps": 25, "width": 1024}
---

# 图片生成/图生图/Qwen Image 2.1 Turbo 人物角色替换_2108901380495859713.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen Image 2.1 Turbo 人物角色替换_2108901380495859713.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（17 个）：
- `UNETLoader` ★核心
- `Note`
- `MarkdownNote`
- `Image Comparer (rgthree)`
- `ResolutionSelector`
- `EmptyLatentImage` ★核心
- `QwenImage21Cache`
- `KSampler` ★核心
- `VAEDecode` ★核心
- `ComfySwitchNode`
- `LoraLoaderModelOnly` ★核心
- `SaveImage`
- `LoadImage`
- `LoadImage`
- `CLIPLoader`
- `VAELoader`
- `TextEncodeQwenImage21`

## 关键参数

- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`
- `seed` = `452003132594248`
- `steps` = `25`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **76%**（13/17）

**有卡**：`UNETLoader`、`ResolutionSelector`、`EmptyLatentImage`、`QwenImage21Cache`、`KSampler`、`VAEDecode`、`LoraLoaderModelOnly`、`SaveImage`、`LoadImage`、`CLIPLoader`、`VAELoader`、`TextEncodeQwenImage21`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、CLIPLoader、EmptyLatentImage、ResolutionSelector

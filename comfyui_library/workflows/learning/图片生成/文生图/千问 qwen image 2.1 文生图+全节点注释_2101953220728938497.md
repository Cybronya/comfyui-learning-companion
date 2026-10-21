---
key: 图片生成/文生图/千问 qwen image 2.1 文生图+全节点注释_2101953220728938497.json
name: 千问 qwen image 2.1 文生图+全节点注释_2101953220728938497
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/千问 qwen image 2.1 文生图+全节点注释_2101953220728938497.json
hash: f5330a712fa48e9b
coverage: 0.5
learned_at: 2026-10-20 01:52:19
nodes: [VAEDecode, EmptyLatentImage, Seed (rgthree), KSampler, ResolutionSelector, UNETLoader, QwenImage21Cache, VAELoader, Anything Everywhere3, CLIPLoader, CLIPLoader, CR Text, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, LoadImage, LoadImage, TextEncodeQwenImage21, TextGenerateLTX2Prompt, CR Prompt Text, Note, Note, Note, SaveImage, Note]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 233778341783997, "steps": 40, "width": 1024}
---

# 图片生成/文生图/千问 qwen image 2.1 文生图+全节点注释_2101953220728938497.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/千问 qwen image 2.1 文生图+全节点注释_2101953220728938497.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（34 个）：
- `VAEDecode` ★核心
- `EmptyLatentImage` ★核心
- `Seed (rgthree)`
- `KSampler` ★核心
- `ResolutionSelector`
- `UNETLoader` ★核心
- `QwenImage21Cache`
- `VAELoader`
- `Anything Everywhere3`
- `CLIPLoader`
- `CLIPLoader`
- `CR Text`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `LoadImage`
- `LoadImage`
- `TextEncodeQwenImage21`
- `TextGenerateLTX2Prompt`
- `CR Prompt Text`
- `Note`
- `Note`
- `Note`
- `SaveImage`
- `Note`

## 关键参数

- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`
- `seed` = `233778341783997`
- `steps` = `40`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **50%**（17/34）

**有卡**：`VAEDecode`、`EmptyLatentImage`、`Seed (rgthree)`、`KSampler`、`ResolutionSelector`、`UNETLoader`、`QwenImage21Cache`、`VAELoader`、`CLIPLoader`、`CR Text`、`LoadImage`、`TextEncodeQwenImage21`、`TextGenerateLTX2Prompt`、`CR Prompt Text`、`SaveImage`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、EmptyLatentImage、ResolutionSelector、LoadImage

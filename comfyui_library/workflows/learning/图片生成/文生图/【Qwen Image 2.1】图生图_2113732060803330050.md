---
key: 图片生成/文生图/【Qwen Image 2.1】图生图_2113732060803330050.json
name: 【Qwen Image 2.1】图生图_2113732060803330050
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/【Qwen Image 2.1】图生图_2113732060803330050.json
hash: 0fd3b77970a01253
coverage: 0.727273
learned_at: 2026-10-26 22:09:18
nodes: [easy setNode, VAEDecode, TextEncodeQwenImage21, EmptyLatentImage, Seed (rgthree), KSampler, SaveImage, CR Prompt Text, ResolutionSelector, TextGenerateLTX2Prompt, easy showAnything, UNETLoader, QwenImage21Cache, VAELoader, Anything Everywhere3, SetNode, SetNode, GetNode, CLIPLoader, CLIPLoader, CLIPLoader, Fast Groups Bypasser (rgthree)]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 1024811089150458, "steps": 40, "width": 1024}
---

# 图片生成/文生图/【Qwen Image 2.1】图生图_2113732060803330050.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/【Qwen Image 2.1】图生图_2113732060803330050.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（22 个）：
- `easy setNode`
- `VAEDecode` ★核心
- `TextEncodeQwenImage21`
- `EmptyLatentImage` ★核心
- `Seed (rgthree)`
- `KSampler` ★核心
- `SaveImage`
- `CR Prompt Text`
- `ResolutionSelector`
- `TextGenerateLTX2Prompt`
- `easy showAnything`
- `UNETLoader` ★核心
- `QwenImage21Cache`
- `VAELoader`
- `Anything Everywhere3`
- `SetNode`
- `SetNode`
- `GetNode`
- `CLIPLoader`
- `CLIPLoader`
- `CLIPLoader`
- `Fast Groups Bypasser (rgthree)`

## 关键参数

- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`
- `seed` = `1024811089150458`
- `steps` = `40`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **73%**（16/22）

**有卡**：`easy setNode`、`VAEDecode`、`TextEncodeQwenImage21`、`EmptyLatentImage`、`Seed (rgthree)`、`KSampler`、`SaveImage`、`CR Prompt Text`、`ResolutionSelector`、`TextGenerateLTX2Prompt`、`UNETLoader`、`QwenImage21Cache`、`VAELoader`、`CLIPLoader`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、EmptyLatentImage、ResolutionSelector、QwenImage21Cache

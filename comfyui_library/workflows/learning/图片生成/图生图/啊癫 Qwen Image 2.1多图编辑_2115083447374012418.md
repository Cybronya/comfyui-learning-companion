---
key: 图片生成/图生图/啊癫 Qwen Image 2.1多图编辑_2115083447374012418.json
name: 啊癫 Qwen Image 2.1多图编辑_2115083447374012418
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/啊癫 Qwen Image 2.1多图编辑_2115083447374012418.json
hash: 3cc79bc9c945573c
coverage: 0.709677
learned_at: 2026-10-30 17:52:59
nodes: [easy setNode, VAEDecode, SaveImage, UNETLoader, QwenImage21Cache, VAELoader, Anything Everywhere3, SetNode, SetNode, BatchImagesNode, Note, Fast Groups Bypasser (rgthree), TextEncodeQwenImage21, LoadImage, LoadImage, LoadImage, GetNode, ResolutionSelector, EmptyLatentImage, ComfySwitchNode, LoadImage, LoadImage, Fast Groups Bypasser (rgthree), PreviewAny, TextGenerateLTX2Prompt, LoadImage, KSampler, CR Prompt Text, CLIPLoader, CLIPLoader, CLIPLoader]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 259927290205888, "steps": 40, "width": 1024}
---

# 图片生成/图生图/啊癫 Qwen Image 2.1多图编辑_2115083447374012418.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/啊癫 Qwen Image 2.1多图编辑_2115083447374012418.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（31 个）：
- `easy setNode`
- `VAEDecode` ★核心
- `SaveImage`
- `UNETLoader` ★核心
- `QwenImage21Cache`
- `VAELoader`
- `Anything Everywhere3`
- `SetNode`
- `SetNode`
- `BatchImagesNode`
- `Note`
- `Fast Groups Bypasser (rgthree)`
- `TextEncodeQwenImage21`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `GetNode`
- `ResolutionSelector`
- `EmptyLatentImage` ★核心
- `ComfySwitchNode`
- `LoadImage`
- `LoadImage`
- `Fast Groups Bypasser (rgthree)`
- `PreviewAny`
- `TextGenerateLTX2Prompt`
- `LoadImage`
- `KSampler` ★核心
- `CR Prompt Text`
- `CLIPLoader`
- `CLIPLoader`
- `CLIPLoader`

## 关键参数

- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`
- `seed` = `259927290205888`
- `steps` = `40`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **71%**（22/31）

**有卡**：`easy setNode`、`VAEDecode`、`SaveImage`、`UNETLoader`、`QwenImage21Cache`、`VAELoader`、`BatchImagesNode`、`TextEncodeQwenImage21`、`LoadImage`、`ResolutionSelector`、`EmptyLatentImage`、`TextGenerateLTX2Prompt`、`KSampler`、`CR Prompt Text`、`CLIPLoader`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、EmptyLatentImage、ResolutionSelector、LoadImage

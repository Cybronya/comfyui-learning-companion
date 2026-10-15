---
key: 图片生成/图生图/Qwen Image 2.1多图编辑_2102401818163765249.json
name: Qwen Image 2.1多图编辑_2102401818163765249
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen Image 2.1多图编辑_2102401818163765249.json
hash: 7a5bcf4a479fc1b7
coverage: 0.894737
learned_at: 2026-10-15 22:25:14
nodes: [CLIPLoader, TextGenerateLTX2Prompt, UNETLoader, QwenImage21Cache, LoadImage, VAEDecode, KSampler, LoadImage, LoadImage, SaveImage, easy imageConcat, ResolutionSelector, JjkText, TextEncodeQwenImage21, ComfySwitchNode, CLIPLoader, VAELoader, EmptyLatentImage, BatchImagesNode]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 404510389590621, "steps": 50, "width": 1024}
---

# 图片生成/图生图/Qwen Image 2.1多图编辑_2102401818163765249.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen Image 2.1多图编辑_2102401818163765249.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（19 个）：
- `CLIPLoader`
- `TextGenerateLTX2Prompt`
- `UNETLoader` ★核心
- `QwenImage21Cache`
- `LoadImage`
- `VAEDecode` ★核心
- `KSampler` ★核心
- `LoadImage`
- `LoadImage`
- `SaveImage`
- `easy imageConcat`
- `ResolutionSelector`
- `JjkText`
- `TextEncodeQwenImage21`
- `ComfySwitchNode`
- `CLIPLoader`
- `VAELoader`
- `EmptyLatentImage` ★核心
- `BatchImagesNode`

## 关键参数

- `seed` = `404510389590621`
- `steps` = `50`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`
- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`

## 知识

覆盖率 **89%**（17/19）

**有卡**：`CLIPLoader`、`TextGenerateLTX2Prompt`、`UNETLoader`、`QwenImage21Cache`、`LoadImage`、`VAEDecode`、`KSampler`、`SaveImage`、`easy imageConcat`、`ResolutionSelector`、`TextEncodeQwenImage21`、`VAELoader`、`EmptyLatentImage`、`BatchImagesNode`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、EmptyLatentImage、ResolutionSelector、LoadImage

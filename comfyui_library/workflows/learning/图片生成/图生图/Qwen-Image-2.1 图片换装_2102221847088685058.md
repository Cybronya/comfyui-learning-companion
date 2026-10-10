---
key: 图片生成/图生图/Qwen-Image-2.1 图片换装_2102221847088685058.json
name: Qwen-Image-2.1 图片换装_2102221847088685058
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen-Image-2.1 图片换装_2102221847088685058.json
hash: 5fb41f950c1dfa52
coverage: 0.882353
learned_at: 2026-10-10 20:48:09
nodes: [KSampler, QwenImage21Cache, TextEncodeQwenImage21, LoadImage, JjkText, SaveImage, UNETLoader, CLIPLoader, CLIPLoader, VAELoader, EmptyLatentImage, TextGenerateLTX2Prompt, VAEDecode, LoadImage, ResolutionSelector, BatchImagesNode, ComfySwitchNode]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 88208452847262, "steps": 50, "width": 1024}
---

# 图片生成/图生图/Qwen-Image-2.1 图片换装_2102221847088685058.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen-Image-2.1 图片换装_2102221847088685058.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（17 个）：
- `KSampler` ★核心
- `QwenImage21Cache`
- `TextEncodeQwenImage21`
- `LoadImage`
- `JjkText`
- `SaveImage`
- `UNETLoader` ★核心
- `CLIPLoader`
- `CLIPLoader`
- `VAELoader`
- `EmptyLatentImage` ★核心
- `TextGenerateLTX2Prompt`
- `VAEDecode` ★核心
- `LoadImage`
- `ResolutionSelector`
- `BatchImagesNode`
- `ComfySwitchNode`

## 关键参数

- `seed` = `88208452847262`
- `steps` = `50`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`
- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`

## 知识

覆盖率 **88%**（15/17）

**有卡**：`KSampler`、`QwenImage21Cache`、`TextEncodeQwenImage21`、`LoadImage`、`SaveImage`、`UNETLoader`、`CLIPLoader`、`VAELoader`、`EmptyLatentImage`、`TextGenerateLTX2Prompt`、`VAEDecode`、`ResolutionSelector`、`BatchImagesNode`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、EmptyLatentImage、ResolutionSelector、LoadImage

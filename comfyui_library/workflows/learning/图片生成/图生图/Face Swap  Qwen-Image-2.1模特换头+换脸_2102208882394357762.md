---
key: 图片生成/图生图/Face Swap  Qwen-Image-2.1模特换头+换脸_2102208882394357762.json
name: Face Swap  Qwen-Image-2.1模特换头+换脸_2102208882394357762.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Face Swap  Qwen-Image-2.1模特换头+换脸_2102208882394357762.json
hash: 5ffc466d48136fed
coverage: 0.882353
learned_at: 2026-10-09 22:27:09
nodes: [ComfySwitchNode, VAEDecode, KSampler, QwenImage21Cache, TextGenerateLTX2Prompt, TextEncodeQwenImage21, UNETLoader, BatchImagesNode, CLIPLoader, CLIPLoader, VAELoader, EmptyLatentImage, ResolutionSelector, JjkText, SaveImage, LoadImage, LoadImage]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 946347068825616, "steps": 50, "width": 1024}
---

# 图片生成/图生图/Face Swap  Qwen-Image-2.1模特换头+换脸_2102208882394357762.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/2102208882394357762.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（17 个）：
- `ComfySwitchNode`
- `VAEDecode` ★核心
- `KSampler` ★核心
- `QwenImage21Cache`
- `TextGenerateLTX2Prompt`
- `TextEncodeQwenImage21`
- `UNETLoader` ★核心
- `BatchImagesNode`
- `CLIPLoader`
- `CLIPLoader`
- `VAELoader`
- `EmptyLatentImage` ★核心
- `ResolutionSelector`
- `JjkText`
- `SaveImage`
- `LoadImage`
- `LoadImage`

## 关键参数

- `seed` = `946347068825616`
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

**有卡**：`VAEDecode`、`KSampler`、`QwenImage21Cache`、`TextGenerateLTX2Prompt`、`TextEncodeQwenImage21`、`UNETLoader`、`BatchImagesNode`、`CLIPLoader`、`VAELoader`、`EmptyLatentImage`、`ResolutionSelector`、`SaveImage`、`LoadImage`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、EmptyLatentImage、ResolutionSelector、LoadImage

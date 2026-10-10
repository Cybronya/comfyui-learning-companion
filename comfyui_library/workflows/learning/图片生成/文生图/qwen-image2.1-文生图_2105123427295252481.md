---
key: qwen-image2.1-文生图_2105123427295252481.json
name: qwen-image2.1-文生图_2105123427295252481
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/qwen-image2.1-文生图_2105123427295252481.json
hash: 0bc727415b66a286
coverage: 0.857143
learned_at: 2026-10-10 20:59:25
nodes: [UNETLoader, TextEncodeQwenImage21, CLIPLoader, VAELoader, EmptyLatentImage, CLIPLoader, PrimitiveStringMultiline, PreviewAny, TextGenerateLTX2Prompt, SaveImageAdvanced, VAEDecode, KSampler, SaveImage, ResolutionSelector]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 0, "steps": 25, "width": 1024}
---

# qwen-image2.1-文生图_2105123427295252481.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/qwen-image2.1-文生图_2105123427295252481.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（14 个）：
- `UNETLoader` ★核心
- `TextEncodeQwenImage21`
- `CLIPLoader`
- `VAELoader`
- `EmptyLatentImage` ★核心
- `CLIPLoader`
- `PrimitiveStringMultiline`
- `PreviewAny`
- `TextGenerateLTX2Prompt`
- `SaveImageAdvanced`
- `VAEDecode` ★核心
- `KSampler` ★核心
- `SaveImage`
- `ResolutionSelector`

## 关键参数

- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`
- `seed` = `0`
- `steps` = `25`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **86%**（12/14）

**有卡**：`UNETLoader`、`TextEncodeQwenImage21`、`CLIPLoader`、`VAELoader`、`EmptyLatentImage`、`TextGenerateLTX2Prompt`、`SaveImageAdvanced`、`VAEDecode`、`KSampler`、`SaveImage`、`ResolutionSelector`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、EmptyLatentImage、ResolutionSelector、UNETLoader

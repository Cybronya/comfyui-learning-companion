---
key: 图片生成/图生图/Qwen-image2.1  多图像编辑工作流V2_2102399015068454914.json
name: Qwen-image2.1  多图像编辑工作流V2_2102399015068454914
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen-image2.1  多图像编辑工作流V2_2102399015068454914.json
hash: d91eec86807c1bc3
coverage: 0.909091
learned_at: 2026-10-15 22:25:24
nodes: [UNETLoader, CLIPLoader, VAELoader, EmptyLatentImage, ComfySwitchNode, QwenImage21Cache, VAEDecode, TextEncodeQwenImage21, SaveImage, CLIPLoader, BatchImagesNode, KSampler, PreviewAny, TextGenerateLTX2Prompt, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, CR Text, ResolutionSelector]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 278486116395680, "steps": 25, "width": 1024}
---

# 图片生成/图生图/Qwen-image2.1  多图像编辑工作流V2_2102399015068454914.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen-image2.1  多图像编辑工作流V2_2102399015068454914.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（22 个）：
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `EmptyLatentImage` ★核心
- `ComfySwitchNode`
- `QwenImage21Cache`
- `VAEDecode` ★核心
- `TextEncodeQwenImage21`
- `SaveImage`
- `CLIPLoader`
- `BatchImagesNode`
- `KSampler` ★核心
- `PreviewAny`
- `TextGenerateLTX2Prompt`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `CR Text`
- `ResolutionSelector`

## 关键参数

- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`
- `seed` = `278486116395680`
- `steps` = `25`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **91%**（20/22）

**有卡**：`UNETLoader`、`CLIPLoader`、`VAELoader`、`EmptyLatentImage`、`QwenImage21Cache`、`VAEDecode`、`TextEncodeQwenImage21`、`SaveImage`、`BatchImagesNode`、`KSampler`、`TextGenerateLTX2Prompt`、`LoadImage`、`CR Text`、`ResolutionSelector`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、EmptyLatentImage、ResolutionSelector、LoadImage

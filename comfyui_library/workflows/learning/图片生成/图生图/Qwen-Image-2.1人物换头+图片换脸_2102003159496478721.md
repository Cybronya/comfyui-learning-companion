---
key: 图片生成/图生图/Qwen-Image-2.1人物换头+图片换脸_2102003159496478721.json
name: Qwen-Image-2.1人物换头+图片换脸_2102003159496478721
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen-Image-2.1人物换头+图片换脸_2102003159496478721.json
hash: 047d1004d728d4b8
coverage: 0.882353
learned_at: 2026-10-21 00:43:15
nodes: [ComfySwitchNode, VAEDecode, KSampler, QwenImage21Cache, TextGenerateLTX2Prompt, TextEncodeQwenImage21, UNETLoader, JjkText, BatchImagesNode, CLIPLoader, CLIPLoader, VAELoader, EmptyLatentImage, LoadImage, ResolutionSelector, SaveImage, LoadImage]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 34925851638200, "steps": 50, "width": 1024}
---

# 图片生成/图生图/Qwen-Image-2.1人物换头+图片换脸_2102003159496478721.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen-Image-2.1人物换头+图片换脸_2102003159496478721.json`

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
- `JjkText`
- `BatchImagesNode`
- `CLIPLoader`
- `CLIPLoader`
- `VAELoader`
- `EmptyLatentImage` ★核心
- `LoadImage`
- `ResolutionSelector`
- `SaveImage`
- `LoadImage`

## 关键参数

- `seed` = `34925851638200`
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

**有卡**：`VAEDecode`、`KSampler`、`QwenImage21Cache`、`TextGenerateLTX2Prompt`、`TextEncodeQwenImage21`、`UNETLoader`、`BatchImagesNode`、`CLIPLoader`、`VAELoader`、`EmptyLatentImage`、`LoadImage`、`ResolutionSelector`、`SaveImage`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、EmptyLatentImage、ResolutionSelector、LoadImage

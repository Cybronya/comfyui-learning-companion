---
key: 图片生成/图生图/【API】Qwen-Image2.1图像编辑（提示词反推）_2111987132129701889.json
name: 【API】Qwen-Image2.1图像编辑（提示词反推）_2111987132129701889
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/【API】Qwen-Image2.1图像编辑（提示词反推）_2111987132129701889.json
hash: 68a42563b1b6949d
coverage: 0.96
learned_at: 2026-10-26 22:04:27
nodes: [Label (rgthree), LoadImage, LoadImage, LoadImage, LoadImage, TextGenerateLTX2Prompt, SaveImage, KSampler, VAEDecode, ComfySwitchNode, EmptyLatentImage, ResolutionSelector, QwenImage21Cache, LoadImage, TextEncodeQwenImage21, BatchImagesNode, UNETLoader, CLIPLoader, CLIPLoader, VAELoader, LoadImage, CR Prompt Text, easy cleanGpuUsed, PlaySound|pysssss, 忽略多组孤海]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 542568869129434, "steps": 40, "width": 1024}
---

# 图片生成/图生图/【API】Qwen-Image2.1图像编辑（提示词反推）_2111987132129701889.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/【API】Qwen-Image2.1图像编辑（提示词反推）_2111987132129701889.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（25 个）：
- `Label (rgthree)`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `TextGenerateLTX2Prompt`
- `SaveImage`
- `KSampler` ★核心
- `VAEDecode` ★核心
- `ComfySwitchNode`
- `EmptyLatentImage` ★核心
- `ResolutionSelector`
- `QwenImage21Cache`
- `LoadImage`
- `TextEncodeQwenImage21`
- `BatchImagesNode`
- `UNETLoader` ★核心
- `CLIPLoader`
- `CLIPLoader`
- `VAELoader`
- `LoadImage`
- `CR Prompt Text`
- `easy cleanGpuUsed`
- `PlaySound|pysssss`
- `忽略多组孤海`

## 关键参数

- `seed` = `542568869129434`
- `steps` = `40`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`
- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`

## 知识

覆盖率 **96%**（24/25）

**有卡**：`Label (rgthree)`、`LoadImage`、`TextGenerateLTX2Prompt`、`SaveImage`、`KSampler`、`VAEDecode`、`EmptyLatentImage`、`ResolutionSelector`、`QwenImage21Cache`、`TextEncodeQwenImage21`、`BatchImagesNode`、`UNETLoader`、`CLIPLoader`、`VAELoader`、`CR Prompt Text`、`easy cleanGpuUsed`、`PlaySound|pysssss`、`忽略多组孤海`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、EmptyLatentImage、ResolutionSelector、LoadImage

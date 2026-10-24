---
key: 图片生成/图生图/开源最强图片模型 Qwen-image2.1  qwen2.1图生图，图像编辑_2112866530273882114.json
name: 开源最强图片模型 Qwen-image2.1  qwen2.1图生图，图像编辑_2112866530273882114
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/开源最强图片模型 Qwen-image2.1  qwen2.1图生图，图像编辑_2112866530273882114.json
hash: bfe941fd63e15761
coverage: 0.9375
learned_at: 2026-10-23 12:51:22
nodes: [UNETLoader, CLIPLoader, VAELoader, EmptyLatentImage, ComfySwitchNode, QwenImage21Cache, TextEncodeQwenImage21, SaveImage, KSampler, VAEDecode, ResolutionSelector, LoadImage, LoadImage, CR Text, CLIPLoader, TextGenerateLTX2Prompt]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 358953682245973, "steps": 25, "width": 1024}
---

# 图片生成/图生图/开源最强图片模型 Qwen-image2.1  qwen2.1图生图，图像编辑_2112866530273882114.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/开源最强图片模型 Qwen-image2.1  qwen2.1图生图，图像编辑_2112866530273882114.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（16 个）：
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `EmptyLatentImage` ★核心
- `ComfySwitchNode`
- `QwenImage21Cache`
- `TextEncodeQwenImage21`
- `SaveImage`
- `KSampler` ★核心
- `VAEDecode` ★核心
- `ResolutionSelector`
- `LoadImage`
- `LoadImage`
- `CR Text`
- `CLIPLoader`
- `TextGenerateLTX2Prompt`

## 关键参数

- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`
- `seed` = `358953682245973`
- `steps` = `25`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **94%**（15/16）

**有卡**：`UNETLoader`、`CLIPLoader`、`VAELoader`、`EmptyLatentImage`、`QwenImage21Cache`、`TextEncodeQwenImage21`、`SaveImage`、`KSampler`、`VAEDecode`、`ResolutionSelector`、`LoadImage`、`CR Text`、`TextGenerateLTX2Prompt`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、EmptyLatentImage、ResolutionSelector、LoadImage

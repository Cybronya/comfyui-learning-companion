---
key: 图片生成/图生图/Qwen Image 2.1 一键图片换装_2102585909454659586.json
name: Qwen Image 2.1 一键图片换装_2102585909454659586
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen Image 2.1 一键图片换装_2102585909454659586.json
hash: 73617c53d9d566d5
coverage: 0.882353
learned_at: 2026-10-10 20:48:05
nodes: [CLIPLoader, CLIPLoader, BatchImagesNode, VAELoader, EmptyLatentImage, ComfySwitchNode, VAEDecode, KSampler, QwenImage21Cache, TextGenerateLTX2Prompt, TextEncodeQwenImage21, UNETLoader, JjkText, SaveImage, LoadImage, LoadImage, ResolutionSelector]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 238292605658064, "steps": 50, "width": 1024}
---

# 图片生成/图生图/Qwen Image 2.1 一键图片换装_2102585909454659586.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen Image 2.1 一键图片换装_2102585909454659586.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（17 个）：
- `CLIPLoader`
- `CLIPLoader`
- `BatchImagesNode`
- `VAELoader`
- `EmptyLatentImage` ★核心
- `ComfySwitchNode`
- `VAEDecode` ★核心
- `KSampler` ★核心
- `QwenImage21Cache`
- `TextGenerateLTX2Prompt`
- `TextEncodeQwenImage21`
- `UNETLoader` ★核心
- `JjkText`
- `SaveImage`
- `LoadImage`
- `LoadImage`
- `ResolutionSelector`

## 关键参数

- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`
- `seed` = `238292605658064`
- `steps` = `50`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **88%**（15/17）

**有卡**：`CLIPLoader`、`BatchImagesNode`、`VAELoader`、`EmptyLatentImage`、`VAEDecode`、`KSampler`、`QwenImage21Cache`、`TextGenerateLTX2Prompt`、`TextEncodeQwenImage21`、`UNETLoader`、`SaveImage`、`LoadImage`、`ResolutionSelector`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、EmptyLatentImage、ResolutionSelector、LoadImage

---
key: 图片生成/图生图/换头换脸Face+Swap++Qwen-Image-2.1模特换头+换脸_2111625667644317697.json
name: 换头换脸Face+Swap++Qwen-Image-2.1模特换头+换脸_2111625667644317697
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/换头换脸Face+Swap++Qwen-Image-2.1模特换头+换脸_2111625667644317697.json
hash: 96be4a065f4e433f
coverage: 0.882353
learned_at: 2026-10-23 12:56:09
nodes: [ComfySwitchNode, VAEDecode, KSampler, QwenImage21Cache, TextGenerateLTX2Prompt, TextEncodeQwenImage21, UNETLoader, BatchImagesNode, CLIPLoader, CLIPLoader, VAELoader, EmptyLatentImage, ResolutionSelector, JjkText, SaveImage, LoadImage, LoadImage]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 1100563087488738, "steps": 50, "width": 1024}
---

# 图片生成/图生图/换头换脸Face+Swap++Qwen-Image-2.1模特换头+换脸_2111625667644317697.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/换头换脸Face+Swap++Qwen-Image-2.1模特换头+换脸_2111625667644317697.json`

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

- `seed` = `1100563087488738`
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

---
key: 图片生成/文生图/【API】Qwen-Image2.1文生图（提示词反推）_2111987215688622081.json
name: 【API】Qwen-Image2.1文生图（提示词反推）_2111987215688622081
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/【API】Qwen-Image2.1文生图（提示词反推）_2111987215688622081.json
hash: c9c75df451b40925
coverage: 0.9375
learned_at: 2026-10-26 22:09:17
nodes: [EmptyLatentImage, KSampler, TextGenerateLTX2Prompt, easy showAnything, ResolutionSelector, VAEDecode, SaveImage, QwenImage21Cache, PlaySound|pysssss, TextEncodeQwenImage21, UNETLoader, CLIPLoader, CLIPLoader, VAELoader, easy cleanGpuUsed, CR Prompt Text]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 691876987034136, "steps": 40, "width": 1024}
---

# 图片生成/文生图/【API】Qwen-Image2.1文生图（提示词反推）_2111987215688622081.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/【API】Qwen-Image2.1文生图（提示词反推）_2111987215688622081.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（16 个）：
- `EmptyLatentImage` ★核心
- `KSampler` ★核心
- `TextGenerateLTX2Prompt`
- `easy showAnything`
- `ResolutionSelector`
- `VAEDecode` ★核心
- `SaveImage`
- `QwenImage21Cache`
- `PlaySound|pysssss`
- `TextEncodeQwenImage21`
- `UNETLoader` ★核心
- `CLIPLoader`
- `CLIPLoader`
- `VAELoader`
- `easy cleanGpuUsed`
- `CR Prompt Text`

## 关键参数

- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`
- `seed` = `691876987034136`
- `steps` = `40`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **94%**（15/16）

**有卡**：`EmptyLatentImage`、`KSampler`、`TextGenerateLTX2Prompt`、`ResolutionSelector`、`VAEDecode`、`SaveImage`、`QwenImage21Cache`、`PlaySound|pysssss`、`TextEncodeQwenImage21`、`UNETLoader`、`CLIPLoader`、`VAELoader`、`easy cleanGpuUsed`、`CR Prompt Text`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、EmptyLatentImage、ResolutionSelector、QwenImage21Cache

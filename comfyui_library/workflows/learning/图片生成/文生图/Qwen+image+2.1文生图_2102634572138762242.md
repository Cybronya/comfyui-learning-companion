---
key: Qwen+image+2.1文生图_2102634572138762242.json
name: Qwen+image+2.1文生图_2102634572138762242
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Qwen+image+2.1文生图_2102634572138762242.json
hash: 70924446fd2b385b
coverage: 1
learned_at: 2026-10-10 20:58:58
nodes: [UNETLoader, CLIPLoader, VAELoader, TextEncodeQwenImage21, KSampler, CLIPLoader, EmptyLatentImage, Text, TextGenerateLTX2Prompt, ResolutionSelector, SaveImage, VAEDecode]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 842850240, "steps": 50, "width": 1024}
---

# Qwen+image+2.1文生图_2102634572138762242.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Qwen+image+2.1文生图_2102634572138762242.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（12 个）：
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `TextEncodeQwenImage21`
- `KSampler` ★核心
- `CLIPLoader`
- `EmptyLatentImage` ★核心
- `Text`
- `TextGenerateLTX2Prompt`
- `ResolutionSelector`
- `SaveImage`
- `VAEDecode` ★核心

## 关键参数

- `seed` = `842850240`
- `steps` = `50`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`
- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`

## 知识

覆盖率 **100%**（12/12）

**有卡**：`UNETLoader`、`CLIPLoader`、`VAELoader`、`TextEncodeQwenImage21`、`KSampler`、`EmptyLatentImage`、`Text`、`TextGenerateLTX2Prompt`、`ResolutionSelector`、`SaveImage`、`VAEDecode`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、EmptyLatentImage、ResolutionSelector、UNETLoader

---
key: 图片生成/文生图/Qwen+image+2.1文生图_2102634572138762242.json
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

# 图片生成/文生图/Qwen+image+2.1文生图_2102634572138762242.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Qwen+image+2.1文生图_2102634572138762242.json`

## 结构

**节点**（12 个）：
- `UNETLoader`
- `CLIPLoader`
- `VAELoader`
- `TextEncodeQwenImage21`
- `KSampler`
- `CLIPLoader`
- `EmptyLatentImage`
- `Text`
- `TextGenerateLTX2Prompt`
- `ResolutionSelector`
- `SaveImage`
- `VAEDecode`

## 关键参数

- `batch_size` = `1`
- `cfg` = `1`
- `denoise` = `1`
- `height` = `1024`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `seed` = `842850240`
- `steps` = `50`
- `width` = `1024`

## 知识

覆盖率 **100%**（12/12）

**有卡**：`UNETLoader`、`CLIPLoader`、`VAELoader`、`TextEncodeQwenImage21`、`KSampler`、`EmptyLatentImage`、`Text`、`TextGenerateLTX2Prompt`、`ResolutionSelector`、`SaveImage`、`VAEDecode`

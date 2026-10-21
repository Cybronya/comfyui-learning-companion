---
key: 图片生成/文生图/Qwen_Image_2.1_文生图_纯净官流40步无PE_2107976735823323137.json
name: Qwen_Image_2.1_文生图_纯净官流40步无PE_2107976735823323137
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Qwen_Image_2.1_文生图_纯净官流40步无PE_2107976735823323137.json
hash: 31f94ba4ea2b9881
coverage: 0.833333
learned_at: 2026-10-20 01:51:27
nodes: [SaveImage, UNETLoader, TextEncodeQwenImage21, CLIPLoader, VAELoader, KSampler, VAEDecode, EmptyLatentImage, ResolutionSelector, PrimitiveStringMultiline, EmptyImage, PreviewImage]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 561660676528607, "steps": 40, "width": 1024}
---

# 图片生成/文生图/Qwen_Image_2.1_文生图_纯净官流40步无PE_2107976735823323137.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Qwen_Image_2.1_文生图_纯净官流40步无PE_2107976735823323137.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（12 个）：
- `SaveImage`
- `UNETLoader` ★核心
- `TextEncodeQwenImage21`
- `CLIPLoader`
- `VAELoader`
- `KSampler` ★核心
- `VAEDecode` ★核心
- `EmptyLatentImage` ★核心
- `ResolutionSelector`
- `PrimitiveStringMultiline`
- `EmptyImage`
- `PreviewImage`

## 关键参数

- `seed` = `561660676528607`
- `steps` = `40`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`
- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`

## 知识

覆盖率 **83%**（10/12）

**有卡**：`SaveImage`、`UNETLoader`、`TextEncodeQwenImage21`、`CLIPLoader`、`VAELoader`、`KSampler`、`VAEDecode`、`EmptyLatentImage`、`ResolutionSelector`、`EmptyImage`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、EmptyLatentImage、ResolutionSelector、UNETLoader

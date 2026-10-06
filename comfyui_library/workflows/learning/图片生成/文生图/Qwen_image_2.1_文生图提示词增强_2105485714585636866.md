---
key: 图片生成/文生图/Qwen_image_2.1_文生图提示词增强_2105485714585636866.json
name: Qwen_image_2.1_文生图提示词增强_2105485714585636866
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Qwen_image_2.1_文生图提示词增强_2105485714585636866.json
hash: 6518a82079d1275d
coverage: 0.857143
learned_at: 2026-10-06 22:58:39
nodes: [TextEncodeQwenImage21, EmptyLatentImage, VAEDecode, UNETLoader, CLIPLoader, VAELoader, easy showAnything, SaveImageAdvanced, KSampler, ResolutionSelector, CLIPLoader, PrimitiveStringMultiline, TextGenerateLTX2Prompt, SaveImage]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 673343643974885, "steps": 25, "width": 1024}
---

# 图片生成/文生图/Qwen_image_2.1_文生图提示词增强_2105485714585636866.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Qwen_image_2.1_文生图提示词增强_2105485714585636866.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（14 个）：
- `TextEncodeQwenImage21`
- `EmptyLatentImage` ★核心
- `VAEDecode` ★核心
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `easy showAnything`
- `SaveImageAdvanced`
- `KSampler` ★核心
- `ResolutionSelector`
- `CLIPLoader`
- `PrimitiveStringMultiline`
- `TextGenerateLTX2Prompt`
- `SaveImage`

## 关键参数

- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`
- `seed` = `673343643974885`
- `steps` = `25`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **86%**（12/14）

**有卡**：`TextEncodeQwenImage21`、`EmptyLatentImage`、`VAEDecode`、`UNETLoader`、`CLIPLoader`、`VAELoader`、`SaveImageAdvanced`、`KSampler`、`ResolutionSelector`、`TextGenerateLTX2Prompt`、`SaveImage`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、EmptyLatentImage、ResolutionSelector、UNETLoader

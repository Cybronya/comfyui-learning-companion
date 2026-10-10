---
key: Qwen image 2.1 文生图_2102236635739017218.json
name: Qwen image 2.1 文生图_2102236635739017218
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Qwen image 2.1 文生图_2102236635739017218.json
hash: 7058f74ea127a57b
coverage: 0.866667
learned_at: 2026-10-10 20:58:57
nodes: [TextEncodeQwenImage21, VAEDecode, UNETLoader, CLIPLoader, VAELoader, CLIPLoader, easy showAnything, EmptyLatentImage, KSampler, SaveImage, TextGenerateLTX2Prompt, StringToInt, StringToInt, PrimitiveStringMultiline, SaveImageAdvanced]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 1075605267898907, "steps": 50, "width": 1024}
---

# Qwen image 2.1 文生图_2102236635739017218.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Qwen image 2.1 文生图_2102236635739017218.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（15 个）：
- `TextEncodeQwenImage21`
- `VAEDecode` ★核心
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `CLIPLoader`
- `easy showAnything`
- `EmptyLatentImage` ★核心
- `KSampler` ★核心
- `SaveImage`
- `TextGenerateLTX2Prompt`
- `StringToInt`
- `StringToInt`
- `PrimitiveStringMultiline`
- `SaveImageAdvanced`

## 关键参数

- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`
- `seed` = `1075605267898907`
- `steps` = `50`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **87%**（13/15）

**有卡**：`TextEncodeQwenImage21`、`VAEDecode`、`UNETLoader`、`CLIPLoader`、`VAELoader`、`EmptyLatentImage`、`KSampler`、`SaveImage`、`TextGenerateLTX2Prompt`、`StringToInt`、`SaveImageAdvanced`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、EmptyLatentImage、UNETLoader、TextGenerateLTX2Prompt

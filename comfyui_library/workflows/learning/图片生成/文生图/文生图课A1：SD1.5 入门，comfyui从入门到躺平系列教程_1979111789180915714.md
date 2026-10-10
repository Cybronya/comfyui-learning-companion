---
key: 文生图课A1：SD1.5 入门，comfyui从入门到躺平系列教程_1979111789180915714.json
name: 文生图课A1：SD1.5 入门，comfyui从入门到躺平系列教程_1979111789180915714
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/文生图课A1：SD1.5 入门，comfyui从入门到躺平系列教程_1979111789180915714.json
hash: 0bf1562d061b2ea5
coverage: 0.666667
learned_at: 2026-10-10 20:59:49
nodes: [SaveImage, MarkdownNote, MarkdownNote, EmptyLatentImage, CLIPTextEncode, CLIPTextEncode, VAEDecode, MarkdownNote, LoadImage, CheckpointLoaderSimple, MarkdownNote, KSampler]
patterns: [text_to_image]
missing: []
parameters: {"batch_size": 1, "cfg": 3, "checkpoint": "v1-5-pruned-emaonly.safetensors", "denoise": 1, "height": 512, "sampler_name": "dpmpp_2m_sde", "scheduler": "karras", "seed": 123456789, "steps": 28, "width": 512}
---

# 文生图课A1：SD1.5 入门，comfyui从入门到躺平系列教程_1979111789180915714.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/文生图课A1：SD1.5 入门，comfyui从入门到躺平系列教程_1979111789180915714.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（12 个）：
- `SaveImage`
- `MarkdownNote`
- `MarkdownNote`
- `EmptyLatentImage` ★核心
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `VAEDecode` ★核心
- `MarkdownNote`
- `LoadImage`
- `CheckpointLoaderSimple` ★核心
- `MarkdownNote`
- `KSampler` ★核心

**识别到的模式**：text_to_image

## 关键参数

- `width` = `512`
- `height` = `512`
- `batch_size` = `1`
- `checkpoint` = `v1-5-pruned-emaonly.safetensors`
- `seed` = `123456789`
- `steps` = `28`
- `cfg` = `3`
- `sampler_name` = `dpmpp_2m_sde`
- `scheduler` = `karras`
- `denoise` = `1`

## 知识

覆盖率 **67%**（8/12）

**有卡**：`SaveImage`、`EmptyLatentImage`、`CLIPTextEncode`、`VAEDecode`、`LoadImage`、`CheckpointLoaderSimple`、`KSampler`

**用到的条目**：KSampler、VAEDecode、CheckpointLoaderSimple、CLIPTextEncode、EmptyLatentImage、LoadImage、SaveImage、sd15-t2i-basic

---
key: 图片生成/文生图/千问qwen-image-2.1文生图工作流_2104553799485583362.json
name: 千问qwen-image-2.1文生图工作流_2104553799485583362
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/千问qwen-image-2.1文生图工作流_2104553799485583362.json
hash: 8edbee92f88aa335
coverage: 0.909091
learned_at: 2026-10-07 02:37:12
nodes: [ConditioningZeroOut, VAEDecode, SaveImage, LoraLoaderModelOnly, UNETLoader, VAELoader, CLIPLoader, EmptyLatentImage, PreviewImage, KSampler, CLIPTextEncode]
patterns: [text_to_image]
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1920, "sampler_name": "euler", "scheduler": "simple", "seed": 135300370575368, "steps": 30, "width": 1440}
---

# 图片生成/文生图/千问qwen-image-2.1文生图工作流_2104553799485583362.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/千问qwen-image-2.1文生图工作流_2104553799485583362.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output

**节点**（11 个）：
- `ConditioningZeroOut`
- `VAEDecode` ★核心
- `SaveImage`
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `VAELoader`
- `CLIPLoader`
- `EmptyLatentImage` ★核心
- `PreviewImage`
- `KSampler` ★核心
- `CLIPTextEncode` ★核心

**识别到的模式**：text_to_image

## 关键参数

- `width` = `1440`
- `height` = `1920`
- `batch_size` = `1`
- `seed` = `135300370575368`
- `steps` = `30`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **91%**（10/11）

**有卡**：`ConditioningZeroOut`、`VAEDecode`、`SaveImage`、`LoraLoaderModelOnly`、`UNETLoader`、`VAELoader`、`CLIPLoader`、`EmptyLatentImage`、`KSampler`、`CLIPTextEncode`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、EmptyLatentImage

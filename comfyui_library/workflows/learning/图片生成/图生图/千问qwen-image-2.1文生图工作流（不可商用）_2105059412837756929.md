---
key: 图片生成/图生图/千问qwen-image-2.1文生图工作流（不可商用）_2105059412837756929.json
name: 千问qwen-image-2.1文生图工作流（不可商用）_2105059412837756929
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/千问qwen-image-2.1文生图工作流（不可商用）_2105059412837756929.json
hash: 4b4624cd9c2b3560
coverage: 0.923077
learned_at: 2026-10-21 00:50:40
nodes: [ConditioningZeroOut, VAEDecode, SaveImage, UNETLoader, EmptyLatentImage, PreviewImage, CLIPLoader, VAELoader, LoraLoaderModelOnly, LoraLoaderModelOnly, CLIPTextEncode, KSampler, LoraLoaderModelOnly]
patterns: [text_to_image]
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1920, "sampler_name": "euler", "scheduler": "simple", "seed": 296957157559061, "steps": 50, "width": 1440}
---

# 图片生成/图生图/千问qwen-image-2.1文生图工作流（不可商用）_2105059412837756929.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/千问qwen-image-2.1文生图工作流（不可商用）_2105059412837756929.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output

**节点**（13 个）：
- `ConditioningZeroOut`
- `VAEDecode` ★核心
- `SaveImage`
- `UNETLoader` ★核心
- `EmptyLatentImage` ★核心
- `PreviewImage`
- `CLIPLoader`
- `VAELoader`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `CLIPTextEncode` ★核心
- `KSampler` ★核心
- `LoraLoaderModelOnly` ★核心

**识别到的模式**：text_to_image

## 关键参数

- `width` = `1440`
- `height` = `1920`
- `batch_size` = `1`
- `seed` = `296957157559061`
- `steps` = `50`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **92%**（12/13）

**有卡**：`ConditioningZeroOut`、`VAEDecode`、`SaveImage`、`UNETLoader`、`EmptyLatentImage`、`CLIPLoader`、`VAELoader`、`LoraLoaderModelOnly`、`CLIPTextEncode`、`KSampler`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、EmptyLatentImage

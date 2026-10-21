---
key: 图片生成/文生图/【Flux-2-Klein+Z-image-turbo+Z-image-base】文生图对比_2018868825004969985.json
name: 【Flux-2-Klein+Z-image-turbo+Z-image-base】文生图对比_2018868825004969985
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/【Flux-2-Klein+Z-image-turbo+Z-image-base】文生图对比_2018868825004969985.json
hash: da1900c7444e2e6c
coverage: 0.864865
learned_at: 2026-10-19 22:30:17
nodes: [VAELoader, EmptyLatentImage, CLIPLoader, VAEDecode, VAELoader, PreviewImage, EmptyLatentImage, CLIPTextEncode, CLIPTextEncode, KSamplerSelect, Flux2Scheduler, CFGGuider, PrimitiveInt, PrimitiveInt, RandomNoise, CLIPTextEncode, SamplerCustomAdvanced, VAEDecode, CLIPTextEncode, CLIPTextEncode, CLIPTextEncode, EmptyFlux2LatentImage, PreviewImage, SaveImage, UNETLoader, CLIPLoader, VAELoader, UNETLoader, UNETLoader, VAEDecode, PreviewImage, SaveImage, Text Multiline, CLIPLoader, KSampler, KSampler, SaveImage]
patterns: [text_to_image]
missing: []
parameters: {"batch_size": 1, "cfg": 3, "denoise": 1, "height": 1920, "sampler_name": "euler", "scheduler": "simple", "seed": 1039556414884274, "steps": 30, "width": 1080}
---

# 图片生成/文生图/【Flux-2-Klein+Z-image-turbo+Z-image-base】文生图对比_2018868825004969985.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/【Flux-2-Klein+Z-image-turbo+Z-image-base】文生图对比_2018868825004969985.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（37 个）：
- `VAELoader`
- `EmptyLatentImage` ★核心
- `CLIPLoader`
- `VAEDecode` ★核心
- `VAELoader`
- `PreviewImage`
- `EmptyLatentImage` ★核心
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `KSamplerSelect` ★核心
- `Flux2Scheduler`
- `CFGGuider`
- `PrimitiveInt`
- `PrimitiveInt`
- `RandomNoise`
- `CLIPTextEncode` ★核心
- `SamplerCustomAdvanced` ★核心
- `VAEDecode` ★核心
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `EmptyFlux2LatentImage`
- `PreviewImage`
- `SaveImage`
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `VAEDecode` ★核心
- `PreviewImage`
- `SaveImage`
- `Text Multiline`
- `CLIPLoader`
- `KSampler` ★核心
- `KSampler` ★核心
- `SaveImage`

**识别到的模式**：text_to_image

## 关键参数

- `width` = `1080`
- `height` = `1920`
- `batch_size` = `1`
- `seed` = `1039556414884274`
- `steps` = `30`
- `cfg` = `3`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **86%**（32/37）

**有卡**：`VAELoader`、`EmptyLatentImage`、`CLIPLoader`、`VAEDecode`、`CLIPTextEncode`、`KSamplerSelect`、`Flux2Scheduler`、`CFGGuider`、`RandomNoise`、`SamplerCustomAdvanced`、`EmptyFlux2LatentImage`、`SaveImage`、`UNETLoader`、`Text Multiline`、`KSampler`

**用到的条目**：KSampler、VAEDecode、VAELoader、UNETLoader、CLIPTextEncode、CLIPLoader、EmptyLatentImage、CFGGuider

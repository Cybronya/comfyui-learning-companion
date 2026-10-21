---
key: 图片生成/文生图/Z-Image VS Z-Image-turbo VS Qwen image 2512_2016491036381552641.json
name: Z-Image VS Z-Image-turbo VS Qwen image 2512_2016491036381552641
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Z-Image VS Z-Image-turbo VS Qwen image 2512_2016491036381552641.json
hash: 0d83330de121e05a
coverage: 0.972973
learned_at: 2026-10-19 22:15:22
nodes: [UNETLoader, VAELoader, ModelSamplingAuraFlow, CLIPTextEncode, VAEDecode, UNETLoader, CLIPLoader, VAELoader, ModelSamplingAuraFlow, ConditioningZeroOut, VAEDecode, UNETLoader, CLIPLoader, VAELoader, ConditioningZeroOut, VAEDecode, ImageConcanate, ImageConcanate, LoraLoaderModelOnly, EmptyLatentImage, CLIPTextEncode, AddLabel, AddLabel, KSampler, KSamplerAdvanced, KSamplerAdvanced, Fast Groups Bypasser (rgthree), CLIPTextEncode, CLIPTextEncode, CLIPLoader, SaveImage, SaveImage, SaveImage, AddLabel, SaveImage, easy promptList, easy promptList]
patterns: [text_to_image]
missing: []
parameters: {"batch_size": 1, "cfg": 8, "denoise": "FlowMatchEulerDiscreteScheduler", "height": 1536, "sampler_name": 1, "scheduler": "euler", "seed": "enable", "steps": "fixed", "width": 1024}
---

# 图片生成/文生图/Z-Image VS Z-Image-turbo VS Qwen image 2512_2016491036381552641.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Z-Image VS Z-Image-turbo VS Qwen image 2512_2016491036381552641.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（37 个）：
- `UNETLoader` ★核心
- `VAELoader`
- `ModelSamplingAuraFlow`
- `CLIPTextEncode` ★核心
- `VAEDecode` ★核心
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `ModelSamplingAuraFlow`
- `ConditioningZeroOut`
- `VAEDecode` ★核心
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `ConditioningZeroOut`
- `VAEDecode` ★核心
- `ImageConcanate`
- `ImageConcanate`
- `LoraLoaderModelOnly` ★核心
- `EmptyLatentImage` ★核心
- `CLIPTextEncode` ★核心
- `AddLabel`
- `AddLabel`
- `KSampler` ★核心
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `Fast Groups Bypasser (rgthree)`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `CLIPLoader`
- `SaveImage`
- `SaveImage`
- `SaveImage`
- `AddLabel`
- `SaveImage`
- `easy promptList`
- `easy promptList`

**识别到的模式**：text_to_image

## 关键参数

- `width` = `1024`
- `height` = `1536`
- `batch_size` = `1`
- `seed` = `enable`
- `steps` = `fixed`
- `cfg` = `8`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `FlowMatchEulerDiscreteScheduler`

## 知识

覆盖率 **97%**（36/37）

**有卡**：`UNETLoader`、`VAELoader`、`ModelSamplingAuraFlow`、`CLIPTextEncode`、`VAEDecode`、`CLIPLoader`、`ConditioningZeroOut`、`ImageConcanate`、`LoraLoaderModelOnly`、`EmptyLatentImage`、`AddLabel`、`KSampler`、`KSamplerAdvanced`、`SaveImage`、`easy promptList`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、EmptyLatentImage

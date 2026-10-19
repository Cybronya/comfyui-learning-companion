---
key: 图片生成/文生图/tonnie-SDXL一键表情包（Juggernaut）_1993322961151213569.json
name: tonnie-SDXL一键表情包（Juggernaut）_1993322961151213569
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/tonnie-SDXL一键表情包（Juggernaut）_1993322961151213569.json
hash: ec8ad9f0cea0d211
coverage: 0.8125
learned_at: 2026-10-19 21:33:15
nodes: [PreviewImage, easy negative, CLIPTextEncode, VAEDecode, EmptyLatentImage, CLIPSetLastLayer, CheckpointLoaderSimple, easy fullLoader, easy fullkSampler, KSampler, easy positive, CLIPTextEncode, easy fullLoader, SaveImage, Fast Groups Bypasser (rgthree), Note]
patterns: [text_to_image]
missing: []
parameters: {"batch_size": 1, "cfg": 8, "checkpoint": "SDXL_Juggernaut.safetensors", "denoise": 1, "height": 768, "sampler_name": "dpmpp_2m_sde", "scheduler": "karras", "seed": 300539271463057, "steps": 25, "width": 1280}
---

# 图片生成/文生图/tonnie-SDXL一键表情包（Juggernaut）_1993322961151213569.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/tonnie-SDXL一键表情包（Juggernaut）_1993322961151213569.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（16 个）：
- `PreviewImage`
- `easy negative`
- `CLIPTextEncode` ★核心
- `VAEDecode` ★核心
- `EmptyLatentImage` ★核心
- `CLIPSetLastLayer`
- `CheckpointLoaderSimple` ★核心
- `easy fullLoader`
- `easy fullkSampler` ★核心
- `KSampler` ★核心
- `easy positive`
- `CLIPTextEncode` ★核心
- `easy fullLoader`
- `SaveImage`
- `Fast Groups Bypasser (rgthree)`
- `Note`

**识别到的模式**：text_to_image

## 关键参数

- `width` = `1280`
- `height` = `768`
- `batch_size` = `1`
- `checkpoint` = `SDXL_Juggernaut.safetensors`
- `seed` = `300539271463057`
- `steps` = `25`
- `cfg` = `8`
- `sampler_name` = `dpmpp_2m_sde`
- `scheduler` = `karras`
- `denoise` = `1`

## 知识

覆盖率 **81%**（13/16）

**有卡**：`easy negative`、`CLIPTextEncode`、`VAEDecode`、`EmptyLatentImage`、`CLIPSetLastLayer`、`CheckpointLoaderSimple`、`easy fullLoader`、`easy fullkSampler`、`KSampler`、`easy positive`、`SaveImage`

**用到的条目**：KSampler、VAEDecode、CheckpointLoaderSimple、CLIPTextEncode、EmptyLatentImage、easy fullkSampler、CLIPSetLastLayer、easy negative

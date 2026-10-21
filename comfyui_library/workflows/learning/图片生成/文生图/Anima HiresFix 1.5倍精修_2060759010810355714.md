---
key: 图片生成/文生图/Anima HiresFix 1.5倍精修_2060759010810355714.json
name: Anima HiresFix 1.5倍精修_2060759010810355714
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Anima HiresFix 1.5倍精修_2060759010810355714.json
hash: be7cc8601153b98e
coverage: 1
learned_at: 2026-10-19 23:02:09
nodes: [ModelSamplingAuraFlow, CLIPLoader, VAELoader, CLIPTextEncode, CLIPTextEncode, EmptyLatentImage, KSampler, LatentUpscale, KSampler, VAEDecode, SaveImage, UNETLoader]
patterns: [text_to_image]
missing: []
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 0.35, "height": 1024, "sampler_name": "er_sde", "scheduler": "simple", "seed": 45, "steps": 18, "width": 1024}
---

# 图片生成/文生图/Anima HiresFix 1.5倍精修_2060759010810355714.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Anima HiresFix 1.5倍精修_2060759010810355714.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（12 个）：
- `ModelSamplingAuraFlow`
- `CLIPLoader`
- `VAELoader`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `EmptyLatentImage` ★核心
- `KSampler` ★核心
- `LatentUpscale`
- `KSampler` ★核心
- `VAEDecode` ★核心
- `SaveImage`
- `UNETLoader` ★核心

**识别到的模式**：text_to_image

## 关键参数

- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`
- `seed` = `45`
- `steps` = `18`
- `cfg` = `4.5`
- `sampler_name` = `er_sde`
- `scheduler` = `simple`
- `denoise` = `0.35`

## 知识

覆盖率 **100%**（12/12）

**有卡**：`ModelSamplingAuraFlow`、`CLIPLoader`、`VAELoader`、`CLIPTextEncode`、`EmptyLatentImage`、`KSampler`、`LatentUpscale`、`VAEDecode`、`SaveImage`、`UNETLoader`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、EmptyLatentImage、UNETLoader、LatentUpscale

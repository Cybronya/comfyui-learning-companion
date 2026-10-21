---
key: 图片生成/文生图/anima_basev1.0_turbo_t2i_2057191803308298242.json
name: anima_basev1.0_turbo_t2i_2057191803308298242
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/anima_basev1.0_turbo_t2i_2057191803308298242.json
hash: 6fcd1e6f5caf7927
coverage: 0.92
learned_at: 2026-10-19 22:45:57
nodes: [CLIPTextEncode, CLIPLoader, ShowText|pysssss, SDVN Translate, ShowText|pysssss, StringMergeNode, VAEDecode, UNETLoader, CLIPTextEncode, Text Multiline, Text Multiline, FluxKontextImageScale, SaveImage, LatentUpscaleBy, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, KSampler, KSampler, EmptyLatentImage, Text Multiline, SeedGenerator, Text Multiline, VAELoader]
patterns: [text_to_image]
missing: []
parameters: {"batch_size": 1, "cfg": 1.5, "denoise": 1, "height": 1152, "sampler_name": "er_sde", "scheduler": "simple", "seed": 810848040719241, "steps": 10, "width": 768}
---

# 图片生成/文生图/anima_basev1.0_turbo_t2i_2057191803308298242.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/anima_basev1.0_turbo_t2i_2057191803308298242.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（25 个）：
- `CLIPTextEncode` ★核心
- `CLIPLoader`
- `ShowText|pysssss`
- `SDVN Translate`
- `ShowText|pysssss`
- `StringMergeNode`
- `VAEDecode` ★核心
- `UNETLoader` ★核心
- `CLIPTextEncode` ★核心
- `Text Multiline`
- `Text Multiline`
- `FluxKontextImageScale`
- `SaveImage`
- `LatentUpscaleBy`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `KSampler` ★核心
- `KSampler` ★核心
- `EmptyLatentImage` ★核心
- `Text Multiline`
- `SeedGenerator`
- `Text Multiline`
- `VAELoader`

**识别到的模式**：text_to_image

## 关键参数

- `seed` = `810848040719241`
- `steps` = `10`
- `cfg` = `1.5`
- `sampler_name` = `er_sde`
- `scheduler` = `simple`
- `denoise` = `1`
- `width` = `768`
- `height` = `1152`
- `batch_size` = `1`

## 知识

覆盖率 **92%**（23/25）

**有卡**：`CLIPTextEncode`、`CLIPLoader`、`SDVN Translate`、`StringMergeNode`、`VAEDecode`、`UNETLoader`、`Text Multiline`、`FluxKontextImageScale`、`SaveImage`、`LatentUpscaleBy`、`LoraLoaderModelOnly`、`KSampler`、`EmptyLatentImage`、`SeedGenerator`、`VAELoader`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPTextEncode、CLIPLoader、EmptyLatentImage

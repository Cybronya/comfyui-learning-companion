---
key: 平台全量/ShakkerLabs 的 Flux FilmPortrait LoRA_1836379763278770177.json
name: ShakkerLabs 的 Flux FilmPortrait LoRA_1836379763278770177
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/ShakkerLabs 的 Flux FilmPortrait LoRA_1836379763278770177.json
hash: 60151287bdf11a00
coverage: 0.904762
learned_at: 2026-11-14 01:00:39
nodes: [SamplerCustomAdvanced, KSamplerSelect, CLIPTextEncode, BasicScheduler, VAELoader, VAEDecode, UpscaleModelLoader, RandomNoise, BasicGuider, easy promptConcat, CLIPTextEncodeFlux, SDXLEmptyLatentSizePicker+, Text String, DualCLIPLoader, UNETLoader, CR Apply LoRA Stack, UltimateSDUpscale, SaveImage, Image Comparer (rgthree), PreviewImage, CR LoRA Stack]
patterns: []
missing: []
parameters: {"batch_size": 0, "height": 4, "width": "832x1216 (0.68)"}
---

# 平台全量/ShakkerLabs 的 Flux FilmPortrait LoRA_1836379763278770177.json

> 来源文件 `comfyui_library/workflows/平台全量/ShakkerLabs 的 Flux FilmPortrait LoRA_1836379763278770177.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（21 个）：
- `SamplerCustomAdvanced` ★核心
- `KSamplerSelect` ★核心
- `CLIPTextEncode` ★核心
- `BasicScheduler`
- `VAELoader`
- `VAEDecode` ★核心
- `UpscaleModelLoader`
- `RandomNoise`
- `BasicGuider`
- `easy promptConcat`
- `CLIPTextEncodeFlux` ★核心
- `SDXLEmptyLatentSizePicker+` ★核心
- `Text String`
- `DualCLIPLoader`
- `UNETLoader` ★核心
- `CR Apply LoRA Stack`
- `UltimateSDUpscale`
- `SaveImage`
- `Image Comparer (rgthree)`
- `PreviewImage`
- `CR LoRA Stack`

## 关键参数

- `width` = `832x1216 (0.68)`
- `height` = `4`
- `batch_size` = `0`

## 知识

覆盖率 **90%**（19/21）

**有卡**：`SamplerCustomAdvanced`、`KSamplerSelect`、`CLIPTextEncode`、`BasicScheduler`、`VAELoader`、`VAEDecode`、`UpscaleModelLoader`、`RandomNoise`、`BasicGuider`、`easy promptConcat`、`CLIPTextEncodeFlux`、`SDXLEmptyLatentSizePicker+`、`Text String`、`DualCLIPLoader`、`UNETLoader`、`CR Apply LoRA Stack`、`UltimateSDUpscale`、`SaveImage`、`CR LoRA Stack`

**用到的条目**：VAEDecode、VAELoader、UNETLoader、CLIPTextEncode、KSamplerSelect、SamplerCustomAdvanced、CLIPTextEncodeFlux、SDXLEmptyLatentSizePicker+

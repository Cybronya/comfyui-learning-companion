---
key: 平台全量/Flux FilmPortrait LoRA by ShakkerLabs_1887680608641155073.json
name: Flux FilmPortrait LoRA by ShakkerLabs_1887680608641155073
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/Flux FilmPortrait LoRA by ShakkerLabs_1887680608641155073.json
hash: 1471fc6f4fa88b41
coverage: 0.954545
learned_at: 2026-11-14 00:27:40
nodes: [BasicScheduler, CR Apply LoRA Stack, CR LoRA Stack, SDXLEmptyLatentSizePicker+, CLIPTextEncode, CLIPTextEncodeFlux, easy promptConcat, VAELoader, UpscaleModelLoader, KSamplerSelect, BasicGuider, RandomNoise, UltimateSDUpscale, VAEDecode, SaveImage, easy cleanGpuUsed, SamplerCustomAdvanced, Image Comparer (rgthree), UNETLoader, DualCLIPLoader, easy prompt, easy prompt]
patterns: []
missing: []
parameters: {"batch_size": 0, "height": 1, "width": "832x1216 (0.68)"}
---

# 平台全量/Flux FilmPortrait LoRA by ShakkerLabs_1887680608641155073.json

> 来源文件 `comfyui_library/workflows/平台全量/Flux FilmPortrait LoRA by ShakkerLabs_1887680608641155073.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（22 个）：
- `BasicScheduler`
- `CR Apply LoRA Stack`
- `CR LoRA Stack`
- `SDXLEmptyLatentSizePicker+` ★核心
- `CLIPTextEncode` ★核心
- `CLIPTextEncodeFlux` ★核心
- `easy promptConcat`
- `VAELoader`
- `UpscaleModelLoader`
- `KSamplerSelect` ★核心
- `BasicGuider`
- `RandomNoise`
- `UltimateSDUpscale`
- `VAEDecode` ★核心
- `SaveImage`
- `easy cleanGpuUsed`
- `SamplerCustomAdvanced` ★核心
- `Image Comparer (rgthree)`
- `UNETLoader` ★核心
- `DualCLIPLoader`
- `easy prompt`
- `easy prompt`

## 关键参数

- `width` = `832x1216 (0.68)`
- `height` = `1`
- `batch_size` = `0`

## 知识

覆盖率 **95%**（21/22）

**有卡**：`BasicScheduler`、`CR Apply LoRA Stack`、`CR LoRA Stack`、`SDXLEmptyLatentSizePicker+`、`CLIPTextEncode`、`CLIPTextEncodeFlux`、`easy promptConcat`、`VAELoader`、`UpscaleModelLoader`、`KSamplerSelect`、`BasicGuider`、`RandomNoise`、`UltimateSDUpscale`、`VAEDecode`、`SaveImage`、`easy cleanGpuUsed`、`SamplerCustomAdvanced`、`UNETLoader`、`DualCLIPLoader`、`easy prompt`

**用到的条目**：VAEDecode、VAELoader、UNETLoader、CLIPTextEncode、KSamplerSelect、SamplerCustomAdvanced、CLIPTextEncodeFlux、SDXLEmptyLatentSizePicker+

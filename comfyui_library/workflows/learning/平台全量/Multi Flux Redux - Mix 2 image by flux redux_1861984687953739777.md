---
key: 平台全量/Multi Flux Redux - Mix 2 image by flux redux_1861984687953739777.json
name: Multi Flux Redux - Mix 2 image by flux redux_1861984687953739777
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/Multi Flux Redux - Mix 2 image by flux redux_1861984687953739777.json
hash: dcc3f86104538daa
coverage: 1
learned_at: 2026-11-14 00:46:58
nodes: [CLIPVisionLoader, StyleModelApply, StyleModelApply, FluxGuidance, CLIPTextEncode, LoadImage, CLIPVisionEncode, CLIPVisionEncode, StyleModelLoader, LoadImage, UNETLoader, DualCLIPLoader, VAELoader, BasicGuider, SamplerCustomAdvanced, BasicScheduler, KSamplerSelect, RandomNoise, EmptyLatentImage, VAEDecode, SaveImage]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 896, "width": 1152}
---

# 平台全量/Multi Flux Redux - Mix 2 image by flux redux_1861984687953739777.json

> 来源文件 `comfyui_library/workflows/平台全量/Multi Flux Redux - Mix 2 image by flux redux_1861984687953739777.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（21 个）：
- `CLIPVisionLoader`
- `StyleModelApply`
- `StyleModelApply`
- `FluxGuidance`
- `CLIPTextEncode` ★核心
- `LoadImage`
- `CLIPVisionEncode`
- `CLIPVisionEncode`
- `StyleModelLoader`
- `LoadImage`
- `UNETLoader` ★核心
- `DualCLIPLoader`
- `VAELoader`
- `BasicGuider`
- `SamplerCustomAdvanced` ★核心
- `BasicScheduler`
- `KSamplerSelect` ★核心
- `RandomNoise`
- `EmptyLatentImage` ★核心
- `VAEDecode` ★核心
- `SaveImage`

## 关键参数

- `width` = `1152`
- `height` = `896`
- `batch_size` = `1`

## 知识

覆盖率 **100%**（21/21）

**有卡**：`CLIPVisionLoader`、`StyleModelApply`、`FluxGuidance`、`CLIPTextEncode`、`LoadImage`、`CLIPVisionEncode`、`StyleModelLoader`、`UNETLoader`、`DualCLIPLoader`、`VAELoader`、`BasicGuider`、`SamplerCustomAdvanced`、`BasicScheduler`、`KSamplerSelect`、`RandomNoise`、`EmptyLatentImage`、`VAEDecode`、`SaveImage`

**用到的条目**：VAEDecode、VAELoader、UNETLoader、CLIPTextEncode、EmptyLatentImage、LoadImage、FluxGuidance、KSamplerSelect

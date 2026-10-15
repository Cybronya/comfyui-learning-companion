---
key: 图片生成/文生图/JoycaptionBetaOne单图反推+Flux生图_1952670790871396354.json
name: JoycaptionBetaOne单图反推+Flux生图_1952670790871396354
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/JoycaptionBetaOne单图反推+Flux生图_1952670790871396354.json
hash: 0b1dd5bcfa622153
coverage: 1
learned_at: 2026-10-15 22:26:36
nodes: [LoadImage, LayerUtility: LoadJoyCaptionBeta1Model, LayerUtility: JoyCaptionBeta1, LayerUtility: JoyCaptionBeta1ExtraOptions, VAELoader, KSamplerSelect, BasicGuider, BasicScheduler, SamplerCustomAdvanced, VAEDecode, DualCLIPLoader, RandomNoise, UNETLoader, CLIPTextEncode, ShowText, LoraLoaderModelOnly, EmptyLatentImage, SaveImage, LoraLoaderModelOnly]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 1024, "width": 1280}
---

# 图片生成/文生图/JoycaptionBetaOne单图反推+Flux生图_1952670790871396354.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/JoycaptionBetaOne单图反推+Flux生图_1952670790871396354.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（19 个）：
- `LoadImage`
- `LayerUtility: LoadJoyCaptionBeta1Model`
- `LayerUtility: JoyCaptionBeta1`
- `LayerUtility: JoyCaptionBeta1ExtraOptions`
- `VAELoader`
- `KSamplerSelect` ★核心
- `BasicGuider`
- `BasicScheduler`
- `SamplerCustomAdvanced` ★核心
- `VAEDecode` ★核心
- `DualCLIPLoader`
- `RandomNoise`
- `UNETLoader` ★核心
- `CLIPTextEncode` ★核心
- `ShowText`
- `LoraLoaderModelOnly` ★核心
- `EmptyLatentImage` ★核心
- `SaveImage`
- `LoraLoaderModelOnly` ★核心

## 关键参数

- `width` = `1280`
- `height` = `1024`
- `batch_size` = `1`

## 知识

覆盖率 **100%**（19/19）

**有卡**：`LoadImage`、`LayerUtility: LoadJoyCaptionBeta1Model`、`LayerUtility: JoyCaptionBeta1`、`LayerUtility: JoyCaptionBeta1ExtraOptions`、`VAELoader`、`KSamplerSelect`、`BasicGuider`、`BasicScheduler`、`SamplerCustomAdvanced`、`VAEDecode`、`DualCLIPLoader`、`RandomNoise`、`UNETLoader`、`CLIPTextEncode`、`ShowText`、`LoraLoaderModelOnly`、`EmptyLatentImage`、`SaveImage`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、EmptyLatentImage、LoadImage、UNETLoader、KSamplerSelect

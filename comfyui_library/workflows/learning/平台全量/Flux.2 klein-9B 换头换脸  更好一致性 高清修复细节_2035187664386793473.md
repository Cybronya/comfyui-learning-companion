---
key: 平台全量/Flux.2 klein-9B 换头换脸  更好一致性 高清修复细节_2035187664386793473.json
name: Flux.2 klein-9B 换头换脸  更好一致性 高清修复细节_2035187664386793473
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/平台全量/Flux.2 klein-9B 换头换脸  更好一致性 高清修复细节_2035187664386793473.json
hash: cb92b6107bb5ec9c
coverage: 0.944444
learned_at: 2026-11-14 00:28:56
nodes: [CLIPLoader, VAELoader, UNETLoader, KSampler, ReferenceLatent, ReferenceLatent, ConditioningZeroOut, EmptyFlux2LatentImage, VAEEncode, VAEEncode, LoraLoaderModelOnly, CLIPTextEncode, LoadImage, LoadImage, SaveImage, VAEDecode, LayerUtility: ImageScaleByAspectRatio V2, Image Comparer (rgthree)]
patterns: [image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 23552964039883, "steps": 8}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 平台全量/Flux.2 klein-9B 换头换脸  更好一致性 高清修复细节_2035187664386793473.json

> 来源文件 `comfyui_library/workflows/平台全量/Flux.2 klein-9B 换头换脸  更好一致性 高清修复细节_2035187664386793473.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（18 个）：
- `CLIPLoader`
- `VAELoader`
- `UNETLoader` ★核心
- `KSampler` ★核心
- `ReferenceLatent`
- `ReferenceLatent`
- `ConditioningZeroOut`
- `EmptyFlux2LatentImage`
- `VAEEncode` ★核心
- `VAEEncode` ★核心
- `LoraLoaderModelOnly` ★核心
- `CLIPTextEncode` ★核心
- `LoadImage`
- `LoadImage`
- `SaveImage`
- `VAEDecode` ★核心
- `LayerUtility: ImageScaleByAspectRatio V2`
- `Image Comparer (rgthree)`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `23552964039883`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **94%**（17/18）

**有卡**：`CLIPLoader`、`VAELoader`、`UNETLoader`、`KSampler`、`ReferenceLatent`、`ConditioningZeroOut`、`EmptyFlux2LatentImage`、`VAEEncode`、`LoraLoaderModelOnly`、`CLIPTextEncode`、`LoadImage`、`SaveImage`、`VAEDecode`、`LayerUtility: ImageScaleByAspectRatio V2`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPLoader、CLIPTextEncode、ConditioningZeroOut

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

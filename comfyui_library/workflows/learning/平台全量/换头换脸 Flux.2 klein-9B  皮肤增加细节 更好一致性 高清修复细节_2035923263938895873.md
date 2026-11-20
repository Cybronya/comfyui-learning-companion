---
key: 平台全量/换头换脸 Flux.2 klein-9B  皮肤增加细节 更好一致性 高清修复细节_2035923263938895873.json
name: 换头换脸 Flux.2 klein-9B  皮肤增加细节 更好一致性 高清修复细节_2035923263938895873
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/平台全量/换头换脸 Flux.2 klein-9B  皮肤增加细节 更好一致性 高清修复细节_2035923263938895873.json
hash: ae7241f60f71f881
coverage: 0.944444
learned_at: 2026-11-14 02:07:30
nodes: [CLIPLoader, VAELoader, UNETLoader, KSampler, ReferenceLatent, ReferenceLatent, ConditioningZeroOut, EmptyFlux2LatentImage, VAEEncode, VAEEncode, LoraLoaderModelOnly, CLIPTextEncode, SaveImage, VAEDecode, LayerUtility: ImageScaleByAspectRatio V2, Image Comparer (rgthree), LoadImage, LoadImage]
patterns: [image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 548033651754866, "steps": 8}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 平台全量/换头换脸 Flux.2 klein-9B  皮肤增加细节 更好一致性 高清修复细节_2035923263938895873.json

> 来源文件 `comfyui_library/workflows/平台全量/换头换脸 Flux.2 klein-9B  皮肤增加细节 更好一致性 高清修复细节_2035923263938895873.json`

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
- `SaveImage`
- `VAEDecode` ★核心
- `LayerUtility: ImageScaleByAspectRatio V2`
- `Image Comparer (rgthree)`
- `LoadImage`
- `LoadImage`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `548033651754866`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **94%**（17/18）

**有卡**：`CLIPLoader`、`VAELoader`、`UNETLoader`、`KSampler`、`ReferenceLatent`、`ConditioningZeroOut`、`EmptyFlux2LatentImage`、`VAEEncode`、`LoraLoaderModelOnly`、`CLIPTextEncode`、`SaveImage`、`VAEDecode`、`LayerUtility: ImageScaleByAspectRatio V2`、`LoadImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPLoader、CLIPTextEncode、ConditioningZeroOut

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

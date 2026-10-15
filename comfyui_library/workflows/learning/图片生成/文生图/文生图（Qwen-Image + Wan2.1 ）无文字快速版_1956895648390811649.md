---
key: 图片生成/文生图/文生图（Qwen-Image + Wan2.1 ）无文字快速版_1956895648390811649.json
name: 文生图（Qwen-Image + Wan2.1 ）无文字快速版_1956895648390811649
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/文生图（Qwen-Image + Wan2.1 ）无文字快速版_1956895648390811649.json
hash: 47fd1c174cbb8307
coverage: 0.971429
learned_at: 2026-10-15 22:28:51
nodes: [CLIPLoader, VAELoader, CLIPTextEncode, CLIPTextEncode, EmptySD3LatentImage, CLIPLoader, CLIPTextEncode, CLIPTextEncode, LoraLoaderModelOnly, UNETLoader, Note, ImageSharpen, EsesImageEffectBloom, BetterFilmGrain, UpscaleModelLoader, PathchSageAttentionKJ, ModelSamplingSD3, VAEEncode, LayerUtility: PurgeVRAM, VAEDecode, ImageScaleToMegapixels, JWInteger, JWInteger, VAELoader, LoraLoaderModelOnly, LoraLoaderModelOnly, CR Prompt Text, SaveImage, SaveImage, VAEDecode, UNETLoader, ModelSamplingAuraFlow, CFGNorm, KSampler, KSampler]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 0.15000000000000002, "sampler_name": "uni_pc", "scheduler": "simple", "seed": 965369974524576, "steps": 10}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/文生图/文生图（Qwen-Image + Wan2.1 ）无文字快速版_1956895648390811649.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/文生图（Qwen-Image + Wan2.1 ）无文字快速版_1956895648390811649.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（35 个）：
- `CLIPLoader`
- `VAELoader`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `EmptySD3LatentImage`
- `CLIPLoader`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `Note`
- `ImageSharpen`
- `EsesImageEffectBloom`
- `BetterFilmGrain`
- `UpscaleModelLoader`
- `PathchSageAttentionKJ`
- `ModelSamplingSD3`
- `VAEEncode` ★核心
- `LayerUtility: PurgeVRAM`
- `VAEDecode` ★核心
- `ImageScaleToMegapixels`
- `JWInteger`
- `JWInteger`
- `VAELoader`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `CR Prompt Text`
- `SaveImage`
- `SaveImage`
- `VAEDecode` ★核心
- `UNETLoader` ★核心
- `ModelSamplingAuraFlow`
- `CFGNorm`
- `KSampler` ★核心
- `KSampler` ★核心

## 关键参数

- `seed` = `965369974524576`
- `steps` = `10`
- `cfg` = `1`
- `sampler_name` = `uni_pc`
- `scheduler` = `simple`
- `denoise` = `0.15000000000000002`

## 知识

覆盖率 **97%**（34/35）

**有卡**：`CLIPLoader`、`VAELoader`、`CLIPTextEncode`、`EmptySD3LatentImage`、`LoraLoaderModelOnly`、`UNETLoader`、`ImageSharpen`、`EsesImageEffectBloom`、`BetterFilmGrain`、`UpscaleModelLoader`、`PathchSageAttentionKJ`、`ModelSamplingSD3`、`VAEEncode`、`LayerUtility: PurgeVRAM`、`VAEDecode`、`ImageScaleToMegapixels`、`JWInteger`、`CR Prompt Text`、`SaveImage`、`ModelSamplingAuraFlow`、`CFGNorm`、`KSampler`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、UNETLoader、CFGNorm

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

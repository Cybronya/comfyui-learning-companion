---
key: 图片生成/文生图/文生图（Qwen-Image + Wan2.1 ）无文字快速版_1956895648390811649.json
name: 文生图（Qwen-Image + Wan2.1 ）无文字快速版_1956895648390811649
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/文生图（Qwen-Image + Wan2.1 ）无文字快速版_1956895648390811649.json
hash: 47fd1c174cbb8307
coverage: 0.914286
learned_at: 2026-10-10 20:59:49
nodes: [CLIPLoader, VAELoader, CLIPTextEncode, CLIPTextEncode, EmptySD3LatentImage, CLIPLoader, CLIPTextEncode, CLIPTextEncode, LoraLoaderModelOnly, UNETLoader, Note, ImageSharpen, EsesImageEffectBloom, BetterFilmGrain, UpscaleModelLoader, PathchSageAttentionKJ, ModelSamplingSD3, VAEEncode, LayerUtility: PurgeVRAM, VAEDecode, ImageScaleToMegapixels, JWInteger, JWInteger, VAELoader, LoraLoaderModelOnly, LoraLoaderModelOnly, CR Prompt Text, SaveImage, SaveImage, VAEDecode, UNETLoader, ModelSamplingAuraFlow, CFGNorm, KSampler, KSampler]
patterns: []
missing: [LayerUtility: PurgeVRAM, CR Prompt Text]
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 0.15000000000000002, "sampler_name": "uni_pc", "scheduler": "simple", "seed": 965369974524576, "steps": 10}
discoveries: [次要节点 `LayerUtility: PurgeVRAM` 知识库中没有该节点类型的任何知识, 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/文生图/文生图（Qwen-Image + Wan2.1 ）无文字快速版_1956895648390811649.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/文生图（Qwen-Image + Wan2.1 ）无文字快速版_1956895648390811649.json`

## 结构

**节点**（35 个）：
- `CLIPLoader`
- `VAELoader`
- `CLIPTextEncode`
- `CLIPTextEncode`
- `EmptySD3LatentImage`
- `CLIPLoader`
- `CLIPTextEncode`
- `CLIPTextEncode`
- `LoraLoaderModelOnly`
- `UNETLoader`
- `Note`
- `ImageSharpen`
- `EsesImageEffectBloom`
- `BetterFilmGrain`
- `UpscaleModelLoader`
- `PathchSageAttentionKJ`
- `ModelSamplingSD3`
- `VAEEncode`
- `LayerUtility: PurgeVRAM`
- `VAEDecode`
- `ImageScaleToMegapixels`
- `JWInteger`
- `JWInteger`
- `VAELoader`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `CR Prompt Text`
- `SaveImage`
- `SaveImage`
- `VAEDecode`
- `UNETLoader`
- `ModelSamplingAuraFlow`
- `CFGNorm`
- `KSampler`
- `KSampler`

## 关键参数

- `cfg` = `1`
- `denoise` = `0.15000000000000002`
- `sampler_name` = `uni_pc`
- `scheduler` = `simple`
- `seed` = `965369974524576`
- `steps` = `10`

## 知识

覆盖率 **91%**（32/35）

**有卡**：`CLIPLoader`、`VAELoader`、`CLIPTextEncode`、`EmptySD3LatentImage`、`LoraLoaderModelOnly`、`UNETLoader`、`Note`、`ImageSharpen`、`EsesImageEffectBloom`、`BetterFilmGrain`、`UpscaleModelLoader`、`PathchSageAttentionKJ`、`ModelSamplingSD3`、`VAEEncode`、`LayerUtility: PurgeVRAM`、`VAEDecode`、`ImageScaleToMegapixels`、`JWInteger`、`CR Prompt Text`、`SaveImage`、`ModelSamplingAuraFlow`

**缺卡**（2）：`LayerUtility: PurgeVRAM`、`CR Prompt Text`

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- 次要节点 `LayerUtility: PurgeVRAM` 知识库中没有该节点类型的任何知识
- 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

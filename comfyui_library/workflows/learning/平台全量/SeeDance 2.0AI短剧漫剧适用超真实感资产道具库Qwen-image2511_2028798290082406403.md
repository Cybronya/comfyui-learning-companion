---
key: 平台全量/SeeDance 2.0AI短剧漫剧适用超真实感资产道具库Qwen-image2511_2028798290082406403.json
name: SeeDance 2.0AI短剧漫剧适用超真实感资产道具库Qwen-image2511_2028798290082406403
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/平台全量/SeeDance 2.0AI短剧漫剧适用超真实感资产道具库Qwen-image2511_2028798290082406403.json
hash: f2bc4dac4730343a
coverage: 0.892857
learned_at: 2026-11-14 00:58:35
nodes: [TextEncodeQwenImageEditPlus, ModelSamplingAuraFlow, CFGNorm, FluxKontextMultiReferenceLatentMethod, KSampler, VAEDecode, LoraLoaderModelOnly, LoraLoaderModelOnly, CLIPLoader, VAELoader, CR Prompt List, TextEncodeQwenImageEditPlus, SaveImage, JWInteger, JWInteger, RHHiddenNodes, UNETLoader, VAEEncode, SaveImage, FluxKontextMultiReferenceLatentMethod, Any Switch (rgthree), Fast Groups Bypasser (rgthree), LoadImage, PrimitiveStringMultiline, WujiSampler, WujiCleaner, WujiEditor, WujiUpscaler]
patterns: [image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 786088284134603, "steps": 4}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 平台全量/SeeDance 2.0AI短剧漫剧适用超真实感资产道具库Qwen-image2511_2028798290082406403.json

> 来源文件 `comfyui_library/workflows/平台全量/SeeDance 2.0AI短剧漫剧适用超真实感资产道具库Qwen-image2511_2028798290082406403.json`

## 结构

**生成流程**：Model → Encode → Sampling → Decode → Process → Output → Other

**节点**（28 个）：
- `TextEncodeQwenImageEditPlus`
- `ModelSamplingAuraFlow`
- `CFGNorm`
- `FluxKontextMultiReferenceLatentMethod`
- `KSampler` ★核心
- `VAEDecode` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `CLIPLoader`
- `VAELoader`
- `CR Prompt List`
- `TextEncodeQwenImageEditPlus`
- `SaveImage`
- `JWInteger`
- `JWInteger`
- `RHHiddenNodes`
- `UNETLoader` ★核心
- `VAEEncode` ★核心
- `SaveImage`
- `FluxKontextMultiReferenceLatentMethod`
- `Any Switch (rgthree)`
- `Fast Groups Bypasser (rgthree)`
- `LoadImage`
- `PrimitiveStringMultiline`
- `WujiSampler` ★核心
- `WujiCleaner`
- `WujiEditor`
- `WujiUpscaler`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `786088284134603`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **89%**（25/28）

**有卡**：`TextEncodeQwenImageEditPlus`、`ModelSamplingAuraFlow`、`CFGNorm`、`FluxKontextMultiReferenceLatentMethod`、`KSampler`、`VAEDecode`、`LoraLoaderModelOnly`、`CLIPLoader`、`VAELoader`、`CR Prompt List`、`SaveImage`、`JWInteger`、`RHHiddenNodes`、`UNETLoader`、`VAEEncode`、`LoadImage`、`WujiSampler`、`WujiCleaner`、`WujiEditor`、`WujiUpscaler`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPLoader、LoadImage、CFGNorm

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

---
key: 图片生成/文生图/SeeDance 2.0AI短剧漫剧专用超真实感资产道具库Qwen-image2511_2026667723161346050.json
name: SeeDance 2.0AI短剧漫剧专用超真实感资产道具库Qwen-image2511_2026667723161346050
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/SeeDance 2.0AI短剧漫剧专用超真实感资产道具库Qwen-image2511_2026667723161346050.json
hash: 79cf11ab248bbefc
coverage: 0.884615
learned_at: 2026-10-19 22:29:53
nodes: [TextEncodeQwenImageEditPlus, CFGNorm, LoadImage, SaveImage, WujiCleaner, JWInteger, JWInteger, WujiSampler, RHHiddenNodes, SaveImage, WujiUpscaler, WujiEditor, Fast Groups Bypasser (rgthree), VAEEncode, FluxKontextMultiReferenceLatentMethod, FluxKontextMultiReferenceLatentMethod, Any Switch (rgthree), ModelSamplingAuraFlow, KSampler, VAEDecode, WujiCleaner, CR LoRA Stack, PrimitiveStringMultiline, CheckpointLoaderSimple, CR Prompt List, TextEncodeQwenImageEditPlus]
patterns: [image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "checkpoint": "WuJi_Qwen2511-AIONSFW聚合版_2603.safetensors", "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 1081275042074653, "steps": 4}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/文生图/SeeDance 2.0AI短剧漫剧专用超真实感资产道具库Qwen-image2511_2026667723161346050.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/SeeDance 2.0AI短剧漫剧专用超真实感资产道具库Qwen-image2511_2026667723161346050.json`

## 结构

**生成流程**：Model → Encode → Sampling → Decode → Process → Output → Other

**节点**（26 个）：
- `TextEncodeQwenImageEditPlus`
- `CFGNorm`
- `LoadImage`
- `SaveImage`
- `WujiCleaner`
- `JWInteger`
- `JWInteger`
- `WujiSampler` ★核心
- `RHHiddenNodes`
- `SaveImage`
- `WujiUpscaler`
- `WujiEditor`
- `Fast Groups Bypasser (rgthree)`
- `VAEEncode` ★核心
- `FluxKontextMultiReferenceLatentMethod`
- `FluxKontextMultiReferenceLatentMethod`
- `Any Switch (rgthree)`
- `ModelSamplingAuraFlow`
- `KSampler` ★核心
- `VAEDecode` ★核心
- `WujiCleaner`
- `CR LoRA Stack`
- `PrimitiveStringMultiline`
- `CheckpointLoaderSimple` ★核心
- `CR Prompt List`
- `TextEncodeQwenImageEditPlus`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `1081275042074653`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`
- `checkpoint` = `WuJi_Qwen2511-AIONSFW聚合版_2603.safetensors`

## 知识

覆盖率 **88%**（23/26）

**有卡**：`TextEncodeQwenImageEditPlus`、`CFGNorm`、`LoadImage`、`SaveImage`、`WujiCleaner`、`JWInteger`、`WujiSampler`、`RHHiddenNodes`、`WujiUpscaler`、`WujiEditor`、`VAEEncode`、`FluxKontextMultiReferenceLatentMethod`、`ModelSamplingAuraFlow`、`KSampler`、`VAEDecode`、`CR LoRA Stack`、`CheckpointLoaderSimple`、`CR Prompt List`

**用到的条目**：KSampler、VAEDecode、CheckpointLoaderSimple、LoadImage、CFGNorm、WujiSampler、FluxKontextMultiReferenceLatentMethod、TextEncodeQwenImageEditPlus

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

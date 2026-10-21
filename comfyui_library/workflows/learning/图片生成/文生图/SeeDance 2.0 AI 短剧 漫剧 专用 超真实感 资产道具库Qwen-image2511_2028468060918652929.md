---
key: 图片生成/文生图/SeeDance 2.0 AI 短剧 漫剧 专用 超真实感 资产道具库Qwen-image2511_2028468060918652929.json
name: SeeDance 2.0 AI 短剧 漫剧 专用 超真实感 资产道具库Qwen-image2511_2028468060918652929
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/SeeDance 2.0 AI 短剧 漫剧 专用 超真实感 资产道具库Qwen-image2511_2028468060918652929.json
hash: 1fa14679c04fe287
coverage: 0.892857
learned_at: 2026-10-20 23:21:47
nodes: [TextEncodeQwenImageEditPlus, ModelSamplingAuraFlow, CFGNorm, FluxKontextMultiReferenceLatentMethod, KSampler, VAEDecode, PrimitiveStringMultiline, LoraLoaderModelOnly, LoraLoaderModelOnly, CLIPLoader, VAELoader, LoadImage, CR Prompt List, TextEncodeQwenImageEditPlus, SaveImage, WujiCleaner, JWInteger, JWInteger, WujiSampler, RHHiddenNodes, UNETLoader, VAEEncode, SaveImage, FluxKontextMultiReferenceLatentMethod, Any Switch (rgthree), WujiUpscaler, WujiEditor, Fast Groups Bypasser (rgthree)]
patterns: [image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 590737319366375, "steps": 4}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/文生图/SeeDance 2.0 AI 短剧 漫剧 专用 超真实感 资产道具库Qwen-image2511_2028468060918652929.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/SeeDance 2.0 AI 短剧 漫剧 专用 超真实感 资产道具库Qwen-image2511_2028468060918652929.json`

## 结构

**生成流程**：Model → Encode → Sampling → Decode → Process → Output → Other

**节点**（28 个）：
- `TextEncodeQwenImageEditPlus`
- `ModelSamplingAuraFlow`
- `CFGNorm`
- `FluxKontextMultiReferenceLatentMethod`
- `KSampler` ★核心
- `VAEDecode` ★核心
- `PrimitiveStringMultiline`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `CLIPLoader`
- `VAELoader`
- `LoadImage`
- `CR Prompt List`
- `TextEncodeQwenImageEditPlus`
- `SaveImage`
- `WujiCleaner`
- `JWInteger`
- `JWInteger`
- `WujiSampler` ★核心
- `RHHiddenNodes`
- `UNETLoader` ★核心
- `VAEEncode` ★核心
- `SaveImage`
- `FluxKontextMultiReferenceLatentMethod`
- `Any Switch (rgthree)`
- `WujiUpscaler`
- `WujiEditor`
- `Fast Groups Bypasser (rgthree)`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `590737319366375`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **89%**（25/28）

**有卡**：`TextEncodeQwenImageEditPlus`、`ModelSamplingAuraFlow`、`CFGNorm`、`FluxKontextMultiReferenceLatentMethod`、`KSampler`、`VAEDecode`、`LoraLoaderModelOnly`、`CLIPLoader`、`VAELoader`、`LoadImage`、`CR Prompt List`、`SaveImage`、`WujiCleaner`、`JWInteger`、`WujiSampler`、`RHHiddenNodes`、`UNETLoader`、`VAEEncode`、`WujiUpscaler`、`WujiEditor`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPLoader、LoadImage、CFGNorm

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

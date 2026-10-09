---
key: 图片生成/文生图/文生图（Qwen-Image + Wan2.2 低噪）_1968189243870838785.json
name: 文生图（Qwen-Image + Wan2.2 低噪）_1968189243870838785.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/文生图（Qwen-Image + Wan2.2 低噪）_1968189243870838785.json
hash: 51b3a4f4f2e27d1b
coverage: 0.95
learned_at: 2026-10-09 02:01:38
nodes: [VAELoader, CLIPTextEncode, VAELoader, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, ModelSamplingSD3, VAEEncode, CLIPTextEncode, ImageScaleToMegapixels, VAEDecode, UpscaleModelLoader, SaveImage, CLIPLoader, VAEDecode, ImageScaleToMegapixels, BetterFilmGrain, ImageSharpen, JWInteger, JWInteger, CLIPTextEncode, PrimitiveStringMultiline, CLIPTextEncode, CLIPLoader, KSampler, KSampler, UNETLoader, ModelSamplingAuraFlow, CFGNorm, NunchakuQwenImageDiTLoader, LoraLoaderModelOnly, ModelSamplingAuraFlow, LoraLoaderModelOnly, JWInteger, JWInteger, EmptySD3LatentImage, Note, SaveImage, LazySwitch2way, PrimitiveBoolean]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 1088836026456039, "steps": 8}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/文生图/文生图（Qwen-Image + Wan2.2 低噪）_1968189243870838785.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/1968189243870838785.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（40 个）：
- `VAELoader`
- `CLIPTextEncode` ★核心
- `VAELoader`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `ModelSamplingSD3`
- `VAEEncode` ★核心
- `CLIPTextEncode` ★核心
- `ImageScaleToMegapixels`
- `VAEDecode` ★核心
- `UpscaleModelLoader`
- `SaveImage`
- `CLIPLoader`
- `VAEDecode` ★核心
- `ImageScaleToMegapixels`
- `BetterFilmGrain`
- `ImageSharpen`
- `JWInteger`
- `JWInteger`
- `CLIPTextEncode` ★核心
- `PrimitiveStringMultiline`
- `CLIPTextEncode` ★核心
- `CLIPLoader`
- `KSampler` ★核心
- `KSampler` ★核心
- `UNETLoader` ★核心
- `ModelSamplingAuraFlow`
- `CFGNorm`
- `NunchakuQwenImageDiTLoader`
- `LoraLoaderModelOnly` ★核心
- `ModelSamplingAuraFlow`
- `LoraLoaderModelOnly` ★核心
- `JWInteger`
- `JWInteger`
- `EmptySD3LatentImage`
- `Note`
- `SaveImage`
- `LazySwitch2way`
- `PrimitiveBoolean`

## 关键参数

- `seed` = `1088836026456039`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **95%**（38/40）

**有卡**：`VAELoader`、`CLIPTextEncode`、`UNETLoader`、`LoraLoaderModelOnly`、`ModelSamplingSD3`、`VAEEncode`、`ImageScaleToMegapixels`、`VAEDecode`、`UpscaleModelLoader`、`SaveImage`、`CLIPLoader`、`BetterFilmGrain`、`ImageSharpen`、`JWInteger`、`KSampler`、`ModelSamplingAuraFlow`、`CFGNorm`、`NunchakuQwenImageDiTLoader`、`EmptySD3LatentImage`、`LazySwitch2way`、`PrimitiveBoolean`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、UNETLoader、CFGNorm

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

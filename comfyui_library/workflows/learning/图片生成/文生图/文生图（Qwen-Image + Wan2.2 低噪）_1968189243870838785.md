---
key: 图片生成/文生图/文生图（Qwen-Image + Wan2.2 低噪）_1968189243870838785.json
name: 文生图（Qwen-Image + Wan2.2 低噪）_1968189243870838785
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/文生图（Qwen-Image + Wan2.2 低噪）_1968189243870838785.json
hash: 51b3a4f4f2e27d1b
coverage: 0.95
learned_at: 2026-10-10 20:59:49
nodes: [VAELoader, CLIPTextEncode, VAELoader, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, ModelSamplingSD3, VAEEncode, CLIPTextEncode, ImageScaleToMegapixels, VAEDecode, UpscaleModelLoader, SaveImage, CLIPLoader, VAEDecode, ImageScaleToMegapixels, BetterFilmGrain, ImageSharpen, JWInteger, JWInteger, CLIPTextEncode, PrimitiveStringMultiline, CLIPTextEncode, CLIPLoader, KSampler, KSampler, UNETLoader, ModelSamplingAuraFlow, CFGNorm, NunchakuQwenImageDiTLoader, LoraLoaderModelOnly, ModelSamplingAuraFlow, LoraLoaderModelOnly, JWInteger, JWInteger, EmptySD3LatentImage, Note, SaveImage, LazySwitch2way, PrimitiveBoolean]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 1088836026456039, "steps": 8}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/文生图/文生图（Qwen-Image + Wan2.2 低噪）_1968189243870838785.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/文生图（Qwen-Image + Wan2.2 低噪）_1968189243870838785.json`

## 结构

**节点**（40 个）：
- `VAELoader`
- `CLIPTextEncode`
- `VAELoader`
- `UNETLoader`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `ModelSamplingSD3`
- `VAEEncode`
- `CLIPTextEncode`
- `ImageScaleToMegapixels`
- `VAEDecode`
- `UpscaleModelLoader`
- `SaveImage`
- `CLIPLoader`
- `VAEDecode`
- `ImageScaleToMegapixels`
- `BetterFilmGrain`
- `ImageSharpen`
- `JWInteger`
- `JWInteger`
- `CLIPTextEncode`
- `PrimitiveStringMultiline`
- `CLIPTextEncode`
- `CLIPLoader`
- `KSampler`
- `KSampler`
- `UNETLoader`
- `ModelSamplingAuraFlow`
- `CFGNorm`
- `NunchakuQwenImageDiTLoader`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `LoraLoaderModelOnly`
- `JWInteger`
- `JWInteger`
- `EmptySD3LatentImage`
- `Note`
- `SaveImage`
- `LazySwitch2way`
- `PrimitiveBoolean`

## 关键参数

- `cfg` = `1`
- `denoise` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `seed` = `1088836026456039`
- `steps` = `8`

## 知识

覆盖率 **95%**（38/40）

**有卡**：`VAELoader`、`CLIPTextEncode`、`UNETLoader`、`LoraLoaderModelOnly`、`ModelSamplingSD3`、`VAEEncode`、`ImageScaleToMegapixels`、`VAEDecode`、`UpscaleModelLoader`、`SaveImage`、`CLIPLoader`、`BetterFilmGrain`、`ImageSharpen`、`JWInteger`、`PrimitiveStringMultiline`、`KSampler`、`ModelSamplingAuraFlow`、`CFGNorm`、`NunchakuQwenImageDiTLoader`、`EmptySD3LatentImage`、`Note`

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

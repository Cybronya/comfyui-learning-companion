---
key: 平台全量/Flux found footage images_1881247430573268993.json
name: Flux found footage images_1881247430573268993
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/Flux found footage images_1881247430573268993.json
hash: 9f03a13dac1bcce3
coverage: 0.733333
learned_at: 2026-11-14 00:28:07
nodes: [FluxGuidance, ModelSamplingFlux, CLIPTextEncode, RandomNoise, SamplerCustomAdvanced, BasicGuider, KSamplerSelect, BasicScheduler, EmptyLatentImage, Note, Note, Note, UnetLoaderGGUF, StringConstantMultiline, LoraLoaderModelOnly, LoraLoaderModelOnly, Note, Note, PreviewImage, StringConstantMultiline, ShowText|pysssss, String Replace (mtb), DualCLIPLoader, VAELoader, LoraLoaderModelOnly, VAEDecode, FilmGrain, SaveImage, Reroute, TeaCache]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 512, "width": 512}
---

# 平台全量/Flux found footage images_1881247430573268993.json

> 来源文件 `comfyui_library/workflows/平台全量/Flux found footage images_1881247430573268993.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（30 个）：
- `FluxGuidance`
- `ModelSamplingFlux`
- `CLIPTextEncode` ★核心
- `RandomNoise`
- `SamplerCustomAdvanced` ★核心
- `BasicGuider`
- `KSamplerSelect` ★核心
- `BasicScheduler`
- `EmptyLatentImage` ★核心
- `Note`
- `Note`
- `Note`
- `UnetLoaderGGUF` ★核心
- `StringConstantMultiline`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `Note`
- `Note`
- `PreviewImage`
- `StringConstantMultiline`
- `ShowText|pysssss`
- `String Replace (mtb)`
- `DualCLIPLoader`
- `VAELoader`
- `LoraLoaderModelOnly` ★核心
- `VAEDecode` ★核心
- `FilmGrain`
- `SaveImage`
- `Reroute`
- `TeaCache`

## 关键参数

- `width` = `512`
- `height` = `512`
- `batch_size` = `1`

## 知识

覆盖率 **73%**（22/30）

**有卡**：`FluxGuidance`、`ModelSamplingFlux`、`CLIPTextEncode`、`RandomNoise`、`SamplerCustomAdvanced`、`BasicGuider`、`KSamplerSelect`、`BasicScheduler`、`EmptyLatentImage`、`UnetLoaderGGUF`、`StringConstantMultiline`、`LoraLoaderModelOnly`、`String Replace (mtb)`、`DualCLIPLoader`、`VAELoader`、`VAEDecode`、`FilmGrain`、`SaveImage`、`TeaCache`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、EmptyLatentImage、FluxGuidance、KSamplerSelect、SamplerCustomAdvanced

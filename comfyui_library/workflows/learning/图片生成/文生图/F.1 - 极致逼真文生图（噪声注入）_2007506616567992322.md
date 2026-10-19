---
key: 图片生成/文生图/F.1 - 极致逼真文生图（噪声注入）_2007506616567992322.json
name: F.1 - 极致逼真文生图（噪声注入）_2007506616567992322
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/F.1 - 极致逼真文生图（噪声注入）_2007506616567992322.json
hash: ae0f0f1717002a8a
coverage: 0.931034
learned_at: 2026-10-19 22:00:28
nodes: [LatentInterpolate, DisableNoise, BasicGuider, LoraLoaderModelOnly, PrimitiveNode, PrimitiveNode, InjectLatentNoise+, FluxGuidance, ModelSamplingFlux, SplitSigmasDenoise, BasicGuider, BasicScheduler, SamplerCustomAdvanced, EmptyLatentImage, RandomNoise, LoraLoaderModelOnly, ImageSmartSharpen+, SamplerCustomAdvanced, VAEDecode, BasicScheduler, RandomNoise, SamplerCustomAdvanced, KSamplerSelect, UNETLoader, DualCLIPLoader, VAELoader, LoraLoaderModelOnly, SaveImage, CLIPTextEncode]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 1920, "width": 1024}
---

# 图片生成/文生图/F.1 - 极致逼真文生图（噪声注入）_2007506616567992322.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/F.1 - 极致逼真文生图（噪声注入）_2007506616567992322.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（29 个）：
- `LatentInterpolate`
- `DisableNoise`
- `BasicGuider`
- `LoraLoaderModelOnly` ★核心
- `PrimitiveNode`
- `PrimitiveNode`
- `InjectLatentNoise+`
- `FluxGuidance`
- `ModelSamplingFlux`
- `SplitSigmasDenoise`
- `BasicGuider`
- `BasicScheduler`
- `SamplerCustomAdvanced` ★核心
- `EmptyLatentImage` ★核心
- `RandomNoise`
- `LoraLoaderModelOnly` ★核心
- `ImageSmartSharpen+`
- `SamplerCustomAdvanced` ★核心
- `VAEDecode` ★核心
- `BasicScheduler`
- `RandomNoise`
- `SamplerCustomAdvanced` ★核心
- `KSamplerSelect` ★核心
- `UNETLoader` ★核心
- `DualCLIPLoader`
- `VAELoader`
- `LoraLoaderModelOnly` ★核心
- `SaveImage`
- `CLIPTextEncode` ★核心

## 关键参数

- `width` = `1024`
- `height` = `1920`
- `batch_size` = `1`

## 知识

覆盖率 **93%**（27/29）

**有卡**：`LatentInterpolate`、`DisableNoise`、`BasicGuider`、`LoraLoaderModelOnly`、`InjectLatentNoise+`、`FluxGuidance`、`ModelSamplingFlux`、`SplitSigmasDenoise`、`BasicScheduler`、`SamplerCustomAdvanced`、`EmptyLatentImage`、`RandomNoise`、`ImageSmartSharpen+`、`VAEDecode`、`KSamplerSelect`、`UNETLoader`、`DualCLIPLoader`、`VAELoader`、`SaveImage`、`CLIPTextEncode`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPTextEncode、EmptyLatentImage、FluxGuidance、KSamplerSelect

---
key: 平台全量/FLUX.1_wavespeed加速_1879188150349193218.json
name: FLUX.1_wavespeed加速_1879188150349193218
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/FLUX.1_wavespeed加速_1879188150349193218.json
hash: 48634141f0b48ed5
coverage: 0.888889
learned_at: 2026-11-14 00:25:07
nodes: [FluxGuidance, BasicGuider, KSamplerSelect, ModelSamplingFlux, VAEDecode, PrimitiveNode, EmptyLatentImage, PrimitiveNode, CLIPTextEncode, RandomNoise, ApplyFBCacheOnModel, EnhancedCompileModel, SaveImage, VAELoader, DualCLIPLoader, UNETLoader, BasicScheduler, SamplerCustomAdvanced]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 1024, "width": 1024}
---

# 平台全量/FLUX.1_wavespeed加速_1879188150349193218.json

> 来源文件 `comfyui_library/workflows/平台全量/FLUX.1_wavespeed加速_1879188150349193218.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（18 个）：
- `FluxGuidance`
- `BasicGuider`
- `KSamplerSelect` ★核心
- `ModelSamplingFlux`
- `VAEDecode` ★核心
- `PrimitiveNode`
- `EmptyLatentImage` ★核心
- `PrimitiveNode`
- `CLIPTextEncode` ★核心
- `RandomNoise`
- `ApplyFBCacheOnModel`
- `EnhancedCompileModel`
- `SaveImage`
- `VAELoader`
- `DualCLIPLoader`
- `UNETLoader` ★核心
- `BasicScheduler`
- `SamplerCustomAdvanced` ★核心

## 关键参数

- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`

## 知识

覆盖率 **89%**（16/18）

**有卡**：`FluxGuidance`、`BasicGuider`、`KSamplerSelect`、`ModelSamplingFlux`、`VAEDecode`、`EmptyLatentImage`、`CLIPTextEncode`、`RandomNoise`、`ApplyFBCacheOnModel`、`EnhancedCompileModel`、`SaveImage`、`VAELoader`、`DualCLIPLoader`、`UNETLoader`、`BasicScheduler`、`SamplerCustomAdvanced`

**用到的条目**：VAEDecode、VAELoader、UNETLoader、CLIPTextEncode、EmptyLatentImage、FluxGuidance、KSamplerSelect、SamplerCustomAdvanced

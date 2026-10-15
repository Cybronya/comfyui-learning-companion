---
key: 图片生成/文生图/腾讯flux.1-dev-SRPO文生图_1966306088582811649.json
name: 腾讯flux.1-dev-SRPO文生图_1966306088582811649
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/腾讯flux.1-dev-SRPO文生图_1966306088582811649.json
hash: 992ece76e5bfca07
coverage: 0.875
learned_at: 2026-10-15 22:29:03
nodes: [DualCLIPLoader, BasicScheduler, KSamplerSelect, SamplerCustomAdvanced, RandomNoise, ModelSamplingFlux, EmptySD3LatentImage, Note, VAELoader, BasicGuider, FluxGuidance, CLIPTextEncode, RH_Translator, Note, UNETLoader, SeedVR2ExtraArgs, CR SDXL Aspect Ratio, SaveImage, VAEDecode, easy clearCacheAll, PreviewImage, SeedVR2BlockSwap, SeedVR2GGUF, MathExpression|pysssss]
patterns: []
missing: []
---

# 图片生成/文生图/腾讯flux.1-dev-SRPO文生图_1966306088582811649.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/腾讯flux.1-dev-SRPO文生图_1966306088582811649.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（24 个）：
- `DualCLIPLoader`
- `BasicScheduler`
- `KSamplerSelect` ★核心
- `SamplerCustomAdvanced` ★核心
- `RandomNoise`
- `ModelSamplingFlux`
- `EmptySD3LatentImage`
- `Note`
- `VAELoader`
- `BasicGuider`
- `FluxGuidance`
- `CLIPTextEncode` ★核心
- `RH_Translator`
- `Note`
- `UNETLoader` ★核心
- `SeedVR2ExtraArgs`
- `CR SDXL Aspect Ratio`
- `SaveImage`
- `VAEDecode` ★核心
- `easy clearCacheAll`
- `PreviewImage`
- `SeedVR2BlockSwap`
- `SeedVR2GGUF`
- `MathExpression|pysssss`

## 知识

覆盖率 **88%**（21/24）

**有卡**：`DualCLIPLoader`、`BasicScheduler`、`KSamplerSelect`、`SamplerCustomAdvanced`、`RandomNoise`、`ModelSamplingFlux`、`EmptySD3LatentImage`、`VAELoader`、`BasicGuider`、`FluxGuidance`、`CLIPTextEncode`、`RH_Translator`、`UNETLoader`、`SeedVR2ExtraArgs`、`CR SDXL Aspect Ratio`、`SaveImage`、`VAEDecode`、`easy clearCacheAll`、`SeedVR2BlockSwap`、`SeedVR2GGUF`、`MathExpression|pysssss`

**用到的条目**：VAEDecode、VAELoader、UNETLoader、CLIPTextEncode、FluxGuidance、KSamplerSelect、SamplerCustomAdvanced、SeedVR2BlockSwap

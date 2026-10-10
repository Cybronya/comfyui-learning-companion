---
key: nunchaku-FLUX.1-Krea_1951667086886121474.json
name: nunchaku-FLUX.1-Krea_1951667086886121474
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/nunchaku-FLUX.1-Krea_1951667086886121474.json
hash: 1f8ea36a7f2370a6
coverage: 0.884615
learned_at: 2026-10-10 20:59:23
nodes: [NunchakuFluxDiTLoader, PrimitiveNode, PrimitiveNode, SaveImage, BasicGuider, EmptySD3LatentImage, VAELoader, NunchakuFluxLoraLoader, NunchakuTextEncoderLoader, SamplerCustomAdvanced, ClownsharKSampler_Beta, LatentUpscaleBy, ClownOptions_DetailBoost_Beta, SharkOptions_Beta, ClownOptions_SwapSampler_Beta, RandomNoise, ModelSamplingFlux, VAEDecode, FluxGuidance, Fast Groups Bypasser (rgthree), KSamplerSelect, BasicScheduler, VAEDecode, SaveImage, NunchakuFluxLoraLoader, CLIPTextEncode]
patterns: []
missing: []
parameters: {"cfg": 10, "denoise": 1.0000000000000002, "sampler_name": -1, "scheduler": -0.6700000000000002, "seed": 0.5, "steps": "bong_tangent"}
---

# nunchaku-FLUX.1-Krea_1951667086886121474.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/nunchaku-FLUX.1-Krea_1951667086886121474.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（26 个）：
- `NunchakuFluxDiTLoader`
- `PrimitiveNode`
- `PrimitiveNode`
- `SaveImage`
- `BasicGuider`
- `EmptySD3LatentImage`
- `VAELoader`
- `NunchakuFluxLoraLoader` ★核心
- `NunchakuTextEncoderLoader`
- `SamplerCustomAdvanced` ★核心
- `ClownsharKSampler_Beta` ★核心
- `LatentUpscaleBy`
- `ClownOptions_DetailBoost_Beta`
- `SharkOptions_Beta`
- `ClownOptions_SwapSampler_Beta` ★核心
- `RandomNoise`
- `ModelSamplingFlux`
- `VAEDecode` ★核心
- `FluxGuidance`
- `Fast Groups Bypasser (rgthree)`
- `KSamplerSelect` ★核心
- `BasicScheduler`
- `VAEDecode` ★核心
- `SaveImage`
- `NunchakuFluxLoraLoader` ★核心
- `CLIPTextEncode` ★核心

## 关键参数

- `seed` = `0.5`
- `steps` = `bong_tangent`
- `cfg` = `10`
- `sampler_name` = `-1`
- `scheduler` = `-0.6700000000000002`
- `denoise` = `1.0000000000000002`

## 知识

覆盖率 **88%**（23/26）

**有卡**：`NunchakuFluxDiTLoader`、`SaveImage`、`BasicGuider`、`EmptySD3LatentImage`、`VAELoader`、`NunchakuFluxLoraLoader`、`NunchakuTextEncoderLoader`、`SamplerCustomAdvanced`、`ClownsharKSampler_Beta`、`LatentUpscaleBy`、`ClownOptions_DetailBoost_Beta`、`SharkOptions_Beta`、`ClownOptions_SwapSampler_Beta`、`RandomNoise`、`ModelSamplingFlux`、`VAEDecode`、`FluxGuidance`、`KSamplerSelect`、`BasicScheduler`、`CLIPTextEncode`

**用到的条目**：VAEDecode、VAELoader、CLIPTextEncode、FluxGuidance、KSamplerSelect、SamplerCustomAdvanced、ClownsharKSampler_Beta、ClownOptions_SwapSampler_Beta

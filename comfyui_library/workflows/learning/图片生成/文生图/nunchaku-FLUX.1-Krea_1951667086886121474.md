---
key: 图片生成/文生图/nunchaku-FLUX.1-Krea_1951667086886121474.json
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

# 图片生成/文生图/nunchaku-FLUX.1-Krea_1951667086886121474.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/nunchaku-FLUX.1-Krea_1951667086886121474.json`

## 结构

**节点**（26 个）：
- `NunchakuFluxDiTLoader`
- `PrimitiveNode`
- `PrimitiveNode`
- `SaveImage`
- `BasicGuider`
- `EmptySD3LatentImage`
- `VAELoader`
- `NunchakuFluxLoraLoader`
- `NunchakuTextEncoderLoader`
- `SamplerCustomAdvanced`
- `ClownsharKSampler_Beta`
- `LatentUpscaleBy`
- `ClownOptions_DetailBoost_Beta`
- `SharkOptions_Beta`
- `ClownOptions_SwapSampler_Beta`
- `RandomNoise`
- `ModelSamplingFlux`
- `VAEDecode`
- `FluxGuidance`
- `Fast Groups Bypasser (rgthree)`
- `KSamplerSelect`
- `BasicScheduler`
- `VAEDecode`
- `SaveImage`
- `NunchakuFluxLoraLoader`
- `CLIPTextEncode`

## 关键参数

- `cfg` = `10`
- `denoise` = `1.0000000000000002`
- `sampler_name` = `-1`
- `scheduler` = `-0.6700000000000002`
- `seed` = `0.5`
- `steps` = `bong_tangent`

## 知识

覆盖率 **88%**（23/26）

**有卡**：`NunchakuFluxDiTLoader`、`PrimitiveNode`、`SaveImage`、`BasicGuider`、`EmptySD3LatentImage`、`VAELoader`、`NunchakuFluxLoraLoader`、`NunchakuTextEncoderLoader`、`SamplerCustomAdvanced`、`ClownsharKSampler_Beta`、`LatentUpscaleBy`、`ClownOptions_DetailBoost_Beta`、`SharkOptions_Beta`、`ClownOptions_SwapSampler_Beta`、`RandomNoise`、`ModelSamplingFlux`、`VAEDecode`、`FluxGuidance`、`Fast Groups Bypasser (rgthree)`、`KSamplerSelect`、`BasicScheduler`

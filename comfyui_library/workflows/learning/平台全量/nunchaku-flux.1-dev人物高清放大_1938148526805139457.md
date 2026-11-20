---
key: 平台全量/nunchaku-flux.1-dev人物高清放大_1938148526805139457.json
name: nunchaku-flux.1-dev人物高清放大_1938148526805139457
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/nunchaku-flux.1-dev人物高清放大_1938148526805139457.json
hash: dafc563568d6f030
coverage: 0.862069
learned_at: 2026-11-14 01:15:32
nodes: [NunchakuFluxDiTLoader, NunchakuTextEncoderLoader, VAELoader, RandomNoise, KSamplerSelect, BasicScheduler, ModelSamplingFlux, SamplerCustomAdvanced, PrimitiveNode, PrimitiveNode, FluxGuidance, BasicGuider, easy cleanGpuUsed, SAMLoader, ImageUpscaleWithModel, SaveImage, CLIPTextEncode, CLIPTextEncode, EmptySD3LatentImage, VAEDecode, FaceDetailer, PreviewImage, SaveImage, Fast Groups Bypasser (rgthree), NunchakuFluxLoraLoader, NunchakuFluxLoraLoader, CLIPTextEncode, UltralyticsDetectorProvider, UpscaleModelLoader]
patterns: []
missing: []
---

# 平台全量/nunchaku-flux.1-dev人物高清放大_1938148526805139457.json

> 来源文件 `comfyui_library/workflows/平台全量/nunchaku-flux.1-dev人物高清放大_1938148526805139457.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（29 个）：
- `NunchakuFluxDiTLoader`
- `NunchakuTextEncoderLoader`
- `VAELoader`
- `RandomNoise`
- `KSamplerSelect` ★核心
- `BasicScheduler`
- `ModelSamplingFlux`
- `SamplerCustomAdvanced` ★核心
- `PrimitiveNode`
- `PrimitiveNode`
- `FluxGuidance`
- `BasicGuider`
- `easy cleanGpuUsed`
- `SAMLoader`
- `ImageUpscaleWithModel`
- `SaveImage`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `EmptySD3LatentImage`
- `VAEDecode` ★核心
- `FaceDetailer`
- `PreviewImage`
- `SaveImage`
- `Fast Groups Bypasser (rgthree)`
- `NunchakuFluxLoraLoader` ★核心
- `NunchakuFluxLoraLoader` ★核心
- `CLIPTextEncode` ★核心
- `UltralyticsDetectorProvider`
- `UpscaleModelLoader`

## 知识

覆盖率 **86%**（25/29）

**有卡**：`NunchakuFluxDiTLoader`、`NunchakuTextEncoderLoader`、`VAELoader`、`RandomNoise`、`KSamplerSelect`、`BasicScheduler`、`ModelSamplingFlux`、`SamplerCustomAdvanced`、`FluxGuidance`、`BasicGuider`、`easy cleanGpuUsed`、`SAMLoader`、`ImageUpscaleWithModel`、`SaveImage`、`CLIPTextEncode`、`EmptySD3LatentImage`、`VAEDecode`、`FaceDetailer`、`NunchakuFluxLoraLoader`、`UltralyticsDetectorProvider`、`UpscaleModelLoader`

**用到的条目**：VAEDecode、VAELoader、CLIPTextEncode、FluxGuidance、KSamplerSelect、SamplerCustomAdvanced、NunchakuTextEncoderLoader、NunchakuFluxLoraLoader

---
key: 图片生成/文生图/文生图 — Flux 美女摄影快速出图工作流 v1.5_1910272215428886529.json
name: 文生图 — Flux 美女摄影快速出图工作流 v1.5_1910272215428886529.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/文生图 — Flux 美女摄影快速出图工作流 v1.5_1910272215428886529.json
hash: ebe37527e5f96048
coverage: 0.842105
learned_at: 2026-10-07 19:12:41
nodes: [FluxGuidance, SamplerCustomAdvanced, PrimitiveNode, BasicGuider, VAELoader, EmptySD3LatentImage, PrimitiveNode, VAEDecode, SaveImage, KSamplerSelect, RandomNoise, BasicScheduler, ModelSamplingFlux, NunchakuFluxLoraLoader, NunchakuFluxLoraLoader, NunchakuTextEncoderLoader, NunchakuFluxDiTLoader, CLIPTextEncode, PreviewImage]
patterns: []
missing: []
---

# 图片生成/文生图/文生图 — Flux 美女摄影快速出图工作流 v1.5_1910272215428886529.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/1910272215428886529.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（19 个）：
- `FluxGuidance`
- `SamplerCustomAdvanced` ★核心
- `PrimitiveNode`
- `BasicGuider`
- `VAELoader`
- `EmptySD3LatentImage`
- `PrimitiveNode`
- `VAEDecode` ★核心
- `SaveImage`
- `KSamplerSelect` ★核心
- `RandomNoise`
- `BasicScheduler`
- `ModelSamplingFlux`
- `NunchakuFluxLoraLoader` ★核心
- `NunchakuFluxLoraLoader` ★核心
- `NunchakuTextEncoderLoader`
- `NunchakuFluxDiTLoader`
- `CLIPTextEncode` ★核心
- `PreviewImage`

## 知识

覆盖率 **84%**（16/19）

**有卡**：`FluxGuidance`、`SamplerCustomAdvanced`、`BasicGuider`、`VAELoader`、`EmptySD3LatentImage`、`VAEDecode`、`SaveImage`、`KSamplerSelect`、`RandomNoise`、`BasicScheduler`、`ModelSamplingFlux`、`NunchakuFluxLoraLoader`、`NunchakuTextEncoderLoader`、`NunchakuFluxDiTLoader`、`CLIPTextEncode`

**用到的条目**：VAEDecode、VAELoader、CLIPTextEncode、FluxGuidance、KSamplerSelect、SamplerCustomAdvanced、NunchakuTextEncoderLoader、NunchakuFluxLoraLoader

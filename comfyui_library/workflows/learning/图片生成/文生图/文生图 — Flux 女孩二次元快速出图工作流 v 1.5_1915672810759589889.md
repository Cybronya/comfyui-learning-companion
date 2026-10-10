---
key: 文生图 — Flux 女孩二次元快速出图工作流 v 1.5_1915672810759589889.json
name: 文生图 — Flux 女孩二次元快速出图工作流 v 1.5_1915672810759589889
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/文生图 — Flux 女孩二次元快速出图工作流 v 1.5_1915672810759589889.json
hash: 644274a734b5cb3e
coverage: 0.888889
learned_at: 2026-10-10 20:59:46
nodes: [NunchakuFluxLoraLoader, NunchakuFluxLoraLoader, NunchakuFluxDiTLoader, PrimitiveNode, BasicGuider, SamplerCustomAdvanced, VAELoader, NunchakuTextEncoderLoader, FluxGuidance, VAEDecode, ModelSamplingFlux, PrimitiveNode, BasicScheduler, EmptySD3LatentImage, RandomNoise, KSamplerSelect, SaveImage, CLIPTextEncode]
patterns: []
missing: []
---

# 文生图 — Flux 女孩二次元快速出图工作流 v 1.5_1915672810759589889.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/文生图 — Flux 女孩二次元快速出图工作流 v 1.5_1915672810759589889.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（18 个）：
- `NunchakuFluxLoraLoader` ★核心
- `NunchakuFluxLoraLoader` ★核心
- `NunchakuFluxDiTLoader`
- `PrimitiveNode`
- `BasicGuider`
- `SamplerCustomAdvanced` ★核心
- `VAELoader`
- `NunchakuTextEncoderLoader`
- `FluxGuidance`
- `VAEDecode` ★核心
- `ModelSamplingFlux`
- `PrimitiveNode`
- `BasicScheduler`
- `EmptySD3LatentImage`
- `RandomNoise`
- `KSamplerSelect` ★核心
- `SaveImage`
- `CLIPTextEncode` ★核心

## 知识

覆盖率 **89%**（16/18）

**有卡**：`NunchakuFluxLoraLoader`、`NunchakuFluxDiTLoader`、`BasicGuider`、`SamplerCustomAdvanced`、`VAELoader`、`NunchakuTextEncoderLoader`、`FluxGuidance`、`VAEDecode`、`ModelSamplingFlux`、`BasicScheduler`、`EmptySD3LatentImage`、`RandomNoise`、`KSamplerSelect`、`SaveImage`、`CLIPTextEncode`

**用到的条目**：VAEDecode、VAELoader、CLIPTextEncode、FluxGuidance、KSamplerSelect、SamplerCustomAdvanced、NunchakuTextEncoderLoader、NunchakuFluxLoraLoader

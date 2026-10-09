---
key: 图片生成/文生图/nunchaku-flux.1-dev_1929809956793434113.json
name: nunchaku-flux.1-dev_1929809956793434113.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/nunchaku-flux.1-dev_1929809956793434113.json
hash: 3647e606d8b5266d
coverage: 0.888889
learned_at: 2026-10-07 22:34:21
nodes: [NunchakuFluxLoraLoader, NunchakuFluxLoraLoader, NunchakuFluxDiTLoader, PrimitiveNode, PrimitiveNode, EmptySD3LatentImage, RandomNoise, BasicScheduler, VAELoader, SamplerCustomAdvanced, VAEDecode, SaveImage, NunchakuTextEncoderLoader, CLIPTextEncode, BasicGuider, FluxGuidance, ModelSamplingFlux, KSamplerSelect]
patterns: []
missing: []
---

# 图片生成/文生图/nunchaku-flux.1-dev_1929809956793434113.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/1929809956793434113.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（18 个）：
- `NunchakuFluxLoraLoader` ★核心
- `NunchakuFluxLoraLoader` ★核心
- `NunchakuFluxDiTLoader`
- `PrimitiveNode`
- `PrimitiveNode`
- `EmptySD3LatentImage`
- `RandomNoise`
- `BasicScheduler`
- `VAELoader`
- `SamplerCustomAdvanced` ★核心
- `VAEDecode` ★核心
- `SaveImage`
- `NunchakuTextEncoderLoader`
- `CLIPTextEncode` ★核心
- `BasicGuider`
- `FluxGuidance`
- `ModelSamplingFlux`
- `KSamplerSelect` ★核心

## 知识

覆盖率 **89%**（16/18）

**有卡**：`NunchakuFluxLoraLoader`、`NunchakuFluxDiTLoader`、`EmptySD3LatentImage`、`RandomNoise`、`BasicScheduler`、`VAELoader`、`SamplerCustomAdvanced`、`VAEDecode`、`SaveImage`、`NunchakuTextEncoderLoader`、`CLIPTextEncode`、`BasicGuider`、`FluxGuidance`、`ModelSamplingFlux`、`KSamplerSelect`

**用到的条目**：VAEDecode、VAELoader、CLIPTextEncode、FluxGuidance、KSamplerSelect、SamplerCustomAdvanced、NunchakuTextEncoderLoader、NunchakuFluxLoraLoader

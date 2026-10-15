---
key: 图片生成/文生图/nunchaku-flux.1-dev_1929809956793434113.json
name: nunchaku-flux.1-dev_1929809956793434113
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/nunchaku-flux.1-dev_1929809956793434113.json
hash: 3647e606d8b5266d
coverage: 0.888889
learned_at: 2026-10-10 20:59:23
nodes: [NunchakuFluxLoraLoader, NunchakuFluxLoraLoader, NunchakuFluxDiTLoader, PrimitiveNode, PrimitiveNode, EmptySD3LatentImage, RandomNoise, BasicScheduler, VAELoader, SamplerCustomAdvanced, VAEDecode, SaveImage, NunchakuTextEncoderLoader, CLIPTextEncode, BasicGuider, FluxGuidance, ModelSamplingFlux, KSamplerSelect]
patterns: []
missing: []
---

# 图片生成/文生图/nunchaku-flux.1-dev_1929809956793434113.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/nunchaku-flux.1-dev_1929809956793434113.json`

## 结构

**节点**（18 个）：
- `NunchakuFluxLoraLoader`
- `NunchakuFluxLoraLoader`
- `NunchakuFluxDiTLoader`
- `PrimitiveNode`
- `PrimitiveNode`
- `EmptySD3LatentImage`
- `RandomNoise`
- `BasicScheduler`
- `VAELoader`
- `SamplerCustomAdvanced`
- `VAEDecode`
- `SaveImage`
- `NunchakuTextEncoderLoader`
- `CLIPTextEncode`
- `BasicGuider`
- `FluxGuidance`
- `ModelSamplingFlux`
- `KSamplerSelect`

## 知识

覆盖率 **89%**（16/18）

**有卡**：`NunchakuFluxLoraLoader`、`NunchakuFluxDiTLoader`、`PrimitiveNode`、`EmptySD3LatentImage`、`RandomNoise`、`BasicScheduler`、`VAELoader`、`SamplerCustomAdvanced`、`VAEDecode`、`SaveImage`、`NunchakuTextEncoderLoader`、`CLIPTextEncode`、`BasicGuider`、`FluxGuidance`

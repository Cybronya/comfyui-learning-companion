---
key: nunchaku-flux.1-dev flux秒出图_1910558383181656066.json
name: nunchaku-flux.1-dev flux秒出图_1910558383181656066
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/nunchaku-flux.1-dev flux秒出图_1910558383181656066.json
hash: 6fd91689f9bf8d18
coverage: 0.842105
learned_at: 2026-10-10 20:59:23
nodes: [KSamplerSelect, VAEDecode, BasicGuider, EmptySD3LatentImage, SamplerCustomAdvanced, RandomNoise, ModelSamplingFlux, VAELoader, PrimitiveNode, PrimitiveNode, SaveImage, BasicScheduler, CLIPTextEncode, NunchakuFluxDiTLoader, NunchakuTextEncoderLoader, NunchakuFluxLoraLoader, NunchakuFluxLoraLoader, FluxGuidance, Note _O]
patterns: []
missing: [Note _O]
discoveries: [次要节点 `Note _O` 知识库中没有该节点类型的任何知识]
---

# nunchaku-flux.1-dev flux秒出图_1910558383181656066.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/nunchaku-flux.1-dev flux秒出图_1910558383181656066.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（19 个）：
- `KSamplerSelect` ★核心
- `VAEDecode` ★核心
- `BasicGuider`
- `EmptySD3LatentImage`
- `SamplerCustomAdvanced` ★核心
- `RandomNoise`
- `ModelSamplingFlux`
- `VAELoader`
- `PrimitiveNode`
- `PrimitiveNode`
- `SaveImage`
- `BasicScheduler`
- `CLIPTextEncode` ★核心
- `NunchakuFluxDiTLoader`
- `NunchakuTextEncoderLoader`
- `NunchakuFluxLoraLoader` ★核心
- `NunchakuFluxLoraLoader` ★核心
- `FluxGuidance`
- `Note _O`

## 知识

覆盖率 **84%**（16/19）

**有卡**：`KSamplerSelect`、`VAEDecode`、`BasicGuider`、`EmptySD3LatentImage`、`SamplerCustomAdvanced`、`RandomNoise`、`ModelSamplingFlux`、`VAELoader`、`SaveImage`、`BasicScheduler`、`CLIPTextEncode`、`NunchakuFluxDiTLoader`、`NunchakuTextEncoderLoader`、`NunchakuFluxLoraLoader`、`FluxGuidance`

**缺卡**（1）：`Note _O`

**用到的条目**：VAEDecode、VAELoader、CLIPTextEncode、FluxGuidance、KSamplerSelect、SamplerCustomAdvanced、NunchakuTextEncoderLoader、NunchakuFluxLoraLoader

## 学习发现

- 次要节点 `Note _O` 知识库中没有该节点类型的任何知识

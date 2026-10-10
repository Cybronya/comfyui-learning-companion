---
key: nunchaku-flux.1-dev 官方加速工作流_1909669429062631425.json
name: nunchaku-flux.1-dev 官方加速工作流_1909669429062631425
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/nunchaku-flux.1-dev 官方加速工作流_1909669429062631425.json
hash: 0db3207766bdf153
coverage: 0.888889
learned_at: 2026-10-10 20:59:23
nodes: [FluxGuidance, KSamplerSelect, VAEDecode, BasicGuider, EmptySD3LatentImage, SamplerCustomAdvanced, RandomNoise, ModelSamplingFlux, VAELoader, PrimitiveNode, PrimitiveNode, SaveImage, BasicScheduler, CLIPTextEncode, NunchakuFluxDiTLoader, NunchakuTextEncoderLoader, NunchakuFluxLoraLoader, NunchakuFluxLoraLoader]
patterns: []
missing: []
---

# nunchaku-flux.1-dev 官方加速工作流_1909669429062631425.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/nunchaku-flux.1-dev 官方加速工作流_1909669429062631425.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（18 个）：
- `FluxGuidance`
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

## 知识

覆盖率 **89%**（16/18）

**有卡**：`FluxGuidance`、`KSamplerSelect`、`VAEDecode`、`BasicGuider`、`EmptySD3LatentImage`、`SamplerCustomAdvanced`、`RandomNoise`、`ModelSamplingFlux`、`VAELoader`、`SaveImage`、`BasicScheduler`、`CLIPTextEncode`、`NunchakuFluxDiTLoader`、`NunchakuTextEncoderLoader`、`NunchakuFluxLoraLoader`

**用到的条目**：VAEDecode、VAELoader、CLIPTextEncode、FluxGuidance、KSamplerSelect、SamplerCustomAdvanced、NunchakuTextEncoderLoader、NunchakuFluxLoraLoader

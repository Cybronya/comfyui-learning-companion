---
key: 图片生成/文生图/nunchaku-flux.1-dev 个人加速工作流V1_2028335440100597762.json
name: nunchaku-flux.1-dev 个人加速工作流V1_2028335440100597762
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/nunchaku-flux.1-dev 个人加速工作流V1_2028335440100597762.json
hash: a07e3b3b92748294
coverage: 1
learned_at: 2026-10-20 23:22:00
nodes: [FluxGuidance, KSamplerSelect, VAEDecode, BasicGuider, EmptySD3LatentImage, SamplerCustomAdvanced, RandomNoise, ModelSamplingFlux, VAELoader, SaveImage, BasicScheduler, NunchakuFluxDiTLoader, NunchakuTextEncoderLoader, NunchakuFluxLoraLoader, CLIPTextEncode]
patterns: []
missing: []
---

# 图片生成/文生图/nunchaku-flux.1-dev 个人加速工作流V1_2028335440100597762.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/nunchaku-flux.1-dev 个人加速工作流V1_2028335440100597762.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（15 个）：
- `FluxGuidance`
- `KSamplerSelect` ★核心
- `VAEDecode` ★核心
- `BasicGuider`
- `EmptySD3LatentImage`
- `SamplerCustomAdvanced` ★核心
- `RandomNoise`
- `ModelSamplingFlux`
- `VAELoader`
- `SaveImage`
- `BasicScheduler`
- `NunchakuFluxDiTLoader`
- `NunchakuTextEncoderLoader`
- `NunchakuFluxLoraLoader` ★核心
- `CLIPTextEncode` ★核心

## 知识

覆盖率 **100%**（15/15）

**有卡**：`FluxGuidance`、`KSamplerSelect`、`VAEDecode`、`BasicGuider`、`EmptySD3LatentImage`、`SamplerCustomAdvanced`、`RandomNoise`、`ModelSamplingFlux`、`VAELoader`、`SaveImage`、`BasicScheduler`、`NunchakuFluxDiTLoader`、`NunchakuTextEncoderLoader`、`NunchakuFluxLoraLoader`、`CLIPTextEncode`

**用到的条目**：VAEDecode、VAELoader、CLIPTextEncode、FluxGuidance、KSamplerSelect、SamplerCustomAdvanced、NunchakuTextEncoderLoader、NunchakuFluxLoraLoader

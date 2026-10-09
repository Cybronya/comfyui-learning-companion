---
key: 图片生成/文生图/【AI由北】nunchaku-flux.1_1915753087057723394.json
name: 【AI由北】nunchaku-flux.1_1915753087057723394.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/【AI由北】nunchaku-flux.1_1915753087057723394.json
hash: dd679a677f441d42
coverage: 0.894737
learned_at: 2026-10-07 22:07:38
nodes: [KSamplerSelect, VAELoader, BasicScheduler, NunchakuFluxLoraLoader, NunchakuFluxDiTLoader, NunchakuFluxLoraLoader, ModelSamplingFlux, SamplerCustomAdvanced, EmptySD3LatentImage, BasicGuider, NunchakuTextEncoderLoader, VAEDecode, SaveImage, FluxGuidance, RandomNoise, PrimitiveNode, PrimitiveNode, CLIPTextEncode, LoadImage]
patterns: []
missing: []
---

# 图片生成/文生图/【AI由北】nunchaku-flux.1_1915753087057723394.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/1915753087057723394.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（19 个）：
- `KSamplerSelect` ★核心
- `VAELoader`
- `BasicScheduler`
- `NunchakuFluxLoraLoader` ★核心
- `NunchakuFluxDiTLoader`
- `NunchakuFluxLoraLoader` ★核心
- `ModelSamplingFlux`
- `SamplerCustomAdvanced` ★核心
- `EmptySD3LatentImage`
- `BasicGuider`
- `NunchakuTextEncoderLoader`
- `VAEDecode` ★核心
- `SaveImage`
- `FluxGuidance`
- `RandomNoise`
- `PrimitiveNode`
- `PrimitiveNode`
- `CLIPTextEncode` ★核心
- `LoadImage`

## 知识

覆盖率 **89%**（17/19）

**有卡**：`KSamplerSelect`、`VAELoader`、`BasicScheduler`、`NunchakuFluxLoraLoader`、`NunchakuFluxDiTLoader`、`ModelSamplingFlux`、`SamplerCustomAdvanced`、`EmptySD3LatentImage`、`BasicGuider`、`NunchakuTextEncoderLoader`、`VAEDecode`、`SaveImage`、`FluxGuidance`、`RandomNoise`、`CLIPTextEncode`、`LoadImage`

**用到的条目**：VAEDecode、VAELoader、CLIPTextEncode、LoadImage、FluxGuidance、KSamplerSelect、SamplerCustomAdvanced、NunchakuTextEncoderLoader

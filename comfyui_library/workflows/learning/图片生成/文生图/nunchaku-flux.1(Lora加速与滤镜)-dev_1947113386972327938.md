---
key: 图片生成/文生图/nunchaku-flux.1(Lora加速与滤镜)-dev_1947113386972327938.json
name: nunchaku-flux.1(Lora加速与滤镜)-dev_1947113386972327938.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/nunchaku-flux.1(Lora加速与滤镜)-dev_1947113386972327938.json
hash: 5a680aff64c9f6dc
coverage: 0.809524
learned_at: 2026-10-07 22:52:54
nodes: [SamplerCustomAdvanced, RandomNoise, BasicGuider, KSamplerSelect, BasicScheduler, FluxGuidance, VAELoader, ModelSamplingFlux, PrimitiveNode, PrimitiveNode, VAEDecode, SaveImage, PreviewImage, NunchakuFluxLoraLoader, NunchakuTextEncoderLoader, Fast Groups Bypasser (rgthree), NunchakuFluxLoraLoader, NunchakuFluxLoraLoader, NunchakuFluxDiTLoader, EmptySD3LatentImage, CLIPTextEncode]
patterns: []
missing: []
---

# 图片生成/文生图/nunchaku-flux.1(Lora加速与滤镜)-dev_1947113386972327938.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/1947113386972327938.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（21 个）：
- `SamplerCustomAdvanced` ★核心
- `RandomNoise`
- `BasicGuider`
- `KSamplerSelect` ★核心
- `BasicScheduler`
- `FluxGuidance`
- `VAELoader`
- `ModelSamplingFlux`
- `PrimitiveNode`
- `PrimitiveNode`
- `VAEDecode` ★核心
- `SaveImage`
- `PreviewImage`
- `NunchakuFluxLoraLoader` ★核心
- `NunchakuTextEncoderLoader`
- `Fast Groups Bypasser (rgthree)`
- `NunchakuFluxLoraLoader` ★核心
- `NunchakuFluxLoraLoader` ★核心
- `NunchakuFluxDiTLoader`
- `EmptySD3LatentImage`
- `CLIPTextEncode` ★核心

## 知识

覆盖率 **81%**（17/21）

**有卡**：`SamplerCustomAdvanced`、`RandomNoise`、`BasicGuider`、`KSamplerSelect`、`BasicScheduler`、`FluxGuidance`、`VAELoader`、`ModelSamplingFlux`、`VAEDecode`、`SaveImage`、`NunchakuFluxLoraLoader`、`NunchakuTextEncoderLoader`、`NunchakuFluxDiTLoader`、`EmptySD3LatentImage`、`CLIPTextEncode`

**用到的条目**：VAEDecode、VAELoader、CLIPTextEncode、FluxGuidance、KSamplerSelect、SamplerCustomAdvanced、NunchakuTextEncoderLoader、NunchakuFluxLoraLoader

---
key: 一秒两张 Flux Nunchaku Turbo四步极速出图工作流-StarAI_1912263987780878337.json
name: 一秒两张 Flux Nunchaku Turbo四步极速出图工作流-StarAI_1912263987780878337
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/一秒两张 Flux Nunchaku Turbo四步极速出图工作流-StarAI_1912263987780878337.json
hash: 674ea517a99dfd3f
coverage: 0.866667
learned_at: 2026-10-10 20:59:32
nodes: [VAELoader, NunchakuTextEncoderLoader, KSamplerSelect, NunchakuFluxDiTLoader, ModelSamplingFlux, FluxGuidance, ConditioningZeroOut, PrimitiveNode, PrimitiveNode, EmptySD3LatentImage, LoraLoaderModelOnly, CLIPTextEncode, SaveImage, VAEDecode, KSampler]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "normal", "seed": 550949447103486, "steps": 4}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 一秒两张 Flux Nunchaku Turbo四步极速出图工作流-StarAI_1912263987780878337.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/一秒两张 Flux Nunchaku Turbo四步极速出图工作流-StarAI_1912263987780878337.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（15 个）：
- `VAELoader`
- `NunchakuTextEncoderLoader`
- `KSamplerSelect` ★核心
- `NunchakuFluxDiTLoader`
- `ModelSamplingFlux`
- `FluxGuidance`
- `ConditioningZeroOut`
- `PrimitiveNode`
- `PrimitiveNode`
- `EmptySD3LatentImage`
- `LoraLoaderModelOnly` ★核心
- `CLIPTextEncode` ★核心
- `SaveImage`
- `VAEDecode` ★核心
- `KSampler` ★核心

## 关键参数

- `seed` = `550949447103486`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `normal`
- `denoise` = `1`

## 知识

覆盖率 **87%**（13/15）

**有卡**：`VAELoader`、`NunchakuTextEncoderLoader`、`KSamplerSelect`、`NunchakuFluxDiTLoader`、`ModelSamplingFlux`、`FluxGuidance`、`ConditioningZeroOut`、`EmptySD3LatentImage`、`LoraLoaderModelOnly`、`CLIPTextEncode`、`SaveImage`、`VAEDecode`、`KSampler`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、ConditioningZeroOut、FluxGuidance、KSamplerSelect

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

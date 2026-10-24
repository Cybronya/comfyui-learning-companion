---
key: 图片生成/图生图/2025-04-15-nunchaku-flux.1-fill_1912069428291301378.json
name: 2025-04-15-nunchaku-flux.1-fill_1912069428291301378
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/2025-04-15-nunchaku-flux.1-fill_1912069428291301378.json
hash: ab6295d7fc0b5ad8
coverage: 1
learned_at: 2026-10-23 10:48:08
nodes: [VAEDecode, InpaintModelConditioning, KSampler, ConditioningZeroOut, FluxGuidance, NunchakuFluxDiTLoader, NunchakuTextEncoderLoader, VAELoader, CLIPTextEncode, SaveImage, LoadImage]
patterns: []
missing: []
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "normal", "seed": 918727737913760, "steps": 20}
---

# 图片生成/图生图/2025-04-15-nunchaku-flux.1-fill_1912069428291301378.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/2025-04-15-nunchaku-flux.1-fill_1912069428291301378.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Output → Other

**节点**（11 个）：
- `VAEDecode` ★核心
- `InpaintModelConditioning`
- `KSampler` ★核心
- `ConditioningZeroOut`
- `FluxGuidance`
- `NunchakuFluxDiTLoader`
- `NunchakuTextEncoderLoader`
- `VAELoader`
- `CLIPTextEncode` ★核心
- `SaveImage`
- `LoadImage`

## 关键参数

- `seed` = `918727737913760`
- `steps` = `20`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `normal`
- `denoise` = `1`

## 知识

覆盖率 **100%**（11/11）

**有卡**：`VAEDecode`、`InpaintModelConditioning`、`KSampler`、`ConditioningZeroOut`、`FluxGuidance`、`NunchakuFluxDiTLoader`、`NunchakuTextEncoderLoader`、`VAELoader`、`CLIPTextEncode`、`SaveImage`、`LoadImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、ConditioningZeroOut、LoadImage、FluxGuidance、NunchakuTextEncoderLoader

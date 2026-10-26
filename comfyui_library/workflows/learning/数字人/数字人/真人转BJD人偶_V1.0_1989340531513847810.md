---
key: 数字人/数字人/真人转BJD人偶_V1.0_1989340531513847810.json
name: 真人转BJD人偶_V1.0_1989340531513847810
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/数字人/数字人/真人转BJD人偶_V1.0_1989340531513847810.json
hash: 2d1a3e6e24107ad1
coverage: 0.777778
learned_at: 2026-10-26 02:04:05
nodes: [FluxGuidance, ReferenceLatent, ConditioningZeroOut, JjkText, LoadImage, KSampler, CLIPTextEncode, VAELoader, NunchakuFluxDiTLoader, VAEEncode, Anything Everywhere3, NunchakuFluxLoraLoader, DualCLIPLoader, NunchakuFluxLoraLoader, VAEDecode, SaveImage, Reroute, Image Comparer (rgthree)]
patterns: [image_to_image]
missing: []
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 777777777777777, "steps": 20}
---

# 数字人/数字人/真人转BJD人偶_V1.0_1989340531513847810.json

> 来源文件 `comfyui_library/workflows/数字人/数字人/真人转BJD人偶_V1.0_1989340531513847810.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Output → Other

**节点**（18 个）：
- `FluxGuidance`
- `ReferenceLatent`
- `ConditioningZeroOut`
- `JjkText`
- `LoadImage`
- `KSampler` ★核心
- `CLIPTextEncode` ★核心
- `VAELoader`
- `NunchakuFluxDiTLoader`
- `VAEEncode` ★核心
- `Anything Everywhere3`
- `NunchakuFluxLoraLoader` ★核心
- `DualCLIPLoader`
- `NunchakuFluxLoraLoader` ★核心
- `VAEDecode` ★核心
- `SaveImage`
- `Reroute`
- `Image Comparer (rgthree)`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `777777777777777`
- `steps` = `20`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **78%**（14/18）

**有卡**：`FluxGuidance`、`ReferenceLatent`、`ConditioningZeroOut`、`LoadImage`、`KSampler`、`CLIPTextEncode`、`VAELoader`、`NunchakuFluxDiTLoader`、`VAEEncode`、`NunchakuFluxLoraLoader`、`DualCLIPLoader`、`VAEDecode`、`SaveImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、ConditioningZeroOut、LoadImage、FluxGuidance、ReferenceLatent

---
key: 图片生成/图生图/FLUX.kontext 产品精修官方工作流_1938785654178566146.json
name: FLUX.kontext 产品精修官方工作流_1938785654178566146
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/FLUX.kontext 产品精修官方工作流_1938785654178566146.json
hash: 2af0f698697c95cd
coverage: 0.9375
learned_at: 2026-10-23 10:54:17
nodes: [ReferenceLatent, FluxGuidance, CLIPTextEncode, ConditioningZeroOut, FluxKontextImageScale, VAEEncode, KSampler, VAEDecode, SaveImage, ConstrainImage|pysssss, LoadImage, Note, UNETLoader, DualCLIPLoader, VAELoader, RH_Translator]
patterns: [image_to_image]
missing: []
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 598135497155679, "steps": 25}
---

# 图片生成/图生图/FLUX.kontext 产品精修官方工作流_1938785654178566146.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/FLUX.kontext 产品精修官方工作流_1938785654178566146.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（16 个）：
- `ReferenceLatent`
- `FluxGuidance`
- `CLIPTextEncode` ★核心
- `ConditioningZeroOut`
- `FluxKontextImageScale`
- `VAEEncode` ★核心
- `KSampler` ★核心
- `VAEDecode` ★核心
- `SaveImage`
- `ConstrainImage|pysssss`
- `LoadImage`
- `Note`
- `UNETLoader` ★核心
- `DualCLIPLoader`
- `VAELoader`
- `RH_Translator`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `598135497155679`
- `steps` = `25`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **94%**（15/16）

**有卡**：`ReferenceLatent`、`FluxGuidance`、`CLIPTextEncode`、`ConditioningZeroOut`、`FluxKontextImageScale`、`VAEEncode`、`KSampler`、`VAEDecode`、`SaveImage`、`ConstrainImage|pysssss`、`LoadImage`、`UNETLoader`、`DualCLIPLoader`、`VAELoader`、`RH_Translator`

**用到的条目**：KSampler、VAEDecode、VAELoader、UNETLoader、CLIPTextEncode、ConditioningZeroOut、LoadImage、FluxGuidance

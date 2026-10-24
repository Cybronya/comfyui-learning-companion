---
key: 图片生成/图生图/nunchaku-flux.1-kontext-dev-8步快速出图_1942473442157342721.json
name: nunchaku-flux.1-kontext-dev-8步快速出图_1942473442157342721
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/nunchaku-flux.1-kontext-dev-8步快速出图_1942473442157342721.json
hash: 3d2409bd4964cd55
coverage: 0.9375
learned_at: 2026-10-23 11:41:18
nodes: [VAELoader, ConditioningZeroOut, FluxGuidance, ReferenceLatent, VAEDecode, VAEEncode, CLIPTextEncode, KSampler, LayerUtility: ImageScaleByAspectRatio V2, ShowText|pysssss, RH_LLMAPI_NODE, LoadImage, RH_Translator, DualCLIPLoader, SaveImage, NunchakuFluxDiTLoader]
patterns: [image_to_image]
missing: []
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 9583576189740, "steps": 20}
---

# 图片生成/图生图/nunchaku-flux.1-kontext-dev-8步快速出图_1942473442157342721.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/nunchaku-flux.1-kontext-dev-8步快速出图_1942473442157342721.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（16 个）：
- `VAELoader`
- `ConditioningZeroOut`
- `FluxGuidance`
- `ReferenceLatent`
- `VAEDecode` ★核心
- `VAEEncode` ★核心
- `CLIPTextEncode` ★核心
- `KSampler` ★核心
- `LayerUtility: ImageScaleByAspectRatio V2`
- `ShowText|pysssss`
- `RH_LLMAPI_NODE`
- `LoadImage`
- `RH_Translator`
- `DualCLIPLoader`
- `SaveImage`
- `NunchakuFluxDiTLoader`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `9583576189740`
- `steps` = `20`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **94%**（15/16）

**有卡**：`VAELoader`、`ConditioningZeroOut`、`FluxGuidance`、`ReferenceLatent`、`VAEDecode`、`VAEEncode`、`CLIPTextEncode`、`KSampler`、`LayerUtility: ImageScaleByAspectRatio V2`、`RH_LLMAPI_NODE`、`LoadImage`、`RH_Translator`、`DualCLIPLoader`、`SaveImage`、`NunchakuFluxDiTLoader`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、ConditioningZeroOut、LoadImage、FluxGuidance、ReferenceLatent

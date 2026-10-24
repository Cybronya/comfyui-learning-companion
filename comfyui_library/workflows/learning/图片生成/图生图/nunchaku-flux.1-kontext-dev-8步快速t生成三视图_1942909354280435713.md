---
key: 图片生成/图生图/nunchaku-flux.1-kontext-dev-8步快速t生成三视图_1942909354280435713.json
name: nunchaku-flux.1-kontext-dev-8步快速t生成三视图_1942909354280435713
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/nunchaku-flux.1-kontext-dev-8步快速t生成三视图_1942909354280435713.json
hash: 24958ac3f1cc0a72
coverage: 0.882353
learned_at: 2026-10-23 11:41:18
nodes: [LayerUtility: ImageScaleByAspectRatio V2, ShowText|pysssss, RH_LLMAPI_NODE, CLIPTextEncode, LoadImage, SaveImage, PreviewImage, ReferenceLatent, FluxGuidance, ConditioningZeroOut, VAEDecode, VAELoader, VAEEncode, DualCLIPLoader, NunchakuFluxDiTLoader, RH_Translator, KSampler]
patterns: [image_to_image]
missing: []
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 413113557353378, "steps": 20}
---

# 图片生成/图生图/nunchaku-flux.1-kontext-dev-8步快速t生成三视图_1942909354280435713.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/nunchaku-flux.1-kontext-dev-8步快速t生成三视图_1942909354280435713.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（17 个）：
- `LayerUtility: ImageScaleByAspectRatio V2`
- `ShowText|pysssss`
- `RH_LLMAPI_NODE`
- `CLIPTextEncode` ★核心
- `LoadImage`
- `SaveImage`
- `PreviewImage`
- `ReferenceLatent`
- `FluxGuidance`
- `ConditioningZeroOut`
- `VAEDecode` ★核心
- `VAELoader`
- `VAEEncode` ★核心
- `DualCLIPLoader`
- `NunchakuFluxDiTLoader`
- `RH_Translator`
- `KSampler` ★核心

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `413113557353378`
- `steps` = `20`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **88%**（15/17）

**有卡**：`LayerUtility: ImageScaleByAspectRatio V2`、`RH_LLMAPI_NODE`、`CLIPTextEncode`、`LoadImage`、`SaveImage`、`ReferenceLatent`、`FluxGuidance`、`ConditioningZeroOut`、`VAEDecode`、`VAELoader`、`VAEEncode`、`DualCLIPLoader`、`NunchakuFluxDiTLoader`、`RH_Translator`、`KSampler`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、ConditioningZeroOut、LoadImage、FluxGuidance、ReferenceLatent

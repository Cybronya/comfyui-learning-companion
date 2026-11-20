---
key: 平台全量/Flux_ControlNet Upscaler 高清放大模型直接用_1961788462322139138.json
name: Flux_ControlNet Upscaler 高清放大模型直接用_1961788462322139138
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/平台全量/Flux_ControlNet Upscaler 高清放大模型直接用_1961788462322139138.json
hash: 7f65e85e957ecde8
coverage: 0.772727
learned_at: 2026-11-14 00:30:12
nodes: [LayerUtility: JoyCaptionBeta1, LayerUtility: LoadJoyCaptionBeta1Model, UNETLoader, DualCLIPLoader, ConditioningZeroOut, FluxGuidance, VAELoader, Reroute, CLIPTextEncode, CLIPTextEncode, ControlNetLoader, VAEEncode, ShowText|pysssss, Anything Everywhere3, ControlNetApplySD3, ImageScaleBy, KSampler, Image Comparer (rgthree), Note, VAEDecode, SaveImage, LoadImage]
patterns: [image_to_image]
missing: []
parameters: {"cfg": 1, "controlnet_strength": 0.7000000000000002, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 598192057051737, "steps": 20}
---

# 平台全量/Flux_ControlNet Upscaler 高清放大模型直接用_1961788462322139138.json

> 来源文件 `comfyui_library/workflows/平台全量/Flux_ControlNet Upscaler 高清放大模型直接用_1961788462322139138.json`

## 结构

**生成流程**：Model → Encode → Condition → Control → Sampling → Decode → Process → Output → Other

**节点**（22 个）：
- `LayerUtility: JoyCaptionBeta1`
- `LayerUtility: LoadJoyCaptionBeta1Model`
- `UNETLoader` ★核心
- `DualCLIPLoader`
- `ConditioningZeroOut`
- `FluxGuidance`
- `VAELoader`
- `Reroute`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `ControlNetLoader`
- `VAEEncode` ★核心
- `ShowText|pysssss`
- `Anything Everywhere3`
- `ControlNetApplySD3` ★核心
- `ImageScaleBy`
- `KSampler` ★核心
- `Image Comparer (rgthree)`
- `Note`
- `VAEDecode` ★核心
- `SaveImage`
- `LoadImage`

**识别到的模式**：image_to_image

## 关键参数

- `controlnet_strength` = `0.7000000000000002`
- `seed` = `598192057051737`
- `steps` = `20`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **77%**（17/22）

**有卡**：`LayerUtility: JoyCaptionBeta1`、`LayerUtility: LoadJoyCaptionBeta1Model`、`UNETLoader`、`DualCLIPLoader`、`ConditioningZeroOut`、`FluxGuidance`、`VAELoader`、`CLIPTextEncode`、`ControlNetLoader`、`VAEEncode`、`ControlNetApplySD3`、`ImageScaleBy`、`KSampler`、`VAEDecode`、`SaveImage`、`LoadImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、UNETLoader、CLIPTextEncode、ConditioningZeroOut、LoadImage、ControlNetApplySD3

---
key: 图片生成/图生图/nunchaku-flux.1-kontext-dev-扩图-8步快速出图_1954878812870754306.json
name: nunchaku-flux.1-kontext-dev-扩图-8步快速出图_1954878812870754306
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/nunchaku-flux.1-kontext-dev-扩图-8步快速出图_1954878812870754306.json
hash: 699166c2cd3419ce
coverage: 0.809524
learned_at: 2026-10-23 11:41:18
nodes: [PreviewImage, SaveImage, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, VAELoader, ConditioningZeroOut, FluxGuidance, ReferenceLatent, VAEDecode, VAEEncode, DualCLIPLoader, NunchakuFluxDiTLoader, easy imageConcat, PreviewImage, CLIPTextEncode, UpscaleModelLoader, ImageUpscaleWithModel, PreviewImage, KSampler, PrimitiveInt, ImagePadForOutpaint]
patterns: [image_to_image]
missing: []
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 46324645609181, "steps": 343}
---

# 图片生成/图生图/nunchaku-flux.1-kontext-dev-扩图-8步快速出图_1954878812870754306.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/nunchaku-flux.1-kontext-dev-扩图-8步快速出图_1954878812870754306.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（21 个）：
- `PreviewImage`
- `SaveImage`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `VAELoader`
- `ConditioningZeroOut`
- `FluxGuidance`
- `ReferenceLatent`
- `VAEDecode` ★核心
- `VAEEncode` ★核心
- `DualCLIPLoader`
- `NunchakuFluxDiTLoader`
- `easy imageConcat`
- `PreviewImage`
- `CLIPTextEncode` ★核心
- `UpscaleModelLoader`
- `ImageUpscaleWithModel`
- `PreviewImage`
- `KSampler` ★核心
- `PrimitiveInt`
- `ImagePadForOutpaint`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `46324645609181`
- `steps` = `343`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **81%**（17/21）

**有卡**：`SaveImage`、`LayerUtility: ImageScaleByAspectRatio V2`、`LoadImage`、`VAELoader`、`ConditioningZeroOut`、`FluxGuidance`、`ReferenceLatent`、`VAEDecode`、`VAEEncode`、`DualCLIPLoader`、`NunchakuFluxDiTLoader`、`easy imageConcat`、`CLIPTextEncode`、`UpscaleModelLoader`、`ImageUpscaleWithModel`、`KSampler`、`ImagePadForOutpaint`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、ConditioningZeroOut、LoadImage、FluxGuidance、ReferenceLatent

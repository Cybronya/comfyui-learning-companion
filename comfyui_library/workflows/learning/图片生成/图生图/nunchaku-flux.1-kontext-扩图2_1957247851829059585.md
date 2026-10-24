---
key: 图片生成/图生图/nunchaku-flux.1-kontext-扩图2_1957247851829059585.json
name: nunchaku-flux.1-kontext-扩图2_1957247851829059585
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/nunchaku-flux.1-kontext-扩图2_1957247851829059585.json
hash: 2737d02a8a84eb58
coverage: 0.944444
learned_at: 2026-10-23 11:41:20
nodes: [VAELoader, ConditioningZeroOut, FluxGuidance, NunchakuFluxDiTLoader, DualCLIPLoader, ReferenceLatent, KSampler, SaveImage, GetImageSize+, EmptyImage, LayerUtility: ImageCombineAlpha, VAEDecode, Image Comparer (rgthree), LoadImage, VAEEncode, CLIPTextEncode, ImageCompositeMasked, ImagePadForOutpaint]
patterns: [image_to_image]
missing: []
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "normal", "seed": 95164126357381, "steps": 20}
---

# 图片生成/图生图/nunchaku-flux.1-kontext-扩图2_1957247851829059585.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/nunchaku-flux.1-kontext-扩图2_1957247851829059585.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（18 个）：
- `VAELoader`
- `ConditioningZeroOut`
- `FluxGuidance`
- `NunchakuFluxDiTLoader`
- `DualCLIPLoader`
- `ReferenceLatent`
- `KSampler` ★核心
- `SaveImage`
- `GetImageSize+`
- `EmptyImage`
- `LayerUtility: ImageCombineAlpha`
- `VAEDecode` ★核心
- `Image Comparer (rgthree)`
- `LoadImage`
- `VAEEncode` ★核心
- `CLIPTextEncode` ★核心
- `ImageCompositeMasked`
- `ImagePadForOutpaint`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `95164126357381`
- `steps` = `20`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `normal`
- `denoise` = `1`

## 知识

覆盖率 **94%**（17/18）

**有卡**：`VAELoader`、`ConditioningZeroOut`、`FluxGuidance`、`NunchakuFluxDiTLoader`、`DualCLIPLoader`、`ReferenceLatent`、`KSampler`、`SaveImage`、`GetImageSize+`、`EmptyImage`、`LayerUtility: ImageCombineAlpha`、`VAEDecode`、`LoadImage`、`VAEEncode`、`CLIPTextEncode`、`ImageCompositeMasked`、`ImagePadForOutpaint`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、ConditioningZeroOut、LoadImage、FluxGuidance、ReferenceLatent

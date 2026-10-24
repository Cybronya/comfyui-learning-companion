---
key: 图片生成/图生图/nunchaku-flux.1-kontext-扩图_1956295255689711618.json
name: nunchaku-flux.1-kontext-扩图_1956295255689711618
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/nunchaku-flux.1-kontext-扩图_1956295255689711618.json
hash: d19dae5c07e1ba61
coverage: 0.882353
learned_at: 2026-10-23 11:41:20
nodes: [VAELoader, ConditioningZeroOut, FluxGuidance, NunchakuFluxDiTLoader, DualCLIPLoader, ReferenceLatent, VAEEncode, KSampler, PreviewImage, VAEDecode, SaveImage, Image Comparer (rgthree), CLIPTextEncode, GetImageSize+, EmptySD3LatentImage, ImagePadForOutpaint, LoadImage]
patterns: [image_to_image]
missing: []
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "normal", "seed": 1040221997483393, "steps": 20}
---

# 图片生成/图生图/nunchaku-flux.1-kontext-扩图_1956295255689711618.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/nunchaku-flux.1-kontext-扩图_1956295255689711618.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（17 个）：
- `VAELoader`
- `ConditioningZeroOut`
- `FluxGuidance`
- `NunchakuFluxDiTLoader`
- `DualCLIPLoader`
- `ReferenceLatent`
- `VAEEncode` ★核心
- `KSampler` ★核心
- `PreviewImage`
- `VAEDecode` ★核心
- `SaveImage`
- `Image Comparer (rgthree)`
- `CLIPTextEncode` ★核心
- `GetImageSize+`
- `EmptySD3LatentImage`
- `ImagePadForOutpaint`
- `LoadImage`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `1040221997483393`
- `steps` = `20`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `normal`
- `denoise` = `1`

## 知识

覆盖率 **88%**（15/17）

**有卡**：`VAELoader`、`ConditioningZeroOut`、`FluxGuidance`、`NunchakuFluxDiTLoader`、`DualCLIPLoader`、`ReferenceLatent`、`VAEEncode`、`KSampler`、`VAEDecode`、`SaveImage`、`CLIPTextEncode`、`GetImageSize+`、`EmptySD3LatentImage`、`ImagePadForOutpaint`、`LoadImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、ConditioningZeroOut、LoadImage、FluxGuidance、ReferenceLatent

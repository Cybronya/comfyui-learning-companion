---
key: 图片生成/图生图/【工业设计】kontext 画线控制=肌理棱线 V2.0(已有全新升级应用链接简介区)_1946911324820369409.json
name: 【工业设计】kontext 画线控制=肌理棱线 V2.0(已有全新升级应用链接简介区)_1946911324820369409
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/【工业设计】kontext 画线控制=肌理棱线 V2.0(已有全新升级应用链接简介区)_1946911324820369409.json
hash: 65c8e98a89c80451
coverage: 0.857143
learned_at: 2026-10-23 11:49:57
nodes: [FluxGuidance, FluxKontextImageScale, ReferenceLatent, ConditioningZeroOut, VAEEncode, VAELoader, VAEDecode, TextCombinerTwo, RH_Translator, Bjornulf_TextReplace, easy showAnything, RH_Captioner, LoraLoaderModelOnly, UNETLoader, DualCLIPLoader, easy showAnything, CLIPTextEncode, LayerUtility: ImageReelComposit, SaveImage, LayerUtility: ImageReel, SaveImage, KSampler, PreviewImage, PrimitiveFloat, LoadImage, MaskToImage, LayerStyle: ColorOverlay, SaveImage]
patterns: [image_to_image]
missing: []
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "er_sde", "scheduler": "beta", "seed": 56660551018566, "steps": 20}
---

# 图片生成/图生图/【工业设计】kontext 画线控制=肌理棱线 V2.0(已有全新升级应用链接简介区)_1946911324820369409.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/【工业设计】kontext 画线控制=肌理棱线 V2.0(已有全新升级应用链接简介区)_1946911324820369409.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（28 个）：
- `FluxGuidance`
- `FluxKontextImageScale`
- `ReferenceLatent`
- `ConditioningZeroOut`
- `VAEEncode` ★核心
- `VAELoader`
- `VAEDecode` ★核心
- `TextCombinerTwo`
- `RH_Translator`
- `Bjornulf_TextReplace`
- `easy showAnything`
- `RH_Captioner`
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `DualCLIPLoader`
- `easy showAnything`
- `CLIPTextEncode` ★核心
- `LayerUtility: ImageReelComposit`
- `SaveImage`
- `LayerUtility: ImageReel`
- `SaveImage`
- `KSampler` ★核心
- `PreviewImage`
- `PrimitiveFloat`
- `LoadImage`
- `MaskToImage`
- `LayerStyle: ColorOverlay`
- `SaveImage`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `56660551018566`
- `steps` = `20`
- `cfg` = `1`
- `sampler_name` = `er_sde`
- `scheduler` = `beta`
- `denoise` = `1`

## 知识

覆盖率 **86%**（24/28）

**有卡**：`FluxGuidance`、`FluxKontextImageScale`、`ReferenceLatent`、`ConditioningZeroOut`、`VAEEncode`、`VAELoader`、`VAEDecode`、`TextCombinerTwo`、`RH_Translator`、`Bjornulf_TextReplace`、`RH_Captioner`、`LoraLoaderModelOnly`、`UNETLoader`、`DualCLIPLoader`、`CLIPTextEncode`、`LayerUtility: ImageReelComposit`、`SaveImage`、`LayerUtility: ImageReel`、`KSampler`、`LoadImage`、`MaskToImage`、`LayerStyle: ColorOverlay`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPTextEncode、ConditioningZeroOut、LoadImage

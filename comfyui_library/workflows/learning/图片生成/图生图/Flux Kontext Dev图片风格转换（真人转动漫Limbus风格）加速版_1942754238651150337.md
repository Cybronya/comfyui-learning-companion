---
key: 图片生成/图生图/Flux Kontext Dev图片风格转换（真人转动漫Limbus风格）加速版_1942754238651150337.json
name: Flux Kontext Dev图片风格转换（真人转动漫Limbus风格）加速版_1942754238651150337
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Flux Kontext Dev图片风格转换（真人转动漫Limbus风格）加速版_1942754238651150337.json
hash: 5f22478159caadee
coverage: 1
learned_at: 2026-10-23 10:57:06
nodes: [ImageStitch, FluxGuidance, ReferenceLatent, ConditioningZeroOut, VAEEncode, VAEDecode, SaveImage, FluxKontextImageScale, CLIPTextEncode, RH_Translator, DualCLIPLoader, VAELoader, UNETLoader, SaveImage, ImageConcatMulti, NunchakuFluxDiTLoader, NunchakuFluxLoraLoader, MagCache, LoraLoaderModelOnly, UnetLoaderGGUF, LoadImage, Text Multiline, PMRF, SaveImage, KSampler]
patterns: [image_to_image]
missing: []
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 95177397952175, "steps": 20}
---

# 图片生成/图生图/Flux Kontext Dev图片风格转换（真人转动漫Limbus风格）加速版_1942754238651150337.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Flux Kontext Dev图片风格转换（真人转动漫Limbus风格）加速版_1942754238651150337.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（25 个）：
- `ImageStitch`
- `FluxGuidance`
- `ReferenceLatent`
- `ConditioningZeroOut`
- `VAEEncode` ★核心
- `VAEDecode` ★核心
- `SaveImage`
- `FluxKontextImageScale`
- `CLIPTextEncode` ★核心
- `RH_Translator`
- `DualCLIPLoader`
- `VAELoader`
- `UNETLoader` ★核心
- `SaveImage`
- `ImageConcatMulti`
- `NunchakuFluxDiTLoader`
- `NunchakuFluxLoraLoader` ★核心
- `MagCache`
- `LoraLoaderModelOnly` ★核心
- `UnetLoaderGGUF` ★核心
- `LoadImage`
- `Text Multiline`
- `PMRF`
- `SaveImage`
- `KSampler` ★核心

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `95177397952175`
- `steps` = `20`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **100%**（25/25）

**有卡**：`ImageStitch`、`FluxGuidance`、`ReferenceLatent`、`ConditioningZeroOut`、`VAEEncode`、`VAEDecode`、`SaveImage`、`FluxKontextImageScale`、`CLIPTextEncode`、`RH_Translator`、`DualCLIPLoader`、`VAELoader`、`UNETLoader`、`ImageConcatMulti`、`NunchakuFluxDiTLoader`、`NunchakuFluxLoraLoader`、`MagCache`、`LoraLoaderModelOnly`、`UnetLoaderGGUF`、`LoadImage`、`Text Multiline`、`PMRF`、`KSampler`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPTextEncode、ConditioningZeroOut、LoadImage

---
key: 平台全量/Kontext-产品融合场景2.0（lora版）_1946617154928304129.json
name: Kontext-产品融合场景2.0（lora版）_1946617154928304129
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/平台全量/Kontext-产品融合场景2.0（lora版）_1946617154928304129.json
hash: d86ea1b252372b1b
coverage: 0.774194
learned_at: 2026-11-14 00:34:56
nodes: [MarkdownNote, easy int, Anything Everywhere, SaveImage, VAEDecode, VAELoader, DualCLIPLoader, ConditioningZeroOut, FluxGuidance, ReferenceLatent, UNETLoader, LoadAndResizeImage, LoadAndResizeImage, Anything Everywhere3, Note, Image Comparer (rgthree), KSampler, EmptyLatentImage, LayerUtility: ImageAutoCrop, FluxKontextImageScale, VAEEncode, CLIPTextEncode, LoraLoaderModelOnly, GetImageSize+, ImageScaleBy, PreviewImage, RH_Translator, TextInput_, Fast Groups Bypasser (rgthree), LoadImage, LayerUtility: ImageBlendAdvance]
patterns: [text_to_image, image_to_image]
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1536, "sampler_name": "euler", "scheduler": "simple", "seed": 841332171901910, "steps": 20, "width": 1024}
---

# 平台全量/Kontext-产品融合场景2.0（lora版）_1946617154928304129.json

> 来源文件 `comfyui_library/workflows/平台全量/Kontext-产品融合场景2.0（lora版）_1946617154928304129.json`

## 结构

**生成流程**：Model → Encode → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（31 个）：
- `MarkdownNote`
- `easy int`
- `Anything Everywhere`
- `SaveImage`
- `VAEDecode` ★核心
- `VAELoader`
- `DualCLIPLoader`
- `ConditioningZeroOut`
- `FluxGuidance`
- `ReferenceLatent`
- `UNETLoader` ★核心
- `LoadAndResizeImage`
- `LoadAndResizeImage`
- `Anything Everywhere3`
- `Note`
- `Image Comparer (rgthree)`
- `KSampler` ★核心
- `EmptyLatentImage` ★核心
- `LayerUtility: ImageAutoCrop`
- `FluxKontextImageScale`
- `VAEEncode` ★核心
- `CLIPTextEncode` ★核心
- `LoraLoaderModelOnly` ★核心
- `GetImageSize+`
- `ImageScaleBy`
- `PreviewImage`
- `RH_Translator`
- `TextInput_`
- `Fast Groups Bypasser (rgthree)`
- `LoadImage`
- `LayerUtility: ImageBlendAdvance`

**识别到的模式**：text_to_image、image_to_image

## 关键参数

- `seed` = `841332171901910`
- `steps` = `20`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`
- `width` = `1024`
- `height` = `1536`
- `batch_size` = `1`

## 知识

覆盖率 **77%**（24/31）

**有卡**：`easy int`、`SaveImage`、`VAEDecode`、`VAELoader`、`DualCLIPLoader`、`ConditioningZeroOut`、`FluxGuidance`、`ReferenceLatent`、`UNETLoader`、`LoadAndResizeImage`、`KSampler`、`EmptyLatentImage`、`LayerUtility: ImageAutoCrop`、`FluxKontextImageScale`、`VAEEncode`、`CLIPTextEncode`、`LoraLoaderModelOnly`、`GetImageSize+`、`ImageScaleBy`、`RH_Translator`、`TextInput_`、`LoadImage`、`LayerUtility: ImageBlendAdvance`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPTextEncode、ConditioningZeroOut、EmptyLatentImage

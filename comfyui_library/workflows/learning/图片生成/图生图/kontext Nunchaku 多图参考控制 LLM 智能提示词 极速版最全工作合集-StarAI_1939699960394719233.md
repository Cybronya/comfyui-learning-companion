---
key: 图片生成/图生图/kontext Nunchaku 多图参考控制 LLM 智能提示词 极速版最全工作合集-StarAI_1939699960394719233.json
name: kontext Nunchaku 多图参考控制 LLM 智能提示词 极速版最全工作合集-StarAI_1939699960394719233
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/kontext Nunchaku 多图参考控制 LLM 智能提示词 极速版最全工作合集-StarAI_1939699960394719233.json
hash: 7b7fe7978d3fde7d
coverage: 0.913793
learned_at: 2026-10-23 11:38:42
nodes: [ReferenceLatent, Note Plus (mtb), DualCLIPLoader, VAEEncode, FluxKontextImageScale, VAEDecode, FluxGuidance, ConditioningZeroOut, KSampler, RH_LLMAPI_NODE, CLIPTextEncode, VAELoader, LoadImage, Text, SaveImage, RH_LLMAPI_NODE, MathExpression|pysssss, MathExpression|pysssss, MathExpression|pysssss, EmptyLatentImage, MathExpression|pysssss, VAELoader, DualCLIPLoader, ConditioningZeroOut, ReferenceLatent, FluxGuidance, VAEEncode, DifferentialDiffusion, ImageConcanate, FluxKontextImageScale, LayerUtility: ImageScaleByAspectRatio V2, ImageResize+, CLIPTextEncode, LoadImage, PreviewImage, LoadImage, RMBG, CR Text, FluxResolutionNode, VAEDecode, KSampler, easy showAnything, VAEEncode, ReferenceLatent, EmptyLatentImage, ConditioningZeroOut, KSampler, VAEDecode, FluxGuidance, MathExpression|pysssss, MathExpression|pysssss, MathExpression|pysssss, MathExpression|pysssss, PreviewImage, PreviewImage, RMBG, LayerUtility: CropByMask V2, LayerUtility: ImageRemoveAlpha, ImageConcanate, LayerUtility: ImageScaleByAspectRatio V2, ImageConcanate, ImageResize+, RMBG, LoadImage, LoadImage, PreviewImage, LoadImage, RH_LLMAPI_NODE, CLIPTextEncode, Text, DualCLIPLoader, VAELoader, ModelSamplingFlux, easy imageRemBg, LoadImage, ImageScaleToMegapixels, LoadImage, ImageScaleToMegapixels, easy imageRemBg, LoadImage, CompositorConfig3, ImageScaleToMegapixels, ShowText|pysssss, Compositor3, CR Text, SaveImage, SaveImage, KSampler, VAEDecode, ImageConcatMulti, ImageConcanate, PreviewImage, DualCLIPLoader, RH_LLMAPI_NODE, ConditioningZeroOut, FluxGuidance, VAEEncode, ReferenceLatent, FluxKontextImageScale, ImageScaleToMegapixels, CLIPTextEncode, VAELoader, SaveImage, SaveImage, FluxResolutionNode, NunchakuFluxDiTLoader, NunchakuFluxDiTLoader, NunchakuFluxDiTLoader, NunchakuFluxDiTLoader, MarkdownNote, Fast Groups Bypasser (rgthree), UnetLoaderGGUF, ImpactSwitch, NunchakuFluxDiTLoader, UNETLoader, Int]
patterns: [text_to_image, image_to_image]
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1280, "sampler_name": "euler", "scheduler": "simple", "seed": 1079957549505869, "steps": 20, "width": 1024}
---

# 图片生成/图生图/kontext Nunchaku 多图参考控制 LLM 智能提示词 极速版最全工作合集-StarAI_1939699960394719233.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/kontext Nunchaku 多图参考控制 LLM 智能提示词 极速版最全工作合集-StarAI_1939699960394719233.json`

## 结构

**生成流程**：Model → Encode → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（116 个）：
- `ReferenceLatent`
- `Note Plus (mtb)`
- `DualCLIPLoader`
- `VAEEncode` ★核心
- `FluxKontextImageScale`
- `VAEDecode` ★核心
- `FluxGuidance`
- `ConditioningZeroOut`
- `KSampler` ★核心
- `RH_LLMAPI_NODE`
- `CLIPTextEncode` ★核心
- `VAELoader`
- `LoadImage`
- `Text`
- `SaveImage`
- `RH_LLMAPI_NODE`
- `MathExpression|pysssss`
- `MathExpression|pysssss`
- `MathExpression|pysssss`
- `EmptyLatentImage` ★核心
- `MathExpression|pysssss`
- `VAELoader`
- `DualCLIPLoader`
- `ConditioningZeroOut`
- `ReferenceLatent`
- `FluxGuidance`
- `VAEEncode` ★核心
- `DifferentialDiffusion`
- `ImageConcanate`
- `FluxKontextImageScale`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `ImageResize+`
- `CLIPTextEncode` ★核心
- `LoadImage`
- `PreviewImage`
- `LoadImage`
- `RMBG`
- `CR Text`
- `FluxResolutionNode`
- `VAEDecode` ★核心
- `KSampler` ★核心
- `easy showAnything`
- `VAEEncode` ★核心
- `ReferenceLatent`
- `EmptyLatentImage` ★核心
- `ConditioningZeroOut`
- `KSampler` ★核心
- `VAEDecode` ★核心
- `FluxGuidance`
- `MathExpression|pysssss`
- `MathExpression|pysssss`
- `MathExpression|pysssss`
- `MathExpression|pysssss`
- `PreviewImage`
- `PreviewImage`
- `RMBG`
- `LayerUtility: CropByMask V2`
- `LayerUtility: ImageRemoveAlpha`
- `ImageConcanate`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `ImageConcanate`
- `ImageResize+`
- `RMBG`
- `LoadImage`
- `LoadImage`
- `PreviewImage`
- `LoadImage`
- `RH_LLMAPI_NODE`
- `CLIPTextEncode` ★核心
- `Text`
- `DualCLIPLoader`
- `VAELoader`
- `ModelSamplingFlux`
- `easy imageRemBg`
- `LoadImage`
- `ImageScaleToMegapixels`
- `LoadImage`
- `ImageScaleToMegapixels`
- `easy imageRemBg`
- `LoadImage`
- `CompositorConfig3`
- `ImageScaleToMegapixels`
- `ShowText|pysssss`
- `Compositor3`
- `CR Text`
- `SaveImage`
- `SaveImage`
- `KSampler` ★核心
- `VAEDecode` ★核心
- `ImageConcatMulti`
- `ImageConcanate`
- `PreviewImage`
- `DualCLIPLoader`
- `RH_LLMAPI_NODE`
- `ConditioningZeroOut`
- `FluxGuidance`
- `VAEEncode` ★核心
- `ReferenceLatent`
- `FluxKontextImageScale`
- `ImageScaleToMegapixels`
- `CLIPTextEncode` ★核心
- `VAELoader`
- `SaveImage`
- `SaveImage`
- `FluxResolutionNode`
- `NunchakuFluxDiTLoader`
- `NunchakuFluxDiTLoader`
- `NunchakuFluxDiTLoader`
- `NunchakuFluxDiTLoader`
- `MarkdownNote`
- `Fast Groups Bypasser (rgthree)`
- `UnetLoaderGGUF` ★核心
- `ImpactSwitch`
- `NunchakuFluxDiTLoader`
- `UNETLoader` ★核心
- `Int`

**识别到的模式**：text_to_image、image_to_image

## 关键参数

- `seed` = `1079957549505869`
- `steps` = `20`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`
- `width` = `1024`
- `height` = `1280`
- `batch_size` = `1`

## 知识

覆盖率 **91%**（106/116）

**有卡**：`ReferenceLatent`、`Note Plus (mtb)`、`DualCLIPLoader`、`VAEEncode`、`FluxKontextImageScale`、`VAEDecode`、`FluxGuidance`、`ConditioningZeroOut`、`KSampler`、`RH_LLMAPI_NODE`、`CLIPTextEncode`、`VAELoader`、`LoadImage`、`Text`、`SaveImage`、`MathExpression|pysssss`、`EmptyLatentImage`、`DifferentialDiffusion`、`ImageConcanate`、`LayerUtility: ImageScaleByAspectRatio V2`、`ImageResize+`、`RMBG`、`CR Text`、`FluxResolutionNode`、`LayerUtility: CropByMask V2`、`LayerUtility: ImageRemoveAlpha`、`ModelSamplingFlux`、`easy imageRemBg`、`ImageScaleToMegapixels`、`CompositorConfig3`、`Compositor3`、`ImageConcatMulti`、`NunchakuFluxDiTLoader`、`UnetLoaderGGUF`、`UNETLoader`、`Int`

**用到的条目**：KSampler、VAEDecode、VAELoader、UNETLoader、CLIPTextEncode、ConditioningZeroOut、EmptyLatentImage、LoadImage

---
key: 图片生成/图生图/一分钟极速换脸Nunchaku FLUX ACE+Redux面部迁移双截棍工作流-StarAI_1915382481413931009.json
name: 一分钟极速换脸Nunchaku FLUX ACE+Redux面部迁移双截棍工作流-StarAI_1915382481413931009
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/一分钟极速换脸Nunchaku FLUX ACE+Redux面部迁移双截棍工作流-StarAI_1915382481413931009.json
hash: ed0759a8c0e8501d
coverage: 0.857143
learned_at: 2026-10-23 11:53:14
nodes: [LayerUtility: Florence2Image2Prompt, LayerUtility: PurgeVRAM, Text Concatenate (JPS), LayerMask: LoadFlorence2Model, VAELoader, CLIPVisionLoader, StyleModelLoader, InpaintModelConditioning, ConditioningZeroOut, KSampler, VAEDecode, LayerUtility: PurgeVRAM, PreviewImage, LayerUtility: RestoreCropBox, GrowMaskWithBlur, LayerMask: PersonMaskUltra V2, SaveImage, CR Text, ImageCrop, Image Comparer (rgthree), ReduxAdvanced, LoadImage, CLIPTextEncode, FluxGuidance, NunchakuFluxDiTLoader, MaskToSEGS, PreviewImage, LayerUtility: PurgeVRAM, DetailerForEach, PreviewImage, MaskPreview+, Note Plus (mtb), NunchakuFluxDiTLoader, NunchakuTextEncoderLoader, NunchakuFluxLoraLoader, NunchakuFluxLoraLoader, MaskPreview+, PreviewImage, ImageAndMaskPreview, RHHiddenNodes, LoadImage, Fast Groups Bypasser (rgthree)]
patterns: []
missing: []
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "normal", "seed": 1114746832794843, "steps": 20}
---

# 图片生成/图生图/一分钟极速换脸Nunchaku FLUX ACE+Redux面部迁移双截棍工作流-StarAI_1915382481413931009.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/一分钟极速换脸Nunchaku FLUX ACE+Redux面部迁移双截棍工作流-StarAI_1915382481413931009.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（42 个）：
- `LayerUtility: Florence2Image2Prompt`
- `LayerUtility: PurgeVRAM`
- `Text Concatenate (JPS)`
- `LayerMask: LoadFlorence2Model`
- `VAELoader`
- `CLIPVisionLoader`
- `StyleModelLoader`
- `InpaintModelConditioning`
- `ConditioningZeroOut`
- `KSampler` ★核心
- `VAEDecode` ★核心
- `LayerUtility: PurgeVRAM`
- `PreviewImage`
- `LayerUtility: RestoreCropBox`
- `GrowMaskWithBlur`
- `LayerMask: PersonMaskUltra V2`
- `SaveImage`
- `CR Text`
- `ImageCrop`
- `Image Comparer (rgthree)`
- `ReduxAdvanced`
- `LoadImage`
- `CLIPTextEncode` ★核心
- `FluxGuidance`
- `NunchakuFluxDiTLoader`
- `MaskToSEGS`
- `PreviewImage`
- `LayerUtility: PurgeVRAM`
- `DetailerForEach`
- `PreviewImage`
- `MaskPreview+`
- `Note Plus (mtb)`
- `NunchakuFluxDiTLoader`
- `NunchakuTextEncoderLoader`
- `NunchakuFluxLoraLoader` ★核心
- `NunchakuFluxLoraLoader` ★核心
- `MaskPreview+`
- `PreviewImage`
- `ImageAndMaskPreview`
- `RHHiddenNodes`
- `LoadImage`
- `Fast Groups Bypasser (rgthree)`

## 关键参数

- `seed` = `1114746832794843`
- `steps` = `20`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `normal`
- `denoise` = `1`

## 知识

覆盖率 **86%**（36/42）

**有卡**：`LayerUtility: Florence2Image2Prompt`、`LayerUtility: PurgeVRAM`、`Text Concatenate (JPS)`、`LayerMask: LoadFlorence2Model`、`VAELoader`、`CLIPVisionLoader`、`StyleModelLoader`、`InpaintModelConditioning`、`ConditioningZeroOut`、`KSampler`、`VAEDecode`、`LayerUtility: RestoreCropBox`、`GrowMaskWithBlur`、`LayerMask: PersonMaskUltra V2`、`SaveImage`、`CR Text`、`ImageCrop`、`ReduxAdvanced`、`LoadImage`、`CLIPTextEncode`、`FluxGuidance`、`NunchakuFluxDiTLoader`、`MaskToSEGS`、`DetailerForEach`、`MaskPreview+`、`Note Plus (mtb)`、`NunchakuTextEncoderLoader`、`NunchakuFluxLoraLoader`、`ImageAndMaskPreview`、`RHHiddenNodes`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、ConditioningZeroOut、LoadImage、FluxGuidance、NunchakuTextEncoderLoader

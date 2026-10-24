---
key: 图片生成/图生图/sam3.1 语义分割提取_2048535121246031874.json
name: sam3.1 语义分割提取_2048535121246031874
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/sam3.1 语义分割提取_2048535121246031874.json
hash: f751092f105a46f9
coverage: 0.860294
learned_at: 2026-10-23 11:44:50
nodes: [VAELoader, Image Comparer (rgthree), SaveImage, CLIPLoader, CLIPLoader, VAELoader, Image Comparer (rgthree), SaveImage, InpaintModelConditioning, InpaintStitchImproved, ConditioningZeroOut, Image Comparer (rgthree), InpaintCropImproved, VAEDecode, ImageAndMaskPreview, INTConstant, VAELoader, ReferenceLatent, InpaintStitchImproved, LayerUtility: PurgeVRAM V2, INTConstant, VAEEncode, ReferenceLatent, ConditioningZeroOut, ColorMatch, LoraLoaderModelOnly, INPAINT_ExpandMask, INPAINT_ExpandMask, LoraLoaderModelOnly, VAEDecode, ReferenceLatent, ImageAndMaskPreview, Image Comparer (rgthree), UNETLoader, VAEEncode, KSampler, CLIPTextEncode, UNETLoader, ColorMatch, KSampler, KSamplerSelect, Flux2Scheduler, ReferenceLatent, ReferenceLatent, VAEEncode, ReferenceLatent, ReferenceLatent, CFGGuider, RandomNoise, LoraLoaderModelOnly, Image Comparer (rgthree), EmptyFlux2LatentImage, DrawMaskOnImage, CLIPLoader, VAELoader, VAEEncode, ImageScaleToTotalPixels, SaveImage, Image Comparer (rgthree), LayerUtility: ImageScaleByAspectRatio V2, ConditioningZeroOut, INPAINT_ExpandMask, LayerUtility: PurgeVRAM V2, Seed (rgthree), LoadImage, InpaintCropImproved, ConditioningZeroOut, LayerUtility: PurgeVRAM V2, ImageCompositeMasked, VAEDecode, LoraLoaderModelOnly, SamplerCustomAdvanced, ImageAndMaskPreview, Seed (rgthree), LoadImage, UNETLoader, CLIPTextEncode, KSampler, ImageAndMaskPreview, ImageAndMaskPreview, INPAINT_ExpandMask, DifferentialDiffusion, ReferenceLatent, DrawMaskOnImage, EmptyFlux2LatentImage, INPAINT_ExpandMask, VAEDecode, ColorMatch, SaveImage, SaveImage, LoadImage, easy int, Seed (rgthree), CLIPTextEncode, ImageCompositeMasked, Fast Groups Bypasser (rgthree), Fast Groups Bypasser (rgthree), Fast Groups Bypasser (rgthree), Seed (rgthree), Fast Groups Bypasser (rgthree), Fast Groups Bypasser (rgthree), SAM3_Detect, CheckpointLoaderSimple, ImageAndMaskPreview, CLIPTextEncode, Fast Groups Bypasser (rgthree), SAM3_Detect, CLIPTextEncode, CheckpointLoaderSimple, SAM3_Detect, CheckpointLoaderSimple, ImageAndMaskPreview, PreviewImage, CLIPTextEncode, SAM3_Detect, CheckpointLoaderSimple, Fast Groups Bypasser (rgthree), CheckpointLoaderSimple, Fast Groups Bypasser (rgthree), CLIPTextEncode, DeepTranslatorTextNode, easy showAnything, LoadImage, LoadImage, ImageAndMaskPreview, SAM3_Detect, Fast Groups Bypasser (rgthree), Fast Groups Bypasser (rgthree), Fast Groups Bypasser (rgthree), CLIPTextEncode, UNETLoader, CLIPLoader, InpaintModelConditioning, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, CLIPTextEncode]
patterns: [image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "checkpoint": "sam3.1_multiplex_fp16.safetensors", "denoise": 0.6, "sampler_name": "euler", "scheduler": "simple", "seed": 1044160720030426, "steps": 5}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/sam3.1 语义分割提取_2048535121246031874.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/sam3.1 语义分割提取_2048535121246031874.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（136 个）：
- `VAELoader`
- `Image Comparer (rgthree)`
- `SaveImage`
- `CLIPLoader`
- `CLIPLoader`
- `VAELoader`
- `Image Comparer (rgthree)`
- `SaveImage`
- `InpaintModelConditioning`
- `InpaintStitchImproved`
- `ConditioningZeroOut`
- `Image Comparer (rgthree)`
- `InpaintCropImproved`
- `VAEDecode` ★核心
- `ImageAndMaskPreview`
- `INTConstant`
- `VAELoader`
- `ReferenceLatent`
- `InpaintStitchImproved`
- `LayerUtility: PurgeVRAM V2`
- `INTConstant`
- `VAEEncode` ★核心
- `ReferenceLatent`
- `ConditioningZeroOut`
- `ColorMatch`
- `LoraLoaderModelOnly` ★核心
- `INPAINT_ExpandMask`
- `INPAINT_ExpandMask`
- `LoraLoaderModelOnly` ★核心
- `VAEDecode` ★核心
- `ReferenceLatent`
- `ImageAndMaskPreview`
- `Image Comparer (rgthree)`
- `UNETLoader` ★核心
- `VAEEncode` ★核心
- `KSampler` ★核心
- `CLIPTextEncode` ★核心
- `UNETLoader` ★核心
- `ColorMatch`
- `KSampler` ★核心
- `KSamplerSelect` ★核心
- `Flux2Scheduler`
- `ReferenceLatent`
- `ReferenceLatent`
- `VAEEncode` ★核心
- `ReferenceLatent`
- `ReferenceLatent`
- `CFGGuider`
- `RandomNoise`
- `LoraLoaderModelOnly` ★核心
- `Image Comparer (rgthree)`
- `EmptyFlux2LatentImage`
- `DrawMaskOnImage`
- `CLIPLoader`
- `VAELoader`
- `VAEEncode` ★核心
- `ImageScaleToTotalPixels`
- `SaveImage`
- `Image Comparer (rgthree)`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `ConditioningZeroOut`
- `INPAINT_ExpandMask`
- `LayerUtility: PurgeVRAM V2`
- `Seed (rgthree)`
- `LoadImage`
- `InpaintCropImproved`
- `ConditioningZeroOut`
- `LayerUtility: PurgeVRAM V2`
- `ImageCompositeMasked`
- `VAEDecode` ★核心
- `LoraLoaderModelOnly` ★核心
- `SamplerCustomAdvanced` ★核心
- `ImageAndMaskPreview`
- `Seed (rgthree)`
- `LoadImage`
- `UNETLoader` ★核心
- `CLIPTextEncode` ★核心
- `KSampler` ★核心
- `ImageAndMaskPreview`
- `ImageAndMaskPreview`
- `INPAINT_ExpandMask`
- `DifferentialDiffusion`
- `ReferenceLatent`
- `DrawMaskOnImage`
- `EmptyFlux2LatentImage`
- `INPAINT_ExpandMask`
- `VAEDecode` ★核心
- `ColorMatch`
- `SaveImage`
- `SaveImage`
- `LoadImage`
- `easy int`
- `Seed (rgthree)`
- `CLIPTextEncode` ★核心
- `ImageCompositeMasked`
- `Fast Groups Bypasser (rgthree)`
- `Fast Groups Bypasser (rgthree)`
- `Fast Groups Bypasser (rgthree)`
- `Seed (rgthree)`
- `Fast Groups Bypasser (rgthree)`
- `Fast Groups Bypasser (rgthree)`
- `SAM3_Detect`
- `CheckpointLoaderSimple` ★核心
- `ImageAndMaskPreview`
- `CLIPTextEncode` ★核心
- `Fast Groups Bypasser (rgthree)`
- `SAM3_Detect`
- `CLIPTextEncode` ★核心
- `CheckpointLoaderSimple` ★核心
- `SAM3_Detect`
- `CheckpointLoaderSimple` ★核心
- `ImageAndMaskPreview`
- `PreviewImage`
- `CLIPTextEncode` ★核心
- `SAM3_Detect`
- `CheckpointLoaderSimple` ★核心
- `Fast Groups Bypasser (rgthree)`
- `CheckpointLoaderSimple` ★核心
- `Fast Groups Bypasser (rgthree)`
- `CLIPTextEncode` ★核心
- `DeepTranslatorTextNode`
- `easy showAnything`
- `LoadImage`
- `LoadImage`
- `ImageAndMaskPreview`
- `SAM3_Detect`
- `Fast Groups Bypasser (rgthree)`
- `Fast Groups Bypasser (rgthree)`
- `Fast Groups Bypasser (rgthree)`
- `CLIPTextEncode` ★核心
- `UNETLoader` ★核心
- `CLIPLoader`
- `InpaintModelConditioning`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `CLIPTextEncode` ★核心

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `1044160720030426`
- `steps` = `5`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `0.6`
- `checkpoint` = `sam3.1_multiplex_fp16.safetensors`

## 知识

覆盖率 **86%**（117/136）

**有卡**：`VAELoader`、`SaveImage`、`CLIPLoader`、`InpaintModelConditioning`、`InpaintStitchImproved`、`ConditioningZeroOut`、`InpaintCropImproved`、`VAEDecode`、`ImageAndMaskPreview`、`INTConstant`、`ReferenceLatent`、`LayerUtility: PurgeVRAM V2`、`VAEEncode`、`ColorMatch`、`LoraLoaderModelOnly`、`INPAINT_ExpandMask`、`UNETLoader`、`KSampler`、`CLIPTextEncode`、`KSamplerSelect`、`Flux2Scheduler`、`CFGGuider`、`RandomNoise`、`EmptyFlux2LatentImage`、`DrawMaskOnImage`、`ImageScaleToTotalPixels`、`LayerUtility: ImageScaleByAspectRatio V2`、`Seed (rgthree)`、`LoadImage`、`ImageCompositeMasked`、`SamplerCustomAdvanced`、`DifferentialDiffusion`、`easy int`、`SAM3_Detect`、`CheckpointLoaderSimple`、`DeepTranslatorTextNode`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CheckpointLoaderSimple、UNETLoader、CLIPTextEncode、CLIPLoader

## 参数体检

发现 3 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

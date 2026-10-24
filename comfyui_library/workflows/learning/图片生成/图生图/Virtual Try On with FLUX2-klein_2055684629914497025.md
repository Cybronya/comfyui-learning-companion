---
key: 图片生成/图生图/Virtual Try On with FLUX2-klein_2055684629914497025.json
name: Virtual Try On with FLUX2-klein_2055684629914497025
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Virtual Try On with FLUX2-klein_2055684629914497025.json
hash: dc73605bd0f05511
coverage: 0.99
learned_at: 2026-10-23 11:27:20
nodes: [CR Text, ImageScaleToTotalPixels, LayerUtility: PurgeVRAM V2, CR Text, CR Text Concatenate, easy showAnything, CLIPLoader, CLIPTextEncode, VAELoader, VAEEncode, ReferenceLatent, VAEEncode, ReferenceLatent, ConditioningZeroOut, ReferenceLatent, ReferenceLatent, CFGGuider, KSamplerSelect, easy int, LayerUtility: ImageScaleByAspectRatio V2, Flux2Scheduler, EmptyFlux2LatentImage, SamplerCustomAdvanced, LayerUtility: PurgeVRAM V2, VAEDecode, easy sam3ImageSegmentation, easy sam3ImageSegmentation, AddMask, Mask Fill Holes, INPAINT_ExpandMask, ImageCompositeMasked, LayerUtility: PurgeVRAM V2, RandomNoise, CR Text, CR Text Concatenate, CLIPTextEncode, easy int, LayerUtility: ImageScaleByAspectRatio V2, VAEEncode, ReferenceLatent, ReferenceLatent, CFGGuider, KSamplerSelect, Flux2Scheduler, EmptyFlux2LatentImage, SamplerCustomAdvanced, LayerUtility: PurgeVRAM V2, DrawMaskOnImage, SaveImage, ImageCompositeMasked, SaveImage, DrawMaskOnImage, SaveImage, SaveImage, VAEDecode, SaveImage, INPAINT_ExpandMask, Mask Invert, JoinImageWithAlpha, ColorMatch, INPAINT_ExpandMask, Mask Invert, ImageCompositeMasked, SaveImage, ReferenceLatent, VAEEncode, CFGGuider, RandomNoise, KSamplerSelect, Flux2Scheduler, CLIPLoader, VAELoader, ConditioningZeroOut, LayerUtility: PurgeVRAM V2, VAEDecode, EmptyFlux2LatentImage, ImageScaleToTotalPixels, GetImageSize, ImageResizeKJv2, SaveImage, CLIPTextEncode, SamplerCustomAdvanced, CR Text, LayerUtility: ImageScaleByAspectRatio V2, easy sam3ModelLoader, SaveImage, LoraLoaderModelOnly, UNETLoader, LoraLoaderModelOnly, UNETLoader, AILab_QwenVL, AILab_QwenVL, LoadImage, LoadImage, SaveImage, RandomNoise, ReferenceLatent, Seed (rgthree), Seed (rgthree), ImageSmartSharpen+]
patterns: []
missing: []
---

# 图片生成/图生图/Virtual Try On with FLUX2-klein_2055684629914497025.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Virtual Try On with FLUX2-klein_2055684629914497025.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（100 个）：
- `CR Text`
- `ImageScaleToTotalPixels`
- `LayerUtility: PurgeVRAM V2`
- `CR Text`
- `CR Text Concatenate`
- `easy showAnything`
- `CLIPLoader`
- `CLIPTextEncode` ★核心
- `VAELoader`
- `VAEEncode` ★核心
- `ReferenceLatent`
- `VAEEncode` ★核心
- `ReferenceLatent`
- `ConditioningZeroOut`
- `ReferenceLatent`
- `ReferenceLatent`
- `CFGGuider`
- `KSamplerSelect` ★核心
- `easy int`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `Flux2Scheduler`
- `EmptyFlux2LatentImage`
- `SamplerCustomAdvanced` ★核心
- `LayerUtility: PurgeVRAM V2`
- `VAEDecode` ★核心
- `easy sam3ImageSegmentation`
- `easy sam3ImageSegmentation`
- `AddMask`
- `Mask Fill Holes`
- `INPAINT_ExpandMask`
- `ImageCompositeMasked`
- `LayerUtility: PurgeVRAM V2`
- `RandomNoise`
- `CR Text`
- `CR Text Concatenate`
- `CLIPTextEncode` ★核心
- `easy int`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `VAEEncode` ★核心
- `ReferenceLatent`
- `ReferenceLatent`
- `CFGGuider`
- `KSamplerSelect` ★核心
- `Flux2Scheduler`
- `EmptyFlux2LatentImage`
- `SamplerCustomAdvanced` ★核心
- `LayerUtility: PurgeVRAM V2`
- `DrawMaskOnImage`
- `SaveImage`
- `ImageCompositeMasked`
- `SaveImage`
- `DrawMaskOnImage`
- `SaveImage`
- `SaveImage`
- `VAEDecode` ★核心
- `SaveImage`
- `INPAINT_ExpandMask`
- `Mask Invert`
- `JoinImageWithAlpha`
- `ColorMatch`
- `INPAINT_ExpandMask`
- `Mask Invert`
- `ImageCompositeMasked`
- `SaveImage`
- `ReferenceLatent`
- `VAEEncode` ★核心
- `CFGGuider`
- `RandomNoise`
- `KSamplerSelect` ★核心
- `Flux2Scheduler`
- `CLIPLoader`
- `VAELoader`
- `ConditioningZeroOut`
- `LayerUtility: PurgeVRAM V2`
- `VAEDecode` ★核心
- `EmptyFlux2LatentImage`
- `ImageScaleToTotalPixels`
- `GetImageSize`
- `ImageResizeKJv2`
- `SaveImage`
- `CLIPTextEncode` ★核心
- `SamplerCustomAdvanced` ★核心
- `CR Text`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `easy sam3ModelLoader`
- `SaveImage`
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `AILab_QwenVL`
- `AILab_QwenVL`
- `LoadImage`
- `LoadImage`
- `SaveImage`
- `RandomNoise`
- `ReferenceLatent`
- `Seed (rgthree)`
- `Seed (rgthree)`
- `ImageSmartSharpen+`

## 知识

覆盖率 **99%**（99/100）

**有卡**：`CR Text`、`ImageScaleToTotalPixels`、`LayerUtility: PurgeVRAM V2`、`CR Text Concatenate`、`CLIPLoader`、`CLIPTextEncode`、`VAELoader`、`VAEEncode`、`ReferenceLatent`、`ConditioningZeroOut`、`CFGGuider`、`KSamplerSelect`、`easy int`、`LayerUtility: ImageScaleByAspectRatio V2`、`Flux2Scheduler`、`EmptyFlux2LatentImage`、`SamplerCustomAdvanced`、`VAEDecode`、`easy sam3ImageSegmentation`、`AddMask`、`Mask Fill Holes`、`INPAINT_ExpandMask`、`ImageCompositeMasked`、`RandomNoise`、`DrawMaskOnImage`、`SaveImage`、`Mask Invert`、`JoinImageWithAlpha`、`ColorMatch`、`GetImageSize`、`ImageResizeKJv2`、`easy sam3ModelLoader`、`LoraLoaderModelOnly`、`UNETLoader`、`AILab_QwenVL`、`LoadImage`、`Seed (rgthree)`、`ImageSmartSharpen+`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、LoadImage

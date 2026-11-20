---
key: 平台全量/Flux.2 klein 换头_换脸_人脸参考IP-局部重绘-聚焦裁剪「色块填充版」_2013655608490205185.json
name: Flux.2 klein 换头_换脸_人脸参考IP-局部重绘-聚焦裁剪「色块填充版」_2013655608490205185
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/平台全量/Flux.2 klein 换头_换脸_人脸参考IP-局部重绘-聚焦裁剪「色块填充版」_2013655608490205185.json
hash: f8c59486f8179632
coverage: 0.511236
learned_at: 2026-11-14 00:28:56
nodes: [InstantIDFaceAnalysis, ControlNetLoader, SetNode, SetNode, ApplyInstantID, CLIPTextEncode, CLIPTextEncode, GetNode, LayerMask: PersonMaskUltra V2, KSampler, easy imageRemBg, LayerMask: PersonMaskUltra V2, PreviewImage, SetNode, DifferentialDiffusion, InpaintModelConditioning, CheckpointLoaderSimple, GetNode, InstantIDModelLoader, SetNode, GetNode, ImageAndMaskPreview, GetNode, GetNode, SetNode, SetNode, GetNode, GetNode, ImageSmartSharpen+, GetNode, SetNode, VAEDecode, InpaintStitchImproved, SetNode, SetNode, easy cleanGpuUsed, GetImageSize, SetNode, PreviewImage, GetNode, InpaintCropImproved, LayerMask: PersonMaskUltra V2, SegsToCombinedMask, SetNode, SetNode, Reroute, LayerMask: PersonMaskUltra V2, easy imageRemBg, GetNode, Reroute, SetNode, SetNode, Reroute, LayerMask: MaskGrow, LayerMask: MaskGrow, ImageAndMaskPreview, InvertMask (segment anything), InvertMask (segment anything), LayerMask: PersonMaskUltra V2, BlockifyMask, ImpactConditionalBranch, GetNode, SetNode, SetNode, SetNode, SetNode, SetNode, GetNode, GetNode, GetNode, GetNode, GetNode, InpaintStitchImproved, GetNode, SetNode, SetNode, GetNode, GetNode, GetNode, SetNode, SetNode, GetNode, GetNode, GetNode, GetNode, InpaintCropImproved, KSamplerSelect, GetNode, workflow>mask mover, CLIPTextEncode, FluxGuidance, SetNode, GetNode, GetNode, RepeatLatentBatch, Anything Everywhere, SetNode, Int, Int, GetNode, PreviewImage, RebatchLatents, CFGGuider, VAEEncode, ConditioningZeroOut, ReferenceLatent, VAEEncode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, PreviewImage, RandomNoise, GetNode, VAELoader, ImpactSwitch, CLIPLoader, SamplerCustomAdvanced, GetNode, GetImageSize, EmptyFlux2LatentImage, GetNode, PreviewImage, ReferenceLatent, ImageScale, ReferenceLatent, GetNode, VAEEncode, DWPreprocessor, ImageAndMaskPreview, LayerMask: MaskGrow, SetNode, InpaintCropImproved, GetNode, LayerMask: MaskGrow, GetNode, LayerMask: MaskGrow, SetNode, PreviewImage, ImageCompositeMasked, ImageCompositeMasked, InpaintStitchImproved, MaskToSEGS, Flux2Scheduler, ImpactSwitch, easy boolean, easy seed, SaveImage, PIP_图像联结, PIP_图像联结, DrawMaskOnImage, LoraLoaderModelOnly, LoraLoaderModelOnly, DifferentialDiffusion, Anything Everywhere, GetNode, VAEDecode, InpaintCropImproved, CR Text, GetNode, LoadImage, LoadImage, ImpactSwitch, MaskToSEGS, SetNode, SegsToCombinedMask, LG_Color_Match_V2, SetNode, easy cleanGpuUsed, Image Comparer (rgthree), UNETLoader, PreviewImage, SaveImage, SaveImage, LayerFilter: FilmV2, LayerFilter: FilmV2]
patterns: [image_to_image]
missing: []
parameters: {"cfg": 1.5, "checkpoint": "realvisxlV50_v50Bakedvae.safetensors", "denoise": 0.5000000000000001, "sampler_name": "dpmpp_2m", "scheduler": "karras", "seed": 838243704115371, "steps": 20}
---

# 平台全量/Flux.2 klein 换头_换脸_人脸参考IP-局部重绘-聚焦裁剪「色块填充版」_2013655608490205185.json

> 来源文件 `comfyui_library/workflows/平台全量/Flux.2 klein 换头_换脸_人脸参考IP-局部重绘-聚焦裁剪「色块填充版」_2013655608490205185.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（178 个）：
- `InstantIDFaceAnalysis`
- `ControlNetLoader`
- `SetNode`
- `SetNode`
- `ApplyInstantID`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `GetNode`
- `LayerMask: PersonMaskUltra V2`
- `KSampler` ★核心
- `easy imageRemBg`
- `LayerMask: PersonMaskUltra V2`
- `PreviewImage`
- `SetNode`
- `DifferentialDiffusion`
- `InpaintModelConditioning`
- `CheckpointLoaderSimple` ★核心
- `GetNode`
- `InstantIDModelLoader`
- `SetNode`
- `GetNode`
- `ImageAndMaskPreview`
- `GetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `ImageSmartSharpen+`
- `GetNode`
- `SetNode`
- `VAEDecode` ★核心
- `InpaintStitchImproved`
- `SetNode`
- `SetNode`
- `easy cleanGpuUsed`
- `GetImageSize`
- `SetNode`
- `PreviewImage`
- `GetNode`
- `InpaintCropImproved`
- `LayerMask: PersonMaskUltra V2`
- `SegsToCombinedMask`
- `SetNode`
- `SetNode`
- `Reroute`
- `LayerMask: PersonMaskUltra V2`
- `easy imageRemBg`
- `GetNode`
- `Reroute`
- `SetNode`
- `SetNode`
- `Reroute`
- `LayerMask: MaskGrow`
- `LayerMask: MaskGrow`
- `ImageAndMaskPreview`
- `InvertMask (segment anything)`
- `InvertMask (segment anything)`
- `LayerMask: PersonMaskUltra V2`
- `BlockifyMask`
- `ImpactConditionalBranch`
- `GetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `InpaintStitchImproved`
- `GetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `InpaintCropImproved`
- `KSamplerSelect` ★核心
- `GetNode`
- `workflow>mask mover`
- `CLIPTextEncode` ★核心
- `FluxGuidance`
- `SetNode`
- `GetNode`
- `GetNode`
- `RepeatLatentBatch`
- `Anything Everywhere`
- `SetNode`
- `Int`
- `Int`
- `GetNode`
- `PreviewImage`
- `RebatchLatents`
- `CFGGuider`
- `VAEEncode` ★核心
- `ConditioningZeroOut`
- `ReferenceLatent`
- `VAEEncode` ★核心
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `PreviewImage`
- `RandomNoise`
- `GetNode`
- `VAELoader`
- `ImpactSwitch`
- `CLIPLoader`
- `SamplerCustomAdvanced` ★核心
- `GetNode`
- `GetImageSize`
- `EmptyFlux2LatentImage`
- `GetNode`
- `PreviewImage`
- `ReferenceLatent`
- `ImageScale`
- `ReferenceLatent`
- `GetNode`
- `VAEEncode` ★核心
- `DWPreprocessor`
- `ImageAndMaskPreview`
- `LayerMask: MaskGrow`
- `SetNode`
- `InpaintCropImproved`
- `GetNode`
- `LayerMask: MaskGrow`
- `GetNode`
- `LayerMask: MaskGrow`
- `SetNode`
- `PreviewImage`
- `ImageCompositeMasked`
- `ImageCompositeMasked`
- `InpaintStitchImproved`
- `MaskToSEGS`
- `Flux2Scheduler`
- `ImpactSwitch`
- `easy boolean`
- `easy seed`
- `SaveImage`
- `PIP_图像联结`
- `PIP_图像联结`
- `DrawMaskOnImage`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `DifferentialDiffusion`
- `Anything Everywhere`
- `GetNode`
- `VAEDecode` ★核心
- `InpaintCropImproved`
- `CR Text`
- `GetNode`
- `LoadImage`
- `LoadImage`
- `ImpactSwitch`
- `MaskToSEGS`
- `SetNode`
- `SegsToCombinedMask`
- `LG_Color_Match_V2`
- `SetNode`
- `easy cleanGpuUsed`
- `Image Comparer (rgthree)`
- `UNETLoader` ★核心
- `PreviewImage`
- `SaveImage`
- `SaveImage`
- `LayerFilter: FilmV2`
- `LayerFilter: FilmV2`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `838243704115371`
- `steps` = `20`
- `cfg` = `1.5`
- `sampler_name` = `dpmpp_2m`
- `scheduler` = `karras`
- `denoise` = `0.5000000000000001`
- `checkpoint` = `realvisxlV50_v50Bakedvae.safetensors`

## 知识

覆盖率 **51%**（91/178）

**有卡**：`InstantIDFaceAnalysis`、`ControlNetLoader`、`ApplyInstantID`、`CLIPTextEncode`、`LayerMask: PersonMaskUltra V2`、`KSampler`、`easy imageRemBg`、`DifferentialDiffusion`、`InpaintModelConditioning`、`CheckpointLoaderSimple`、`InstantIDModelLoader`、`ImageAndMaskPreview`、`ImageSmartSharpen+`、`VAEDecode`、`InpaintStitchImproved`、`easy cleanGpuUsed`、`GetImageSize`、`InpaintCropImproved`、`SegsToCombinedMask`、`LayerMask: MaskGrow`、`InvertMask (segment anything)`、`BlockifyMask`、`ImpactConditionalBranch`、`KSamplerSelect`、`workflow>mask mover`、`FluxGuidance`、`RepeatLatentBatch`、`Int`、`RebatchLatents`、`CFGGuider`、`VAEEncode`、`ConditioningZeroOut`、`ReferenceLatent`、`RandomNoise`、`VAELoader`、`CLIPLoader`、`SamplerCustomAdvanced`、`EmptyFlux2LatentImage`、`ImageScale`、`DWPreprocessor`、`ImageCompositeMasked`、`MaskToSEGS`、`Flux2Scheduler`、`easy boolean`、`easy seed`、`SaveImage`、`PIP_图像联结`、`DrawMaskOnImage`、`LoraLoaderModelOnly`、`CR Text`、`LoadImage`、`LG_Color_Match_V2`、`UNETLoader`、`LayerFilter: FilmV2`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CheckpointLoaderSimple、UNETLoader、CLIPLoader、CLIPTextEncode

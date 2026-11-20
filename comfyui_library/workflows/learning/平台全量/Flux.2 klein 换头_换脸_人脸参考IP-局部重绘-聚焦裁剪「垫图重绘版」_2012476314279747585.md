---
key: 平台全量/Flux.2 klein 换头_换脸_人脸参考IP-局部重绘-聚焦裁剪「垫图重绘版」_2012476314279747585.json
name: Flux.2 klein 换头_换脸_人脸参考IP-局部重绘-聚焦裁剪「垫图重绘版」_2012476314279747585
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/平台全量/Flux.2 klein 换头_换脸_人脸参考IP-局部重绘-聚焦裁剪「垫图重绘版」_2012476314279747585.json
hash: 321e5308b7e3ee21
coverage: 0.502762
learned_at: 2026-11-14 00:28:55
nodes: [InstantIDFaceAnalysis, ControlNetLoader, SetNode, SetNode, ApplyInstantID, CLIPTextEncode, CLIPTextEncode, GetNode, LayerMask: PersonMaskUltra V2, KSampler, easy imageRemBg, LayerMask: PersonMaskUltra V2, PreviewImage, SetNode, DifferentialDiffusion, InpaintModelConditioning, CheckpointLoaderSimple, GetNode, InstantIDModelLoader, SetNode, GetNode, ImageAndMaskPreview, GetNode, GetNode, SetNode, SetNode, GetNode, GetNode, ImageSmartSharpen+, GetNode, SetNode, VAEDecode, InpaintStitchImproved, SetNode, SetNode, easy cleanGpuUsed, GetImageSize, SetNode, PreviewImage, GetNode, LayerMask: PersonMaskUltra V2, SegsToCombinedMask, SetNode, SetNode, Reroute, LayerMask: PersonMaskUltra V2, easy imageRemBg, GetNode, Reroute, SetNode, SetNode, Reroute, LayerMask: MaskGrow, LayerMask: MaskGrow, ImpactSwitch, InpaintStitchImproved, ImageAndMaskPreview, InvertMask (segment anything), InvertMask (segment anything), LayerMask: PersonMaskUltra V2, BlockifyMask, ImpactConditionalBranch, easy boolean, ImageCompositeMasked, ImageCompositeMasked, GetNode, LayerMask: MaskGrow, SetNode, SetNode, SetNode, SetNode, SetNode, GetNode, GetNode, GetNode, GetNode, PIP_图像联结, GetNode, InpaintStitchImproved, GetNode, SetNode, SetNode, GetNode, GetNode, LayerMask: MaskGrow, SetNode, GetNode, SetNode, GetNode, SetNode, SetNode, GetNode, GetNode, GetNode, GetNode, GetNode, PIP_图像联结, LayerMask: MaskPreview, KSamplerSelect, GetNode, workflow>mask mover, CLIPTextEncode, FluxGuidance, SetNode, GetNode, GetNode, GetNode, RepeatLatentBatch, PreviewImage, Anything Everywhere, SetNode, Int, Int, GetNode, GetNode, PreviewImage, RebatchLatents, CFGGuider, GetNode, VAEEncode, GetNode, ConditioningZeroOut, ReferenceLatent, ReferenceLatent, VAEEncode, ImageScale, GetNode, PreviewImage, DrawMaskOnImage, ImageCompositeMasked, DWPreprocessor, GetNode, GetNode, GetNode, GetNode, GetNode, PreviewImage, MaskToSEGS, LayerMask: MaskGrow, SamplerCustomAdvanced, RandomNoise, RandomNoise, ImpactSwitch, GetNode, GetImageSize, Flux2Scheduler, GetNode, VAELoader, InpaintModelConditioning, BasicScheduler, BasicScheduler, GetNode, ImageAndMaskPreview, easy seed, ImpactSwitch, CLIPLoader, SaveImage, PreviewImage, SaveImage, VAEDecode, SamplerCustomAdvanced, DifferentialDiffusion, LoraLoaderModelOnly, Anything Everywhere, SetNode, easy cleanGpuUsed, PreviewImage, LoraLoaderModelOnly, CR Text, GetNode, LoadImage, UNETLoader, LoadImage, VAEDecode, PreviewImage, InpaintCropImproved, PreviewImage, InpaintCropImproved, SaveImage, InpaintCropImproved, InpaintCropImproved]
patterns: [image_to_image]
missing: []
parameters: {"cfg": 1.5, "checkpoint": "realvisxlV50_v50Bakedvae.safetensors", "denoise": 0.5000000000000001, "sampler_name": "dpmpp_2m", "scheduler": "karras", "seed": 786470348490692, "steps": 20}
---

# 平台全量/Flux.2 klein 换头_换脸_人脸参考IP-局部重绘-聚焦裁剪「垫图重绘版」_2012476314279747585.json

> 来源文件 `comfyui_library/workflows/平台全量/Flux.2 klein 换头_换脸_人脸参考IP-局部重绘-聚焦裁剪「垫图重绘版」_2012476314279747585.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（181 个）：
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
- `ImpactSwitch`
- `InpaintStitchImproved`
- `ImageAndMaskPreview`
- `InvertMask (segment anything)`
- `InvertMask (segment anything)`
- `LayerMask: PersonMaskUltra V2`
- `BlockifyMask`
- `ImpactConditionalBranch`
- `easy boolean`
- `ImageCompositeMasked`
- `ImageCompositeMasked`
- `GetNode`
- `LayerMask: MaskGrow`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `PIP_图像联结`
- `GetNode`
- `InpaintStitchImproved`
- `GetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `LayerMask: MaskGrow`
- `SetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `PIP_图像联结`
- `LayerMask: MaskPreview`
- `KSamplerSelect` ★核心
- `GetNode`
- `workflow>mask mover`
- `CLIPTextEncode` ★核心
- `FluxGuidance`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `RepeatLatentBatch`
- `PreviewImage`
- `Anything Everywhere`
- `SetNode`
- `Int`
- `Int`
- `GetNode`
- `GetNode`
- `PreviewImage`
- `RebatchLatents`
- `CFGGuider`
- `GetNode`
- `VAEEncode` ★核心
- `GetNode`
- `ConditioningZeroOut`
- `ReferenceLatent`
- `ReferenceLatent`
- `VAEEncode` ★核心
- `ImageScale`
- `GetNode`
- `PreviewImage`
- `DrawMaskOnImage`
- `ImageCompositeMasked`
- `DWPreprocessor`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `PreviewImage`
- `MaskToSEGS`
- `LayerMask: MaskGrow`
- `SamplerCustomAdvanced` ★核心
- `RandomNoise`
- `RandomNoise`
- `ImpactSwitch`
- `GetNode`
- `GetImageSize`
- `Flux2Scheduler`
- `GetNode`
- `VAELoader`
- `InpaintModelConditioning`
- `BasicScheduler`
- `BasicScheduler`
- `GetNode`
- `ImageAndMaskPreview`
- `easy seed`
- `ImpactSwitch`
- `CLIPLoader`
- `SaveImage`
- `PreviewImage`
- `SaveImage`
- `VAEDecode` ★核心
- `SamplerCustomAdvanced` ★核心
- `DifferentialDiffusion`
- `LoraLoaderModelOnly` ★核心
- `Anything Everywhere`
- `SetNode`
- `easy cleanGpuUsed`
- `PreviewImage`
- `LoraLoaderModelOnly` ★核心
- `CR Text`
- `GetNode`
- `LoadImage`
- `UNETLoader` ★核心
- `LoadImage`
- `VAEDecode` ★核心
- `PreviewImage`
- `InpaintCropImproved`
- `PreviewImage`
- `InpaintCropImproved`
- `SaveImage`
- `InpaintCropImproved`
- `InpaintCropImproved`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `786470348490692`
- `steps` = `20`
- `cfg` = `1.5`
- `sampler_name` = `dpmpp_2m`
- `scheduler` = `karras`
- `denoise` = `0.5000000000000001`
- `checkpoint` = `realvisxlV50_v50Bakedvae.safetensors`

## 知识

覆盖率 **50%**（91/181）

**有卡**：`InstantIDFaceAnalysis`、`ControlNetLoader`、`ApplyInstantID`、`CLIPTextEncode`、`LayerMask: PersonMaskUltra V2`、`KSampler`、`easy imageRemBg`、`DifferentialDiffusion`、`InpaintModelConditioning`、`CheckpointLoaderSimple`、`InstantIDModelLoader`、`ImageAndMaskPreview`、`ImageSmartSharpen+`、`VAEDecode`、`InpaintStitchImproved`、`easy cleanGpuUsed`、`GetImageSize`、`SegsToCombinedMask`、`LayerMask: MaskGrow`、`InvertMask (segment anything)`、`BlockifyMask`、`ImpactConditionalBranch`、`easy boolean`、`ImageCompositeMasked`、`PIP_图像联结`、`LayerMask: MaskPreview`、`KSamplerSelect`、`workflow>mask mover`、`FluxGuidance`、`RepeatLatentBatch`、`Int`、`RebatchLatents`、`CFGGuider`、`VAEEncode`、`ConditioningZeroOut`、`ReferenceLatent`、`ImageScale`、`DrawMaskOnImage`、`DWPreprocessor`、`MaskToSEGS`、`SamplerCustomAdvanced`、`RandomNoise`、`Flux2Scheduler`、`VAELoader`、`BasicScheduler`、`easy seed`、`CLIPLoader`、`SaveImage`、`LoraLoaderModelOnly`、`CR Text`、`LoadImage`、`UNETLoader`、`InpaintCropImproved`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CheckpointLoaderSimple、UNETLoader、CLIPLoader、CLIPTextEncode

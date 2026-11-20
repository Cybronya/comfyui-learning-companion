---
key: 平台全量/🈚️flux.1 kontext dev-局部重绘-换头_换脸_1955488211936186370.json
name: 🈚️flux.1 kontext dev-局部重绘-换头_换脸_1955488211936186370
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/平台全量/🈚️flux.1 kontext dev-局部重绘-换头_换脸_1955488211936186370.json
hash: 4a66d6e705b5235c
coverage: 0.512821
learned_at: 2026-11-14 02:54:27
nodes: [InstantIDFaceAnalysis, ControlNetLoader, SetNode, SetNode, ApplyInstantID, CLIPTextEncode, CLIPTextEncode, GetNode, LayerMask: PersonMaskUltra V2, KSampler, easy imageRemBg, LayerMask: PersonMaskUltra V2, PreviewImage, SetNode, DifferentialDiffusion, InpaintModelConditioning, CheckpointLoaderSimple, GetNode, InstantIDModelLoader, SetNode, GetNode, ImageAndMaskPreview, GetNode, GetNode, SetNode, SetNode, GetNode, GetNode, ImageSmartSharpen+, PreviewImage, GetNode, SetNode, VAEDecode, InpaintStitchImproved, SetNode, SetNode, easy cleanGpuUsed, SetNode, CLIPTextEncode, VAEEncode, GetImageSize, SetNode, PreviewImage, GetNode, InpaintCropImproved, LayerMask: PersonMaskUltra V2, SegsToCombinedMask, SetNode, SetNode, Reroute, LayerMask: PersonMaskUltra V2, easy imageRemBg, GetNode, Reroute, SetNode, SetNode, ImpactSwitch, Reroute, LayerMask: MaskGrow, LayerMask: MaskGrow, ImpactSwitch, InpaintStitchImproved, ImageAndMaskPreview, ImageAndMaskPreview, InvertMask (segment anything), InvertMask (segment anything), MaskToSEGS, LayerMask: PersonMaskUltra V2, BlockifyMask, ImpactConditionalBranch, easy boolean, ImageCompositeMasked, ImageCompositeMasked, GetNode, LayerMask: MaskGrow, LayerMask: MaskGrow, SetNode, SetNode, SetNode, Int, SetNode, SetNode, easy seed, Int, LoadImage, LoadImage, GetNode, GetNode, GetNode, GetNode, GetNode, PIP_图像联结, GetNode, GetNode, workflow>mask mover, InpaintStitchImproved, GetNode, SetNode, SetNode, GetNode, GetNode, LayerMask: MaskGrow, SetNode, GetNode, SetNode, GetNode, SetNode, SetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, DualCLIPLoader, Anything Everywhere, VAELoader, Anything Everywhere, DifferentialDiffusion, SetNode, InpaintCropImproved, InpaintCropImproved, PIP_图像联结, GetNode, VAEDecode, SaveImage, GetNode, PreviewImage, LayerMask: MaskPreview, FluxGuidance, GetNode, ReferenceLatent, ConditioningZeroOut, InpaintCropImproved, RepeatLatentBatch, RebatchLatents, ControlNetLoader, GetNode, GetNode, CR Text, DWPreprocessor, PreviewImage, KSampler, UNETLoader, TeaCache, LoraLoaderModelOnly, LoraLoaderModelOnly, ImpactSwitch, SetUnionControlNetType, ControlNetApplySD3, InpaintModelConditioning, LoraLoaderModelOnly, PreviewImage, SaveImage, SaveImage]
patterns: [image_to_image]
missing: []
parameters: {"cfg": 1, "checkpoint": "realvisxlV50_v50Bakedvae.safetensors", "controlnet_strength": 1, "denoise": 0.8000000000000002, "sampler_name": "euler", "scheduler": "simple", "seed": 865924003419982, "steps": 10}
---

# 平台全量/🈚️flux.1 kontext dev-局部重绘-换头_换脸_1955488211936186370.json

> 来源文件 `comfyui_library/workflows/平台全量/🈚️flux.1 kontext dev-局部重绘-换头_换脸_1955488211936186370.json`

## 结构

**生成流程**：Model → Encode → Condition → Control → Sampling → Decode → Process → Output → Other

**节点**（156 个）：
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
- `PreviewImage`
- `GetNode`
- `SetNode`
- `VAEDecode` ★核心
- `InpaintStitchImproved`
- `SetNode`
- `SetNode`
- `easy cleanGpuUsed`
- `SetNode`
- `CLIPTextEncode` ★核心
- `VAEEncode` ★核心
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
- `ImpactSwitch`
- `Reroute`
- `LayerMask: MaskGrow`
- `LayerMask: MaskGrow`
- `ImpactSwitch`
- `InpaintStitchImproved`
- `ImageAndMaskPreview`
- `ImageAndMaskPreview`
- `InvertMask (segment anything)`
- `InvertMask (segment anything)`
- `MaskToSEGS`
- `LayerMask: PersonMaskUltra V2`
- `BlockifyMask`
- `ImpactConditionalBranch`
- `easy boolean`
- `ImageCompositeMasked`
- `ImageCompositeMasked`
- `GetNode`
- `LayerMask: MaskGrow`
- `LayerMask: MaskGrow`
- `SetNode`
- `SetNode`
- `SetNode`
- `Int`
- `SetNode`
- `SetNode`
- `easy seed`
- `Int`
- `LoadImage`
- `LoadImage`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `PIP_图像联结`
- `GetNode`
- `GetNode`
- `workflow>mask mover`
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
- `GetNode`
- `GetNode`
- `DualCLIPLoader`
- `Anything Everywhere`
- `VAELoader`
- `Anything Everywhere`
- `DifferentialDiffusion`
- `SetNode`
- `InpaintCropImproved`
- `InpaintCropImproved`
- `PIP_图像联结`
- `GetNode`
- `VAEDecode` ★核心
- `SaveImage`
- `GetNode`
- `PreviewImage`
- `LayerMask: MaskPreview`
- `FluxGuidance`
- `GetNode`
- `ReferenceLatent`
- `ConditioningZeroOut`
- `InpaintCropImproved`
- `RepeatLatentBatch`
- `RebatchLatents`
- `ControlNetLoader`
- `GetNode`
- `GetNode`
- `CR Text`
- `DWPreprocessor`
- `PreviewImage`
- `KSampler` ★核心
- `UNETLoader` ★核心
- `TeaCache`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `ImpactSwitch`
- `SetUnionControlNetType`
- `ControlNetApplySD3` ★核心
- `InpaintModelConditioning`
- `LoraLoaderModelOnly` ★核心
- `PreviewImage`
- `SaveImage`
- `SaveImage`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `865924003419982`
- `steps` = `10`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `0.8000000000000002`
- `checkpoint` = `realvisxlV50_v50Bakedvae.safetensors`
- `controlnet_strength` = `1`

## 知识

覆盖率 **51%**（80/156）

**有卡**：`InstantIDFaceAnalysis`、`ControlNetLoader`、`ApplyInstantID`、`CLIPTextEncode`、`LayerMask: PersonMaskUltra V2`、`KSampler`、`easy imageRemBg`、`DifferentialDiffusion`、`InpaintModelConditioning`、`CheckpointLoaderSimple`、`InstantIDModelLoader`、`ImageAndMaskPreview`、`ImageSmartSharpen+`、`VAEDecode`、`InpaintStitchImproved`、`easy cleanGpuUsed`、`VAEEncode`、`GetImageSize`、`InpaintCropImproved`、`SegsToCombinedMask`、`LayerMask: MaskGrow`、`InvertMask (segment anything)`、`MaskToSEGS`、`BlockifyMask`、`ImpactConditionalBranch`、`easy boolean`、`ImageCompositeMasked`、`Int`、`easy seed`、`LoadImage`、`PIP_图像联结`、`workflow>mask mover`、`DualCLIPLoader`、`VAELoader`、`SaveImage`、`LayerMask: MaskPreview`、`FluxGuidance`、`ReferenceLatent`、`ConditioningZeroOut`、`RepeatLatentBatch`、`RebatchLatents`、`CR Text`、`DWPreprocessor`、`UNETLoader`、`TeaCache`、`LoraLoaderModelOnly`、`SetUnionControlNetType`、`ControlNetApplySD3`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CheckpointLoaderSimple、UNETLoader、CLIPTextEncode、ConditioningZeroOut

---
key: 平台全量/🈚️Flux.1 fill+Redux+Ace+instant ID 单图参考随机姿势_1955915022851604482.json
name: 🈚️Flux.1 fill+Redux+Ace+instant ID 单图参考随机姿势_1955915022851604482
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/🈚️Flux.1 fill+Redux+Ace+instant ID 单图参考随机姿势_1955915022851604482.json
hash: 9834bece7106f66e
coverage: 0.576577
learned_at: 2026-11-14 02:54:24
nodes: [SetNode, CLIPTextEncode, DualCLIPLoader, CLIPTextEncode, Florence2Run, GetNode, LayerUtility: TextJoin, SetNode, Florence2ModelLoader, GetNode, LayerUtility: CropByMask V2, LayerMask: PersonMaskUltra V2, InstantIDFaceAnalysis, ControlNetLoader, SetNode, SetNode, SetNode, CheckpointLoaderSimple, InstantIDModelLoader, DifferentialDiffusion, ApplyInstantID, GetNode, CLIPTextEncode, easy cleanGpuUsed, SetNode, SetNode, LayerMask: MaskPreview, CLIPTextEncode, GetNode, VAEDecode, GetNode, InpaintModelConditioning, SetNode, GetNode, GetNode, ImageSmartSharpen+, GetNode, LayerMask: PersonMaskUltra V2, GetNode, SetNode, SetNode, PreviewImage, easy cleanGpuUsed, GetNode, GetNode, SetNode, SetNode, SetNode, PreviewImage, GetNode, SolidMask, SetNode, SetNode, SolidMask, GetNode, KSampler, LayerUtility: ImageScaleByAspectRatio V2, ShowText|pysssss, UNETLoader, GetNode, LayerMask: MaskPreview, LayerMask: MaskPreview, ImageAndMaskPreview, RebatchLatents, SetNode, GetNode, ConditioningZeroOut, SetNode, FluxGuidance, SetNode, GetNode, LoraLoaderModelOnly, SetNode, easy imageRemBg, LayerMask: MaskGrow, ReduxAdvanced, ReduxAdvanced, GetNode, GetNode, VAEDecode, GetNode, Crop (mtb), SetNode, PreviewImage, InpaintModelConditioning, LayerColor: ColorAdapter, RepeatLatentBatch, GetNode, GetNode, KSampler, easy makeImageForICLora, PreviewImage, InpaintStitchImproved, easy imageRemBg, LayerMask: PersonMaskUltra V2, SetNode, InpaintCropImproved, InpaintCropImproved, Int, RH_Translator, LoadImage, StyleModelLoader, CLIPVisionLoader, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, VAELoader, LayerColor: ColorAdapter, SaveImage, SaveImage]
patterns: []
missing: []
parameters: {"cfg": 1, "checkpoint": "realvisxlV50_v50Bakedvae.safetensors", "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 779610258658915, "steps": 20}
---

# 平台全量/🈚️Flux.1 fill+Redux+Ace+instant ID 单图参考随机姿势_1955915022851604482.json

> 来源文件 `comfyui_library/workflows/平台全量/🈚️Flux.1 fill+Redux+Ace+instant ID 单图参考随机姿势_1955915022851604482.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（111 个）：
- `SetNode`
- `CLIPTextEncode` ★核心
- `DualCLIPLoader`
- `CLIPTextEncode` ★核心
- `Florence2Run`
- `GetNode`
- `LayerUtility: TextJoin`
- `SetNode`
- `Florence2ModelLoader`
- `GetNode`
- `LayerUtility: CropByMask V2`
- `LayerMask: PersonMaskUltra V2`
- `InstantIDFaceAnalysis`
- `ControlNetLoader`
- `SetNode`
- `SetNode`
- `SetNode`
- `CheckpointLoaderSimple` ★核心
- `InstantIDModelLoader`
- `DifferentialDiffusion`
- `ApplyInstantID`
- `GetNode`
- `CLIPTextEncode` ★核心
- `easy cleanGpuUsed`
- `SetNode`
- `SetNode`
- `LayerMask: MaskPreview`
- `CLIPTextEncode` ★核心
- `GetNode`
- `VAEDecode` ★核心
- `GetNode`
- `InpaintModelConditioning`
- `SetNode`
- `GetNode`
- `GetNode`
- `ImageSmartSharpen+`
- `GetNode`
- `LayerMask: PersonMaskUltra V2`
- `GetNode`
- `SetNode`
- `SetNode`
- `PreviewImage`
- `easy cleanGpuUsed`
- `GetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `PreviewImage`
- `GetNode`
- `SolidMask`
- `SetNode`
- `SetNode`
- `SolidMask`
- `GetNode`
- `KSampler` ★核心
- `LayerUtility: ImageScaleByAspectRatio V2`
- `ShowText|pysssss`
- `UNETLoader` ★核心
- `GetNode`
- `LayerMask: MaskPreview`
- `LayerMask: MaskPreview`
- `ImageAndMaskPreview`
- `RebatchLatents`
- `SetNode`
- `GetNode`
- `ConditioningZeroOut`
- `SetNode`
- `FluxGuidance`
- `SetNode`
- `GetNode`
- `LoraLoaderModelOnly` ★核心
- `SetNode`
- `easy imageRemBg`
- `LayerMask: MaskGrow`
- `ReduxAdvanced`
- `ReduxAdvanced`
- `GetNode`
- `GetNode`
- `VAEDecode` ★核心
- `GetNode`
- `Crop (mtb)`
- `SetNode`
- `PreviewImage`
- `InpaintModelConditioning`
- `LayerColor: ColorAdapter`
- `RepeatLatentBatch`
- `GetNode`
- `GetNode`
- `KSampler` ★核心
- `easy makeImageForICLora`
- `PreviewImage`
- `InpaintStitchImproved`
- `easy imageRemBg`
- `LayerMask: PersonMaskUltra V2`
- `SetNode`
- `InpaintCropImproved`
- `InpaintCropImproved`
- `Int`
- `RH_Translator`
- `LoadImage`
- `StyleModelLoader`
- `CLIPVisionLoader`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `VAELoader`
- `LayerColor: ColorAdapter`
- `SaveImage`
- `SaveImage`

## 关键参数

- `checkpoint` = `realvisxlV50_v50Bakedvae.safetensors`
- `seed` = `779610258658915`
- `steps` = `20`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **58%**（64/111）

**有卡**：`CLIPTextEncode`、`DualCLIPLoader`、`Florence2Run`、`LayerUtility: TextJoin`、`Florence2ModelLoader`、`LayerUtility: CropByMask V2`、`LayerMask: PersonMaskUltra V2`、`InstantIDFaceAnalysis`、`ControlNetLoader`、`CheckpointLoaderSimple`、`InstantIDModelLoader`、`DifferentialDiffusion`、`ApplyInstantID`、`easy cleanGpuUsed`、`LayerMask: MaskPreview`、`VAEDecode`、`InpaintModelConditioning`、`ImageSmartSharpen+`、`SolidMask`、`KSampler`、`LayerUtility: ImageScaleByAspectRatio V2`、`UNETLoader`、`ImageAndMaskPreview`、`RebatchLatents`、`ConditioningZeroOut`、`FluxGuidance`、`LoraLoaderModelOnly`、`easy imageRemBg`、`LayerMask: MaskGrow`、`ReduxAdvanced`、`Crop (mtb)`、`LayerColor: ColorAdapter`、`RepeatLatentBatch`、`easy makeImageForICLora`、`InpaintStitchImproved`、`InpaintCropImproved`、`Int`、`RH_Translator`、`LoadImage`、`StyleModelLoader`、`CLIPVisionLoader`、`VAELoader`、`SaveImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CheckpointLoaderSimple、UNETLoader、CLIPTextEncode、ConditioningZeroOut

---
key: 图片生成/图生图/分镜角色一致性迁移替换Flux Fill+Redux+ACE+Pulid+CN+SeedVR2超分_1938942475358949377.json
name: 分镜角色一致性迁移替换Flux Fill+Redux+ACE+Pulid+CN+SeedVR2超分_1938942475358949377
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/分镜角色一致性迁移替换Flux Fill+Redux+ACE+Pulid+CN+SeedVR2超分_1938942475358949377.json
hash: 3d745667648bfa4c
coverage: 0.590909
learned_at: 2026-10-23 12:24:31
nodes: [SetNode, MaskToImage, PreviewImage, PreviewImage, InpaintResize, SetNode, LayerMask: LoadBiRefNetModelV2, SetNode, SetNode, LayerUtility: Florence2Image2Prompt, SetNode, LayerMask: BiRefNetUltraV2, LayerUtility: ImageRemoveAlpha, PreviewImage, SetNode, GetNode, GetNode, ConditioningZeroOut, CLIPTextEncodeFlux, GetNode, GetNode, VAEDecode, LayerUtility: PurgeVRAM, ImpactImageBatchToImageList, GetNode, PreviewImage, SetNode, SetNode, easy imageSize, GetNode, GetNode, GetNode, SetNode, GetNode, SetNode, GetNode, SetNode, LayerUtility: CropByMask V2, SetNode, LayerMask: MaskPreview, GetNode, GetNode, easy makeImageForICLora, InpaintCrop, String Literal, DeepTranslatorTextNode, SetNode, GetNode, GetNode, ImageCrop+, GetNode, PreviewImage, CropFace, PulidFluxEvaClipLoader, DifferentialDiffusion, Anything Everywhere3, ApplyPulidFlux, PulidFluxInsightFaceLoader, InpaintStitch, LayerMask: LoadFlorence2Model, AIO_Preprocessor, Replace Text _O, DualCLIPLoader, PulidFluxModelLoader, LayerUtility: PurgeVRAM V2, LayerUtility: TextJoin, KSampler, ColorMatch, SeedVR2, JWInteger, UNETLoader, VAELoader, LoraLoaderModelOnly, ApplyTeaCacheAndSkipBlocks, LoraLoaderModelOnly, ReduxAdvanced, InpaintModelConditioning, CR Latent Batch Size, ControlNetApplySD3, SetUnionControlNetType, ControlNetLoader, SaveImage, PreviewImage, StyleModelLoader, CLIPVisionLoader, LoadImage, LoadImage, SetNode]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "controlnet_strength": 0.9, "denoise": 1, "sampler_name": "euler", "scheduler": "normal", "seed": 64767149448769, "steps": 8}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/分镜角色一致性迁移替换Flux Fill+Redux+ACE+Pulid+CN+SeedVR2超分_1938942475358949377.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/分镜角色一致性迁移替换Flux Fill+Redux+ACE+Pulid+CN+SeedVR2超分_1938942475358949377.json`

## 结构

**生成流程**：Model → Condition → Control → Sampling → Decode → Process → Output → Other

**节点**（88 个）：
- `SetNode`
- `MaskToImage`
- `PreviewImage`
- `PreviewImage`
- `InpaintResize`
- `SetNode`
- `LayerMask: LoadBiRefNetModelV2`
- `SetNode`
- `SetNode`
- `LayerUtility: Florence2Image2Prompt`
- `SetNode`
- `LayerMask: BiRefNetUltraV2`
- `LayerUtility: ImageRemoveAlpha`
- `PreviewImage`
- `SetNode`
- `GetNode`
- `GetNode`
- `ConditioningZeroOut`
- `CLIPTextEncodeFlux` ★核心
- `GetNode`
- `GetNode`
- `VAEDecode` ★核心
- `LayerUtility: PurgeVRAM`
- `ImpactImageBatchToImageList`
- `GetNode`
- `PreviewImage`
- `SetNode`
- `SetNode`
- `easy imageSize`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `SetNode`
- `LayerUtility: CropByMask V2`
- `SetNode`
- `LayerMask: MaskPreview`
- `GetNode`
- `GetNode`
- `easy makeImageForICLora`
- `InpaintCrop`
- `String Literal`
- `DeepTranslatorTextNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `ImageCrop+`
- `GetNode`
- `PreviewImage`
- `CropFace`
- `PulidFluxEvaClipLoader`
- `DifferentialDiffusion`
- `Anything Everywhere3`
- `ApplyPulidFlux`
- `PulidFluxInsightFaceLoader`
- `InpaintStitch`
- `LayerMask: LoadFlorence2Model`
- `AIO_Preprocessor`
- `Replace Text _O`
- `DualCLIPLoader`
- `PulidFluxModelLoader`
- `LayerUtility: PurgeVRAM V2`
- `LayerUtility: TextJoin`
- `KSampler` ★核心
- `ColorMatch`
- `SeedVR2`
- `JWInteger`
- `UNETLoader` ★核心
- `VAELoader`
- `LoraLoaderModelOnly` ★核心
- `ApplyTeaCacheAndSkipBlocks`
- `LoraLoaderModelOnly` ★核心
- `ReduxAdvanced`
- `InpaintModelConditioning`
- `CR Latent Batch Size`
- `ControlNetApplySD3` ★核心
- `SetUnionControlNetType`
- `ControlNetLoader`
- `SaveImage`
- `PreviewImage`
- `StyleModelLoader`
- `CLIPVisionLoader`
- `LoadImage`
- `LoadImage`
- `SetNode`

## 关键参数

- `seed` = `64767149448769`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `normal`
- `denoise` = `1`
- `controlnet_strength` = `0.9`

## 知识

覆盖率 **59%**（52/88）

**有卡**：`MaskToImage`、`InpaintResize`、`LayerMask: LoadBiRefNetModelV2`、`LayerUtility: Florence2Image2Prompt`、`LayerMask: BiRefNetUltraV2`、`LayerUtility: ImageRemoveAlpha`、`ConditioningZeroOut`、`CLIPTextEncodeFlux`、`VAEDecode`、`LayerUtility: PurgeVRAM`、`ImpactImageBatchToImageList`、`easy imageSize`、`LayerUtility: CropByMask V2`、`LayerMask: MaskPreview`、`easy makeImageForICLora`、`InpaintCrop`、`String Literal`、`DeepTranslatorTextNode`、`ImageCrop+`、`CropFace`、`PulidFluxEvaClipLoader`、`DifferentialDiffusion`、`ApplyPulidFlux`、`PulidFluxInsightFaceLoader`、`InpaintStitch`、`LayerMask: LoadFlorence2Model`、`AIO_Preprocessor`、`Replace Text _O`、`DualCLIPLoader`、`PulidFluxModelLoader`、`LayerUtility: PurgeVRAM V2`、`LayerUtility: TextJoin`、`KSampler`、`ColorMatch`、`SeedVR2`、`JWInteger`、`UNETLoader`、`VAELoader`、`LoraLoaderModelOnly`、`ApplyTeaCacheAndSkipBlocks`、`ReduxAdvanced`、`InpaintModelConditioning`、`CR Latent Batch Size`、`ControlNetApplySD3`、`SetUnionControlNetType`、`ControlNetLoader`、`SaveImage`、`StyleModelLoader`、`CLIPVisionLoader`、`LoadImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、ConditioningZeroOut、LoadImage、ControlNetLoader

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

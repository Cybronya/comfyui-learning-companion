---
key: 换脸集合[sd1.5,  sdxl, flux]_1912066179786076162.json
name: 换脸集合[sd1.5,  sdxl, flux]_1912066179786076162
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/换脸集合[sd1.5,  sdxl, flux]_1912066179786076162.json
hash: f7c825a5695f9d8d
coverage: 0.900763
learned_at: 2026-10-10 20:59:45
nodes: [InstantIDFaceAnalysis, InstantIDModelLoader, ControlNetLoader, ApplyInstantID, CheckpointLoaderSimple, LoadImage, KSampler, SaveImage, SaveImage, VAEDecode, CheckpointLoaderSimple, CLIPTextEncode, CLIPTextEncode, ControlNetLoader, InstantIDModelLoader, InstantIDFaceAnalysis, ApplyInstantID, InpaintModelConditioning, KSampler, DifferentialDiffusion, VAEDecode, CLIPTextEncode, CheckpointLoaderSimple, LoadImage, ApplyPulid, PulidEvaClipLoader, PulidInsightFaceLoader, PulidModelLoader, CLIPTextEncode, EmptyLatentImage, KSampler, VAEDecode, SaveImage, LoadImage, ApplyPulid, PulidEvaClipLoader, PulidInsightFaceLoader, PulidModelLoader, CLIPTextEncode, CLIPTextEncode, KSampler, VAEDecode, SaveImage, ControlNetApplyAdvanced, CheckpointLoaderSimple, LoadImage, ControlNetLoader, LayerUtility: CropByMask, LoadImage, VAEDecode, LayerUtility: ImageScaleRestore V2, SaveImage, LayerUtility: RestoreCropBox, KSampler, CheckpointLoaderSimple, ApplyZenID, DifferentialDiffusion, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, MaskBlur+, CLIPTextEncode, SaveImage, DWPreprocessor, VAEDecode, LoadImage, CLIPTextEncode, EmptyLatentImage, ControlNetLoader, ControlNetApplyAdvanced, ControlNetLoader, ZenIDCombineFace, LoadImage, LoadImage, PreviewImage, CheckpointLoaderSimple, KSampler, InstantIDModelLoader, EcomIDEvaClipLoader, EcomIDFaceAnalysis, ControlNetLoader, VAEDecode, KSampler, CLIPTextEncode, ApplyEcomID, GetImageSize+, EmptyLatentImage, CLIPTextEncode, CLIPTextEncode, GetImageSize+, EmptyLatentImage, SaveImage, PreviewImage, LayerUtility: ImageBlendAdvance V3, LoadImage, CheckpointLoaderSimple, LoadImage, EmptyImage, Note, ApplyEcomIDAdvanced, Note, Note, VAEDecode, EmptyLatentImage, CLIPTextEncode, LoadImage, CLIPTextEncode, ApplyPulidFlux, PulidFluxEvaClipLoader, PulidFluxModelLoader, UNETLoader, DualCLIPLoader, KSampler, SaveImage, VAELoader, PulidFluxInsightFaceLoader, PulidFluxEvaClipLoader, PulidFluxModelLoader, PulidFluxInsightFaceLoader, LayerUtility: ImageBlendAdvance V3, OpenposePreprocessor, LoadImage, GetImageSize+, EmptyLatentImage, ControlNetLoader, PreviewImage, ApplyPulidFlux, ControlNetLoader, VAELoader, KSampler, VAEDecode, SaveImage, UNETLoader, DualCLIPLoader, CLIPTextEncode, CLIPTextEncode, ControlNetApplyAdvanced, LoadImage, GetImageSize+, EmptyLatentImage, PreviewImage, UNETLoader, DualCLIPLoader, KSampler, VAEDecode, ControlNetLoader, InfiniteYouApply, VAELoader, LoadImage, EmptyLatentImage, CLIPTextEncode, CLIPTextEncode, SaveImage, ControlNetLoader, DualCLIPLoader, CLIPTextEncode, EmptyLatentImage, LoadImage, LoadImage, VAEDecode, KSampler, FaceCombine, CLIPTextEncode, SaveImage, VAELoader, UNETLoader, CheckpointLoaderSimple, CLIPTextEncode, CLIPTextEncode, CLIPTextEncode, EmptyLatentImage, LoadImage, IPAdapterUnifiedLoaderFaceID, CLIPVisionLoader, IPAdapterInsightFaceLoader, IPAdapterFaceID, VAEDecode, SaveImage, KSampler, CLIPTextEncode, EmptyLatentImage, LoadImage, CLIPVisionLoader, IPAdapterInsightFaceLoader, IPAdapterFaceID, VAEDecode, SaveImage, KSampler, CheckpointLoaderSimple, CLIPTextEncode, IPAdapterUnifiedLoaderFaceID, CLIPTextEncode, EmptyLatentImage, LoadImage, CLIPVisionLoader, CLIPTextEncode, CheckpointLoaderSimple, IPAdapterUnifiedLoader, IPAdapterAdvanced, KSampler, VAEDecode, SaveImage, PulidModelLoader, CLIPTextEncode, EmptyLatentImage, LoadImage, CLIPTextEncode, IPAdapterAdvanced, KSampler, VAEDecode, SaveImage, CheckpointLoaderSimple, CLIPVisionLoader, IPAdapterUnifiedLoader, LoadImage, OpenposePreprocessor, ReActorFaceSwap, ReActorFaceBoost, LoadImage, LoadImage, SaveImage, DualCLIPLoader, CLIPTextEncode, VAEDecode, CLIPVisionLoader, VAELoader, LoraLoaderModelOnly, InpaintModelConditioning, CLIPVisionEncode, CLIPTextEncode, FluxGuidance, ImageIC, StyleModelApply, StyleModelLoader, UNETLoader, PreviewImage, MaskPreview+, KSampler, EmptyImage, LayerUtility: CropByMask V2, LayerUtility: ImageScaleByAspectRatio V2, Mask Gaussian Region, ImageSharpen, LayerUtility: ImageScaleRestore V2, LayerUtility: RestoreCropBox, LoadImage, SaveImage, DualCLIPLoader, LoadImage, LoadImage, LayerUtility: CropByMask, SaveImage, UNETLoader, ControlNetLoader, KSampler, DifferentialDiffusion, VAELoader, VAEDecode, LoadImage, LoadImage, SaveImage, ImpactGaussianBlurMask, FaceSwap_InfiniteYou]
patterns: [text_to_image]
missing: [LayerUtility: CropByMask, LayerUtility: CropByMask, LayerUtility: CropByMask V2, LayerUtility: ImageBlendAdvance V3, LayerUtility: ImageBlendAdvance V3, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: ImageScaleRestore V2, LayerUtility: ImageScaleRestore V2, LayerUtility: RestoreCropBox, LayerUtility: RestoreCropBox, Mask Gaussian Region, MaskBlur+, GetImageSize+, GetImageSize+, GetImageSize+, GetImageSize+, MaskPreview+]
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 1, "checkpoint": "LEOSAM HelloWorld 新世界 - V7.safetensors", "controlnet_strength": 0.8000000000000002, "denoise": 0.5500000000000002, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 474562052770258, "steps": 10, "width": 1024}
discoveries: [次要节点 `LayerUtility: CropByMask` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: CropByMask` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: CropByMask V2` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: ImageBlendAdvance V3` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: ImageBlendAdvance V3` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: ImageScaleRestore V2` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: ImageScaleRestore V2` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: RestoreCropBox` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: RestoreCropBox` 知识库中没有该节点类型的任何知识, 次要节点 `Mask Gaussian Region` 知识库中没有该节点类型的任何知识, 次要节点 `MaskBlur+` 知识库中没有该节点类型的任何知识, 次要节点 `GetImageSize+` 仅有 Resolution 的通用知识，没有该节点自己的说明, 次要节点 `GetImageSize+` 仅有 Resolution 的通用知识，没有该节点自己的说明, 次要节点 `GetImageSize+` 仅有 Resolution 的通用知识，没有该节点自己的说明, 次要节点 `GetImageSize+` 仅有 Resolution 的通用知识，没有该节点自己的说明, 次要节点 `MaskPreview+` 仅有 SaveImage 的通用知识，没有该节点自己的说明, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 换脸集合[sd1.5,  sdxl, flux]_1912066179786076162.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/换脸集合[sd1.5,  sdxl, flux]_1912066179786076162.json`

## 结构

**生成流程**：Model → Condition → Latent → Control → Sampling → Decode → Process → Output → Other

**节点**（262 个）：
- `InstantIDFaceAnalysis`
- `InstantIDModelLoader`
- `ControlNetLoader`
- `ApplyInstantID`
- `CheckpointLoaderSimple` ★核心
- `LoadImage`
- `KSampler` ★核心
- `SaveImage`
- `SaveImage`
- `VAEDecode` ★核心
- `CheckpointLoaderSimple` ★核心
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `ControlNetLoader`
- `InstantIDModelLoader`
- `InstantIDFaceAnalysis`
- `ApplyInstantID`
- `InpaintModelConditioning`
- `KSampler` ★核心
- `DifferentialDiffusion`
- `VAEDecode` ★核心
- `CLIPTextEncode` ★核心
- `CheckpointLoaderSimple` ★核心
- `LoadImage`
- `ApplyPulid`
- `PulidEvaClipLoader`
- `PulidInsightFaceLoader`
- `PulidModelLoader`
- `CLIPTextEncode` ★核心
- `EmptyLatentImage` ★核心
- `KSampler` ★核心
- `VAEDecode` ★核心
- `SaveImage`
- `LoadImage`
- `ApplyPulid`
- `PulidEvaClipLoader`
- `PulidInsightFaceLoader`
- `PulidModelLoader`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `KSampler` ★核心
- `VAEDecode` ★核心
- `SaveImage`
- `ControlNetApplyAdvanced` ★核心
- `CheckpointLoaderSimple` ★核心
- `LoadImage`
- `ControlNetLoader`
- `LayerUtility: CropByMask`
- `LoadImage`
- `VAEDecode` ★核心
- `LayerUtility: ImageScaleRestore V2`
- `SaveImage`
- `LayerUtility: RestoreCropBox`
- `KSampler` ★核心
- `CheckpointLoaderSimple` ★核心
- `ApplyZenID`
- `DifferentialDiffusion`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `MaskBlur+`
- `CLIPTextEncode` ★核心
- `SaveImage`
- `DWPreprocessor`
- `VAEDecode` ★核心
- `LoadImage`
- `CLIPTextEncode` ★核心
- `EmptyLatentImage` ★核心
- `ControlNetLoader`
- `ControlNetApplyAdvanced` ★核心
- `ControlNetLoader`
- `ZenIDCombineFace`
- `LoadImage`
- `LoadImage`
- `PreviewImage`
- `CheckpointLoaderSimple` ★核心
- `KSampler` ★核心
- `InstantIDModelLoader`
- `EcomIDEvaClipLoader`
- `EcomIDFaceAnalysis`
- `ControlNetLoader`
- `VAEDecode` ★核心
- `KSampler` ★核心
- `CLIPTextEncode` ★核心
- `ApplyEcomID`
- `GetImageSize+`
- `EmptyLatentImage` ★核心
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `GetImageSize+`
- `EmptyLatentImage` ★核心
- `SaveImage`
- `PreviewImage`
- `LayerUtility: ImageBlendAdvance V3`
- `LoadImage`
- `CheckpointLoaderSimple` ★核心
- `LoadImage`
- `EmptyImage`
- `Note`
- `ApplyEcomIDAdvanced`
- `Note`
- `Note`
- `VAEDecode` ★核心
- `EmptyLatentImage` ★核心
- `CLIPTextEncode` ★核心
- `LoadImage`
- `CLIPTextEncode` ★核心
- `ApplyPulidFlux`
- `PulidFluxEvaClipLoader`
- `PulidFluxModelLoader`
- `UNETLoader` ★核心
- `DualCLIPLoader`
- `KSampler` ★核心
- `SaveImage`
- `VAELoader`
- `PulidFluxInsightFaceLoader`
- `PulidFluxEvaClipLoader`
- `PulidFluxModelLoader`
- `PulidFluxInsightFaceLoader`
- `LayerUtility: ImageBlendAdvance V3`
- `OpenposePreprocessor`
- `LoadImage`
- `GetImageSize+`
- `EmptyLatentImage` ★核心
- `ControlNetLoader`
- `PreviewImage`
- `ApplyPulidFlux`
- `ControlNetLoader`
- `VAELoader`
- `KSampler` ★核心
- `VAEDecode` ★核心
- `SaveImage`
- `UNETLoader` ★核心
- `DualCLIPLoader`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `ControlNetApplyAdvanced` ★核心
- `LoadImage`
- `GetImageSize+`
- `EmptyLatentImage` ★核心
- `PreviewImage`
- `UNETLoader` ★核心
- `DualCLIPLoader`
- `KSampler` ★核心
- `VAEDecode` ★核心
- `ControlNetLoader`
- `InfiniteYouApply`
- `VAELoader`
- `LoadImage`
- `EmptyLatentImage` ★核心
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `SaveImage`
- `ControlNetLoader`
- `DualCLIPLoader`
- `CLIPTextEncode` ★核心
- `EmptyLatentImage` ★核心
- `LoadImage`
- `LoadImage`
- `VAEDecode` ★核心
- `KSampler` ★核心
- `FaceCombine`
- `CLIPTextEncode` ★核心
- `SaveImage`
- `VAELoader`
- `UNETLoader` ★核心
- `CheckpointLoaderSimple` ★核心
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `EmptyLatentImage` ★核心
- `LoadImage`
- `IPAdapterUnifiedLoaderFaceID`
- `CLIPVisionLoader`
- `IPAdapterInsightFaceLoader`
- `IPAdapterFaceID`
- `VAEDecode` ★核心
- `SaveImage`
- `KSampler` ★核心
- `CLIPTextEncode` ★核心
- `EmptyLatentImage` ★核心
- `LoadImage`
- `CLIPVisionLoader`
- `IPAdapterInsightFaceLoader`
- `IPAdapterFaceID`
- `VAEDecode` ★核心
- `SaveImage`
- `KSampler` ★核心
- `CheckpointLoaderSimple` ★核心
- `CLIPTextEncode` ★核心
- `IPAdapterUnifiedLoaderFaceID`
- `CLIPTextEncode` ★核心
- `EmptyLatentImage` ★核心
- `LoadImage`
- `CLIPVisionLoader`
- `CLIPTextEncode` ★核心
- `CheckpointLoaderSimple` ★核心
- `IPAdapterUnifiedLoader`
- `IPAdapterAdvanced`
- `KSampler` ★核心
- `VAEDecode` ★核心
- `SaveImage`
- `PulidModelLoader`
- `CLIPTextEncode` ★核心
- `EmptyLatentImage` ★核心
- `LoadImage`
- `CLIPTextEncode` ★核心
- `IPAdapterAdvanced`
- `KSampler` ★核心
- `VAEDecode` ★核心
- `SaveImage`
- `CheckpointLoaderSimple` ★核心
- `CLIPVisionLoader`
- `IPAdapterUnifiedLoader`
- `LoadImage`
- `OpenposePreprocessor`
- `ReActorFaceSwap`
- `ReActorFaceBoost`
- `LoadImage`
- `LoadImage`
- `SaveImage`
- `DualCLIPLoader`
- `CLIPTextEncode` ★核心
- `VAEDecode` ★核心
- `CLIPVisionLoader`
- `VAELoader`
- `LoraLoaderModelOnly` ★核心
- `InpaintModelConditioning`
- `CLIPVisionEncode`
- `CLIPTextEncode` ★核心
- `FluxGuidance`
- `ImageIC`
- `StyleModelApply`
- `StyleModelLoader`
- `UNETLoader` ★核心
- `PreviewImage`
- `MaskPreview+`
- `KSampler` ★核心
- `EmptyImage`
- `LayerUtility: CropByMask V2`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `Mask Gaussian Region`
- `ImageSharpen`
- `LayerUtility: ImageScaleRestore V2`
- `LayerUtility: RestoreCropBox`
- `LoadImage`
- `SaveImage`
- `DualCLIPLoader`
- `LoadImage`
- `LoadImage`
- `LayerUtility: CropByMask`
- `SaveImage`
- `UNETLoader` ★核心
- `ControlNetLoader`
- `KSampler` ★核心
- `DifferentialDiffusion`
- `VAELoader`
- `VAEDecode` ★核心
- `LoadImage`
- `LoadImage`
- `SaveImage`
- `ImpactGaussianBlurMask`
- `FaceSwap_InfiniteYou`

**识别到的模式**：text_to_image

## 关键参数

- `checkpoint` = `LEOSAM HelloWorld 新世界 - V7.safetensors`
- `seed` = `474562052770258`
- `steps` = `10`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `0.5500000000000002`
- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`
- `controlnet_strength` = `0.8000000000000002`

## 知识

覆盖率 **90%**（236/262）

**有卡**：`InstantIDFaceAnalysis`、`InstantIDModelLoader`、`ControlNetLoader`、`ApplyInstantID`、`CheckpointLoaderSimple`、`LoadImage`、`KSampler`、`SaveImage`、`VAEDecode`、`CLIPTextEncode`、`InpaintModelConditioning`、`DifferentialDiffusion`、`ApplyPulid`、`PulidEvaClipLoader`、`PulidInsightFaceLoader`、`PulidModelLoader`、`EmptyLatentImage`、`ControlNetApplyAdvanced`、`ApplyZenID`、`DWPreprocessor`、`ZenIDCombineFace`、`EcomIDEvaClipLoader`、`EcomIDFaceAnalysis`、`ApplyEcomID`、`EmptyImage`、`ApplyEcomIDAdvanced`、`ApplyPulidFlux`、`PulidFluxEvaClipLoader`、`PulidFluxModelLoader`、`UNETLoader`、`DualCLIPLoader`、`VAELoader`、`PulidFluxInsightFaceLoader`、`OpenposePreprocessor`、`InfiniteYouApply`、`FaceCombine`、`IPAdapterUnifiedLoaderFaceID`、`CLIPVisionLoader`、`IPAdapterInsightFaceLoader`、`IPAdapterFaceID`、`IPAdapterUnifiedLoader`、`IPAdapterAdvanced`、`ReActorFaceSwap`、`ReActorFaceBoost`、`LoraLoaderModelOnly`、`CLIPVisionEncode`、`FluxGuidance`、`ImageIC`、`StyleModelApply`、`StyleModelLoader`、`ImageSharpen`、`ImpactGaussianBlurMask`、`FaceSwap_InfiniteYou`

**缺卡**（18）：`LayerUtility: CropByMask`、`LayerUtility: CropByMask`、`LayerUtility: CropByMask V2`、`LayerUtility: ImageBlendAdvance V3`、`LayerUtility: ImageBlendAdvance V3`、`LayerUtility: ImageScaleByAspectRatio V2`、`LayerUtility: ImageScaleByAspectRatio V2`、`LayerUtility: ImageScaleRestore V2`、`LayerUtility: ImageScaleRestore V2`、`LayerUtility: RestoreCropBox`、`LayerUtility: RestoreCropBox`、`Mask Gaussian Region`、`MaskBlur+`、`GetImageSize+`、`GetImageSize+`、`GetImageSize+`、`GetImageSize+`、`MaskPreview+`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CheckpointLoaderSimple、UNETLoader、CLIPTextEncode、EmptyLatentImage

## 参数体检

发现 2 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- 次要节点 `LayerUtility: CropByMask` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: CropByMask` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: CropByMask V2` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: ImageBlendAdvance V3` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: ImageBlendAdvance V3` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: ImageScaleRestore V2` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: ImageScaleRestore V2` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: RestoreCropBox` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: RestoreCropBox` 知识库中没有该节点类型的任何知识
- 次要节点 `Mask Gaussian Region` 知识库中没有该节点类型的任何知识
- 次要节点 `MaskBlur+` 知识库中没有该节点类型的任何知识
- 次要节点 `GetImageSize+` 仅有 Resolution 的通用知识，没有该节点自己的说明
- 次要节点 `GetImageSize+` 仅有 Resolution 的通用知识，没有该节点自己的说明
- 次要节点 `GetImageSize+` 仅有 Resolution 的通用知识，没有该节点自己的说明
- 次要节点 `GetImageSize+` 仅有 Resolution 的通用知识，没有该节点自己的说明
- 次要节点 `MaskPreview+` 仅有 SaveImage 的通用知识，没有该节点自己的说明
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

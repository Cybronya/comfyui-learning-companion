---
key: 平台全量/Krea联动wan2.2大画幅出图_1953001969473548289.json
name: Krea联动wan2.2大画幅出图_1953001969473548289
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/平台全量/Krea联动wan2.2大画幅出图_1953001969473548289.json
hash: 31ca8154d87d867f
coverage: 0.714286
learned_at: 2026-11-14 00:36:35
nodes: [ImageFromBatch, ImageFromBatch, ImageFromBatch, ImageFromBatch, ImageFromBatch, ImageFromBatch, ImageFromBatch, ImageFromBatch, ImageConcanateOfUtils, ImageConcanateOfUtils, ImageUpscaleWithModel, Image Tiled, ImageConcanateOfUtils, LoraLoaderModelOnly, SetNode, SetNode, LoadImage, GetNode, SetNode, JWImageResizeByLongerSide, GetNode, SetNode, GetNode, StyleModelLoader, GetNode, DualCLIPLoader, EmptyLatentImage, CLIPVisionLoader, GetNode, LyingSigmaSampler, BasicScheduler, VAELoader, PulidFluxInsightFaceLoader, PulidFluxEvaClipLoader, StyleModelApply, CLIPVisionEncode, ConditioningZeroOut, FluxGuidance, KSamplerSelect, ApplyPulidFlux, SamplerCustom, easy seed, SplitSigmas, CFGZeroStar, SamplerCustom, ApplyPulidFlux, PathchSageAttentionKJ, UNETLoader, CFGZeroStar, GetNode, UNETLoader, LayerUtility: PurgeVRAM, PathchSageAttentionKJ, ModelSamplingSD3, CLIPTextEncode, CLIPLoader, VAELoader, PreviewImage, Image Comparer (rgthree), ImageScaleBy, UpscaleModelLoader, DetectFaces, CropFaces, Reroute, GetNode, ControlNetLoader, InstantIDModelLoader, VAEEncode, VAEDecode, PreviewImage, Image Comparer (rgthree), Anything Everywhere3, Anything Everywhere3, PulidFluxModelLoader, PathchSageAttentionKJ, ImageUpscaleWithModel, VAEEncode, UNETLoader, Reroute, PreviewImage, Anything Everywhere3, ImageScaleBy, JWImageResizeByLongerSide, SaveImage, SaveImage, SaveImage, PreviewImage, ImageConcanate, GetNode, GetNode, ImageConcanate, PreviewImage, SaveImage, LoadImage, CLIPTextEncode, ApplyInstantID, CLIPTextEncode, CheckpointLoaderSimple, WarpFacesBack, InstantIDFaceAnalysis, KSampler, RH_Translator, Note, VAEDecodeTiled, CLIPTextEncode, RH_LLMAPI_NODE, CLIPTextEncode, ShowText|pysssss, PreviewImage, UpscaleModelLoader, VAEDecode, LoadImage, LoadImage, ShowText|pysssss, easy imageColorMatch, KSampler, LayerMask: MaskGrow, CR Text, Note, Fast Groups Bypasser (rgthree), Note, LoadImage, Fast Groups Bypasser (rgthree), Fast Groups Bypasser (rgthree), Note, Note]
patterns: [text_to_image, image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 1, "checkpoint": "juggernautXL_v9Rdphoto2Lightning.safetensors", "denoise": 0.10000000000000002, "height": 1152, "sampler_name": "euler", "scheduler": "simple", "seed": 695326231073603, "steps": 6, "width": 896}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 平台全量/Krea联动wan2.2大画幅出图_1953001969473548289.json

> 来源文件 `comfyui_library/workflows/平台全量/Krea联动wan2.2大画幅出图_1953001969473548289.json`

## 结构

**生成流程**：Model → Encode → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（126 个）：
- `ImageFromBatch`
- `ImageFromBatch`
- `ImageFromBatch`
- `ImageFromBatch`
- `ImageFromBatch`
- `ImageFromBatch`
- `ImageFromBatch`
- `ImageFromBatch`
- `ImageConcanateOfUtils`
- `ImageConcanateOfUtils`
- `ImageUpscaleWithModel`
- `Image Tiled`
- `ImageConcanateOfUtils`
- `LoraLoaderModelOnly` ★核心
- `SetNode`
- `SetNode`
- `LoadImage`
- `GetNode`
- `SetNode`
- `JWImageResizeByLongerSide`
- `GetNode`
- `SetNode`
- `GetNode`
- `StyleModelLoader`
- `GetNode`
- `DualCLIPLoader`
- `EmptyLatentImage` ★核心
- `CLIPVisionLoader`
- `GetNode`
- `LyingSigmaSampler` ★核心
- `BasicScheduler`
- `VAELoader`
- `PulidFluxInsightFaceLoader`
- `PulidFluxEvaClipLoader`
- `StyleModelApply`
- `CLIPVisionEncode`
- `ConditioningZeroOut`
- `FluxGuidance`
- `KSamplerSelect` ★核心
- `ApplyPulidFlux`
- `SamplerCustom` ★核心
- `easy seed`
- `SplitSigmas`
- `CFGZeroStar`
- `SamplerCustom` ★核心
- `ApplyPulidFlux`
- `PathchSageAttentionKJ`
- `UNETLoader` ★核心
- `CFGZeroStar`
- `GetNode`
- `UNETLoader` ★核心
- `LayerUtility: PurgeVRAM`
- `PathchSageAttentionKJ`
- `ModelSamplingSD3`
- `CLIPTextEncode` ★核心
- `CLIPLoader`
- `VAELoader`
- `PreviewImage`
- `Image Comparer (rgthree)`
- `ImageScaleBy`
- `UpscaleModelLoader`
- `DetectFaces`
- `CropFaces`
- `Reroute`
- `GetNode`
- `ControlNetLoader`
- `InstantIDModelLoader`
- `VAEEncode` ★核心
- `VAEDecode` ★核心
- `PreviewImage`
- `Image Comparer (rgthree)`
- `Anything Everywhere3`
- `Anything Everywhere3`
- `PulidFluxModelLoader`
- `PathchSageAttentionKJ`
- `ImageUpscaleWithModel`
- `VAEEncode` ★核心
- `UNETLoader` ★核心
- `Reroute`
- `PreviewImage`
- `Anything Everywhere3`
- `ImageScaleBy`
- `JWImageResizeByLongerSide`
- `SaveImage`
- `SaveImage`
- `SaveImage`
- `PreviewImage`
- `ImageConcanate`
- `GetNode`
- `GetNode`
- `ImageConcanate`
- `PreviewImage`
- `SaveImage`
- `LoadImage`
- `CLIPTextEncode` ★核心
- `ApplyInstantID`
- `CLIPTextEncode` ★核心
- `CheckpointLoaderSimple` ★核心
- `WarpFacesBack`
- `InstantIDFaceAnalysis`
- `KSampler` ★核心
- `RH_Translator`
- `Note`
- `VAEDecodeTiled` ★核心
- `CLIPTextEncode` ★核心
- `RH_LLMAPI_NODE`
- `CLIPTextEncode` ★核心
- `ShowText|pysssss`
- `PreviewImage`
- `UpscaleModelLoader`
- `VAEDecode` ★核心
- `LoadImage`
- `LoadImage`
- `ShowText|pysssss`
- `easy imageColorMatch`
- `KSampler` ★核心
- `LayerMask: MaskGrow`
- `CR Text`
- `Note`
- `Fast Groups Bypasser (rgthree)`
- `Note`
- `LoadImage`
- `Fast Groups Bypasser (rgthree)`
- `Fast Groups Bypasser (rgthree)`
- `Note`
- `Note`

**识别到的模式**：text_to_image、image_to_image

## 关键参数

- `width` = `896`
- `height` = `1152`
- `batch_size` = `1`
- `checkpoint` = `juggernautXL_v9Rdphoto2Lightning.safetensors`
- `seed` = `695326231073603`
- `steps` = `6`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `0.10000000000000002`

## 知识

覆盖率 **71%**（90/126）

**有卡**：`ImageFromBatch`、`ImageConcanateOfUtils`、`ImageUpscaleWithModel`、`Image Tiled`、`LoraLoaderModelOnly`、`LoadImage`、`JWImageResizeByLongerSide`、`StyleModelLoader`、`DualCLIPLoader`、`EmptyLatentImage`、`CLIPVisionLoader`、`LyingSigmaSampler`、`BasicScheduler`、`VAELoader`、`PulidFluxInsightFaceLoader`、`PulidFluxEvaClipLoader`、`StyleModelApply`、`CLIPVisionEncode`、`ConditioningZeroOut`、`FluxGuidance`、`KSamplerSelect`、`ApplyPulidFlux`、`SamplerCustom`、`easy seed`、`SplitSigmas`、`CFGZeroStar`、`PathchSageAttentionKJ`、`UNETLoader`、`LayerUtility: PurgeVRAM`、`ModelSamplingSD3`、`CLIPTextEncode`、`CLIPLoader`、`ImageScaleBy`、`UpscaleModelLoader`、`DetectFaces`、`CropFaces`、`ControlNetLoader`、`InstantIDModelLoader`、`VAEEncode`、`VAEDecode`、`PulidFluxModelLoader`、`SaveImage`、`ImageConcanate`、`ApplyInstantID`、`CheckpointLoaderSimple`、`WarpFacesBack`、`InstantIDFaceAnalysis`、`KSampler`、`RH_Translator`、`VAEDecodeTiled`、`RH_LLMAPI_NODE`、`easy imageColorMatch`、`LayerMask: MaskGrow`、`CR Text`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CheckpointLoaderSimple、UNETLoader、CLIPLoader、CLIPTextEncode

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

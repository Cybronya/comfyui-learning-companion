---
key: 平台全量/👨🏻换头_换脸-聚集裁剪-wan 2.2 vace fun for image-图片编辑_1964018130139889665.json
name: 👨🏻换头_换脸-聚集裁剪-wan 2.2 vace fun for image-图片编辑_1964018130139889665
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/👨🏻换头_换脸-聚集裁剪-wan 2.2 vace fun for image-图片编辑_1964018130139889665.json
hash: fb8e44046758873a
coverage: 0.524691
learned_at: 2026-11-14 02:54:51
nodes: [VAELoader, InstantIDFaceAnalysis, ControlNetLoader, SetNode, SetNode, SetNode, CheckpointLoaderSimple, InstantIDModelLoader, DifferentialDiffusion, ApplyInstantID, GetNode, easy cleanGpuUsed, CLIPTextEncode, GetNode, VAEDecode, GetNode, SetNode, GetNode, GetNode, CLIPTextEncode, SetNode, SetNode, SetNode, SetNode, PreviewImage, easy cleanGpuUsed, GetNode, GetNode, InpaintStitchImproved, LayerMask: PersonMaskUltra V2, LayerMask: PersonMaskUltra V2, SetNode, RepeatImageBatch, Reroute, Reroute, easy imageRemBg, GetNode, GetNode, Any Switch (rgthree), GetNode, ImageSmartSharpen+, LayerMask: MaskGrow, LayerMask: PersonMaskUltra V2, ImageCompositeMasked, GetNode, GetNode, LayerMask: MaskGrow, GetNode, SetNode, SetNode, GetNode, FaceAnalysisModels, GetNode, FaceAlign, PreviewImage, InpaintCropImproved, SetNode, GetNode, SetNode, GetNode, GetNode, GetNode, GetImageSizeAndCount, CLIPTextEncode, GetNode, SetNode, UNETLoader, GetNode, WanVaceToVideo, GetNode, GetNode, SetNode, GetNode, Text, GetNode, CLIPTextEncode, InpaintModelConditioning, easy seed, SaveImage, SaveImage, LoadImage, ImageCompositeMasked, Anything Everywhere3, CLIPLoader, LayerMask: MaskGrow, VHS_DuplicateMasks, SetNode, VAEDecode, GetImageRangeFromBatch, GetImageSizeAndCount, SetNode, SetNode, GetNode, CFGNorm, LoraLoaderModelOnly, LoraLoaderModelOnly, PreviewImage, ImageSmartSharpen+, GetNode, PreviewImage, ImageCompositeMasked, ImageResizeKJ, AIO_Preprocessor, SetNode, InpaintStitchImproved, InpaintStitchImproved, workflow>loras, ModelSamplingSD3, Latent Noise Injection, SaveImage, Note, Note, Note, KSamplerAdvanced, Float, Int, InpaintCropImproved, ImpactSwitch, LayerFilter: FilmV2, SetNode, Reroute, LayerMask: MediapipeFacialSegment, LayerMask: MaskGrow, SetNode, SubtractMask, SetNode, GetNode, GetNode, StrToCombo, StrToCombo, ImageBlend, OnnxDetectionModelLoader, GetNode, PoseDetectionOneToAllAnimation, ImpactSwitch, ImpactSwitch, PreviewImage, KSampler, Note, DrawMaskOnImage, LG_Color_Match_V2, ImageFromBatch+, SetNode, LayerMask: PersonMaskUltra V2, LayerMask: MaskGrow, LayerMask: PersonMaskUltra V2, workflow>遮罩块, ImageAndMaskPreview, workflow>遮罩块, SetNode, SetNode, LoadImage, GetNode, workflow>物体检测, GetNode, Reroute, LayerMask: MaskGrow, PrimitiveBoolean, ImageAndMaskPreview, InpaintCropImproved, ImpactSwitch, ImpactSwitch]
patterns: []
missing: []
parameters: {"cfg": 1.5, "checkpoint": "realvisxlV50_v50Bakedvae.safetensors", "denoise": 0.3500000000000001, "sampler_name": "dpmpp_2m", "scheduler": "karras", "seed": 898831127962573, "steps": 20}
---

# 平台全量/👨🏻换头_换脸-聚集裁剪-wan 2.2 vace fun for image-图片编辑_1964018130139889665.json

> 来源文件 `comfyui_library/workflows/平台全量/👨🏻换头_换脸-聚集裁剪-wan 2.2 vace fun for image-图片编辑_1964018130139889665.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（162 个）：
- `VAELoader`
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
- `easy cleanGpuUsed`
- `CLIPTextEncode` ★核心
- `GetNode`
- `VAEDecode` ★核心
- `GetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `CLIPTextEncode` ★核心
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `PreviewImage`
- `easy cleanGpuUsed`
- `GetNode`
- `GetNode`
- `InpaintStitchImproved`
- `LayerMask: PersonMaskUltra V2`
- `LayerMask: PersonMaskUltra V2`
- `SetNode`
- `RepeatImageBatch`
- `Reroute`
- `Reroute`
- `easy imageRemBg`
- `GetNode`
- `GetNode`
- `Any Switch (rgthree)`
- `GetNode`
- `ImageSmartSharpen+`
- `LayerMask: MaskGrow`
- `LayerMask: PersonMaskUltra V2`
- `ImageCompositeMasked`
- `GetNode`
- `GetNode`
- `LayerMask: MaskGrow`
- `GetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `FaceAnalysisModels`
- `GetNode`
- `FaceAlign`
- `PreviewImage`
- `InpaintCropImproved`
- `SetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetImageSizeAndCount`
- `CLIPTextEncode` ★核心
- `GetNode`
- `SetNode`
- `UNETLoader` ★核心
- `GetNode`
- `WanVaceToVideo`
- `GetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `Text`
- `GetNode`
- `CLIPTextEncode` ★核心
- `InpaintModelConditioning`
- `easy seed`
- `SaveImage`
- `SaveImage`
- `LoadImage`
- `ImageCompositeMasked`
- `Anything Everywhere3`
- `CLIPLoader`
- `LayerMask: MaskGrow`
- `VHS_DuplicateMasks`
- `SetNode`
- `VAEDecode` ★核心
- `GetImageRangeFromBatch`
- `GetImageSizeAndCount`
- `SetNode`
- `SetNode`
- `GetNode`
- `CFGNorm`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `PreviewImage`
- `ImageSmartSharpen+`
- `GetNode`
- `PreviewImage`
- `ImageCompositeMasked`
- `ImageResizeKJ`
- `AIO_Preprocessor`
- `SetNode`
- `InpaintStitchImproved`
- `InpaintStitchImproved`
- `workflow>loras`
- `ModelSamplingSD3`
- `Latent Noise Injection`
- `SaveImage`
- `Note`
- `Note`
- `Note`
- `KSamplerAdvanced` ★核心
- `Float`
- `Int`
- `InpaintCropImproved`
- `ImpactSwitch`
- `LayerFilter: FilmV2`
- `SetNode`
- `Reroute`
- `LayerMask: MediapipeFacialSegment`
- `LayerMask: MaskGrow`
- `SetNode`
- `SubtractMask`
- `SetNode`
- `GetNode`
- `GetNode`
- `StrToCombo`
- `StrToCombo`
- `ImageBlend`
- `OnnxDetectionModelLoader`
- `GetNode`
- `PoseDetectionOneToAllAnimation`
- `ImpactSwitch`
- `ImpactSwitch`
- `PreviewImage`
- `KSampler` ★核心
- `Note`
- `DrawMaskOnImage`
- `LG_Color_Match_V2`
- `ImageFromBatch+`
- `SetNode`
- `LayerMask: PersonMaskUltra V2`
- `LayerMask: MaskGrow`
- `LayerMask: PersonMaskUltra V2`
- `workflow>遮罩块`
- `ImageAndMaskPreview`
- `workflow>遮罩块`
- `SetNode`
- `SetNode`
- `LoadImage`
- `GetNode`
- `workflow>物体检测`
- `GetNode`
- `Reroute`
- `LayerMask: MaskGrow`
- `PrimitiveBoolean`
- `ImageAndMaskPreview`
- `InpaintCropImproved`
- `ImpactSwitch`
- `ImpactSwitch`

## 关键参数

- `checkpoint` = `realvisxlV50_v50Bakedvae.safetensors`
- `seed` = `898831127962573`
- `steps` = `20`
- `cfg` = `1.5`
- `sampler_name` = `dpmpp_2m`
- `scheduler` = `karras`
- `denoise` = `0.3500000000000001`

## 知识

覆盖率 **52%**（85/162）

**有卡**：`VAELoader`、`InstantIDFaceAnalysis`、`ControlNetLoader`、`CheckpointLoaderSimple`、`InstantIDModelLoader`、`DifferentialDiffusion`、`ApplyInstantID`、`easy cleanGpuUsed`、`CLIPTextEncode`、`VAEDecode`、`InpaintStitchImproved`、`LayerMask: PersonMaskUltra V2`、`RepeatImageBatch`、`easy imageRemBg`、`ImageSmartSharpen+`、`LayerMask: MaskGrow`、`ImageCompositeMasked`、`FaceAnalysisModels`、`FaceAlign`、`InpaintCropImproved`、`GetImageSizeAndCount`、`UNETLoader`、`WanVaceToVideo`、`Text`、`InpaintModelConditioning`、`easy seed`、`SaveImage`、`LoadImage`、`CLIPLoader`、`VHS_DuplicateMasks`、`GetImageRangeFromBatch`、`CFGNorm`、`LoraLoaderModelOnly`、`ImageResizeKJ`、`AIO_Preprocessor`、`workflow>loras`、`ModelSamplingSD3`、`Latent Noise Injection`、`KSamplerAdvanced`、`Float`、`Int`、`LayerFilter: FilmV2`、`LayerMask: MediapipeFacialSegment`、`SubtractMask`、`StrToCombo`、`ImageBlend`、`OnnxDetectionModelLoader`、`PoseDetectionOneToAllAnimation`、`KSampler`、`DrawMaskOnImage`、`LG_Color_Match_V2`、`ImageFromBatch+`、`workflow>遮罩块`、`ImageAndMaskPreview`、`workflow>物体检测`、`PrimitiveBoolean`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CheckpointLoaderSimple、UNETLoader、CLIPLoader、CLIPTextEncode

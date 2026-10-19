---
key: 图片生成/文生图/Z-Image-Controlnet-2.1-8步文生图+lora修脸贴回+放大_2003343268333092866.json
name: Z-Image-Controlnet-2.1-8步文生图+lora修脸贴回+放大_2003343268333092866
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Z-Image-Controlnet-2.1-8步文生图+lora修脸贴回+放大_2003343268333092866.json
hash: 9dc14cbca32e90de
coverage: 0.852174
learned_at: 2026-10-19 21:47:00
nodes: [DetailDaemonSamplerNode, RandomNoise, SamplerEulerAncestral, VAEEncode, Reroute, TTP_Image_Tile_Batch, easy imageListToImageBatch, TTP_Image_Assy, TTP_Tile_image_size, easy imageBatchToImageList, ImageUpscaleWithModel, CLIPTextEncode, Seed (rgthree), CLIPTextEncode, ImageScaleToTotalPixels, ShowText|pysssss, CLIPLoader, UpscaleModelLoader, ConditioningZeroOut, VAEDecodeTiled, Reroute, CFGGuider, Florence2Run, Florence2ModelLoader, CLIPTextEncode, ModelSamplingAuraFlow, CLIPTextEncode, ImageResize+, GetImageSize+, TTP_Tile_image_size, TTP_Image_Tile_Batch, GetImageSize+, ImageResize+, ImageScaleBy, ImageScaleBy, SeedVR2VideoUpscaler, easy cleanGpuUsed, SeedVR2LoadVAEModel, SeedVR2LoadDiTModel, UNETLoader, TTP_Image_Assy, PrimitiveNode, Note, VAEDecode, VAELoader, SamplerCustomAdvanced, SaveImage, Note, MarkdownNote, Seed (rgthree), ModelPatchLoader, UNETLoader, LoraLoaderModelOnly, VAEEncode, LayerMask: MaskGrow, PreviewImage, CLIPLoader, SamplerEulerAncestral, RandomNoise, DetailDaemonSamplerNode, CFGGuider, ModelSamplingAuraFlow, SaveImage, LayerUtility: RestoreCropBox, VAEDecode, LayerUtility: ImageScaleRestore, PreviewImage, LayerUtility: CropByMask V2, CLIPTextEncode, ConditioningZeroOut, VAELoader, InpaintModelConditioning, LayerUtility: ImageScaleRestore, KSampler, LayerUtility: PurgeVRAM V2, PreviewImage, SDPoseOODLoader, YOLOModelLoader, ImageLoader, AIO_Preprocessor, easy ifElse, SamplerCustomAdvanced, RandomNoise, ModelSamplingAuraFlow, SamplerEulerAncestral, VAEDecode, SamplerCustomAdvanced, VAEDecode, CFGGuider, DetailDaemonSamplerNode, BasicScheduler, BasicScheduler, SamplerCustomAdvanced, LatentUpscaleBy, String Literal, PreviewImage, String Literal, LoraLoaderModelOnly, SDPoseOODProcessor, String Literal, LoraLoaderModelOnly, BasicScheduler, PreviewImage, Image Comparer (rgthree), ImageResizeKJv2, easy int, SplitSigmas, ZImageFunControlnet, VAEEncode, LoadImage, Image Comparer (rgthree), ModelPatchLoader, PreviewImage, PreviewImage, SaveImage]
patterns: [image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 0.25000000000000006, "sampler_name": "euler", "scheduler": "simple", "seed": 1067213692497413, "steps": 8}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/文生图/Z-Image-Controlnet-2.1-8步文生图+lora修脸贴回+放大_2003343268333092866.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Z-Image-Controlnet-2.1-8步文生图+lora修脸贴回+放大_2003343268333092866.json`

## 结构

**生成流程**：Model → Encode → Condition → Control → Sampling → Decode → Process → Output → Other

**节点**（115 个）：
- `DetailDaemonSamplerNode` ★核心
- `RandomNoise`
- `SamplerEulerAncestral` ★核心
- `VAEEncode` ★核心
- `Reroute`
- `TTP_Image_Tile_Batch`
- `easy imageListToImageBatch`
- `TTP_Image_Assy`
- `TTP_Tile_image_size`
- `easy imageBatchToImageList`
- `ImageUpscaleWithModel`
- `CLIPTextEncode` ★核心
- `Seed (rgthree)`
- `CLIPTextEncode` ★核心
- `ImageScaleToTotalPixels`
- `ShowText|pysssss`
- `CLIPLoader`
- `UpscaleModelLoader`
- `ConditioningZeroOut`
- `VAEDecodeTiled` ★核心
- `Reroute`
- `CFGGuider`
- `Florence2Run`
- `Florence2ModelLoader`
- `CLIPTextEncode` ★核心
- `ModelSamplingAuraFlow`
- `CLIPTextEncode` ★核心
- `ImageResize+`
- `GetImageSize+`
- `TTP_Tile_image_size`
- `TTP_Image_Tile_Batch`
- `GetImageSize+`
- `ImageResize+`
- `ImageScaleBy`
- `ImageScaleBy`
- `SeedVR2VideoUpscaler`
- `easy cleanGpuUsed`
- `SeedVR2LoadVAEModel`
- `SeedVR2LoadDiTModel`
- `UNETLoader` ★核心
- `TTP_Image_Assy`
- `PrimitiveNode`
- `Note`
- `VAEDecode` ★核心
- `VAELoader`
- `SamplerCustomAdvanced` ★核心
- `SaveImage`
- `Note`
- `MarkdownNote`
- `Seed (rgthree)`
- `ModelPatchLoader`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `VAEEncode` ★核心
- `LayerMask: MaskGrow`
- `PreviewImage`
- `CLIPLoader`
- `SamplerEulerAncestral` ★核心
- `RandomNoise`
- `DetailDaemonSamplerNode` ★核心
- `CFGGuider`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `LayerUtility: RestoreCropBox`
- `VAEDecode` ★核心
- `LayerUtility: ImageScaleRestore`
- `PreviewImage`
- `LayerUtility: CropByMask V2`
- `CLIPTextEncode` ★核心
- `ConditioningZeroOut`
- `VAELoader`
- `InpaintModelConditioning`
- `LayerUtility: ImageScaleRestore`
- `KSampler` ★核心
- `LayerUtility: PurgeVRAM V2`
- `PreviewImage`
- `SDPoseOODLoader`
- `YOLOModelLoader`
- `ImageLoader`
- `AIO_Preprocessor`
- `easy ifElse`
- `SamplerCustomAdvanced` ★核心
- `RandomNoise`
- `ModelSamplingAuraFlow`
- `SamplerEulerAncestral` ★核心
- `VAEDecode` ★核心
- `SamplerCustomAdvanced` ★核心
- `VAEDecode` ★核心
- `CFGGuider`
- `DetailDaemonSamplerNode` ★核心
- `BasicScheduler`
- `BasicScheduler`
- `SamplerCustomAdvanced` ★核心
- `LatentUpscaleBy`
- `String Literal`
- `PreviewImage`
- `String Literal`
- `LoraLoaderModelOnly` ★核心
- `SDPoseOODProcessor`
- `String Literal`
- `LoraLoaderModelOnly` ★核心
- `BasicScheduler`
- `PreviewImage`
- `Image Comparer (rgthree)`
- `ImageResizeKJv2`
- `easy int`
- `SplitSigmas`
- `ZImageFunControlnet`
- `VAEEncode` ★核心
- `LoadImage`
- `Image Comparer (rgthree)`
- `ModelPatchLoader`
- `PreviewImage`
- `PreviewImage`
- `SaveImage`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `1067213692497413`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `0.25000000000000006`

## 知识

覆盖率 **85%**（98/115）

**有卡**：`DetailDaemonSamplerNode`、`RandomNoise`、`SamplerEulerAncestral`、`VAEEncode`、`TTP_Image_Tile_Batch`、`easy imageListToImageBatch`、`TTP_Image_Assy`、`TTP_Tile_image_size`、`easy imageBatchToImageList`、`ImageUpscaleWithModel`、`CLIPTextEncode`、`Seed (rgthree)`、`ImageScaleToTotalPixels`、`CLIPLoader`、`UpscaleModelLoader`、`ConditioningZeroOut`、`VAEDecodeTiled`、`CFGGuider`、`Florence2Run`、`Florence2ModelLoader`、`ModelSamplingAuraFlow`、`ImageResize+`、`GetImageSize+`、`ImageScaleBy`、`SeedVR2VideoUpscaler`、`easy cleanGpuUsed`、`SeedVR2LoadVAEModel`、`SeedVR2LoadDiTModel`、`UNETLoader`、`VAEDecode`、`VAELoader`、`SamplerCustomAdvanced`、`SaveImage`、`ModelPatchLoader`、`LoraLoaderModelOnly`、`LayerMask: MaskGrow`、`LayerUtility: RestoreCropBox`、`LayerUtility: ImageScaleRestore`、`LayerUtility: CropByMask V2`、`InpaintModelConditioning`、`KSampler`、`LayerUtility: PurgeVRAM V2`、`SDPoseOODLoader`、`YOLOModelLoader`、`ImageLoader`、`AIO_Preprocessor`、`BasicScheduler`、`LatentUpscaleBy`、`String Literal`、`SDPoseOODProcessor`、`ImageResizeKJv2`、`easy int`、`SplitSigmas`、`ZImageFunControlnet`、`LoadImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、LoadImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

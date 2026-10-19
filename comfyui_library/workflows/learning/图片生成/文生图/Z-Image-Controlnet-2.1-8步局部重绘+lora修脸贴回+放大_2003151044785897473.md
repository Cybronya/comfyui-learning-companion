---
key: 图片生成/文生图/Z-Image-Controlnet-2.1-8步局部重绘+lora修脸贴回+放大_2003151044785897473.json
name: Z-Image-Controlnet-2.1-8步局部重绘+lora修脸贴回+放大_2003151044785897473
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Z-Image-Controlnet-2.1-8步局部重绘+lora修脸贴回+放大_2003151044785897473.json
hash: bf347aaf931b735a
coverage: 0.853448
learned_at: 2026-10-19 21:47:00
nodes: [DetailDaemonSamplerNode, RandomNoise, SamplerEulerAncestral, VAEEncode, Reroute, TTP_Image_Tile_Batch, easy imageListToImageBatch, TTP_Image_Assy, TTP_Tile_image_size, easy imageBatchToImageList, ImageUpscaleWithModel, CLIPTextEncode, Seed (rgthree), CLIPTextEncode, ImageScaleToTotalPixels, ShowText|pysssss, CLIPLoader, UpscaleModelLoader, ConditioningZeroOut, VAEDecodeTiled, Reroute, CFGGuider, Florence2Run, Florence2ModelLoader, CLIPTextEncode, ModelSamplingAuraFlow, CLIPTextEncode, ImageResize+, GetImageSize+, TTP_Tile_image_size, TTP_Image_Tile_Batch, GetImageSize+, ImageResize+, ImageScaleBy, ImageScaleBy, SeedVR2VideoUpscaler, easy cleanGpuUsed, SeedVR2LoadVAEModel, SeedVR2LoadDiTModel, UNETLoader, TTP_Image_Assy, PrimitiveNode, Note, VAEDecode, VAELoader, SamplerCustomAdvanced, SetLatentNoiseMask, Note, MarkdownNote, Seed (rgthree), ModelPatchLoader, UNETLoader, LoraLoaderModelOnly, VAEEncode, PreviewImage, CLIPLoader, SamplerEulerAncestral, RandomNoise, DetailDaemonSamplerNode, CFGGuider, ModelSamplingAuraFlow, VAEDecode, CLIPTextEncode, ConditioningZeroOut, VAELoader, InpaintModelConditioning, LayerUtility: PurgeVRAM V2, PreviewImage, PreviewImage, SDPoseOODLoader, YOLOModelLoader, ImageLoader, AIO_Preprocessor, easy ifElse, SamplerCustomAdvanced, RandomNoise, ModelSamplingAuraFlow, SamplerEulerAncestral, VAEDecode, SamplerCustomAdvanced, VAEDecode, CFGGuider, DetailDaemonSamplerNode, BasicScheduler, BasicScheduler, SamplerCustomAdvanced, LatentUpscaleBy, String Literal, LoraLoaderModelOnly, SDPoseOODProcessor, String Literal, LoraLoaderModelOnly, LoadImage, BasicScheduler, PreviewImage, Image Comparer (rgthree), ImageResizeKJv2, ZImageFunControlnet, easy int, SplitSigmas, VAEEncode, ModelPatchLoader, SaveImage, PreviewImage, SaveImage, LayerMask: MaskGrow, LayerUtility: CropByMask V2, LayerUtility: ImageScaleRestore, LayerUtility: ImageScaleRestore, LayerUtility: RestoreCropBox, PreviewImage, String Literal, PreviewImage, KSampler, SaveImage, Image Comparer (rgthree)]
patterns: [image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 0.25000000000000006, "sampler_name": "euler", "scheduler": "simple", "seed": 1067213692497413, "steps": 8}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/文生图/Z-Image-Controlnet-2.1-8步局部重绘+lora修脸贴回+放大_2003151044785897473.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Z-Image-Controlnet-2.1-8步局部重绘+lora修脸贴回+放大_2003151044785897473.json`

## 结构

**生成流程**：Model → Encode → Condition → Control → Sampling → Decode → Process → Output → Other

**节点**（116 个）：
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
- `SetLatentNoiseMask`
- `Note`
- `MarkdownNote`
- `Seed (rgthree)`
- `ModelPatchLoader`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `VAEEncode` ★核心
- `PreviewImage`
- `CLIPLoader`
- `SamplerEulerAncestral` ★核心
- `RandomNoise`
- `DetailDaemonSamplerNode` ★核心
- `CFGGuider`
- `ModelSamplingAuraFlow`
- `VAEDecode` ★核心
- `CLIPTextEncode` ★核心
- `ConditioningZeroOut`
- `VAELoader`
- `InpaintModelConditioning`
- `LayerUtility: PurgeVRAM V2`
- `PreviewImage`
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
- `LoraLoaderModelOnly` ★核心
- `SDPoseOODProcessor`
- `String Literal`
- `LoraLoaderModelOnly` ★核心
- `LoadImage`
- `BasicScheduler`
- `PreviewImage`
- `Image Comparer (rgthree)`
- `ImageResizeKJv2`
- `ZImageFunControlnet`
- `easy int`
- `SplitSigmas`
- `VAEEncode` ★核心
- `ModelPatchLoader`
- `SaveImage`
- `PreviewImage`
- `SaveImage`
- `LayerMask: MaskGrow`
- `LayerUtility: CropByMask V2`
- `LayerUtility: ImageScaleRestore`
- `LayerUtility: ImageScaleRestore`
- `LayerUtility: RestoreCropBox`
- `PreviewImage`
- `String Literal`
- `PreviewImage`
- `KSampler` ★核心
- `SaveImage`
- `Image Comparer (rgthree)`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `1067213692497413`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `0.25000000000000006`

## 知识

覆盖率 **85%**（99/116）

**有卡**：`DetailDaemonSamplerNode`、`RandomNoise`、`SamplerEulerAncestral`、`VAEEncode`、`TTP_Image_Tile_Batch`、`easy imageListToImageBatch`、`TTP_Image_Assy`、`TTP_Tile_image_size`、`easy imageBatchToImageList`、`ImageUpscaleWithModel`、`CLIPTextEncode`、`Seed (rgthree)`、`ImageScaleToTotalPixels`、`CLIPLoader`、`UpscaleModelLoader`、`ConditioningZeroOut`、`VAEDecodeTiled`、`CFGGuider`、`Florence2Run`、`Florence2ModelLoader`、`ModelSamplingAuraFlow`、`ImageResize+`、`GetImageSize+`、`ImageScaleBy`、`SeedVR2VideoUpscaler`、`easy cleanGpuUsed`、`SeedVR2LoadVAEModel`、`SeedVR2LoadDiTModel`、`UNETLoader`、`VAEDecode`、`VAELoader`、`SamplerCustomAdvanced`、`SetLatentNoiseMask`、`ModelPatchLoader`、`LoraLoaderModelOnly`、`InpaintModelConditioning`、`LayerUtility: PurgeVRAM V2`、`SDPoseOODLoader`、`YOLOModelLoader`、`ImageLoader`、`AIO_Preprocessor`、`BasicScheduler`、`LatentUpscaleBy`、`String Literal`、`SDPoseOODProcessor`、`LoadImage`、`ImageResizeKJv2`、`ZImageFunControlnet`、`easy int`、`SplitSigmas`、`SaveImage`、`LayerMask: MaskGrow`、`LayerUtility: CropByMask V2`、`LayerUtility: ImageScaleRestore`、`LayerUtility: RestoreCropBox`、`KSampler`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、LoadImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

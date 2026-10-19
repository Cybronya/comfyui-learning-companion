---
key: 图片生成/文生图/Z-Image×ControlNet 2.1二阶Refiner增强技巧 LoRA人物替换_2002219399727726593.json
name: Z-Image×ControlNet 2.1二阶Refiner增强技巧 LoRA人物替换_2002219399727726593
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Z-Image×ControlNet 2.1二阶Refiner增强技巧 LoRA人物替换_2002219399727726593.json
hash: e9ac6880f2531eb7
coverage: 0.845361
learned_at: 2026-10-19 21:47:02
nodes: [easy cleanGpuUsed, Qwen3_VQA, SamplerCustomAdvanced, DetailDaemonSamplerNode, RandomNoise, SamplerEulerAncestral, VAEEncode, Reroute, TTP_Image_Tile_Batch, easy imageListToImageBatch, TTP_Image_Assy, TTP_Tile_image_size, easy imageBatchToImageList, ImageUpscaleWithModel, CLIPTextEncode, Seed (rgthree), CLIPTextEncode, ImageScaleToTotalPixels, ShowText|pysssss, CLIPLoader, UltralyticsDetectorProvider, UpscaleModelLoader, ConditioningZeroOut, VAEDecodeTiled, Reroute, KSampler, CFGGuider, RandomNoise, CFGGuider, RandomNoise, SamplerEulerAncestral, PreviewImage, PreviewImage, PreviewImage, SamplerEulerAncestral, Florence2Run, Florence2ModelLoader, easy showAnything, CLIPTextEncode, ModelSamplingAuraFlow, CLIPTextEncode, ImageResize+, GetImageSize+, TTP_Tile_image_size, TTP_Image_Tile_Batch, GetImageSize+, ImageResize+, ImageScaleBy, ImageScaleBy, SeedVR2VideoUpscaler, VAEDecode, easy cleanGpuUsed, SeedVR2LoadVAEModel, SeedVR2LoadDiTModel, BasicScheduler, UNETLoader, Image Comparer (rgthree), TTP_Image_Assy, MultiplePathsInput, JWStringConcat, PrimitiveNode, Note, PreviewImage, ImageScaleBy, SamplerCustomAdvanced, VAEEncode, CFGGuider, Image Comparer (rgthree), PreviewImage, VAEDecode, VAEDecode, DetailDaemonSamplerNode, SaveImage, PreviewImage, PreviewImage, VAELoader, VAEEncode, SetLatentNoiseMask, SamplerCustomAdvanced, SetLatentNoiseMask, ModelPatchLoader, AIO_Preprocessor, QwenImageDiffsynthControlnet, JWStringConcat, String Literal, easy int, SplitSigmas, BasicScheduler, LoraLoaderModelOnly, ModelSamplingAuraFlow, ImageLoader, LoraLoaderModelOnly, RH_Captioner, ImageResizeKJv2, String Literal, FaceDetailer, SaveImage]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 0.30000000000000004, "sampler_name": "euler", "scheduler": "simple", "seed": 1067213692497413, "steps": 8}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/文生图/Z-Image×ControlNet 2.1二阶Refiner增强技巧 LoRA人物替换_2002219399727726593.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Z-Image×ControlNet 2.1二阶Refiner增强技巧 LoRA人物替换_2002219399727726593.json`

## 结构

**生成流程**：Model → Encode → Condition → Control → Sampling → Decode → Process → Output → Other

**节点**（97 个）：
- `easy cleanGpuUsed`
- `Qwen3_VQA`
- `SamplerCustomAdvanced` ★核心
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
- `UltralyticsDetectorProvider`
- `UpscaleModelLoader`
- `ConditioningZeroOut`
- `VAEDecodeTiled` ★核心
- `Reroute`
- `KSampler` ★核心
- `CFGGuider`
- `RandomNoise`
- `CFGGuider`
- `RandomNoise`
- `SamplerEulerAncestral` ★核心
- `PreviewImage`
- `PreviewImage`
- `PreviewImage`
- `SamplerEulerAncestral` ★核心
- `Florence2Run`
- `Florence2ModelLoader`
- `easy showAnything`
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
- `VAEDecode` ★核心
- `easy cleanGpuUsed`
- `SeedVR2LoadVAEModel`
- `SeedVR2LoadDiTModel`
- `BasicScheduler`
- `UNETLoader` ★核心
- `Image Comparer (rgthree)`
- `TTP_Image_Assy`
- `MultiplePathsInput`
- `JWStringConcat`
- `PrimitiveNode`
- `Note`
- `PreviewImage`
- `ImageScaleBy`
- `SamplerCustomAdvanced` ★核心
- `VAEEncode` ★核心
- `CFGGuider`
- `Image Comparer (rgthree)`
- `PreviewImage`
- `VAEDecode` ★核心
- `VAEDecode` ★核心
- `DetailDaemonSamplerNode` ★核心
- `SaveImage`
- `PreviewImage`
- `PreviewImage`
- `VAELoader`
- `VAEEncode` ★核心
- `SetLatentNoiseMask`
- `SamplerCustomAdvanced` ★核心
- `SetLatentNoiseMask`
- `ModelPatchLoader`
- `AIO_Preprocessor`
- `QwenImageDiffsynthControlnet`
- `JWStringConcat`
- `String Literal`
- `easy int`
- `SplitSigmas`
- `BasicScheduler`
- `LoraLoaderModelOnly` ★核心
- `ModelSamplingAuraFlow`
- `ImageLoader`
- `LoraLoaderModelOnly` ★核心
- `RH_Captioner`
- `ImageResizeKJv2`
- `String Literal`
- `FaceDetailer`
- `SaveImage`

## 关键参数

- `seed` = `1067213692497413`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `0.30000000000000004`

## 知识

覆盖率 **85%**（82/97）

**有卡**：`easy cleanGpuUsed`、`Qwen3_VQA`、`SamplerCustomAdvanced`、`DetailDaemonSamplerNode`、`RandomNoise`、`SamplerEulerAncestral`、`VAEEncode`、`TTP_Image_Tile_Batch`、`easy imageListToImageBatch`、`TTP_Image_Assy`、`TTP_Tile_image_size`、`easy imageBatchToImageList`、`ImageUpscaleWithModel`、`CLIPTextEncode`、`Seed (rgthree)`、`ImageScaleToTotalPixels`、`CLIPLoader`、`UltralyticsDetectorProvider`、`UpscaleModelLoader`、`ConditioningZeroOut`、`VAEDecodeTiled`、`KSampler`、`CFGGuider`、`Florence2Run`、`Florence2ModelLoader`、`ModelSamplingAuraFlow`、`ImageResize+`、`GetImageSize+`、`ImageScaleBy`、`SeedVR2VideoUpscaler`、`VAEDecode`、`SeedVR2LoadVAEModel`、`SeedVR2LoadDiTModel`、`BasicScheduler`、`UNETLoader`、`MultiplePathsInput`、`JWStringConcat`、`SaveImage`、`VAELoader`、`SetLatentNoiseMask`、`ModelPatchLoader`、`AIO_Preprocessor`、`QwenImageDiffsynthControlnet`、`String Literal`、`easy int`、`SplitSigmas`、`LoraLoaderModelOnly`、`ImageLoader`、`RH_Captioner`、`ImageResizeKJv2`、`FaceDetailer`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、UNETLoader

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

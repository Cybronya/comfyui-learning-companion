---
key: 图片生成/文生图/造相ControlNet2.0高低噪渲染+SeedVR2亿级像素_2000807895858020353.json
name: 造相ControlNet2.0高低噪渲染+SeedVR2亿级像素_2000807895858020353
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/造相ControlNet2.0高低噪渲染+SeedVR2亿级像素_2000807895858020353.json
hash: 9cf2fd3f82cd4d3a
coverage: 0.84375
learned_at: 2026-10-19 21:47:52
nodes: [easy cleanGpuUsed, Qwen3_VQA, SamplerCustomAdvanced, SamplerCustomAdvanced, DetailDaemonSamplerNode, RandomNoise, SamplerEulerAncestral, VAEEncode, Reroute, TTP_Image_Tile_Batch, easy imageListToImageBatch, TTP_Image_Assy, TTP_Tile_image_size, easy imageBatchToImageList, ImageUpscaleWithModel, CLIPTextEncode, Seed (rgthree), CLIPTextEncode, ImageScaleToTotalPixels, ShowText|pysssss, CLIPLoader, UltralyticsDetectorProvider, UpscaleModelLoader, ConditioningZeroOut, VAEDecodeTiled, Reroute, KSampler, FaceDetailer, CFGGuider, RandomNoise, CFGGuider, ModelSamplingAuraFlow, BasicScheduler, RandomNoise, SamplerEulerAncestral, PreviewImage, PreviewImage, PreviewImage, SamplerEulerAncestral, Florence2Run, Florence2ModelLoader, easy showAnything, CLIPTextEncode, ModelSamplingAuraFlow, CLIPTextEncode, ImageResize+, GetImageSize+, TTP_Tile_image_size, TTP_Image_Tile_Batch, GetImageSize+, ImageResize+, ImageScaleBy, ImageScaleBy, SeedVR2VideoUpscaler, VAEDecode, easy cleanGpuUsed, SeedVR2LoadVAEModel, SeedVR2LoadDiTModel, GetImageSize, BasicScheduler, AIO_Preprocessor, UNETLoader, Image Comparer (rgthree), TTP_Image_Assy, MultiplePathsInput, JWStringConcat, VAELoader, PrimitiveNode, ModelPatchLoader, LoraLoaderModelOnly, VAEEncode, ImageScaleToMaxDimension, EmptySD3LatentImage, Note, PreviewImage, ImageScaleBy, SamplerCustomAdvanced, VAEEncode, CFGGuider, Image Comparer (rgthree), PreviewImage, SplitSigmas, LoraLoaderModelOnly, Model Switch (JPS), ImageLoader, VAEDecode, VAEDecode, PreviewImage, SaveImage, QwenImageDiffsynthControlnet, DetailDaemonSamplerNode, String Literal, String Literal, PreviewImage, easy int, Latent Switch (JPS)]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 0.30000000000000004, "sampler_name": "euler", "scheduler": "simple", "seed": 1067213692497413, "steps": 8}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/文生图/造相ControlNet2.0高低噪渲染+SeedVR2亿级像素_2000807895858020353.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/造相ControlNet2.0高低噪渲染+SeedVR2亿级像素_2000807895858020353.json`

## 结构

**生成流程**：Model → Encode → Condition → Control → Sampling → Decode → Process → Output → Other

**节点**（96 个）：
- `easy cleanGpuUsed`
- `Qwen3_VQA`
- `SamplerCustomAdvanced` ★核心
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
- `FaceDetailer`
- `CFGGuider`
- `RandomNoise`
- `CFGGuider`
- `ModelSamplingAuraFlow`
- `BasicScheduler`
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
- `GetImageSize`
- `BasicScheduler`
- `AIO_Preprocessor`
- `UNETLoader` ★核心
- `Image Comparer (rgthree)`
- `TTP_Image_Assy`
- `MultiplePathsInput`
- `JWStringConcat`
- `VAELoader`
- `PrimitiveNode`
- `ModelPatchLoader`
- `LoraLoaderModelOnly` ★核心
- `VAEEncode` ★核心
- `ImageScaleToMaxDimension`
- `EmptySD3LatentImage`
- `Note`
- `PreviewImage`
- `ImageScaleBy`
- `SamplerCustomAdvanced` ★核心
- `VAEEncode` ★核心
- `CFGGuider`
- `Image Comparer (rgthree)`
- `PreviewImage`
- `SplitSigmas`
- `LoraLoaderModelOnly` ★核心
- `Model Switch (JPS)`
- `ImageLoader`
- `VAEDecode` ★核心
- `VAEDecode` ★核心
- `PreviewImage`
- `SaveImage`
- `QwenImageDiffsynthControlnet`
- `DetailDaemonSamplerNode` ★核心
- `String Literal`
- `String Literal`
- `PreviewImage`
- `easy int`
- `Latent Switch (JPS)`

## 关键参数

- `seed` = `1067213692497413`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `0.30000000000000004`

## 知识

覆盖率 **84%**（81/96）

**有卡**：`easy cleanGpuUsed`、`Qwen3_VQA`、`SamplerCustomAdvanced`、`DetailDaemonSamplerNode`、`RandomNoise`、`SamplerEulerAncestral`、`VAEEncode`、`TTP_Image_Tile_Batch`、`easy imageListToImageBatch`、`TTP_Image_Assy`、`TTP_Tile_image_size`、`easy imageBatchToImageList`、`ImageUpscaleWithModel`、`CLIPTextEncode`、`Seed (rgthree)`、`ImageScaleToTotalPixels`、`CLIPLoader`、`UltralyticsDetectorProvider`、`UpscaleModelLoader`、`ConditioningZeroOut`、`VAEDecodeTiled`、`KSampler`、`FaceDetailer`、`CFGGuider`、`ModelSamplingAuraFlow`、`BasicScheduler`、`Florence2Run`、`Florence2ModelLoader`、`ImageResize+`、`GetImageSize+`、`ImageScaleBy`、`SeedVR2VideoUpscaler`、`VAEDecode`、`SeedVR2LoadVAEModel`、`SeedVR2LoadDiTModel`、`GetImageSize`、`AIO_Preprocessor`、`UNETLoader`、`MultiplePathsInput`、`JWStringConcat`、`VAELoader`、`ModelPatchLoader`、`LoraLoaderModelOnly`、`ImageScaleToMaxDimension`、`EmptySD3LatentImage`、`SplitSigmas`、`Model Switch (JPS)`、`ImageLoader`、`SaveImage`、`QwenImageDiffsynthControlnet`、`String Literal`、`easy int`、`Latent Switch (JPS)`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、UNETLoader

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

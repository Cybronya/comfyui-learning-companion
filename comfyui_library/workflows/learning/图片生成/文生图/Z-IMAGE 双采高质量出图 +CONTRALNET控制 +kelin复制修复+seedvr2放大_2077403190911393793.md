---
key: 图片生成/文生图/Z-IMAGE 双采高质量出图 +CONTRALNET控制 +kelin复制修复+seedvr2放大_2077403190911393793.json
name: Z-IMAGE 双采高质量出图 +CONTRALNET控制 +kelin复制修复+seedvr2放大_2077403190911393793
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Z-IMAGE 双采高质量出图 +CONTRALNET控制 +kelin复制修复+seedvr2放大_2077403190911393793.json
hash: 5d6b0966245317f4
coverage: 0.810526
learned_at: 2026-10-20 00:20:13
nodes: [CLIPLoaderGGUF, PlaySound|pysssss, ConditioningZeroOut, GetNode, ImageScaleBy, easy imageSize, ImageResize+, easy imageSize, TTP_Tile_image_size, TTP_Image_Tile_Batch, ImageScaleBy, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, easy cleanGpuUsed, ImageResize+, TTP_Image_Assy, MemoryCleaner, Image Comparer (rgthree), DWPreprocessor, HEDPreprocessor, AIO_Preprocessor, PreviewImage, QwenImageDiffsynthControlnet, ModelPatchLoader, QwenImageDiffsynthControlnet, ModelPatchLoader, LayerUtility: ImageReel, LayerUtility: ImageReelComposit, Note, PreviewImage, easy seed, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, KSamplerAdvanced, ModelSamplingAuraFlow, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, INTConstant, ConditioningZeroOut, ModelSamplingAuraFlow, KSamplerAdvanced, CLIPTextEncode, CLIPTextEncode, EmptyLatentImage, UNETLoader, CLIPLoader, VAELoader, GetNode, ImageScaleToTotalPixels, LoraLoaderModelOnly, VAEEncode, ReferenceLatent, ReferenceLatent, GetImageSize, CLIPTextEncode, RandomNoise, CFGGuider, KSamplerSelect, Flux2Scheduler, SamplerCustomAdvanced, VAEDecode, SetNode, MemoryCleaner, ColorMatch, EmptyFlux2LatentImage, Note, SaveImage, PreviewImage, SaveImage, Image Comparer (rgthree), DapaoImageCompressionNode, PreviewImage, Fast Groups Bypasser (rgthree), VAEDecode, SetNode, llama_cpp_model_loader, VAELoader, LoraLoaderModelOnly, INTConstant, ShowText|pysssss, CannyEdgePreprocessor, Note, llama_cpp_instruct_adv, JjkText, Any Switch (rgthree), LayerUtility: ImageScaleByAspectRatio V2, TTResolutionSelector, 图像缩放范围孤海, PreviewImage, LoadImage]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 3, "denoise": "simple", "height": 1536, "sampler_name": 1, "scheduler": "res_multistep", "seed": "disable", "steps": "randomize", "width": 1024}
---

# 图片生成/文生图/Z-IMAGE 双采高质量出图 +CONTRALNET控制 +kelin复制修复+seedvr2放大_2077403190911393793.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Z-IMAGE 双采高质量出图 +CONTRALNET控制 +kelin复制修复+seedvr2放大_2077403190911393793.json`

## 结构

**生成流程**：Model → Encode → Condition → Latent → Control → Sampling → Decode → Process → Output → Other

**节点**（95 个）：
- `CLIPLoaderGGUF`
- `PlaySound|pysssss`
- `ConditioningZeroOut`
- `GetNode`
- `ImageScaleBy`
- `easy imageSize`
- `ImageResize+`
- `easy imageSize`
- `TTP_Tile_image_size`
- `TTP_Image_Tile_Batch`
- `ImageScaleBy`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `easy cleanGpuUsed`
- `ImageResize+`
- `TTP_Image_Assy`
- `MemoryCleaner`
- `Image Comparer (rgthree)`
- `DWPreprocessor`
- `HEDPreprocessor`
- `AIO_Preprocessor`
- `PreviewImage`
- `QwenImageDiffsynthControlnet`
- `ModelPatchLoader`
- `QwenImageDiffsynthControlnet`
- `ModelPatchLoader`
- `LayerUtility: ImageReel`
- `LayerUtility: ImageReelComposit`
- `Note`
- `PreviewImage`
- `easy seed`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `KSamplerAdvanced` ★核心
- `ModelSamplingAuraFlow`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `INTConstant`
- `ConditioningZeroOut`
- `ModelSamplingAuraFlow`
- `KSamplerAdvanced` ★核心
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `EmptyLatentImage` ★核心
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `GetNode`
- `ImageScaleToTotalPixels`
- `LoraLoaderModelOnly` ★核心
- `VAEEncode` ★核心
- `ReferenceLatent`
- `ReferenceLatent`
- `GetImageSize`
- `CLIPTextEncode` ★核心
- `RandomNoise`
- `CFGGuider`
- `KSamplerSelect` ★核心
- `Flux2Scheduler`
- `SamplerCustomAdvanced` ★核心
- `VAEDecode` ★核心
- `SetNode`
- `MemoryCleaner`
- `ColorMatch`
- `EmptyFlux2LatentImage`
- `Note`
- `SaveImage`
- `PreviewImage`
- `SaveImage`
- `Image Comparer (rgthree)`
- `DapaoImageCompressionNode`
- `PreviewImage`
- `Fast Groups Bypasser (rgthree)`
- `VAEDecode` ★核心
- `SetNode`
- `llama_cpp_model_loader`
- `VAELoader`
- `LoraLoaderModelOnly` ★核心
- `INTConstant`
- `ShowText|pysssss`
- `CannyEdgePreprocessor`
- `Note`
- `llama_cpp_instruct_adv`
- `JjkText`
- `Any Switch (rgthree)`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `TTResolutionSelector`
- `图像缩放范围孤海`
- `PreviewImage`
- `LoadImage`

## 关键参数

- `seed` = `disable`
- `steps` = `randomize`
- `cfg` = `3`
- `sampler_name` = `1`
- `scheduler` = `res_multistep`
- `denoise` = `simple`
- `width` = `1024`
- `height` = `1536`
- `batch_size` = `1`

## 知识

覆盖率 **81%**（77/95）

**有卡**：`CLIPLoaderGGUF`、`PlaySound|pysssss`、`ConditioningZeroOut`、`ImageScaleBy`、`easy imageSize`、`ImageResize+`、`TTP_Tile_image_size`、`TTP_Image_Tile_Batch`、`SeedVR2LoadDiTModel`、`SeedVR2LoadVAEModel`、`SeedVR2VideoUpscaler`、`easy cleanGpuUsed`、`TTP_Image_Assy`、`MemoryCleaner`、`DWPreprocessor`、`HEDPreprocessor`、`AIO_Preprocessor`、`QwenImageDiffsynthControlnet`、`ModelPatchLoader`、`LayerUtility: ImageReel`、`LayerUtility: ImageReelComposit`、`easy seed`、`UNETLoader`、`LoraLoaderModelOnly`、`KSamplerAdvanced`、`ModelSamplingAuraFlow`、`INTConstant`、`CLIPTextEncode`、`EmptyLatentImage`、`CLIPLoader`、`VAELoader`、`ImageScaleToTotalPixels`、`VAEEncode`、`ReferenceLatent`、`GetImageSize`、`RandomNoise`、`CFGGuider`、`KSamplerSelect`、`Flux2Scheduler`、`SamplerCustomAdvanced`、`VAEDecode`、`ColorMatch`、`EmptyFlux2LatentImage`、`SaveImage`、`DapaoImageCompressionNode`、`llama_cpp_model_loader`、`CannyEdgePreprocessor`、`llama_cpp_instruct_adv`、`LayerUtility: ImageScaleByAspectRatio V2`、`TTResolutionSelector`、`图像缩放范围孤海`、`LoadImage`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、EmptyLatentImage

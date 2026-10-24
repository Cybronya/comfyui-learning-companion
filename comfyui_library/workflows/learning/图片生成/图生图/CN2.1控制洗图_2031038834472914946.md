---
key: 图片生成/图生图/CN2.1控制洗图_2031038834472914946.json
name: CN2.1控制洗图_2031038834472914946
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/CN2.1控制洗图_2031038834472914946.json
hash: 01b9f9aeaf17579e
coverage: 0.784314
learned_at: 2026-10-23 10:51:51
nodes: [EmptyLatentImage, AIO_Preprocessor, AIO_Preprocessor, GetImageSizeAndCount, ImageScaleToTotalPixels, PreviewImage, ConditioningZeroOut, CLIPTextEncode, easy int, AIO_Preprocessor, UNETLoader, GetNode, ModelPatchLoader, SaveImage, CLIPLoader, KSampler, SeedVR2LoadVAEModel, ImageUpscaleWithModel, TTP_Image_Tile_Batch, SeedVR2LoadDiTModel, MarkdownNote, Note, ImageScaleBy, UpscaleModelLoader, SetNode, SetNode, GetNode, LoraLoaderModelOnly, easy cleanGpuUsed, ImpactSwitch, easy cleanGpuUsed, VAEDecode, LayerUtility: PurgeVRAM, LayerUtility: PurgeVRAM, DapaoImageCompressionNode, TTP_Tile_image_size, GetImageSize+, SeedVR2VideoUpscaler, TTP_Image_Assy, ImageResize+, LayerUtility: PurgeVRAM, VAELoader, SaveImage, QwenImageDiffsynthControlnet, CR Text, easy ifElse, easy showAnything, easy isNone, Fast Groups Bypasser (rgthree), RH_Captioner, LoadImage]
patterns: [text_to_image]
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1536, "sampler_name": "euler", "scheduler": "FlowMatchEulerDiscreteScheduler", "seed": 1018637165591119, "steps": 10, "width": 1024}
---

# 图片生成/图生图/CN2.1控制洗图_2031038834472914946.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/CN2.1控制洗图_2031038834472914946.json`

## 结构

**生成流程**：Model → Condition → Latent → Control → Sampling → Decode → Process → Output → Other

**节点**（51 个）：
- `EmptyLatentImage` ★核心
- `AIO_Preprocessor`
- `AIO_Preprocessor`
- `GetImageSizeAndCount`
- `ImageScaleToTotalPixels`
- `PreviewImage`
- `ConditioningZeroOut`
- `CLIPTextEncode` ★核心
- `easy int`
- `AIO_Preprocessor`
- `UNETLoader` ★核心
- `GetNode`
- `ModelPatchLoader`
- `SaveImage`
- `CLIPLoader`
- `KSampler` ★核心
- `SeedVR2LoadVAEModel`
- `ImageUpscaleWithModel`
- `TTP_Image_Tile_Batch`
- `SeedVR2LoadDiTModel`
- `MarkdownNote`
- `Note`
- `ImageScaleBy`
- `UpscaleModelLoader`
- `SetNode`
- `SetNode`
- `GetNode`
- `LoraLoaderModelOnly` ★核心
- `easy cleanGpuUsed`
- `ImpactSwitch`
- `easy cleanGpuUsed`
- `VAEDecode` ★核心
- `LayerUtility: PurgeVRAM`
- `LayerUtility: PurgeVRAM`
- `DapaoImageCompressionNode`
- `TTP_Tile_image_size`
- `GetImageSize+`
- `SeedVR2VideoUpscaler`
- `TTP_Image_Assy`
- `ImageResize+`
- `LayerUtility: PurgeVRAM`
- `VAELoader`
- `SaveImage`
- `QwenImageDiffsynthControlnet`
- `CR Text`
- `easy ifElse`
- `easy showAnything`
- `easy isNone`
- `Fast Groups Bypasser (rgthree)`
- `RH_Captioner`
- `LoadImage`

**识别到的模式**：text_to_image

## 关键参数

- `width` = `1024`
- `height` = `1536`
- `batch_size` = `1`
- `seed` = `1018637165591119`
- `steps` = `10`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `FlowMatchEulerDiscreteScheduler`
- `denoise` = `1`

## 知识

覆盖率 **78%**（40/51）

**有卡**：`EmptyLatentImage`、`AIO_Preprocessor`、`GetImageSizeAndCount`、`ImageScaleToTotalPixels`、`ConditioningZeroOut`、`CLIPTextEncode`、`easy int`、`UNETLoader`、`ModelPatchLoader`、`SaveImage`、`CLIPLoader`、`KSampler`、`SeedVR2LoadVAEModel`、`ImageUpscaleWithModel`、`TTP_Image_Tile_Batch`、`SeedVR2LoadDiTModel`、`ImageScaleBy`、`UpscaleModelLoader`、`LoraLoaderModelOnly`、`easy cleanGpuUsed`、`VAEDecode`、`LayerUtility: PurgeVRAM`、`DapaoImageCompressionNode`、`TTP_Tile_image_size`、`GetImageSize+`、`SeedVR2VideoUpscaler`、`TTP_Image_Assy`、`ImageResize+`、`VAELoader`、`QwenImageDiffsynthControlnet`、`CR Text`、`easy isNone`、`RH_Captioner`、`LoadImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、EmptyLatentImage

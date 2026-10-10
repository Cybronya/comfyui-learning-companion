---
key: 视频生成/文生视频/Z-Image-i2L (Image to LoRA)快速lora训练+联合CN测试+放大_2023308180264067074.json
name: Z-Image-i2L (Image to LoRA)快速lora训练+联合CN测试+放大_2023308180264067074
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/Z-Image-i2L (Image to LoRA)快速lora训练+联合CN测试+放大_2023308180264067074.json
hash: 4909bc07f785fc0d
coverage: 0.806452
learned_at: 2026-10-11 03:16:50
nodes: [RandomNoise, DetailDaemonSamplerNode, LoraLoaderModelOnly, ModelPatchLoader, VAELoader, SamplerEulerAncestral, UNETLoader, SamplerCustomAdvanced, EmptyLatentImage, image_scale_pixel_v2, ZImageFunControlnet, AIO_Preprocessor, BasicScheduler, SamplerEulerAncestral, VAELoader, CLIPTextEncode, easy int, SplitSigmas, CFGGuider, PreviewImage, SamplerCustomAdvanced, RandomNoise, CFGGuider, easy cleanGpuUsed, RunningHub_ZImageI2L_Loader, VAEEncode, Reroute, TTP_Image_Tile_Batch, easy imageListToImageBatch, TTP_Image_Assy, TTP_Tile_image_size, easy imageBatchToImageList, ImageUpscaleWithModel, Seed (rgthree), ImageScaleToTotalPixels, ShowText|pysssss, VAEDecodeTiled, Florence2Run, Florence2ModelLoader, SaveImage, Reroute, KSampler, VAEDecode, CLIPLoader, LoraLoader, CLIPTextEncode, UpscaleModelLoader, SaveImage, Image Comparer (rgthree), ImageBatchMulti, PreviewAny, RunningHub_ZImageI2L_Saver, RunningHub_ZImageI2L_LoraGenerator, ModelSamplingAuraFlow, PrimitiveStringMultiline, CLIPTextEncode, CLIPTextEncode, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage]
patterns: [text_to_image, image_to_image, lora]
missing: [easy cleanGpuUsed, easy imageBatchToImageList, easy imageListToImageBatch, easy int, Seed (rgthree)]
parameters: {"batch_size": 1, "cfg": 3, "denoise": 0.25000000000000006, "height": 472, "lora_name": null, "sampler_name": "euler", "scheduler": "simple", "seed": 1067213692497413, "steps": 20, "strength_clip": 1.0000000000000002, "strength_model": 1.1000000000000003, "width": 512}
discoveries: [次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识, 次要节点 `easy imageBatchToImageList` 知识库中没有该节点类型的任何知识, 次要节点 `easy imageListToImageBatch` 知识库中没有该节点类型的任何知识, 次要节点 `easy int` 知识库中没有该节点类型的任何知识, 次要节点 `Seed (rgthree)` 仅有 KSampler 的通用知识，没有该节点自己的说明]
---

# 视频生成/文生视频/Z-Image-i2L (Image to LoRA)快速lora训练+联合CN测试+放大_2023308180264067074.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/Z-Image-i2L (Image to LoRA)快速lora训练+联合CN测试+放大_2023308180264067074.json`

## 结构

**生成流程**：Model → Encode → Condition → Latent → Control → Sampling → Decode → Process → Output → Other

**节点**（62 个）：
- `RandomNoise`
- `DetailDaemonSamplerNode` ★核心
- `LoraLoaderModelOnly` ★核心
- `ModelPatchLoader`
- `VAELoader`
- `SamplerEulerAncestral` ★核心
- `UNETLoader` ★核心
- `SamplerCustomAdvanced` ★核心
- `EmptyLatentImage` ★核心
- `image_scale_pixel_v2`
- `ZImageFunControlnet`
- `AIO_Preprocessor`
- `BasicScheduler`
- `SamplerEulerAncestral` ★核心
- `VAELoader`
- `CLIPTextEncode` ★核心
- `easy int`
- `SplitSigmas`
- `CFGGuider`
- `PreviewImage`
- `SamplerCustomAdvanced` ★核心
- `RandomNoise`
- `CFGGuider`
- `easy cleanGpuUsed`
- `RunningHub_ZImageI2L_Loader`
- `VAEEncode` ★核心
- `Reroute`
- `TTP_Image_Tile_Batch`
- `easy imageListToImageBatch`
- `TTP_Image_Assy`
- `TTP_Tile_image_size`
- `easy imageBatchToImageList`
- `ImageUpscaleWithModel`
- `Seed (rgthree)`
- `ImageScaleToTotalPixels`
- `ShowText|pysssss`
- `VAEDecodeTiled` ★核心
- `Florence2Run`
- `Florence2ModelLoader`
- `SaveImage`
- `Reroute`
- `KSampler` ★核心
- `VAEDecode` ★核心
- `CLIPLoader`
- `LoraLoader` ★核心
- `CLIPTextEncode` ★核心
- `UpscaleModelLoader`
- `SaveImage`
- `Image Comparer (rgthree)`
- `ImageBatchMulti`
- `PreviewAny`
- `RunningHub_ZImageI2L_Saver`
- `RunningHub_ZImageI2L_LoraGenerator`
- `ModelSamplingAuraFlow`
- `PrimitiveStringMultiline`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`

**识别到的模式**：text_to_image、image_to_image、lora

## 关键参数

- `width` = `512`
- `height` = `472`
- `batch_size` = `1`
- `seed` = `1067213692497413`
- `steps` = `20`
- `cfg` = `3`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `0.25000000000000006`
- `lora_name` = `None`
- `strength_model` = `1.1000000000000003`
- `strength_clip` = `1.0000000000000002`

## 知识

覆盖率 **81%**（50/62）

**有卡**：`RandomNoise`、`DetailDaemonSamplerNode`、`LoraLoaderModelOnly`、`ModelPatchLoader`、`VAELoader`、`SamplerEulerAncestral`、`UNETLoader`、`SamplerCustomAdvanced`、`EmptyLatentImage`、`image_scale_pixel_v2`、`ZImageFunControlnet`、`AIO_Preprocessor`、`BasicScheduler`、`CLIPTextEncode`、`SplitSigmas`、`CFGGuider`、`RunningHub_ZImageI2L_Loader`、`VAEEncode`、`TTP_Image_Tile_Batch`、`TTP_Image_Assy`、`TTP_Tile_image_size`、`ImageUpscaleWithModel`、`ImageScaleToTotalPixels`、`VAEDecodeTiled`、`Florence2Run`、`Florence2ModelLoader`、`SaveImage`、`KSampler`、`VAEDecode`、`CLIPLoader`、`LoraLoader`、`UpscaleModelLoader`、`ImageBatchMulti`、`RunningHub_ZImageI2L_Saver`、`RunningHub_ZImageI2L_LoraGenerator`、`ModelSamplingAuraFlow`、`LoadImage`

**缺卡**（5）：`easy cleanGpuUsed`、`easy imageBatchToImageList`、`easy imageListToImageBatch`、`easy int`、`Seed (rgthree)`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage、LoadImage

## 学习发现

- 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识
- 次要节点 `easy imageBatchToImageList` 知识库中没有该节点类型的任何知识
- 次要节点 `easy imageListToImageBatch` 知识库中没有该节点类型的任何知识
- 次要节点 `easy int` 知识库中没有该节点类型的任何知识
- 次要节点 `Seed (rgthree)` 仅有 KSampler 的通用知识，没有该节点自己的说明

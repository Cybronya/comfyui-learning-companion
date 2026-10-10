---
key: 图片生成/图生图/Qwen Image 2.1最强换头工作流，超高一致性面部替换图生图方案_2106077135336198145.json
name: Qwen Image 2.1最强换头工作流，超高一致性面部替换图生图方案_2106077135336198145
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen Image 2.1最强换头工作流，超高一致性面部替换图生图方案_2106077135336198145.json
hash: d6e74bd950495c4c
coverage: 0.597938
learned_at: 2026-10-10 20:48:08
nodes: [ModelAttentionBackend, QwenImage21Cache, KSamplerSelect, RandomNoise, CFGGuider, BasicScheduler, Seed (rgthree), FaceAnalysisModels, SamplerCustomAdvanced, easy cleanGpuUsed, VAEDecode, PreviewImage, VOSR2ModelLoader, VOSR2Upscale, Images to RGB, easy cleanGpuUsed, easy cleanGpuUsed, PreviewImage, easy cleanGpuUsed, Reroute, Reroute, ImageStitch, ImageStitch, Reroute, Reroute, Reroute, Reroute, Reroute, ImageScaleToMaxDimension, Reroute, SeedVR2LoadVAEModel, PreviewImage, SeedVR2LoadDiTModel, SeedVR2VideoUpscaler, Reroute, easy cleanGpuUsed, PreviewImage, Reroute, PreviewImage, Reroute, Reroute, LoadImage, PreviewImage, UNETLoader, CLIPLoader, Reroute, SaveImage, Image Comparer (rgthree), FaceEmbedDistance, Reroute, Reroute, Image Comparer (rgthree), Reroute, LoadImage, ComfyMathExpression, ComfyMathExpression, easy float, easy cleanGpuUsed, ResizeImageMaskNode, ResizeImageMaskNode, ImageResizeKJv2, TextEncodeQwenImage21, GetImageSizeAndCount, VAELoader, PreviewImage, GetImageSizeAndCount, AIO_Preprocessor, PreviewImage, 孤海注释, 孤海注释, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, KSampler, EmptyLatentImage, JjkText, CLIPTextEncode, CLIPTextEncode, solarL_SaveImagesToZip, VAEDecode, CLIPLoader, VAELoader, Note]
patterns: [text_to_image]
missing: [Images to RGB, easy cleanGpuUsed, easy cleanGpuUsed, easy cleanGpuUsed, easy cleanGpuUsed, easy cleanGpuUsed, easy cleanGpuUsed, easy float, Seed (rgthree)]
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [次要节点 `Images to RGB` 知识库中没有该节点类型的任何知识, 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识, 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识, 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识, 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识, 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识, 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识, 次要节点 `easy float` 知识库中没有该节点类型的任何知识, 次要节点 `Seed (rgthree)` 仅有 KSampler 的通用知识，没有该节点自己的说明, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/Qwen Image 2.1最强换头工作流，超高一致性面部替换图生图方案_2106077135336198145.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen Image 2.1最强换头工作流，超高一致性面部替换图生图方案_2106077135336198145.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（97 个）：
- `ModelAttentionBackend`
- `QwenImage21Cache`
- `KSamplerSelect` ★核心
- `RandomNoise`
- `CFGGuider`
- `BasicScheduler`
- `Seed (rgthree)`
- `FaceAnalysisModels`
- `SamplerCustomAdvanced` ★核心
- `easy cleanGpuUsed`
- `VAEDecode` ★核心
- `PreviewImage`
- `VOSR2ModelLoader`
- `VOSR2Upscale`
- `Images to RGB`
- `easy cleanGpuUsed`
- `easy cleanGpuUsed`
- `PreviewImage`
- `easy cleanGpuUsed`
- `Reroute`
- `Reroute`
- `ImageStitch`
- `ImageStitch`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `ImageScaleToMaxDimension`
- `Reroute`
- `SeedVR2LoadVAEModel`
- `PreviewImage`
- `SeedVR2LoadDiTModel`
- `SeedVR2VideoUpscaler`
- `Reroute`
- `easy cleanGpuUsed`
- `PreviewImage`
- `Reroute`
- `PreviewImage`
- `Reroute`
- `Reroute`
- `LoadImage`
- `PreviewImage`
- `UNETLoader` ★核心
- `CLIPLoader`
- `Reroute`
- `SaveImage`
- `Image Comparer (rgthree)`
- `FaceEmbedDistance`
- `Reroute`
- `Reroute`
- `Image Comparer (rgthree)`
- `Reroute`
- `LoadImage`
- `ComfyMathExpression`
- `ComfyMathExpression`
- `easy float`
- `easy cleanGpuUsed`
- `ResizeImageMaskNode`
- `ResizeImageMaskNode`
- `ImageResizeKJv2`
- `TextEncodeQwenImage21`
- `GetImageSizeAndCount`
- `VAELoader`
- `PreviewImage`
- `GetImageSizeAndCount`
- `AIO_Preprocessor`
- `PreviewImage`
- `孤海注释`
- `孤海注释`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `KSampler` ★核心
- `EmptyLatentImage` ★核心
- `JjkText`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `solarL_SaveImagesToZip`
- `VAEDecode` ★核心
- `CLIPLoader`
- `VAELoader`
- `Note`

**识别到的模式**：text_to_image

## 关键参数

- `seed` = `598626327129635`
- `steps` = `4`
- `cfg` = `4.5`
- `sampler_name` = `er_sde`
- `scheduler` = `beta`
- `denoise` = `1`
- `width` = `80`
- `height` = `80`
- `batch_size` = `1`

## 知识

覆盖率 **60%**（58/97）

**有卡**：`ModelAttentionBackend`、`QwenImage21Cache`、`KSamplerSelect`、`RandomNoise`、`CFGGuider`、`BasicScheduler`、`FaceAnalysisModels`、`SamplerCustomAdvanced`、`VAEDecode`、`VOSR2ModelLoader`、`VOSR2Upscale`、`ImageStitch`、`ImageScaleToMaxDimension`、`SeedVR2LoadVAEModel`、`SeedVR2LoadDiTModel`、`SeedVR2VideoUpscaler`、`LoadImage`、`UNETLoader`、`CLIPLoader`、`SaveImage`、`FaceEmbedDistance`、`ComfyMathExpression`、`ResizeImageMaskNode`、`ImageResizeKJv2`、`TextEncodeQwenImage21`、`GetImageSizeAndCount`、`VAELoader`、`AIO_Preprocessor`、`LoraLoaderModelOnly`、`KSampler`、`EmptyLatentImage`、`CLIPTextEncode`、`solarL_SaveImagesToZip`

**缺卡**（9）：`Images to RGB`、`easy cleanGpuUsed`、`easy cleanGpuUsed`、`easy cleanGpuUsed`、`easy cleanGpuUsed`、`easy cleanGpuUsed`、`easy cleanGpuUsed`、`easy float`、`Seed (rgthree)`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- 次要节点 `Images to RGB` 知识库中没有该节点类型的任何知识
- 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识
- 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识
- 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识
- 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识
- 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识
- 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识
- 次要节点 `easy float` 知识库中没有该节点类型的任何知识
- 次要节点 `Seed (rgthree)` 仅有 KSampler 的通用知识，没有该节点自己的说明
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

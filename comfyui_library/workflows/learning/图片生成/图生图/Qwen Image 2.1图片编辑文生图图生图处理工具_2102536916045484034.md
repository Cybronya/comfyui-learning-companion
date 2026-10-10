---
key: 图片生成/图生图/Qwen Image 2.1图片编辑文生图图生图处理工具_2102536916045484034.json
name: Qwen Image 2.1图片编辑文生图图生图处理工具_2102536916045484034
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen Image 2.1图片编辑文生图图生图处理工具_2102536916045484034.json
hash: 4e40cfb3d2279f33
coverage: 0.639175
learned_at: 2026-10-10 20:48:06
nodes: [QwenImage21Cache, VAEDecode, ResolutionSelector, TextEncodeQwenImage21, ModelAttentionBackend, SamplerCustomAdvanced, RandomNoise, CFGGuider, KSamplerSelect, BasicScheduler, easy cleanGpuUsed, PrimitiveStringMultiline, PrimitiveBoolean, Seed (rgthree), GetImageSizeAndCount, ResizeImageMaskNode, VOSR2ModelLoader, VOSR2Upscale, Images to RGB, Reroute, Reroute, Reroute, Reroute, Reroute, easy cleanGpuUsed, ResizeImageMaskNode, Reroute, Reroute, StringConcatenate, SeedVR2LoadVAEModel, PreviewImage, SeedVR2LoadDiTModel, easy cleanGpuUsed, PrimitiveStringMultiline, PrimitiveStringMultiline, PrimitiveStringMultiline, ComfySwitchNode, StringConcatenate, TextGenerate, TextGenerate, UNETLoader, CLIPLoader, VAELoader, Reroute, Reroute, ShowText|pysssss, Image Comparer (rgthree), Reroute, Reroute, Image Comparer (rgthree), PreviewImage, SaveImage, ComfyOrNode, ComfySwitchNode, EmptyLatentImage, LoadImage, ImageResizeKJv2, ImageScaleToMaxDimension, easy cleanGpuUsed, SeedVR2VideoUpscaler, Reroute, easy cleanGpuUsed, INTConstant, JsonExtractString, PrimitiveStringMultiline, PrimitiveBoolean, CLIPLoader, CLIPLoader, 孤海注释, 孤海注释, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, KSampler, EmptyLatentImage, JjkText, CLIPTextEncode, CLIPTextEncode, solarL_SaveImagesToZip, VAEDecode, CLIPLoader, VAELoader, Note]
patterns: [text_to_image]
missing: [Images to RGB, easy cleanGpuUsed, easy cleanGpuUsed, easy cleanGpuUsed, easy cleanGpuUsed, easy cleanGpuUsed, Seed (rgthree)]
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [次要节点 `Images to RGB` 知识库中没有该节点类型的任何知识, 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识, 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识, 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识, 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识, 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识, 次要节点 `Seed (rgthree)` 仅有 KSampler 的通用知识，没有该节点自己的说明, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/Qwen Image 2.1图片编辑文生图图生图处理工具_2102536916045484034.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen Image 2.1图片编辑文生图图生图处理工具_2102536916045484034.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（97 个）：
- `QwenImage21Cache`
- `VAEDecode` ★核心
- `ResolutionSelector`
- `TextEncodeQwenImage21`
- `ModelAttentionBackend`
- `SamplerCustomAdvanced` ★核心
- `RandomNoise`
- `CFGGuider`
- `KSamplerSelect` ★核心
- `BasicScheduler`
- `easy cleanGpuUsed`
- `PrimitiveStringMultiline`
- `PrimitiveBoolean`
- `Seed (rgthree)`
- `GetImageSizeAndCount`
- `ResizeImageMaskNode`
- `VOSR2ModelLoader`
- `VOSR2Upscale`
- `Images to RGB`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `easy cleanGpuUsed`
- `ResizeImageMaskNode`
- `Reroute`
- `Reroute`
- `StringConcatenate`
- `SeedVR2LoadVAEModel`
- `PreviewImage`
- `SeedVR2LoadDiTModel`
- `easy cleanGpuUsed`
- `PrimitiveStringMultiline`
- `PrimitiveStringMultiline`
- `PrimitiveStringMultiline`
- `ComfySwitchNode`
- `StringConcatenate`
- `TextGenerate`
- `TextGenerate`
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `Reroute`
- `Reroute`
- `ShowText|pysssss`
- `Image Comparer (rgthree)`
- `Reroute`
- `Reroute`
- `Image Comparer (rgthree)`
- `PreviewImage`
- `SaveImage`
- `ComfyOrNode`
- `ComfySwitchNode`
- `EmptyLatentImage` ★核心
- `LoadImage`
- `ImageResizeKJv2`
- `ImageScaleToMaxDimension`
- `easy cleanGpuUsed`
- `SeedVR2VideoUpscaler`
- `Reroute`
- `easy cleanGpuUsed`
- `INTConstant`
- `JsonExtractString`
- `PrimitiveStringMultiline`
- `PrimitiveBoolean`
- `CLIPLoader`
- `CLIPLoader`
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

- `width` = `80`
- `height` = `80`
- `batch_size` = `1`
- `seed` = `598626327129635`
- `steps` = `4`
- `cfg` = `4.5`
- `sampler_name` = `er_sde`
- `scheduler` = `beta`
- `denoise` = `1`

## 知识

覆盖率 **64%**（62/97）

**有卡**：`QwenImage21Cache`、`VAEDecode`、`ResolutionSelector`、`TextEncodeQwenImage21`、`ModelAttentionBackend`、`SamplerCustomAdvanced`、`RandomNoise`、`CFGGuider`、`KSamplerSelect`、`BasicScheduler`、`PrimitiveBoolean`、`GetImageSizeAndCount`、`ResizeImageMaskNode`、`VOSR2ModelLoader`、`VOSR2Upscale`、`StringConcatenate`、`SeedVR2LoadVAEModel`、`SeedVR2LoadDiTModel`、`TextGenerate`、`UNETLoader`、`CLIPLoader`、`VAELoader`、`SaveImage`、`ComfyOrNode`、`EmptyLatentImage`、`LoadImage`、`ImageResizeKJv2`、`ImageScaleToMaxDimension`、`SeedVR2VideoUpscaler`、`INTConstant`、`JsonExtractString`、`LoraLoaderModelOnly`、`KSampler`、`CLIPTextEncode`、`solarL_SaveImagesToZip`

**缺卡**（7）：`Images to RGB`、`easy cleanGpuUsed`、`easy cleanGpuUsed`、`easy cleanGpuUsed`、`easy cleanGpuUsed`、`easy cleanGpuUsed`、`Seed (rgthree)`

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
- 次要节点 `Seed (rgthree)` 仅有 KSampler 的通用知识，没有该节点自己的说明
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

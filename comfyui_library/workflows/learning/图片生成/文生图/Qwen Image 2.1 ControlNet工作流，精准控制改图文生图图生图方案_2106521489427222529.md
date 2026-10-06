---
key: 图片生成/文生图/Qwen Image 2.1 ControlNet工作流，精准控制改图文生图图生图方案_2106521489427222529.json
name: Qwen Image 2.1 ControlNet工作流，精准控制改图文生图图生图方案_2106521489427222529
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Qwen Image 2.1 ControlNet工作流，精准控制改图文生图图生图方案_2106521489427222529.json
hash: 9bf3a3e1258312ad
coverage: 0.776119
learned_at: 2026-10-06 22:36:28
nodes: [QwenImage21Cache, easy seed, VAEDecode, BatchImagesNode, StringConstantMultiline, StringReplace, ResolutionSelector, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: ImageScaleByAspectRatio V2, FluxKontextImageScale, LayerUtility: ImageScaleByAspectRatio V2, VAELoader, EmptyLatentImage, ComfySwitchNode, SaveImage, KSampler, TextGenerate, StringFunction|pysssss, PreviewAny, PreviewAny, StringConstantMultiline, CLIPLoader, CLIPLoader, UNETLoader, TextEncodeQwenImage21, LoadImage, LoadImage, LoadImage, LoadImage, ZImageFunControlnet, Image Comparer (rgthree), AIO_Preprocessor, LoadImage, LoadImage, ModelPatchLoader, PreviewImage, LoadImage, 孤海注释, 孤海注释, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, KSampler, EmptyLatentImage, JjkText, CLIPTextEncode, CLIPTextEncode, solarL_SaveImagesToZip, VAEDecode, CLIPLoader, VAELoader, Note]
patterns: [text_to_image]
missing: [LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: ImageScaleByAspectRatio V2, StringFunction|pysssss, easy seed]
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识, 次要节点 `StringFunction|pysssss` 知识库中没有该节点类型的任何知识, 次要节点 `easy seed` 仅有 KSampler 的通用知识，没有该节点自己的说明, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/文生图/Qwen Image 2.1 ControlNet工作流，精准控制改图文生图图生图方案_2106521489427222529.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Qwen Image 2.1 ControlNet工作流，精准控制改图文生图图生图方案_2106521489427222529.json`

## 结构

**生成流程**：Model → Condition → Latent → Control → Sampling → Decode → Process → Output → Other

**节点**（67 个）：
- `QwenImage21Cache`
- `easy seed`
- `VAEDecode` ★核心
- `BatchImagesNode`
- `StringConstantMultiline`
- `StringReplace`
- `ResolutionSelector`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `FluxKontextImageScale`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `VAELoader`
- `EmptyLatentImage` ★核心
- `ComfySwitchNode`
- `SaveImage`
- `KSampler` ★核心
- `TextGenerate`
- `StringFunction|pysssss`
- `PreviewAny`
- `PreviewAny`
- `StringConstantMultiline`
- `CLIPLoader`
- `CLIPLoader`
- `UNETLoader` ★核心
- `TextEncodeQwenImage21`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `ZImageFunControlnet`
- `Image Comparer (rgthree)`
- `AIO_Preprocessor`
- `LoadImage`
- `LoadImage`
- `ModelPatchLoader`
- `PreviewImage`
- `LoadImage`
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

覆盖率 **78%**（52/67）

**有卡**：`QwenImage21Cache`、`VAEDecode`、`BatchImagesNode`、`StringConstantMultiline`、`StringReplace`、`ResolutionSelector`、`FluxKontextImageScale`、`VAELoader`、`EmptyLatentImage`、`SaveImage`、`KSampler`、`TextGenerate`、`CLIPLoader`、`UNETLoader`、`TextEncodeQwenImage21`、`LoadImage`、`ZImageFunControlnet`、`AIO_Preprocessor`、`ModelPatchLoader`、`LoraLoaderModelOnly`、`CLIPTextEncode`、`solarL_SaveImagesToZip`

**缺卡**（6）：`LayerUtility: ImageScaleByAspectRatio V2`、`LayerUtility: ImageScaleByAspectRatio V2`、`LayerUtility: ImageScaleByAspectRatio V2`、`LayerUtility: ImageScaleByAspectRatio V2`、`StringFunction|pysssss`、`easy seed`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPTextEncode、CLIPLoader

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- 次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识
- 次要节点 `StringFunction|pysssss` 知识库中没有该节点类型的任何知识
- 次要节点 `easy seed` 仅有 KSampler 的通用知识，没有该节点自己的说明
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

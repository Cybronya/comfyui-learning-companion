---
key: 怪獸整理Qwen Image 2.1合集｜文生图换装修图全收录_2103070200995340289.json
name: 怪獸整理Qwen Image 2.1合集｜文生图换装修图全收录_2103070200995340289
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/怪獸整理Qwen Image 2.1合集｜文生图换装修图全收录_2103070200995340289.json
hash: 7b6ccc65fd2b9432
coverage: 0.734513
learned_at: 2026-10-10 20:59:44
nodes: [VAEDecode, easy showAnything, SaveImage, JjkText, PreviewImage, VAEDecode, SaveImage, ComfySwitchNode, GetNode, ResolutionSelector, UNETLoader, SetNode, SetNode, CLIPLoader, CLIPLoader, VAELoader, CLIPLoader, Anything Everywhere3, AIO_Preprocessor, KSampler, LoadImage, LayerMask: BiRefNetUltraV2, BlockifyMask, DrawMaskOnImage, LayerUtility: ImageBlend, DepthAnythingV2Preprocessor, LayerUtility: ImageRemoveAlpha, BatchImagesNode, ImageBlend, LoadImage, QwenImage21Cache, GetNode, PreviewAny, EmptyLatentImage, LayerMask: LoadBiRefNetModelV2, ImageResizeKJ, ImageScaleToTotalPixels, AIO_Preprocessor, LayerMask: BiRefNetUltraV2, Image Comparer (rgthree), LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: ImageScaleByAspectRatio V2, KSampler, GetNode, EmptyLatentImage, ComfySwitchNode, TextEncodeQwenImage21, ShowText|pysssss, LoadImage, ResolutionSelector, EmptyLatentImage, TextEncodeQwenImage21, TextGenerateLTX2Prompt, FastGroupsBypassSwitch, TextEncodeQwenImage21, KSampler, TextGenerateLTX2Prompt, TextGenerateLTX2Prompt, ResolutionSelector, CR Text, SaveImage, VAEDecode, Fast Groups Bypasser (rgthree), Fast Groups Bypasser (rgthree), LoadImage, LoadImage, LoadImage, PreviewImage, LoadImage, CR Prompt Text, 孤海注释, 孤海注释, UNETLoader, CLIPLoader, CLIPTextEncode, VAELoader, EmptyLatentImage, KSampler, VAEDecode, solarL_SaveImagesToZip, JjkText, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, CLIPTextEncode, Note]
patterns: [text_to_image]
missing: [CR Text, LayerMask: BiRefNetUltraV2, LayerMask: BiRefNetUltraV2, LayerMask: LoadBiRefNetModelV2, LayerUtility: ImageBlend, LayerUtility: ImageRemoveAlpha, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: ImageScaleByAspectRatio V2, CR Prompt Text]
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [次要节点 `CR Text` 知识库中没有该节点类型的任何知识, 次要节点 `LayerMask: BiRefNetUltraV2` 知识库中没有该节点类型的任何知识, 次要节点 `LayerMask: BiRefNetUltraV2` 知识库中没有该节点类型的任何知识, 次要节点 `LayerMask: LoadBiRefNetModelV2` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: ImageBlend` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: ImageRemoveAlpha` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识, 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 怪獸整理Qwen Image 2.1合集｜文生图换装修图全收录_2103070200995340289.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/怪獸整理Qwen Image 2.1合集｜文生图换装修图全收录_2103070200995340289.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（113 个）：
- `VAEDecode` ★核心
- `easy showAnything`
- `SaveImage`
- `JjkText`
- `PreviewImage`
- `VAEDecode` ★核心
- `SaveImage`
- `ComfySwitchNode`
- `GetNode`
- `ResolutionSelector`
- `UNETLoader` ★核心
- `SetNode`
- `SetNode`
- `CLIPLoader`
- `CLIPLoader`
- `VAELoader`
- `CLIPLoader`
- `Anything Everywhere3`
- `AIO_Preprocessor`
- `KSampler` ★核心
- `LoadImage`
- `LayerMask: BiRefNetUltraV2`
- `BlockifyMask`
- `DrawMaskOnImage`
- `LayerUtility: ImageBlend`
- `DepthAnythingV2Preprocessor`
- `LayerUtility: ImageRemoveAlpha`
- `BatchImagesNode`
- `ImageBlend`
- `LoadImage`
- `QwenImage21Cache`
- `GetNode`
- `PreviewAny`
- `EmptyLatentImage` ★核心
- `LayerMask: LoadBiRefNetModelV2`
- `ImageResizeKJ`
- `ImageScaleToTotalPixels`
- `AIO_Preprocessor`
- `LayerMask: BiRefNetUltraV2`
- `Image Comparer (rgthree)`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `KSampler` ★核心
- `GetNode`
- `EmptyLatentImage` ★核心
- `ComfySwitchNode`
- `TextEncodeQwenImage21`
- `ShowText|pysssss`
- `LoadImage`
- `ResolutionSelector`
- `EmptyLatentImage` ★核心
- `TextEncodeQwenImage21`
- `TextGenerateLTX2Prompt`
- `FastGroupsBypassSwitch`
- `TextEncodeQwenImage21`
- `KSampler` ★核心
- `TextGenerateLTX2Prompt`
- `TextGenerateLTX2Prompt`
- `ResolutionSelector`
- `CR Text`
- `SaveImage`
- `VAEDecode` ★核心
- `Fast Groups Bypasser (rgthree)`
- `Fast Groups Bypasser (rgthree)`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `PreviewImage`
- `LoadImage`
- `CR Prompt Text`
- `孤海注释`
- `孤海注释`
- `UNETLoader` ★核心
- `CLIPLoader`
- `CLIPTextEncode` ★核心
- `VAELoader`
- `EmptyLatentImage` ★核心
- `KSampler` ★核心
- `VAEDecode` ★核心
- `solarL_SaveImagesToZip`
- `JjkText`
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
- `CLIPTextEncode` ★核心
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

覆盖率 **73%**（83/113）

**有卡**：`VAEDecode`、`SaveImage`、`ResolutionSelector`、`UNETLoader`、`CLIPLoader`、`VAELoader`、`AIO_Preprocessor`、`KSampler`、`LoadImage`、`BlockifyMask`、`DrawMaskOnImage`、`DepthAnythingV2Preprocessor`、`BatchImagesNode`、`ImageBlend`、`QwenImage21Cache`、`EmptyLatentImage`、`ImageResizeKJ`、`ImageScaleToTotalPixels`、`TextEncodeQwenImage21`、`TextGenerateLTX2Prompt`、`FastGroupsBypassSwitch`、`CLIPTextEncode`、`solarL_SaveImagesToZip`、`LoraLoaderModelOnly`

**缺卡**（9）：`CR Text`、`LayerMask: BiRefNetUltraV2`、`LayerMask: BiRefNetUltraV2`、`LayerMask: LoadBiRefNetModelV2`、`LayerUtility: ImageBlend`、`LayerUtility: ImageRemoveAlpha`、`LayerUtility: ImageScaleByAspectRatio V2`、`LayerUtility: ImageScaleByAspectRatio V2`、`CR Prompt Text`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- 次要节点 `CR Text` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerMask: BiRefNetUltraV2` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerMask: BiRefNetUltraV2` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerMask: LoadBiRefNetModelV2` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: ImageBlend` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: ImageRemoveAlpha` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识
- 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

---
key: 图片生成/文生图/怪獸出品Qwen Image 2.1工作流合集｜文生图图生图双模式打包_2103663285953458177.json
name: 怪獸出品Qwen Image 2.1工作流合集｜文生图图生图双模式打包_2103663285953458177
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/怪獸出品Qwen Image 2.1工作流合集｜文生图图生图双模式打包_2103663285953458177.json
hash: 32b355063ca5fd0e
coverage: 0.740741
learned_at: 2026-10-10 20:59:44
nodes: [VAEDecode, easy showAnything, SaveImage, JjkText, PreviewImage, VAEDecode, SaveImage, ComfySwitchNode, GetNode, ResolutionSelector, UNETLoader, SetNode, SetNode, CLIPLoader, VAELoader, CLIPLoader, Anything Everywhere3, AIO_Preprocessor, KSampler, LoadImage, BatchImagesNode, QwenImage21Cache, GetNode, PreviewAny, EmptyLatentImage, Image Comparer (rgthree), KSampler, GetNode, EmptyLatentImage, ComfySwitchNode, TextEncodeQwenImage21, ShowText|pysssss, LoadImage, ResolutionSelector, EmptyLatentImage, TextEncodeQwenImage21, TextGenerateLTX2Prompt, FastGroupsBypassSwitch, KSampler, TextGenerateLTX2Prompt, ResolutionSelector, CR Text, SaveImage, VAEDecode, Fast Groups Bypasser (rgthree), Fast Groups Bypasser (rgthree), LoadImage, LoadImage, LoadImage, easy showAnything, easy sleep, PreviewImage, CLIPLoader, TextEncodeQwenImage21, TextGenerateLTX2Prompt, PreviewAny, LoadImage, LoadImage, CR Prompt Text, CR Text Concatenate, Qwen3VL_Advanced, DWPreprocessor, DepthAnythingPreprocessor, ImageBlend, PreviewImage, 孤海注释, 孤海注释, UNETLoader, CLIPLoader, CLIPTextEncode, VAELoader, EmptyLatentImage, KSampler, VAEDecode, solarL_SaveImagesToZip, JjkText, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, CLIPTextEncode, Note]
patterns: [text_to_image]
missing: [CR Text, CR Text Concatenate, easy sleep, CR Prompt Text]
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [次要节点 `CR Text` 知识库中没有该节点类型的任何知识, 次要节点 `CR Text Concatenate` 知识库中没有该节点类型的任何知识, 次要节点 `easy sleep` 知识库中没有该节点类型的任何知识, 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/文生图/怪獸出品Qwen Image 2.1工作流合集｜文生图图生图双模式打包_2103663285953458177.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/怪獸出品Qwen Image 2.1工作流合集｜文生图图生图双模式打包_2103663285953458177.json`

## 结构

**节点**（108 个）：
- `VAEDecode`
- `easy showAnything`
- `SaveImage`
- `JjkText`
- `PreviewImage`
- `VAEDecode`
- `SaveImage`
- `ComfySwitchNode`
- `GetNode`
- `ResolutionSelector`
- `UNETLoader`
- `SetNode`
- `SetNode`
- `CLIPLoader`
- `VAELoader`
- `CLIPLoader`
- `Anything Everywhere3`
- `AIO_Preprocessor`
- `KSampler`
- `LoadImage`
- `BatchImagesNode`
- `QwenImage21Cache`
- `GetNode`
- `PreviewAny`
- `EmptyLatentImage`
- `Image Comparer (rgthree)`
- `KSampler`
- `GetNode`
- `EmptyLatentImage`
- `ComfySwitchNode`
- `TextEncodeQwenImage21`
- `ShowText|pysssss`
- `LoadImage`
- `ResolutionSelector`
- `EmptyLatentImage`
- `TextEncodeQwenImage21`
- `TextGenerateLTX2Prompt`
- `FastGroupsBypassSwitch`
- `KSampler`
- `TextGenerateLTX2Prompt`
- `ResolutionSelector`
- `CR Text`
- `SaveImage`
- `VAEDecode`
- `Fast Groups Bypasser (rgthree)`
- `Fast Groups Bypasser (rgthree)`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `easy showAnything`
- `easy sleep`
- `PreviewImage`
- `CLIPLoader`
- `TextEncodeQwenImage21`
- `TextGenerateLTX2Prompt`
- `PreviewAny`
- `LoadImage`
- `LoadImage`
- `CR Prompt Text`
- `CR Text Concatenate`
- `Qwen3VL_Advanced`
- `DWPreprocessor`
- `DepthAnythingPreprocessor`
- `ImageBlend`
- `PreviewImage`
- `孤海注释`
- `孤海注释`
- `UNETLoader`
- `CLIPLoader`
- `CLIPTextEncode`
- `VAELoader`
- `EmptyLatentImage`
- `KSampler`
- `VAEDecode`
- `solarL_SaveImagesToZip`
- `JjkText`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `CLIPTextEncode`
- `Note`

**识别到的模式**：text_to_image

## 关键参数

- `batch_size` = `1`
- `cfg` = `4.5`
- `denoise` = `1`
- `height` = `80`
- `sampler_name` = `er_sde`
- `scheduler` = `beta`
- `seed` = `598626327129635`
- `steps` = `4`
- `width` = `80`

## 知识

覆盖率 **74%**（80/108）

**有卡**：`VAEDecode`、`easy showAnything`、`SaveImage`、`JjkText`、`PreviewImage`、`ComfySwitchNode`、`GetNode`、`ResolutionSelector`、`UNETLoader`、`SetNode`、`CLIPLoader`、`VAELoader`、`Anything Everywhere3`、`AIO_Preprocessor`、`KSampler`、`LoadImage`、`BatchImagesNode`、`QwenImage21Cache`、`PreviewAny`、`EmptyLatentImage`、`Image Comparer (rgthree)`、`TextEncodeQwenImage21`、`ShowText|pysssss`、`TextGenerateLTX2Prompt`、`FastGroupsBypassSwitch`、`CR Text`、`Fast Groups Bypasser (rgthree)`、`easy sleep`、`CR Prompt Text`、`CR Text Concatenate`、`Qwen3VL_Advanced`、`DWPreprocessor`、`DepthAnythingPreprocessor`、`ImageBlend`、`孤海注释`、`CLIPTextEncode`、`solarL_SaveImagesToZip`、`LoraLoaderModelOnly`

**缺卡**（4）：`CR Text`、`CR Text Concatenate`、`easy sleep`、`CR Prompt Text`

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- 次要节点 `CR Text` 知识库中没有该节点类型的任何知识
- 次要节点 `CR Text Concatenate` 知识库中没有该节点类型的任何知识
- 次要节点 `easy sleep` 知识库中没有该节点类型的任何知识
- 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

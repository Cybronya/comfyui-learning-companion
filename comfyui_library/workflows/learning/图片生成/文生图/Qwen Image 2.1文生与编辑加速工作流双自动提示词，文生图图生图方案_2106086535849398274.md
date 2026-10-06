---
key: 图片生成/文生图/Qwen Image 2.1文生与编辑加速工作流双自动提示词，文生图图生图方案_2106086535849398274.json
name: Qwen Image 2.1文生与编辑加速工作流双自动提示词，文生图图生图方案_2106086535849398274
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Qwen Image 2.1文生与编辑加速工作流双自动提示词，文生图图生图方案_2106086535849398274.json
hash: 83583eb336dcaf69
coverage: 0.300578
learned_at: 2026-10-06 21:48:37
nodes: [CLIPLoader, VAELoader, VAEDecode, UNETLoader, EmptyLatentImage, KSampler, TextEncodeQwenImage21, VAEDecode, LoadImage, LoadImage, LoadImage, LoadImage, KSampler, SaveImage, QwenImage21Cache, CLIPLoader, StringConcatenate, TextGenerate, JsonExtractString, CLIPLoader, TextGenerate, JsonExtractString, BatchImagesNode, StringConcatenate, StringConcatenate, Any Switch (rgthree), PreviewAny, PreviewAny, llama_cpp_parameters, llama_cpp_instruct_adv, llama_cpp_instruct_adv, BatchImagesNode, SetNode, GetNode, SetNode, GetNode, GetNode, GetNode, SetNode, GetNode, GetNode, SetNode, GetNode, SetNode, GetNode, SetNode, GetNode, SetNode, GetNode, SetNode, GetNode, SetNode, GetNode, SetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, SetNode, GetNode, GetNode, SetNode, GetNode, SetNode, GetNode, GetNode, GetNode, SetNode, GetNode, SetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, LoadImage, SetNode, GetNode, GetNode, GetNode, LoadImage, SetNode, GetNode, GetNode, GetNode, SetNode, GetNode, GetNode, GetNode, LoadImage, SetNode, GetNode, GetNode, GetNode, ImageScaleToMaxDimension, ImageScaleToMaxDimension, ImageScaleToMaxDimension, ImageScaleToMaxDimension, ImageScaleToMaxDimension, ImageScaleToMaxDimension, ImageScaleToMaxDimension, ImageScaleToMaxDimension, ImageScaleToMaxDimension, ImageScaleToMaxDimension, SetNode, GetNode, Image Comparer (rgthree), SetNode, GetNode, ComfySwitchNode, GetNode, ComfySwitchNode, GetNode, KSampler, ComfySwitchNode, SetNode, GetNode, SetNode, GetNode, GetNode, ComfySwitchNode, LoadImage, LoadImage, ResolutionSelector, PrimitiveBoolean, StringConcatenate, SetNode, TextEncodeQwenImage21, SaveImage, CR Prompt Text, LoadImage, PrimitiveBoolean, KSampler, LoraLoaderBypassModelOnly, Any Switch (rgthree), llama_cpp_model_loader, 孤海注释, 孤海注释, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, KSampler, EmptyLatentImage, JjkText, CLIPTextEncode, CLIPTextEncode, solarL_SaveImagesToZip, VAEDecode, CLIPLoader, VAELoader, Note]
patterns: [text_to_image]
missing: [BatchImagesNode, BatchImagesNode, ImageScaleToMaxDimension, ImageScaleToMaxDimension, ImageScaleToMaxDimension, ImageScaleToMaxDimension, ImageScaleToMaxDimension, ImageScaleToMaxDimension, ImageScaleToMaxDimension, ImageScaleToMaxDimension, ImageScaleToMaxDimension, ImageScaleToMaxDimension, JsonExtractString, JsonExtractString, PrimitiveBoolean, PrimitiveBoolean, StringConcatenate, StringConcatenate, StringConcatenate, StringConcatenate, TextGenerate, TextGenerate, llama_cpp_instruct_adv, llama_cpp_instruct_adv, llama_cpp_model_loader, llama_cpp_parameters, LoraLoaderBypassModelOnly, CR Prompt Text, PreviewAny, PreviewAny, solarL_SaveImagesToZip]
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [次要节点 `BatchImagesNode` 知识库中没有该节点类型的任何知识, 次要节点 `BatchImagesNode` 知识库中没有该节点类型的任何知识, 次要节点 `ImageScaleToMaxDimension` 知识库中没有该节点类型的任何知识, 次要节点 `ImageScaleToMaxDimension` 知识库中没有该节点类型的任何知识, 次要节点 `ImageScaleToMaxDimension` 知识库中没有该节点类型的任何知识, 次要节点 `ImageScaleToMaxDimension` 知识库中没有该节点类型的任何知识, 次要节点 `ImageScaleToMaxDimension` 知识库中没有该节点类型的任何知识, 次要节点 `ImageScaleToMaxDimension` 知识库中没有该节点类型的任何知识, 次要节点 `ImageScaleToMaxDimension` 知识库中没有该节点类型的任何知识, 次要节点 `ImageScaleToMaxDimension` 知识库中没有该节点类型的任何知识, 次要节点 `ImageScaleToMaxDimension` 知识库中没有该节点类型的任何知识, 次要节点 `ImageScaleToMaxDimension` 知识库中没有该节点类型的任何知识, 次要节点 `JsonExtractString` 知识库中没有该节点类型的任何知识, 次要节点 `JsonExtractString` 知识库中没有该节点类型的任何知识, 次要节点 `PrimitiveBoolean` 知识库中没有该节点类型的任何知识, 次要节点 `PrimitiveBoolean` 知识库中没有该节点类型的任何知识, 次要节点 `StringConcatenate` 知识库中没有该节点类型的任何知识, 次要节点 `StringConcatenate` 知识库中没有该节点类型的任何知识, 次要节点 `StringConcatenate` 知识库中没有该节点类型的任何知识, 次要节点 `StringConcatenate` 知识库中没有该节点类型的任何知识, 次要节点 `TextGenerate` 知识库中没有该节点类型的任何知识, 次要节点 `TextGenerate` 知识库中没有该节点类型的任何知识, 次要节点 `llama_cpp_instruct_adv` 知识库中没有该节点类型的任何知识, 次要节点 `llama_cpp_instruct_adv` 知识库中没有该节点类型的任何知识, 次要节点 `llama_cpp_model_loader` 知识库中没有该节点类型的任何知识, 次要节点 `llama_cpp_parameters` 知识库中没有该节点类型的任何知识, 核心节点 `LoraLoaderBypassModelOnly` 仅有 LoRA 的通用知识，没有该节点自己的说明, 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明, 次要节点 `PreviewAny` 仅有 SaveImage 的通用知识，没有该节点自己的说明, 次要节点 `PreviewAny` 仅有 SaveImage 的通用知识，没有该节点自己的说明, 次要节点 `solarL_SaveImagesToZip` 仅有 SaveImage 的通用知识，没有该节点自己的说明, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/文生图/Qwen Image 2.1文生与编辑加速工作流双自动提示词，文生图图生图方案_2106086535849398274.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Qwen Image 2.1文生与编辑加速工作流双自动提示词，文生图图生图方案_2106086535849398274.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（173 个）：
- `CLIPLoader`
- `VAELoader`
- `VAEDecode` ★核心
- `UNETLoader` ★核心
- `EmptyLatentImage` ★核心
- `KSampler` ★核心
- `TextEncodeQwenImage21`
- `VAEDecode` ★核心
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `KSampler` ★核心
- `SaveImage`
- `QwenImage21Cache`
- `CLIPLoader`
- `StringConcatenate`
- `TextGenerate`
- `JsonExtractString`
- `CLIPLoader`
- `TextGenerate`
- `JsonExtractString`
- `BatchImagesNode`
- `StringConcatenate`
- `StringConcatenate`
- `Any Switch (rgthree)`
- `PreviewAny`
- `PreviewAny`
- `llama_cpp_parameters`
- `llama_cpp_instruct_adv`
- `llama_cpp_instruct_adv`
- `BatchImagesNode`
- `SetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `LoadImage`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `LoadImage`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `LoadImage`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `ImageScaleToMaxDimension`
- `ImageScaleToMaxDimension`
- `ImageScaleToMaxDimension`
- `ImageScaleToMaxDimension`
- `ImageScaleToMaxDimension`
- `ImageScaleToMaxDimension`
- `ImageScaleToMaxDimension`
- `ImageScaleToMaxDimension`
- `ImageScaleToMaxDimension`
- `ImageScaleToMaxDimension`
- `SetNode`
- `GetNode`
- `Image Comparer (rgthree)`
- `SetNode`
- `GetNode`
- `ComfySwitchNode`
- `GetNode`
- `ComfySwitchNode`
- `GetNode`
- `KSampler` ★核心
- `ComfySwitchNode`
- `SetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `ComfySwitchNode`
- `LoadImage`
- `LoadImage`
- `ResolutionSelector`
- `PrimitiveBoolean`
- `StringConcatenate`
- `SetNode`
- `TextEncodeQwenImage21`
- `SaveImage`
- `CR Prompt Text`
- `LoadImage`
- `PrimitiveBoolean`
- `KSampler` ★核心
- `LoraLoaderBypassModelOnly` ★核心
- `Any Switch (rgthree)`
- `llama_cpp_model_loader`
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

覆盖率 **30%**（52/173）

**有卡**：`CLIPLoader`、`VAELoader`、`VAEDecode`、`UNETLoader`、`EmptyLatentImage`、`KSampler`、`TextEncodeQwenImage21`、`LoadImage`、`SaveImage`、`QwenImage21Cache`、`ResolutionSelector`、`LoraLoaderModelOnly`、`CLIPTextEncode`

**缺卡**（31）：`BatchImagesNode`、`BatchImagesNode`、`ImageScaleToMaxDimension`、`ImageScaleToMaxDimension`、`ImageScaleToMaxDimension`、`ImageScaleToMaxDimension`、`ImageScaleToMaxDimension`、`ImageScaleToMaxDimension`、`ImageScaleToMaxDimension`、`ImageScaleToMaxDimension`、`ImageScaleToMaxDimension`、`ImageScaleToMaxDimension`、`JsonExtractString`、`JsonExtractString`、`PrimitiveBoolean`、`PrimitiveBoolean`、`StringConcatenate`、`StringConcatenate`、`StringConcatenate`、`StringConcatenate`、`TextGenerate`、`TextGenerate`、`llama_cpp_instruct_adv`、`llama_cpp_instruct_adv`、`llama_cpp_model_loader`、`llama_cpp_parameters`、`LoraLoaderBypassModelOnly`、`CR Prompt Text`、`PreviewAny`、`PreviewAny`、`solarL_SaveImagesToZip`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage

## 参数体检

发现 3 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- 次要节点 `BatchImagesNode` 知识库中没有该节点类型的任何知识
- 次要节点 `BatchImagesNode` 知识库中没有该节点类型的任何知识
- 次要节点 `ImageScaleToMaxDimension` 知识库中没有该节点类型的任何知识
- 次要节点 `ImageScaleToMaxDimension` 知识库中没有该节点类型的任何知识
- 次要节点 `ImageScaleToMaxDimension` 知识库中没有该节点类型的任何知识
- 次要节点 `ImageScaleToMaxDimension` 知识库中没有该节点类型的任何知识
- 次要节点 `ImageScaleToMaxDimension` 知识库中没有该节点类型的任何知识
- 次要节点 `ImageScaleToMaxDimension` 知识库中没有该节点类型的任何知识
- 次要节点 `ImageScaleToMaxDimension` 知识库中没有该节点类型的任何知识
- 次要节点 `ImageScaleToMaxDimension` 知识库中没有该节点类型的任何知识
- 次要节点 `ImageScaleToMaxDimension` 知识库中没有该节点类型的任何知识
- 次要节点 `ImageScaleToMaxDimension` 知识库中没有该节点类型的任何知识
- 次要节点 `JsonExtractString` 知识库中没有该节点类型的任何知识
- 次要节点 `JsonExtractString` 知识库中没有该节点类型的任何知识
- 次要节点 `PrimitiveBoolean` 知识库中没有该节点类型的任何知识
- 次要节点 `PrimitiveBoolean` 知识库中没有该节点类型的任何知识
- 次要节点 `StringConcatenate` 知识库中没有该节点类型的任何知识
- 次要节点 `StringConcatenate` 知识库中没有该节点类型的任何知识
- 次要节点 `StringConcatenate` 知识库中没有该节点类型的任何知识
- 次要节点 `StringConcatenate` 知识库中没有该节点类型的任何知识
- 次要节点 `TextGenerate` 知识库中没有该节点类型的任何知识
- 次要节点 `TextGenerate` 知识库中没有该节点类型的任何知识
- 次要节点 `llama_cpp_instruct_adv` 知识库中没有该节点类型的任何知识
- 次要节点 `llama_cpp_instruct_adv` 知识库中没有该节点类型的任何知识
- 次要节点 `llama_cpp_model_loader` 知识库中没有该节点类型的任何知识
- 次要节点 `llama_cpp_parameters` 知识库中没有该节点类型的任何知识
- 核心节点 `LoraLoaderBypassModelOnly` 仅有 LoRA 的通用知识，没有该节点自己的说明
- 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明
- 次要节点 `PreviewAny` 仅有 SaveImage 的通用知识，没有该节点自己的说明
- 次要节点 `PreviewAny` 仅有 SaveImage 的通用知识，没有该节点自己的说明
- 次要节点 `solarL_SaveImagesToZip` 仅有 SaveImage 的通用知识，没有该节点自己的说明
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

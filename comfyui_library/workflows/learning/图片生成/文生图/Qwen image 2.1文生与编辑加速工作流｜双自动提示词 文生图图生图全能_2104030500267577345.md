---
key: 图片生成/文生图/Qwen image 2.1文生与编辑加速工作流｜双自动提示词 文生图图生图全能_2104030500267577345.json
name: Qwen image 2.1文生与编辑加速工作流｜双自动提示词 文生图图生图全能_2104030500267577345
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Qwen image 2.1文生与编辑加速工作流｜双自动提示词 文生图图生图全能_2104030500267577345.json
hash: 64f968837b61efb0
coverage: 0.502674
learned_at: 2026-10-10 20:58:57
nodes: [CLIPLoader, VAELoader, VAEDecode, UNETLoader, EmptyLatentImage, KSampler, TextEncodeQwenImage21, VAEDecode, LoadImage, LoadImage, LoadImage, LoadImage, KSampler, SaveImage, QwenImage21Cache, CLIPLoader, StringConcatenate, TextGenerate, JsonExtractString, CLIPLoader, TextGenerate, JsonExtractString, BatchImagesNode, StringConcatenate, StringConcatenate, Any Switch (rgthree), PreviewAny, PreviewAny, llama_cpp_parameters, llama_cpp_instruct_adv, llama_cpp_instruct_adv, BatchImagesNode, SetNode, GetNode, SetNode, GetNode, GetNode, GetNode, SetNode, GetNode, GetNode, SetNode, GetNode, SetNode, GetNode, SetNode, GetNode, SetNode, GetNode, SetNode, GetNode, SetNode, GetNode, SetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, SetNode, GetNode, GetNode, SetNode, GetNode, SetNode, GetNode, GetNode, GetNode, SetNode, GetNode, SetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, LoadImage, SetNode, GetNode, GetNode, GetNode, LoadImage, SetNode, GetNode, GetNode, GetNode, SetNode, GetNode, GetNode, GetNode, LoadImage, SetNode, GetNode, GetNode, GetNode, ImageScaleToMaxDimension, ImageScaleToMaxDimension, ImageScaleToMaxDimension, ImageScaleToMaxDimension, ImageScaleToMaxDimension, ImageScaleToMaxDimension, ImageScaleToMaxDimension, ImageScaleToMaxDimension, ImageScaleToMaxDimension, ImageScaleToMaxDimension, SetNode, GetNode, Image Comparer (rgthree), SetNode, GetNode, ComfySwitchNode, GetNode, ComfySwitchNode, GetNode, KSampler, ComfySwitchNode, SetNode, GetNode, SetNode, GetNode, GetNode, ComfySwitchNode, LoadImage, LoadImage, ResolutionSelector, PrimitiveBoolean, StringConcatenate, SetNode, TextEncodeQwenImage21, SaveImage, CR Prompt Text, LoadImage, llama_cpp_model_loader, PrimitiveBoolean, KSampler, LoraLoaderBypassModelOnly, Any Switch (rgthree), 孤海注释, 孤海注释, UNETLoader, CLIPLoader, CLIPTextEncode, VAELoader, EmptyLatentImage, KSampler, VAEDecode, solarL_SaveImagesToZip, JjkText, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, CLIPTextEncode, Note]
patterns: [text_to_image]
missing: [CR Prompt Text]
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/文生图/Qwen image 2.1文生与编辑加速工作流｜双自动提示词 文生图图生图全能_2104030500267577345.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Qwen image 2.1文生与编辑加速工作流｜双自动提示词 文生图图生图全能_2104030500267577345.json`

## 结构

**节点**（187 个）：
- `CLIPLoader`
- `VAELoader`
- `VAEDecode`
- `UNETLoader`
- `EmptyLatentImage`
- `KSampler`
- `TextEncodeQwenImage21`
- `VAEDecode`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `KSampler`
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
- `KSampler`
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
- `llama_cpp_model_loader`
- `PrimitiveBoolean`
- `KSampler`
- `LoraLoaderBypassModelOnly`
- `Any Switch (rgthree)`
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

覆盖率 **50%**（94/187）

**有卡**：`CLIPLoader`、`VAELoader`、`VAEDecode`、`UNETLoader`、`EmptyLatentImage`、`KSampler`、`TextEncodeQwenImage21`、`LoadImage`、`SaveImage`、`QwenImage21Cache`、`StringConcatenate`、`TextGenerate`、`JsonExtractString`、`BatchImagesNode`、`Any Switch (rgthree)`、`PreviewAny`、`llama_cpp_parameters`、`llama_cpp_instruct_adv`、`SetNode`、`GetNode`

**缺卡**（1）：`CR Prompt Text`

## 参数体检

发现 3 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

---
key: 图片生成/文生图/Qwen image 2.1 全家桶！加速版！ 图像编辑！文生图！  自动化高清！_2104014492534398977.json
name: Qwen image 2.1 全家桶！加速版！ 图像编辑！文生图！  自动化高清！_2104014492534398977
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Qwen image 2.1 全家桶！加速版！ 图像编辑！文生图！  自动化高清！_2104014492534398977.json
hash: 9dc97e047f108ee3
coverage: 0.396739
learned_at: 2026-10-10 20:58:56
nodes: [LoadImage, LoadImage, LoadImage, LoadImage, 忽略多组孤海, JsonExtractString, TextGenerate, JsonExtractString, BatchImagesNode, StringConcatenate, llama_cpp_instruct_adv, BatchImagesNode, Note, Note, GetNode, GetNode, GetNode, GetNode, SetNode, GetNode, GetNode, SetNode, GetNode, SetNode, GetNode, SetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, SetNode, SetNode, GetNode, SetNode, GetNode, GetNode, GetNode, SetNode, SetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, LoadImage, SetNode, GetNode, GetNode, GetNode, LoadImage, SetNode, GetNode, GetNode, GetNode, SetNode, GetNode, GetNode, GetNode, LoadImage, SetNode, GetNode, GetNode, GetNode, ImageScaleToMaxDimension, ImageScaleToMaxDimension, ImageScaleToMaxDimension, ImageScaleToMaxDimension, ImageScaleToMaxDimension, ImageScaleToMaxDimension, ImageScaleToMaxDimension, ImageScaleToMaxDimension, ImageScaleToMaxDimension, ImageScaleToMaxDimension, GetNode, GetNode, GetNode, LoadImage, SetNode, LoadImage, GetNode, CLIPLoader, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, StringConcatenate, GetNode, CLIPLoader, StringConcatenate, TextGenerate, SetNode, SetNode, llama_cpp_instruct_adv, llama_cpp_model_loader, CLIPLoader, VAELoader, GetNode, SetNode, SetNode, SetNode, SetNode, ComfySwitchNode, GetNode, KSampler, ComfySwitchNode, KSampler, Any Switch (rgthree), TextEncodeQwenImage21, PreviewAny, ComfySwitchNode, SaveImage, VAEDecode, LoadImage, Any Switch (rgthree), PreviewAny, TextEncodeQwenImage21, KSampler, KSampler, ComfySwitchNode, VAEDecode, SetNode, llama_cpp_parameters, StringConcatenate, SetNode, QwenImage21Cache, 忽略多组孤海, SetNode, CLIPTextEncode, UNETLoader, LoraLoaderBypassModelOnly, GetNode, GoohaiAnyExists, GoohaiAnyExists, GetNode, VAEDecode, CLIPTextEncode, SaveImage, SetNode, LatentSwitch, VAEEncode, VAELoader, CLIPLoader, ReferenceLatent, ReferenceLatent, SetNode, EmptyLatentImage, ResolutionSelector, ComfySwitchNode, SetNode, SetNode, SetNode, KSamplerAdvanced, UNETLoader, ImageScaleToTotalPixels, GetNode, JWFloat, PDIMAGE_LongerSize, GetNode, SetNode, CR Prompt Text, Image Comparer (rgthree), 忽略多组孤海, PrimitiveBoolean, Fast Groups Bypasser (rgthree), SeedNode, PrimitiveBoolean, Note, GetNode, PreviewImage, PreviewImage, Image Comparer (rgthree), SaveImage]
patterns: [text_to_image, image_to_image]
missing: [忽略多组孤海, 忽略多组孤海, 忽略多组孤海, CR Prompt Text]
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4, "denoise": "simple", "height": 1024, "sampler_name": 1, "scheduler": "euler", "seed": "enable", "steps": "fixed", "width": 1024}
discoveries: [次要节点 `忽略多组孤海` 知识库中没有该节点类型的任何知识, 次要节点 `忽略多组孤海` 知识库中没有该节点类型的任何知识, 次要节点 `忽略多组孤海` 知识库中没有该节点类型的任何知识, 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/文生图/Qwen image 2.1 全家桶！加速版！ 图像编辑！文生图！  自动化高清！_2104014492534398977.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Qwen image 2.1 全家桶！加速版！ 图像编辑！文生图！  自动化高清！_2104014492534398977.json`

## 结构

**节点**（184 个）：
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `忽略多组孤海`
- `JsonExtractString`
- `TextGenerate`
- `JsonExtractString`
- `BatchImagesNode`
- `StringConcatenate`
- `llama_cpp_instruct_adv`
- `BatchImagesNode`
- `Note`
- `Note`
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
- `SetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
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
- `GetNode`
- `GetNode`
- `GetNode`
- `LoadImage`
- `SetNode`
- `LoadImage`
- `GetNode`
- `CLIPLoader`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `StringConcatenate`
- `GetNode`
- `CLIPLoader`
- `StringConcatenate`
- `TextGenerate`
- `SetNode`
- `SetNode`
- `llama_cpp_instruct_adv`
- `llama_cpp_model_loader`
- `CLIPLoader`
- `VAELoader`
- `GetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `ComfySwitchNode`
- `GetNode`
- `KSampler`
- `ComfySwitchNode`
- `KSampler`
- `Any Switch (rgthree)`
- `TextEncodeQwenImage21`
- `PreviewAny`
- `ComfySwitchNode`
- `SaveImage`
- `VAEDecode`
- `LoadImage`
- `Any Switch (rgthree)`
- `PreviewAny`
- `TextEncodeQwenImage21`
- `KSampler`
- `KSampler`
- `ComfySwitchNode`
- `VAEDecode`
- `SetNode`
- `llama_cpp_parameters`
- `StringConcatenate`
- `SetNode`
- `QwenImage21Cache`
- `忽略多组孤海`
- `SetNode`
- `CLIPTextEncode`
- `UNETLoader`
- `LoraLoaderBypassModelOnly`
- `GetNode`
- `GoohaiAnyExists`
- `GoohaiAnyExists`
- `GetNode`
- `VAEDecode`
- `CLIPTextEncode`
- `SaveImage`
- `SetNode`
- `LatentSwitch`
- `VAEEncode`
- `VAELoader`
- `CLIPLoader`
- `ReferenceLatent`
- `ReferenceLatent`
- `SetNode`
- `EmptyLatentImage`
- `ResolutionSelector`
- `ComfySwitchNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `KSamplerAdvanced`
- `UNETLoader`
- `ImageScaleToTotalPixels`
- `GetNode`
- `JWFloat`
- `PDIMAGE_LongerSize`
- `GetNode`
- `SetNode`
- `CR Prompt Text`
- `Image Comparer (rgthree)`
- `忽略多组孤海`
- `PrimitiveBoolean`
- `Fast Groups Bypasser (rgthree)`
- `SeedNode`
- `PrimitiveBoolean`
- `Note`
- `GetNode`
- `PreviewImage`
- `PreviewImage`
- `Image Comparer (rgthree)`
- `SaveImage`

**识别到的模式**：text_to_image、image_to_image

## 关键参数

- `batch_size` = `1`
- `cfg` = `4`
- `denoise` = `simple`
- `height` = `1024`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `seed` = `enable`
- `steps` = `fixed`
- `width` = `1024`

## 知识

覆盖率 **40%**（73/184）

**有卡**：`LoadImage`、`忽略多组孤海`、`JsonExtractString`、`TextGenerate`、`BatchImagesNode`、`StringConcatenate`、`llama_cpp_instruct_adv`、`Note`、`GetNode`、`SetNode`、`ImageScaleToMaxDimension`

**缺卡**（4）：`忽略多组孤海`、`忽略多组孤海`、`忽略多组孤海`、`CR Prompt Text`

## 参数体检

发现 2 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- 次要节点 `忽略多组孤海` 知识库中没有该节点类型的任何知识
- 次要节点 `忽略多组孤海` 知识库中没有该节点类型的任何知识
- 次要节点 `忽略多组孤海` 知识库中没有该节点类型的任何知识
- 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

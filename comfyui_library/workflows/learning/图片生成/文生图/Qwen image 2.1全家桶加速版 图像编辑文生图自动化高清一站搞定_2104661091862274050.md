---
key: 图片生成/文生图/Qwen image 2.1全家桶加速版 图像编辑文生图自动化高清一站搞定_2104661091862274050.json
name: Qwen image 2.1全家桶加速版 图像编辑文生图自动化高清一站搞定_2104661091862274050
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Qwen image 2.1全家桶加速版 图像编辑文生图自动化高清一站搞定_2104661091862274050.json
hash: 3c4b1f9914a2700a
coverage: 0.47343
learned_at: 2026-10-07 02:17:00
nodes: [LoadImage, LoadImage, LoadImage, LoadImage, JsonExtractString, TextGenerate, JsonExtractString, BatchImagesNode, StringConcatenate, llama_cpp_instruct_adv, BatchImagesNode, GetNode, GetNode, GetNode, GetNode, SetNode, GetNode, GetNode, SetNode, GetNode, SetNode, GetNode, SetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, SetNode, SetNode, GetNode, SetNode, GetNode, GetNode, GetNode, SetNode, SetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, LoadImage, SetNode, GetNode, GetNode, GetNode, LoadImage, SetNode, GetNode, GetNode, GetNode, SetNode, GetNode, GetNode, GetNode, LoadImage, SetNode, GetNode, GetNode, GetNode, ImageScaleToMaxDimension, ImageScaleToMaxDimension, ImageScaleToMaxDimension, ImageScaleToMaxDimension, ImageScaleToMaxDimension, ImageScaleToMaxDimension, ImageScaleToMaxDimension, ImageScaleToMaxDimension, ImageScaleToMaxDimension, ImageScaleToMaxDimension, GetNode, GetNode, GetNode, LoadImage, SetNode, LoadImage, GetNode, CLIPLoader, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, StringConcatenate, GetNode, CLIPLoader, StringConcatenate, TextGenerate, SetNode, SetNode, llama_cpp_instruct_adv, llama_cpp_model_loader, CLIPLoader, VAELoader, GetNode, SetNode, SetNode, SetNode, SetNode, ComfySwitchNode, GetNode, KSampler, ComfySwitchNode, KSampler, Any Switch (rgthree), TextEncodeQwenImage21, PreviewAny, ComfySwitchNode, SaveImage, VAEDecode, LoadImage, Any Switch (rgthree), PreviewAny, TextEncodeQwenImage21, KSampler, KSampler, ComfySwitchNode, VAEDecode, SetNode, llama_cpp_parameters, StringConcatenate, SetNode, QwenImage21Cache, SetNode, CLIPTextEncode, UNETLoader, LoraLoaderBypassModelOnly, GetNode, GoohaiAnyExists, GoohaiAnyExists, GetNode, VAEDecode, CLIPTextEncode, SaveImage, SetNode, LatentSwitch, VAEEncode, VAELoader, CLIPLoader, ReferenceLatent, ReferenceLatent, SetNode, EmptyLatentImage, ResolutionSelector, ComfySwitchNode, SetNode, SetNode, SetNode, KSamplerAdvanced, UNETLoader, ImageScaleToTotalPixels, GetNode, JWFloat, PDIMAGE_LongerSize, GetNode, SetNode, CR Prompt Text, Image Comparer (rgthree), PrimitiveBoolean, Fast Groups Bypasser (rgthree), SeedNode, PrimitiveBoolean, GetNode, PreviewImage, PreviewImage, Image Comparer (rgthree), SaveImage, 孤海注释, 孤海注释, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, KSampler, EmptyLatentImage, JjkText, CLIPTextEncode, CLIPTextEncode, solarL_SaveImagesToZip, VAEDecode, CLIPLoader, VAELoader, Note]
patterns: [text_to_image, image_to_image]
missing: [CR Prompt Text]
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/文生图/Qwen image 2.1全家桶加速版 图像编辑文生图自动化高清一站搞定_2104661091862274050.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Qwen image 2.1全家桶加速版 图像编辑文生图自动化高清一站搞定_2104661091862274050.json`

## 结构

**生成流程**：Model → Encode → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（207 个）：
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `JsonExtractString`
- `TextGenerate`
- `JsonExtractString`
- `BatchImagesNode`
- `StringConcatenate`
- `llama_cpp_instruct_adv`
- `BatchImagesNode`
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
- `KSampler` ★核心
- `ComfySwitchNode`
- `KSampler` ★核心
- `Any Switch (rgthree)`
- `TextEncodeQwenImage21`
- `PreviewAny`
- `ComfySwitchNode`
- `SaveImage`
- `VAEDecode` ★核心
- `LoadImage`
- `Any Switch (rgthree)`
- `PreviewAny`
- `TextEncodeQwenImage21`
- `KSampler` ★核心
- `KSampler` ★核心
- `ComfySwitchNode`
- `VAEDecode` ★核心
- `SetNode`
- `llama_cpp_parameters`
- `StringConcatenate`
- `SetNode`
- `QwenImage21Cache`
- `SetNode`
- `CLIPTextEncode` ★核心
- `UNETLoader` ★核心
- `LoraLoaderBypassModelOnly` ★核心
- `GetNode`
- `GoohaiAnyExists`
- `GoohaiAnyExists`
- `GetNode`
- `VAEDecode` ★核心
- `CLIPTextEncode` ★核心
- `SaveImage`
- `SetNode`
- `LatentSwitch`
- `VAEEncode` ★核心
- `VAELoader`
- `CLIPLoader`
- `ReferenceLatent`
- `ReferenceLatent`
- `SetNode`
- `EmptyLatentImage` ★核心
- `ResolutionSelector`
- `ComfySwitchNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `KSamplerAdvanced` ★核心
- `UNETLoader` ★核心
- `ImageScaleToTotalPixels`
- `GetNode`
- `JWFloat`
- `PDIMAGE_LongerSize`
- `GetNode`
- `SetNode`
- `CR Prompt Text`
- `Image Comparer (rgthree)`
- `PrimitiveBoolean`
- `Fast Groups Bypasser (rgthree)`
- `SeedNode`
- `PrimitiveBoolean`
- `GetNode`
- `PreviewImage`
- `PreviewImage`
- `Image Comparer (rgthree)`
- `SaveImage`
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

**识别到的模式**：text_to_image、image_to_image

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

覆盖率 **47%**（98/207）

**有卡**：`LoadImage`、`JsonExtractString`、`TextGenerate`、`BatchImagesNode`、`StringConcatenate`、`llama_cpp_instruct_adv`、`ImageScaleToMaxDimension`、`CLIPLoader`、`llama_cpp_model_loader`、`VAELoader`、`KSampler`、`TextEncodeQwenImage21`、`SaveImage`、`VAEDecode`、`llama_cpp_parameters`、`QwenImage21Cache`、`CLIPTextEncode`、`UNETLoader`、`LoraLoaderBypassModelOnly`、`GoohaiAnyExists`、`LatentSwitch`、`VAEEncode`、`ReferenceLatent`、`EmptyLatentImage`、`ResolutionSelector`、`KSamplerAdvanced`、`ImageScaleToTotalPixels`、`JWFloat`、`PDIMAGE_LongerSize`、`PrimitiveBoolean`、`SeedNode`、`LoraLoaderModelOnly`、`solarL_SaveImagesToZip`

**缺卡**（1）：`CR Prompt Text`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage

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

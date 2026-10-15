---
key: 图片生成/文生图/Qwen image2.1全能工作流 文生图人像写真一站搞定_2104332186555080705.json
name: Qwen image2.1全能工作流 文生图人像写真一站搞定_2104332186555080705
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Qwen image2.1全能工作流 文生图人像写真一站搞定_2104332186555080705.json
hash: 2c25dc82d2ab782b
coverage: 0.480392
learned_at: 2026-10-10 20:58:57
nodes: [VAEDecode, LayerUtility: ImageScaleByAspectRatio V2, SetNode, LayerUtility: ImageScaleByAspectRatio V2, SetNode, LayerUtility: ImageScaleByAspectRatio V2, SetNode, LayerUtility: ImageScaleByAspectRatio V2, SetNode, SetNode, LayerUtility: PurgeVRAM V2, LayerUtility: PurgeVRAM V2, SaveImage, UNETLoader, CLIPLoader, VAELoader, GetNode, LayerUtility: ImageScaleByAspectRatio V2, SetNode, LoadImage, LoadImage, easy showAnything, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, QwenImage21Cache, TextEncodeQwenImage21, KSampler, LoadImage, Fast Groups Bypasser (rgthree), LayerUtility: ImageScaleByAspectRatio V2, EmptyLatentImage, GetNode, GetImageSize, SetNode, LayerUtility: ImageScaleByAspectRatio V2, GetNode, CR Text, CR Text, CR Text, SetNode, LoadImage, SetNode, SetNode, GetNode, PreviewImage, CR Text, CR Text, AIO_Preprocessor, llama_cpp_parameters, LoadImage, llama_cpp_instruct_adv, llama_cpp_instruct_adv, llama_cpp_model_loader, llama_cpp_parameters, llama_cpp_model_loader, ki_宫格拼图简易版, PreviewImage, GetNode, Image Comparer (rgthree), CR Text Concatenate, easy showAnything, CR Text, LoadImage, LoadImage, 孤海注释, 孤海注释, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, KSampler, EmptyLatentImage, JjkText, CLIPTextEncode, CLIPTextEncode, solarL_SaveImagesToZip, VAEDecode, CLIPLoader, VAELoader, Note]
patterns: [text_to_image]
missing: [CR Text, CR Text, CR Text, CR Text, CR Text, CR Text, CR Text Concatenate, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: PurgeVRAM V2, LayerUtility: PurgeVRAM V2, ki_宫格拼图简易版]
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [次要节点 `CR Text` 知识库中没有该节点类型的任何知识, 次要节点 `CR Text` 知识库中没有该节点类型的任何知识, 次要节点 `CR Text` 知识库中没有该节点类型的任何知识, 次要节点 `CR Text` 知识库中没有该节点类型的任何知识, 次要节点 `CR Text` 知识库中没有该节点类型的任何知识, 次要节点 `CR Text` 知识库中没有该节点类型的任何知识, 次要节点 `CR Text Concatenate` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: PurgeVRAM V2` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: PurgeVRAM V2` 知识库中没有该节点类型的任何知识, 次要节点 `ki_宫格拼图简易版` 知识库中没有该节点类型的任何知识, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/文生图/Qwen image2.1全能工作流 文生图人像写真一站搞定_2104332186555080705.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Qwen image2.1全能工作流 文生图人像写真一站搞定_2104332186555080705.json`

## 结构

**节点**（102 个）：
- `VAEDecode`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `SetNode`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `SetNode`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `SetNode`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `SetNode`
- `SetNode`
- `LayerUtility: PurgeVRAM V2`
- `LayerUtility: PurgeVRAM V2`
- `SaveImage`
- `UNETLoader`
- `CLIPLoader`
- `VAELoader`
- `GetNode`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `SetNode`
- `LoadImage`
- `LoadImage`
- `easy showAnything`
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
- `GetNode`
- `QwenImage21Cache`
- `TextEncodeQwenImage21`
- `KSampler`
- `LoadImage`
- `Fast Groups Bypasser (rgthree)`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `EmptyLatentImage`
- `GetNode`
- `GetImageSize`
- `SetNode`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `GetNode`
- `CR Text`
- `CR Text`
- `CR Text`
- `SetNode`
- `LoadImage`
- `SetNode`
- `SetNode`
- `GetNode`
- `PreviewImage`
- `CR Text`
- `CR Text`
- `AIO_Preprocessor`
- `llama_cpp_parameters`
- `LoadImage`
- `llama_cpp_instruct_adv`
- `llama_cpp_instruct_adv`
- `llama_cpp_model_loader`
- `llama_cpp_parameters`
- `llama_cpp_model_loader`
- `ki_宫格拼图简易版`
- `PreviewImage`
- `GetNode`
- `Image Comparer (rgthree)`
- `CR Text Concatenate`
- `easy showAnything`
- `CR Text`
- `LoadImage`
- `LoadImage`
- `孤海注释`
- `孤海注释`
- `UNETLoader`
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
- `KSampler`
- `EmptyLatentImage`
- `JjkText`
- `CLIPTextEncode`
- `CLIPTextEncode`
- `solarL_SaveImagesToZip`
- `VAEDecode`
- `CLIPLoader`
- `VAELoader`
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

覆盖率 **48%**（49/102）

**有卡**：`VAEDecode`、`LayerUtility: ImageScaleByAspectRatio V2`、`SetNode`、`LayerUtility: PurgeVRAM V2`、`SaveImage`、`UNETLoader`、`CLIPLoader`、`VAELoader`、`GetNode`、`LoadImage`、`easy showAnything`、`QwenImage21Cache`、`TextEncodeQwenImage21`、`KSampler`、`Fast Groups Bypasser (rgthree)`、`EmptyLatentImage`、`GetImageSize`、`CR Text`

**缺卡**（17）：`CR Text`、`CR Text`、`CR Text`、`CR Text`、`CR Text`、`CR Text`、`CR Text Concatenate`、`LayerUtility: ImageScaleByAspectRatio V2`、`LayerUtility: ImageScaleByAspectRatio V2`、`LayerUtility: ImageScaleByAspectRatio V2`、`LayerUtility: ImageScaleByAspectRatio V2`、`LayerUtility: ImageScaleByAspectRatio V2`、`LayerUtility: ImageScaleByAspectRatio V2`、`LayerUtility: ImageScaleByAspectRatio V2`、`LayerUtility: PurgeVRAM V2`、`LayerUtility: PurgeVRAM V2`、`ki_宫格拼图简易版`

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- 次要节点 `CR Text` 知识库中没有该节点类型的任何知识
- 次要节点 `CR Text` 知识库中没有该节点类型的任何知识
- 次要节点 `CR Text` 知识库中没有该节点类型的任何知识
- 次要节点 `CR Text` 知识库中没有该节点类型的任何知识
- 次要节点 `CR Text` 知识库中没有该节点类型的任何知识
- 次要节点 `CR Text` 知识库中没有该节点类型的任何知识
- 次要节点 `CR Text Concatenate` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: PurgeVRAM V2` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: PurgeVRAM V2` 知识库中没有该节点类型的任何知识
- 次要节点 `ki_宫格拼图简易版` 知识库中没有该节点类型的任何知识
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

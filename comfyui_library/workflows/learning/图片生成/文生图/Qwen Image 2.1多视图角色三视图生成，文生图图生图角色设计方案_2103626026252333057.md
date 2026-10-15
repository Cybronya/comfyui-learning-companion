---
key: 图片生成/文生图/Qwen Image 2.1多视图角色三视图生成，文生图图生图角色设计方案_2103626026252333057.json
name: Qwen Image 2.1多视图角色三视图生成，文生图图生图角色设计方案_2103626026252333057
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Qwen Image 2.1多视图角色三视图生成，文生图图生图角色设计方案_2103626026252333057.json
hash: 5bae84f63e91c017
coverage: 0.781818
learned_at: 2026-10-10 20:58:52
nodes: [VAEDecode, LayerUtility: ImageReelComposit, PreviewImage, EmptyLatentImage, Fast Groups Bypasser (rgthree), KSampler, SaveImage, LayerUtility: ImageReel, UNETLoader, CLIPLoader, VAELoader, Anything Everywhere3, TextEncodeQwenImage21, KSampler, VAEDecode, TextEncodeQwenImage21, llama_cpp_model_loader, CR Text, llama_cpp_instruct_adv, PreviewAny, EmptyLatentImage, ResolutionSelector, ResolutionSelector, SaveImage, LoadImage, Fast Groups Bypasser (rgthree), 孤海注释, 孤海注释, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, KSampler, EmptyLatentImage, JjkText, CLIPTextEncode, CLIPTextEncode, solarL_SaveImagesToZip, VAEDecode, CLIPLoader, VAELoader, Note]
patterns: [text_to_image]
missing: [CR Text, LayerUtility: ImageReel, LayerUtility: ImageReelComposit]
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [次要节点 `CR Text` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: ImageReel` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: ImageReelComposit` 知识库中没有该节点类型的任何知识, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/文生图/Qwen Image 2.1多视图角色三视图生成，文生图图生图角色设计方案_2103626026252333057.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Qwen Image 2.1多视图角色三视图生成，文生图图生图角色设计方案_2103626026252333057.json`

## 结构

**节点**（55 个）：
- `VAEDecode`
- `LayerUtility: ImageReelComposit`
- `PreviewImage`
- `EmptyLatentImage`
- `Fast Groups Bypasser (rgthree)`
- `KSampler`
- `SaveImage`
- `LayerUtility: ImageReel`
- `UNETLoader`
- `CLIPLoader`
- `VAELoader`
- `Anything Everywhere3`
- `TextEncodeQwenImage21`
- `KSampler`
- `VAEDecode`
- `TextEncodeQwenImage21`
- `llama_cpp_model_loader`
- `CR Text`
- `llama_cpp_instruct_adv`
- `PreviewAny`
- `EmptyLatentImage`
- `ResolutionSelector`
- `ResolutionSelector`
- `SaveImage`
- `LoadImage`
- `Fast Groups Bypasser (rgthree)`
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

覆盖率 **78%**（43/55）

**有卡**：`VAEDecode`、`LayerUtility: ImageReelComposit`、`PreviewImage`、`EmptyLatentImage`、`Fast Groups Bypasser (rgthree)`、`KSampler`、`SaveImage`、`LayerUtility: ImageReel`、`UNETLoader`、`CLIPLoader`、`VAELoader`、`Anything Everywhere3`、`TextEncodeQwenImage21`、`llama_cpp_model_loader`、`CR Text`、`llama_cpp_instruct_adv`、`PreviewAny`、`ResolutionSelector`、`LoadImage`、`孤海注释`、`LoraLoaderModelOnly`

**缺卡**（3）：`CR Text`、`LayerUtility: ImageReel`、`LayerUtility: ImageReelComposit`

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- 次要节点 `CR Text` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: ImageReel` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: ImageReelComposit` 知识库中没有该节点类型的任何知识
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

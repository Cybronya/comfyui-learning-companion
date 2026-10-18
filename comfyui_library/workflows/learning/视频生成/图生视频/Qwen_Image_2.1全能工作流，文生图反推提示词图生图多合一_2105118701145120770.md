---
key: 视频生成/图生视频/Qwen_Image_2.1全能工作流，文生图反推提示词图生图多合一_2105118701145120770.json
name: Qwen_Image_2.1全能工作流，文生图反推提示词图生图多合一_2105118701145120770
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/Qwen_Image_2.1全能工作流，文生图反推提示词图生图多合一_2105118701145120770.json
hash: aafaf5853313089b
coverage: 0.656863
learned_at: 2026-10-17 22:18:55
nodes: [VAEDecode, LayerUtility: ImageScaleByAspectRatio V2, SetNode, LayerUtility: ImageScaleByAspectRatio V2, SetNode, LayerUtility: ImageScaleByAspectRatio V2, SetNode, LayerUtility: ImageScaleByAspectRatio V2, SetNode, SetNode, LayerUtility: PurgeVRAM V2, LayerUtility: PurgeVRAM V2, SaveImage, UNETLoader, CLIPLoader, VAELoader, GetNode, LayerUtility: ImageScaleByAspectRatio V2, SetNode, LoadImage, LoadImage, easy showAnything, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, QwenImage21Cache, TextEncodeQwenImage21, KSampler, LoadImage, Fast Groups Bypasser (rgthree), LayerUtility: ImageScaleByAspectRatio V2, EmptyLatentImage, GetNode, GetImageSize, SetNode, LayerUtility: ImageScaleByAspectRatio V2, GetNode, CR Text, CR Text, CR Text, SetNode, LoadImage, SetNode, SetNode, GetNode, PreviewImage, CR Text, CR Text, AIO_Preprocessor, llama_cpp_parameters, LoadImage, llama_cpp_instruct_adv, llama_cpp_instruct_adv, llama_cpp_model_loader, llama_cpp_parameters, llama_cpp_model_loader, ki_宫格拼图简易版, PreviewImage, LoadImage, LoadImage, GetNode, Image Comparer (rgthree), CR Text Concatenate, easy showAnything, CR Text, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, KSampler, EmptyLatentImage, JjkText, CLIPTextEncode, CLIPTextEncode, solarL_SaveImagesToZip, VAEDecode, CLIPLoader, VAELoader, Note, EmptyImage, PreviewImage]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/图生视频/Qwen_Image_2.1全能工作流，文生图反推提示词图生图多合一_2105118701145120770.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/Qwen_Image_2.1全能工作流，文生图反推提示词图生图多合一_2105118701145120770.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（102 个）：
- `VAEDecode` ★核心
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
- `UNETLoader` ★核心
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
- `KSampler` ★核心
- `LoadImage`
- `Fast Groups Bypasser (rgthree)`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `EmptyLatentImage` ★核心
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
- `LoadImage`
- `LoadImage`
- `GetNode`
- `Image Comparer (rgthree)`
- `CR Text Concatenate`
- `easy showAnything`
- `CR Text`
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
- `EmptyImage`
- `PreviewImage`

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

覆盖率 **66%**（67/102）

**有卡**：`VAEDecode`、`LayerUtility: ImageScaleByAspectRatio V2`、`LayerUtility: PurgeVRAM V2`、`SaveImage`、`UNETLoader`、`CLIPLoader`、`VAELoader`、`LoadImage`、`QwenImage21Cache`、`TextEncodeQwenImage21`、`KSampler`、`EmptyLatentImage`、`GetImageSize`、`CR Text`、`AIO_Preprocessor`、`llama_cpp_parameters`、`llama_cpp_instruct_adv`、`llama_cpp_model_loader`、`ki_宫格拼图简易版`、`CR Text Concatenate`、`LoraLoaderModelOnly`、`CLIPTextEncode`、`solarL_SaveImagesToZip`、`EmptyImage`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

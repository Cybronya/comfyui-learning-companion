---
key: 图片生成/图生图/Qwen_Image_2.1文生图与图片编辑合一，电商产品图生图多场景适用_2105519436647190529.json
name: Qwen_Image_2.1文生图与图片编辑合一，电商产品图生图多场景适用_2105519436647190529
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen_Image_2.1文生图与图片编辑合一，电商产品图生图多场景适用_2105519436647190529.json
hash: e4b7de6eed6a19e6
coverage: 0.892308
learned_at: 2026-10-21 00:43:57
nodes: [KSampler, VAEDecode, QwenImage21Cache, UNETLoader, llama_cpp_instruct_adv, CLIPLoader, VAELoader, LoadImage, Fast Groups Muter (rgthree), ResolutionSelector, CR Text, EmptyLatentImage, easy boolean, CR Text, ComfySwitchNodeV2, llama_cpp_model_loader, INTConstant, INTConstant, ComfySwitchNodeV2, easy cleanGpuUsed, TextEncodeQwenImage21, XB_BatchImages, Image Comparer (rgthree), LoadImage, Fast Groups Bypasser (rgthree), llama_cpp_instruct_adv, ShowText|pysssss, ComfySwitchNodeV2, ComfySwitchNodeV2, SaveImage, CR Text, CR Text, easy boolean, LoadImage, LoadImage, LoadImage, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, KSampler, EmptyLatentImage, JjkText, CLIPTextEncode, CLIPTextEncode, solarL_SaveImagesToZip, VAEDecode, CLIPLoader, VAELoader, Note, EmptyImage, PreviewImage]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/Qwen_Image_2.1文生图与图片编辑合一，电商产品图生图多场景适用_2105519436647190529.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen_Image_2.1文生图与图片编辑合一，电商产品图生图多场景适用_2105519436647190529.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（65 个）：
- `KSampler` ★核心
- `VAEDecode` ★核心
- `QwenImage21Cache`
- `UNETLoader` ★核心
- `llama_cpp_instruct_adv`
- `CLIPLoader`
- `VAELoader`
- `LoadImage`
- `Fast Groups Muter (rgthree)`
- `ResolutionSelector`
- `CR Text`
- `EmptyLatentImage` ★核心
- `easy boolean`
- `CR Text`
- `ComfySwitchNodeV2`
- `llama_cpp_model_loader`
- `INTConstant`
- `INTConstant`
- `ComfySwitchNodeV2`
- `easy cleanGpuUsed`
- `TextEncodeQwenImage21`
- `XB_BatchImages`
- `Image Comparer (rgthree)`
- `LoadImage`
- `Fast Groups Bypasser (rgthree)`
- `llama_cpp_instruct_adv`
- `ShowText|pysssss`
- `ComfySwitchNodeV2`
- `ComfySwitchNodeV2`
- `SaveImage`
- `CR Text`
- `CR Text`
- `easy boolean`
- `LoadImage`
- `LoadImage`
- `LoadImage`
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

覆盖率 **89%**（58/65）

**有卡**：`KSampler`、`VAEDecode`、`QwenImage21Cache`、`UNETLoader`、`llama_cpp_instruct_adv`、`CLIPLoader`、`VAELoader`、`LoadImage`、`ResolutionSelector`、`CR Text`、`EmptyLatentImage`、`easy boolean`、`ComfySwitchNodeV2`、`llama_cpp_model_loader`、`INTConstant`、`easy cleanGpuUsed`、`TextEncodeQwenImage21`、`XB_BatchImages`、`SaveImage`、`LoraLoaderModelOnly`、`CLIPTextEncode`、`solarL_SaveImagesToZip`、`EmptyImage`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

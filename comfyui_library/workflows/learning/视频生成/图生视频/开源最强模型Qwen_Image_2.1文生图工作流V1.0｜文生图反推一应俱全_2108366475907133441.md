---
key: 视频生成/图生视频/开源最强模型Qwen_Image_2.1文生图工作流V1.0｜文生图反推一应俱全_2108366475907133441.json
name: 开源最强模型Qwen_Image_2.1文生图工作流V1.0｜文生图反推一应俱全_2108366475907133441
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/开源最强模型Qwen_Image_2.1文生图工作流V1.0｜文生图反推一应俱全_2108366475907133441.json
hash: 8188886e9e4734e5
coverage: 0.918919
learned_at: 2026-10-17 22:20:04
nodes: [llama_cpp_parameters, llama_cpp_instruct_adv, LoraLoaderModelOnly, LoraLoaderModelOnly, PathchSageAttentionKJ, LoadImage, CR Prompt Text, llama_cpp_model_loader, PixaromaGroupSwitch, PixaromaGroupSwitch, UNETLoader, CLIPLoader, QwenImage21Cache, SaveImageAdvanced, TextEncodeQwenImage21, KSampler, VAELoader, PixaromaResolution, EmptyLatentImage, KSampler, LoraLoaderModelOnly, Mute / Bypass Repeater (rgthree), Mute / Bypass Repeater (rgthree), VAEDecode, VAEDecode, Fast Bypasser (rgthree), PreviewAny, QwenPERewriteT8, Any Switch (rgthree), Any Switch (rgthree), SaveImage, UNETLoader, CLIPLoader, CLIPTextEncode, VAELoader, EmptyLatentImage, KSampler, VAEDecode, solarL_SaveImagesToZip, JjkText, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, CLIPTextEncode, Note, EmptyImage, PreviewImage]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/图生视频/开源最强模型Qwen_Image_2.1文生图工作流V1.0｜文生图反推一应俱全_2108366475907133441.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/开源最强模型Qwen_Image_2.1文生图工作流V1.0｜文生图反推一应俱全_2108366475907133441.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（74 个）：
- `llama_cpp_parameters`
- `llama_cpp_instruct_adv`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `PathchSageAttentionKJ`
- `LoadImage`
- `CR Prompt Text`
- `llama_cpp_model_loader`
- `PixaromaGroupSwitch`
- `PixaromaGroupSwitch`
- `UNETLoader` ★核心
- `CLIPLoader`
- `QwenImage21Cache`
- `SaveImageAdvanced`
- `TextEncodeQwenImage21`
- `KSampler` ★核心
- `VAELoader`
- `PixaromaResolution`
- `EmptyLatentImage` ★核心
- `KSampler` ★核心
- `LoraLoaderModelOnly` ★核心
- `Mute / Bypass Repeater (rgthree)`
- `Mute / Bypass Repeater (rgthree)`
- `VAEDecode` ★核心
- `VAEDecode` ★核心
- `Fast Bypasser (rgthree)`
- `PreviewAny`
- `QwenPERewriteT8`
- `Any Switch (rgthree)`
- `Any Switch (rgthree)`
- `SaveImage`
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

覆盖率 **92%**（68/74）

**有卡**：`llama_cpp_parameters`、`llama_cpp_instruct_adv`、`LoraLoaderModelOnly`、`PathchSageAttentionKJ`、`LoadImage`、`CR Prompt Text`、`llama_cpp_model_loader`、`PixaromaGroupSwitch`、`UNETLoader`、`CLIPLoader`、`QwenImage21Cache`、`SaveImageAdvanced`、`TextEncodeQwenImage21`、`KSampler`、`VAELoader`、`PixaromaResolution`、`EmptyLatentImage`、`Mute / Bypass Repeater (rgthree)`、`VAEDecode`、`Fast Bypasser (rgthree)`、`QwenPERewriteT8`、`SaveImage`、`CLIPTextEncode`、`solarL_SaveImagesToZip`、`EmptyImage`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage

## 参数体检

发现 2 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

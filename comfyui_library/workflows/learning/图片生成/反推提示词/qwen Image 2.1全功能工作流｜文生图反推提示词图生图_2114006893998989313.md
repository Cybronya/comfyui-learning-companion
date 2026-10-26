---
key: 图片生成/反推提示词/qwen Image 2.1全功能工作流｜文生图反推提示词图生图_2114006893998989313.json
name: qwen Image 2.1全功能工作流｜文生图反推提示词图生图_2114006893998989313
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/反推提示词/qwen Image 2.1全功能工作流｜文生图反推提示词图生图_2114006893998989313.json
hash: 97060b36d9703361
coverage: 0.902439
learned_at: 2026-10-26 22:01:08
nodes: [LayerUtility: ImageReel, LayerUtility: ImageReelComposit, easy setNode, VAEDecode, LoadImage, SaveImage, Anything Everywhere3, LoadImage, PreviewImage, Image Comparer (rgthree), UNETLoader, QwenImage21Cache, CLIPLoader, VAELoader, EmptyLatentImage, ResolutionSelector, llama_cpp_model_loader, llama_cpp_instruct_adv, llama_cpp_parameters, easy showAnything, VAEDecode, KSampler, SaveImage, LoadImage, TextEncodeQwenImage21, RepeatLatentBatch, KSampler, SaveImage, KSampler, TextEncodeQwenImage21, CR Prompt Text, LoadImage, CR Prompt Text, LoadImage, LoadImage, LoadImage, TextEncodeQwenImage21, LoadImage, VAEDecode, 孤海注释, 孤海注释, UNETLoader, CLIPLoader, CLIPTextEncode, VAELoader, EmptyLatentImage, KSampler, VAEDecode, solarL_SaveImagesToZip, JjkText, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, CLIPTextEncode, Note]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/反推提示词/qwen Image 2.1全功能工作流｜文生图反推提示词图生图_2114006893998989313.json

> 来源文件 `comfyui_library/workflows/图片生成/反推提示词/qwen Image 2.1全功能工作流｜文生图反推提示词图生图_2114006893998989313.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（82 个）：
- `LayerUtility: ImageReel`
- `LayerUtility: ImageReelComposit`
- `easy setNode`
- `VAEDecode` ★核心
- `LoadImage`
- `SaveImage`
- `Anything Everywhere3`
- `LoadImage`
- `PreviewImage`
- `Image Comparer (rgthree)`
- `UNETLoader` ★核心
- `QwenImage21Cache`
- `CLIPLoader`
- `VAELoader`
- `EmptyLatentImage` ★核心
- `ResolutionSelector`
- `llama_cpp_model_loader`
- `llama_cpp_instruct_adv`
- `llama_cpp_parameters`
- `easy showAnything`
- `VAEDecode` ★核心
- `KSampler` ★核心
- `SaveImage`
- `LoadImage`
- `TextEncodeQwenImage21`
- `RepeatLatentBatch`
- `KSampler` ★核心
- `SaveImage`
- `KSampler` ★核心
- `TextEncodeQwenImage21`
- `CR Prompt Text`
- `LoadImage`
- `CR Prompt Text`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `TextEncodeQwenImage21`
- `LoadImage`
- `VAEDecode` ★核心
- `孤海注释`
- `孤海注释`
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

覆盖率 **90%**（74/82）

**有卡**：`LayerUtility: ImageReel`、`LayerUtility: ImageReelComposit`、`easy setNode`、`VAEDecode`、`LoadImage`、`SaveImage`、`UNETLoader`、`QwenImage21Cache`、`CLIPLoader`、`VAELoader`、`EmptyLatentImage`、`ResolutionSelector`、`llama_cpp_model_loader`、`llama_cpp_instruct_adv`、`llama_cpp_parameters`、`KSampler`、`TextEncodeQwenImage21`、`RepeatLatentBatch`、`CR Prompt Text`、`CLIPTextEncode`、`solarL_SaveImagesToZip`、`LoraLoaderModelOnly`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

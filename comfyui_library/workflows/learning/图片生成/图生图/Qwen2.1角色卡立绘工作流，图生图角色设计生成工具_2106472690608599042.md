---
key: 图片生成/图生图/Qwen2.1角色卡立绘工作流，图生图角色设计生成工具_2106472690608599042.json
name: Qwen2.1角色卡立绘工作流，图生图角色设计生成工具_2106472690608599042
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen2.1角色卡立绘工作流，图生图角色设计生成工具_2106472690608599042.json
hash: d3127a333d28caa3
coverage: 0.86
learned_at: 2026-10-21 00:43:41
nodes: [VAELoader, TextEncodeQwenImage21, QwenImage21Cache, EmptyLatentImage, SaveImage, UNETLoader, CLIPLoader, ResolutionSelector, llama_cpp_instruct_adv, llama_cpp_parameters, easy clearCacheAll, easy clearCacheAll, llama_cpp_model_loader, LoadImage, PreviewAny, KSampler, JjkText, PreviewImage, easy imageConcat, ImageScaleBy, VAEDecode, 孤海注释, 孤海注释, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, KSampler, EmptyLatentImage, JjkText, CLIPTextEncode, CLIPTextEncode, solarL_SaveImagesToZip, VAEDecode, CLIPLoader, VAELoader, Note]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/Qwen2.1角色卡立绘工作流，图生图角色设计生成工具_2106472690608599042.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen2.1角色卡立绘工作流，图生图角色设计生成工具_2106472690608599042.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（50 个）：
- `VAELoader`
- `TextEncodeQwenImage21`
- `QwenImage21Cache`
- `EmptyLatentImage` ★核心
- `SaveImage`
- `UNETLoader` ★核心
- `CLIPLoader`
- `ResolutionSelector`
- `llama_cpp_instruct_adv`
- `llama_cpp_parameters`
- `easy clearCacheAll`
- `easy clearCacheAll`
- `llama_cpp_model_loader`
- `LoadImage`
- `PreviewAny`
- `KSampler` ★核心
- `JjkText`
- `PreviewImage`
- `easy imageConcat`
- `ImageScaleBy`
- `VAEDecode` ★核心
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

覆盖率 **86%**（43/50）

**有卡**：`VAELoader`、`TextEncodeQwenImage21`、`QwenImage21Cache`、`EmptyLatentImage`、`SaveImage`、`UNETLoader`、`CLIPLoader`、`ResolutionSelector`、`llama_cpp_instruct_adv`、`llama_cpp_parameters`、`easy clearCacheAll`、`llama_cpp_model_loader`、`LoadImage`、`KSampler`、`easy imageConcat`、`ImageScaleBy`、`VAEDecode`、`LoraLoaderModelOnly`、`CLIPTextEncode`、`solarL_SaveImagesToZip`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

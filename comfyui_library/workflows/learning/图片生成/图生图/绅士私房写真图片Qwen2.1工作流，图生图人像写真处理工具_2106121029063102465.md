---
key: 图片生成/图生图/绅士私房写真图片Qwen2.1工作流，图生图人像写真处理工具_2106121029063102465.json
name: 绅士私房写真图片Qwen2.1工作流，图生图人像写真处理工具_2106121029063102465
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/绅士私房写真图片Qwen2.1工作流，图生图人像写真处理工具_2106121029063102465.json
hash: aa2e6fc3ff64919f
coverage: 0.862745
learned_at: 2026-10-21 00:55:40
nodes: [UNETLoader, CLIPLoader, VAELoader, ResolutionSelector, llama_cpp_instruct_adv, llama_cpp_parameters, easy clearCacheAll, easy clearCacheAll, llama_cpp_model_loader, QwenImage21Cache, SaveImage, VAEDecode, PreviewImage, easy imageConcat, TextEncodeQwenImage21, LoadImage, ImageScaleBy, CR Prompt List, PreviewAny, JjkText, KSampler, EmptyLatentImage, 孤海注释, 孤海注释, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, KSampler, EmptyLatentImage, JjkText, CLIPTextEncode, CLIPTextEncode, solarL_SaveImagesToZip, VAEDecode, CLIPLoader, VAELoader, Note]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/绅士私房写真图片Qwen2.1工作流，图生图人像写真处理工具_2106121029063102465.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/绅士私房写真图片Qwen2.1工作流，图生图人像写真处理工具_2106121029063102465.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（51 个）：
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `ResolutionSelector`
- `llama_cpp_instruct_adv`
- `llama_cpp_parameters`
- `easy clearCacheAll`
- `easy clearCacheAll`
- `llama_cpp_model_loader`
- `QwenImage21Cache`
- `SaveImage`
- `VAEDecode` ★核心
- `PreviewImage`
- `easy imageConcat`
- `TextEncodeQwenImage21`
- `LoadImage`
- `ImageScaleBy`
- `CR Prompt List`
- `PreviewAny`
- `JjkText`
- `KSampler` ★核心
- `EmptyLatentImage` ★核心
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

覆盖率 **86%**（44/51）

**有卡**：`UNETLoader`、`CLIPLoader`、`VAELoader`、`ResolutionSelector`、`llama_cpp_instruct_adv`、`llama_cpp_parameters`、`easy clearCacheAll`、`llama_cpp_model_loader`、`QwenImage21Cache`、`SaveImage`、`VAEDecode`、`easy imageConcat`、`TextEncodeQwenImage21`、`LoadImage`、`ImageScaleBy`、`CR Prompt List`、`KSampler`、`EmptyLatentImage`、`LoraLoaderModelOnly`、`CLIPTextEncode`、`solarL_SaveImagesToZip`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

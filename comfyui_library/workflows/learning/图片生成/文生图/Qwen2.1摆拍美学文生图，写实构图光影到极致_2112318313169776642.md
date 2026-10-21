---
key: 图片生成/文生图/Qwen2.1摆拍美学文生图，写实构图光影到极致_2112318313169776642.json
name: Qwen2.1摆拍美学文生图，写实构图光影到极致_2112318313169776642
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Qwen2.1摆拍美学文生图，写实构图光影到极致_2112318313169776642.json
hash: 8886ed51edfe4e98
coverage: 0.903846
learned_at: 2026-10-21 02:54:44
nodes: [UNETLoader, CLIPLoader, VAELoader, KSampler, TextEncodeQwenImage21, EmptyLatentImage, VAEDecode, CR Text, llama_cpp_instruct_adv, JDCN_StringToList, ProcessString, llama_cpp_model_loader, CR Text Replace, PrimitiveInt, llama_cpp_parameters, CR Text, LoadImage, SaveImage, QwenImage21Cache, ResolutionSelector, CR Text, CR Text, CR Text, 孤海注释, 孤海注释, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, KSampler, CLIPTextEncode, CLIPTextEncode, CLIPLoader, JjkText, VAEDecode, EmptyLatentImage, VAELoader, solarL_SaveImagesToZip, Note]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/文生图/Qwen2.1摆拍美学文生图，写实构图光影到极致_2112318313169776642.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Qwen2.1摆拍美学文生图，写实构图光影到极致_2112318313169776642.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（52 个）：
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `KSampler` ★核心
- `TextEncodeQwenImage21`
- `EmptyLatentImage` ★核心
- `VAEDecode` ★核心
- `CR Text`
- `llama_cpp_instruct_adv`
- `JDCN_StringToList`
- `ProcessString`
- `llama_cpp_model_loader`
- `CR Text Replace`
- `PrimitiveInt`
- `llama_cpp_parameters`
- `CR Text`
- `LoadImage`
- `SaveImage`
- `QwenImage21Cache`
- `ResolutionSelector`
- `CR Text`
- `CR Text`
- `CR Text`
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
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `CLIPLoader`
- `JjkText`
- `VAEDecode` ★核心
- `EmptyLatentImage` ★核心
- `VAELoader`
- `solarL_SaveImagesToZip`
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

覆盖率 **90%**（47/52）

**有卡**：`UNETLoader`、`CLIPLoader`、`VAELoader`、`KSampler`、`TextEncodeQwenImage21`、`EmptyLatentImage`、`VAEDecode`、`CR Text`、`llama_cpp_instruct_adv`、`JDCN_StringToList`、`ProcessString`、`llama_cpp_model_loader`、`CR Text Replace`、`llama_cpp_parameters`、`LoadImage`、`SaveImage`、`QwenImage21Cache`、`ResolutionSelector`、`LoraLoaderModelOnly`、`CLIPTextEncode`、`solarL_SaveImagesToZip`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

---
key: 图片生成/文生图/Qwen2.1文图生图提示词增强工作流，文生图人像写真图生图处理方案_2107586964294815746.json
name: Qwen2.1文图生图提示词增强工作流，文生图人像写真图生图处理方案_2107586964294815746
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Qwen2.1文图生图提示词增强工作流，文生图人像写真图生图处理方案_2107586964294815746.json
hash: 8fd1243b170e6367
coverage: 0.88
learned_at: 2026-10-20 01:51:22
nodes: [ConditioningZeroOut, VAELoader, KSampler, easy clearCacheAll, easy saveText, VAEDecode, TextEncodeQwenImage21, TextGenerate, LoadImage, SaveImage, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, ResolutionSelector, PreviewImage, PreviewAny, EmptyLatentImage, CLIPLoader, CLIPLoader, StringConstantMultiline, 孤海注释, 孤海注释, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, KSampler, EmptyLatentImage, JjkText, CLIPTextEncode, CLIPTextEncode, solarL_SaveImagesToZip, VAEDecode, CLIPLoader, VAELoader, Note]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/文生图/Qwen2.1文图生图提示词增强工作流，文生图人像写真图生图处理方案_2107586964294815746.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Qwen2.1文图生图提示词增强工作流，文生图人像写真图生图处理方案_2107586964294815746.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（50 个）：
- `ConditioningZeroOut`
- `VAELoader`
- `KSampler` ★核心
- `easy clearCacheAll`
- `easy saveText`
- `VAEDecode` ★核心
- `TextEncodeQwenImage21`
- `TextGenerate`
- `LoadImage`
- `SaveImage`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `ResolutionSelector`
- `PreviewImage`
- `PreviewAny`
- `EmptyLatentImage` ★核心
- `CLIPLoader`
- `CLIPLoader`
- `StringConstantMultiline`
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

覆盖率 **88%**（44/50）

**有卡**：`ConditioningZeroOut`、`VAELoader`、`KSampler`、`easy clearCacheAll`、`easy saveText`、`VAEDecode`、`TextEncodeQwenImage21`、`TextGenerate`、`LoadImage`、`SaveImage`、`UNETLoader`、`LoraLoaderModelOnly`、`ResolutionSelector`、`EmptyLatentImage`、`CLIPLoader`、`StringConstantMultiline`、`CLIPTextEncode`、`solarL_SaveImagesToZip`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、ConditioningZeroOut

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

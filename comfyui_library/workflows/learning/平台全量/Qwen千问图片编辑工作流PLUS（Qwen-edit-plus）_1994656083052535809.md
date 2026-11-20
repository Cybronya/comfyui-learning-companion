---
key: 平台全量/Qwen千问图片编辑工作流PLUS（Qwen-edit-plus）_1994656083052535809.json
name: Qwen千问图片编辑工作流PLUS（Qwen-edit-plus）_1994656083052535809
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/Qwen千问图片编辑工作流PLUS（Qwen-edit-plus）_1994656083052535809.json
hash: b5884541ecd4131c
coverage: 0.9
learned_at: 2026-11-14 00:53:54
nodes: [LoadImage, ConditioningZeroOut, VAEDecode, SaveImage, VAELoader, UNETLoader, UnetLoaderGGUF, EmptyLatentImage, KSampler, TextEncodeQwenImageEditPlusAdvance_lrzjason, LoraLoaderModelOnly, LoadImage, CLIPLoader, LoraLoaderModelOnly, Note, SaveImage, UpscaleModelLoader, ImageUpscaleWithModel, Image Comparer (rgthree), LoraLoaderModelOnly]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1536, "sampler_name": "euler_ancestral", "scheduler": "simple", "seed": 7, "steps": 5, "width": 1536}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 平台全量/Qwen千问图片编辑工作流PLUS（Qwen-edit-plus）_1994656083052535809.json

> 来源文件 `comfyui_library/workflows/平台全量/Qwen千问图片编辑工作流PLUS（Qwen-edit-plus）_1994656083052535809.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（20 个）：
- `LoadImage`
- `ConditioningZeroOut`
- `VAEDecode` ★核心
- `SaveImage`
- `VAELoader`
- `UNETLoader` ★核心
- `UnetLoaderGGUF` ★核心
- `EmptyLatentImage` ★核心
- `KSampler` ★核心
- `TextEncodeQwenImageEditPlusAdvance_lrzjason`
- `LoraLoaderModelOnly` ★核心
- `LoadImage`
- `CLIPLoader`
- `LoraLoaderModelOnly` ★核心
- `Note`
- `SaveImage`
- `UpscaleModelLoader`
- `ImageUpscaleWithModel`
- `Image Comparer (rgthree)`
- `LoraLoaderModelOnly` ★核心

## 关键参数

- `width` = `1536`
- `height` = `1536`
- `batch_size` = `1`
- `seed` = `7`
- `steps` = `5`
- `cfg` = `1`
- `sampler_name` = `euler_ancestral`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **90%**（18/20）

**有卡**：`LoadImage`、`ConditioningZeroOut`、`VAEDecode`、`SaveImage`、`VAELoader`、`UNETLoader`、`UnetLoaderGGUF`、`EmptyLatentImage`、`KSampler`、`TextEncodeQwenImageEditPlusAdvance_lrzjason`、`LoraLoaderModelOnly`、`CLIPLoader`、`UpscaleModelLoader`、`ImageUpscaleWithModel`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、ConditioningZeroOut、EmptyLatentImage、LoadImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

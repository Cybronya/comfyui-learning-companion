---
key: 图片生成/图生图/Qwen千问图片编辑工作流PLUS（Qwen-edit-plus）_2012389576106582017.json
name: Qwen千问图片编辑工作流PLUS（Qwen-edit-plus）_2012389576106582017
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen千问图片编辑工作流PLUS（Qwen-edit-plus）_2012389576106582017.json
hash: 153a2bbcf18ff264
coverage: 0.9
learned_at: 2026-10-23 11:22:06
nodes: [ConditioningZeroOut, VAEDecode, VAELoader, EmptyLatentImage, LoraLoaderModelOnly, CLIPLoader, LoraLoaderModelOnly, Note, UpscaleModelLoader, ImageUpscaleWithModel, LoraLoaderModelOnly, SaveImage, LoadImage, SaveImage, UNETLoader, UnetLoaderGGUF, LoadImage, TextEncodeQwenImageEditPlusAdvance_lrzjason, KSampler, Image Comparer (rgthree)]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 0.6, "denoise": 1, "height": 1536, "sampler_name": "euler_ancestral", "scheduler": "simple", "seed": 739358437990452, "steps": 5, "width": 1536}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/Qwen千问图片编辑工作流PLUS（Qwen-edit-plus）_2012389576106582017.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen千问图片编辑工作流PLUS（Qwen-edit-plus）_2012389576106582017.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（20 个）：
- `ConditioningZeroOut`
- `VAEDecode` ★核心
- `VAELoader`
- `EmptyLatentImage` ★核心
- `LoraLoaderModelOnly` ★核心
- `CLIPLoader`
- `LoraLoaderModelOnly` ★核心
- `Note`
- `UpscaleModelLoader`
- `ImageUpscaleWithModel`
- `LoraLoaderModelOnly` ★核心
- `SaveImage`
- `LoadImage`
- `SaveImage`
- `UNETLoader` ★核心
- `UnetLoaderGGUF` ★核心
- `LoadImage`
- `TextEncodeQwenImageEditPlusAdvance_lrzjason`
- `KSampler` ★核心
- `Image Comparer (rgthree)`

## 关键参数

- `width` = `1536`
- `height` = `1536`
- `batch_size` = `1`
- `seed` = `739358437990452`
- `steps` = `5`
- `cfg` = `0.6`
- `sampler_name` = `euler_ancestral`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **90%**（18/20）

**有卡**：`ConditioningZeroOut`、`VAEDecode`、`VAELoader`、`EmptyLatentImage`、`LoraLoaderModelOnly`、`CLIPLoader`、`UpscaleModelLoader`、`ImageUpscaleWithModel`、`SaveImage`、`LoadImage`、`UNETLoader`、`UnetLoaderGGUF`、`TextEncodeQwenImageEditPlusAdvance_lrzjason`、`KSampler`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、ConditioningZeroOut、EmptyLatentImage、LoadImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

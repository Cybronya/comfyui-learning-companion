---
key: 图片生成/图生图/提示词行（json格式） 浮云 12.15_2000576227083776002.json
name: 提示词行（json格式） 浮云 12.15_2000576227083776002
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/提示词行（json格式） 浮云 12.15_2000576227083776002.json
hash: 6fb5aefa85a65057
coverage: 0.952381
learned_at: 2026-10-23 13:02:50
nodes: [CR Text Concatenate, CR Text Concatenate, CR Text Concatenate, GetTextFromJson, CR Text Concatenate, easy showAnything, easy promptList, LoadImage, LoadImage, CR Text, RH_Captioner_Pro, CR Text Concatenate, CR Text, GetTextFromJson, GetTextFromJson, GetTextFromJson, easy showAnything, LoadJsonFromText, CR Text, LoraLoaderModelOnly, LoraLoaderModelOnly, CLIPLoader, VAELoader, UNETLoader, LoraLoaderModelOnly, KSampler, TextEncodeQwenImageEdit, ImageConcanate, EmptyLatentImage, ModelSamplingAuraFlow, VAEDecode, easy imageListToImageBatch, ImageFromBatch, ImageConcanate, ImageFromBatch, ImageFromBatch, ImageFromBatch, ImageConcanate, ImageConcanate, ImageConcanate, TextEncodeQwenImageEditPlusAdvance_lrzjason, SaveImage]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1536, "sampler_name": "euler", "scheduler": "beta", "seed": 1, "steps": 8, "width": 1024}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/提示词行（json格式） 浮云 12.15_2000576227083776002.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/提示词行（json格式） 浮云 12.15_2000576227083776002.json`

## 结构

**生成流程**：Model → Latent → Sampling → Decode → Process → Output → Other

**节点**（42 个）：
- `CR Text Concatenate`
- `CR Text Concatenate`
- `CR Text Concatenate`
- `GetTextFromJson`
- `CR Text Concatenate`
- `easy showAnything`
- `easy promptList`
- `LoadImage`
- `LoadImage`
- `CR Text`
- `RH_Captioner_Pro`
- `CR Text Concatenate`
- `CR Text`
- `GetTextFromJson`
- `GetTextFromJson`
- `GetTextFromJson`
- `easy showAnything`
- `LoadJsonFromText`
- `CR Text`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `CLIPLoader`
- `VAELoader`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `KSampler` ★核心
- `TextEncodeQwenImageEdit`
- `ImageConcanate`
- `EmptyLatentImage` ★核心
- `ModelSamplingAuraFlow`
- `VAEDecode` ★核心
- `easy imageListToImageBatch`
- `ImageFromBatch`
- `ImageConcanate`
- `ImageFromBatch`
- `ImageFromBatch`
- `ImageFromBatch`
- `ImageConcanate`
- `ImageConcanate`
- `ImageConcanate`
- `TextEncodeQwenImageEditPlusAdvance_lrzjason`
- `SaveImage`

## 关键参数

- `seed` = `1`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `beta`
- `denoise` = `1`
- `width` = `1024`
- `height` = `1536`
- `batch_size` = `1`

## 知识

覆盖率 **95%**（40/42）

**有卡**：`CR Text Concatenate`、`GetTextFromJson`、`easy promptList`、`LoadImage`、`CR Text`、`RH_Captioner_Pro`、`LoadJsonFromText`、`LoraLoaderModelOnly`、`CLIPLoader`、`VAELoader`、`UNETLoader`、`KSampler`、`TextEncodeQwenImageEdit`、`ImageConcanate`、`EmptyLatentImage`、`ModelSamplingAuraFlow`、`VAEDecode`、`easy imageListToImageBatch`、`ImageFromBatch`、`TextEncodeQwenImageEditPlusAdvance_lrzjason`、`SaveImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、EmptyLatentImage、LoadImage、UNETLoader

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

---
key: 图片生成/图生图/LongCat Edit VS QwenEdit 2509 AIO V5.3_1997646158753411073.json
name: LongCat Edit VS QwenEdit 2509 AIO V5.3_1997646158753411073
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/LongCat Edit VS QwenEdit 2509 AIO V5.3_1997646158753411073.json
hash: f5148de45f59b507
coverage: 0.965517
learned_at: 2026-10-23 11:09:04
nodes: [LongCatImageModelLoader, easy imageConcat, EmptyLatentImage, TextEncodeQwenImageEditPlus, GetImageSizeAndCount, KSampler, TextEncodeQwenImageEditPlus, SaveImage, CR Prompt Text, ImageScaleToTotalPixels, CheckpointLoaderSimple, Float, Note, Text Multiline, LoraLoaderModelOnly, SaveImage, VAEDecode, AddLabel, LongCatImageEdit, LayerUtility: PurgeVRAM, LayerUtility: PurgeVRAM, AddLabel, LoadImage, ImageScaleToTotalPixels, ImageConcanate, SaveImage, SaveImage, AddLabel, ImageConcanate]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 1, "checkpoint": "Qwen-Rapid-AIO-NSFW-v5.3.safetensors", "denoise": 1, "height": 768, "sampler_name": "euler_ancestral", "scheduler": "beta", "seed": 849188784367416, "steps": 8, "width": 768}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/LongCat Edit VS QwenEdit 2509 AIO V5.3_1997646158753411073.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/LongCat Edit VS QwenEdit 2509 AIO V5.3_1997646158753411073.json`

## 结构

**生成流程**：Model → Latent → Sampling → Decode → Process → Output → Other

**节点**（29 个）：
- `LongCatImageModelLoader`
- `easy imageConcat`
- `EmptyLatentImage` ★核心
- `TextEncodeQwenImageEditPlus`
- `GetImageSizeAndCount`
- `KSampler` ★核心
- `TextEncodeQwenImageEditPlus`
- `SaveImage`
- `CR Prompt Text`
- `ImageScaleToTotalPixels`
- `CheckpointLoaderSimple` ★核心
- `Float`
- `Note`
- `Text Multiline`
- `LoraLoaderModelOnly` ★核心
- `SaveImage`
- `VAEDecode` ★核心
- `AddLabel`
- `LongCatImageEdit`
- `LayerUtility: PurgeVRAM`
- `LayerUtility: PurgeVRAM`
- `AddLabel`
- `LoadImage`
- `ImageScaleToTotalPixels`
- `ImageConcanate`
- `SaveImage`
- `SaveImage`
- `AddLabel`
- `ImageConcanate`

## 关键参数

- `width` = `768`
- `height` = `768`
- `batch_size` = `1`
- `seed` = `849188784367416`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `euler_ancestral`
- `scheduler` = `beta`
- `denoise` = `1`
- `checkpoint` = `Qwen-Rapid-AIO-NSFW-v5.3.safetensors`

## 知识

覆盖率 **97%**（28/29）

**有卡**：`LongCatImageModelLoader`、`easy imageConcat`、`EmptyLatentImage`、`TextEncodeQwenImageEditPlus`、`GetImageSizeAndCount`、`KSampler`、`SaveImage`、`CR Prompt Text`、`ImageScaleToTotalPixels`、`CheckpointLoaderSimple`、`Float`、`Text Multiline`、`LoraLoaderModelOnly`、`VAEDecode`、`AddLabel`、`LongCatImageEdit`、`LayerUtility: PurgeVRAM`、`LoadImage`、`ImageConcanate`

**用到的条目**：KSampler、VAEDecode、LoraLoaderModelOnly、CheckpointLoaderSimple、EmptyLatentImage、LoadImage、TextEncodeQwenImageEditPlus、CR Prompt Text

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

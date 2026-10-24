---
key: 图片生成/图生图/AIO V5.3图像编辑王者LongCat Edit_1999826374938554369.json
name: AIO V5.3图像编辑王者LongCat Edit_1999826374938554369
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/AIO V5.3图像编辑王者LongCat Edit_1999826374938554369.json
hash: 16c0a5b100c60b0b
coverage: 1
learned_at: 2026-10-23 10:50:23
nodes: [LongCatImageModelLoader, MemoryCleaner, Text Multiline, Text Multiline, GetImageSizeAndCount, VAEDecode, LayerUtility: PurgeVRAM, EmptyLatentImage, SaveImage, KSampler, ImageScaleToTotalPixels, LoadImage, LoadImage, CheckpointLoaderSimple, ImageScaleToTotalPixels, TextEncodeQwenImageEditPlus, TextEncodeQwenImageEditPlus, LongCatImageEdit, LayerUtility: PurgeVRAM, SaveImage]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 1, "checkpoint": "Qwen-Rapid-AIO-NSFW-v5.3.safetensors", "denoise": 1, "height": 768, "sampler_name": "euler_ancestral", "scheduler": "beta", "seed": 260043968183249, "steps": 8, "width": 768}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/AIO V5.3图像编辑王者LongCat Edit_1999826374938554369.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/AIO V5.3图像编辑王者LongCat Edit_1999826374938554369.json`

## 结构

**生成流程**：Model → Latent → Sampling → Decode → Process → Output → Other

**节点**（20 个）：
- `LongCatImageModelLoader`
- `MemoryCleaner`
- `Text Multiline`
- `Text Multiline`
- `GetImageSizeAndCount`
- `VAEDecode` ★核心
- `LayerUtility: PurgeVRAM`
- `EmptyLatentImage` ★核心
- `SaveImage`
- `KSampler` ★核心
- `ImageScaleToTotalPixels`
- `LoadImage`
- `LoadImage`
- `CheckpointLoaderSimple` ★核心
- `ImageScaleToTotalPixels`
- `TextEncodeQwenImageEditPlus`
- `TextEncodeQwenImageEditPlus`
- `LongCatImageEdit`
- `LayerUtility: PurgeVRAM`
- `SaveImage`

## 关键参数

- `width` = `768`
- `height` = `768`
- `batch_size` = `1`
- `seed` = `260043968183249`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `euler_ancestral`
- `scheduler` = `beta`
- `denoise` = `1`
- `checkpoint` = `Qwen-Rapid-AIO-NSFW-v5.3.safetensors`

## 知识

覆盖率 **100%**（20/20）

**有卡**：`LongCatImageModelLoader`、`MemoryCleaner`、`Text Multiline`、`GetImageSizeAndCount`、`VAEDecode`、`LayerUtility: PurgeVRAM`、`EmptyLatentImage`、`SaveImage`、`KSampler`、`ImageScaleToTotalPixels`、`LoadImage`、`CheckpointLoaderSimple`、`TextEncodeQwenImageEditPlus`、`LongCatImageEdit`

**用到的条目**：KSampler、VAEDecode、CheckpointLoaderSimple、EmptyLatentImage、LoadImage、TextEncodeQwenImageEditPlus、GetImageSizeAndCount、SaveImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

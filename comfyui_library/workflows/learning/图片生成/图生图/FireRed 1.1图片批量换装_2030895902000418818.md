---
key: 图片生成/图生图/FireRed 1.1图片批量换装_2030895902000418818.json
name: FireRed 1.1图片批量换装_2030895902000418818
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/FireRed 1.1图片批量换装_2030895902000418818.json
hash: 335d349d5f0ca4da
coverage: 0.794118
learned_at: 2026-10-23 10:55:24
nodes: [SaveImage, Note, ImageResize+, TextEncodeQwenImageEditPlus, LoadImage, KSampler, Image Comparer (rgthree), VHS_GetImageCount, ImageConcanate, HAIGC_SaveImagesToZip, ImageFromBatch, LayerUtility: PurgeVRAM V2, easy cleanGpuUsed, HAIGC_LoadImagesFromZip, SaveImage, Note, Note, ImageListToBatch+, PreviewImage, easy int, MathExpression|pysssss, easy batchAnything, easy forLoopEnd, ImageResize+, Note, easy forLoopStart, easy showAnything, VAEDecode, TextEncodeQwenImageEditPlusAdvance_lrzjason, CR Text, CLIPLoader, VAELoader, UNETLoader, LoraLoaderModelOnly]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler_ancestral", "scheduler": "simple", "seed": 721841418337982, "steps": 8}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/FireRed 1.1图片批量换装_2030895902000418818.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/FireRed 1.1图片批量换装_2030895902000418818.json`

## 结构

**生成流程**：Model → Sampling → Decode → Process → Output → Other

**节点**（34 个）：
- `SaveImage`
- `Note`
- `ImageResize+`
- `TextEncodeQwenImageEditPlus`
- `LoadImage`
- `KSampler` ★核心
- `Image Comparer (rgthree)`
- `VHS_GetImageCount`
- `ImageConcanate`
- `HAIGC_SaveImagesToZip`
- `ImageFromBatch`
- `LayerUtility: PurgeVRAM V2`
- `easy cleanGpuUsed`
- `HAIGC_LoadImagesFromZip`
- `SaveImage`
- `Note`
- `Note`
- `ImageListToBatch+`
- `PreviewImage`
- `easy int`
- `MathExpression|pysssss`
- `easy batchAnything`
- `easy forLoopEnd`
- `ImageResize+`
- `Note`
- `easy forLoopStart`
- `easy showAnything`
- `VAEDecode` ★核心
- `TextEncodeQwenImageEditPlusAdvance_lrzjason`
- `CR Text`
- `CLIPLoader`
- `VAELoader`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心

## 关键参数

- `seed` = `721841418337982`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `euler_ancestral`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **79%**（27/34）

**有卡**：`SaveImage`、`ImageResize+`、`TextEncodeQwenImageEditPlus`、`LoadImage`、`KSampler`、`VHS_GetImageCount`、`ImageConcanate`、`HAIGC_SaveImagesToZip`、`ImageFromBatch`、`LayerUtility: PurgeVRAM V2`、`easy cleanGpuUsed`、`HAIGC_LoadImagesFromZip`、`ImageListToBatch+`、`easy int`、`MathExpression|pysssss`、`easy batchAnything`、`easy forLoopEnd`、`easy forLoopStart`、`VAEDecode`、`TextEncodeQwenImageEditPlusAdvance_lrzjason`、`CR Text`、`CLIPLoader`、`VAELoader`、`UNETLoader`、`LoraLoaderModelOnly`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、LoadImage、UNETLoader、TextEncodeQwenImageEditPlus

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

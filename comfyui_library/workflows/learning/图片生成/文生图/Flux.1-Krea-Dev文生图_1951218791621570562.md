---
key: 图片生成/文生图/Flux.1-Krea-Dev文生图_1951218791621570562.json
name: Flux.1-Krea-Dev文生图_1951218791621570562
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Flux.1-Krea-Dev文生图_1951218791621570562.json
hash: 27e384e3ace3ab1a
coverage: 0.6875
learned_at: 2026-10-10 20:58:36
nodes: [UNETLoader, DualCLIPLoader, VAELoader, RH_Translator, CLIPTextEncode, easy showAnything, ConditioningZeroOut, LayerUtility: PurgeVRAM V2, SaveImage, EmptyLatentImage, Note, ApplyFBCacheAndSkipBlocks, Note, KSampler, VAEDecode, Text Multiline]
patterns: [text_to_image]
missing: [LayerUtility: PurgeVRAM V2, Text Multiline]
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1920, "sampler_name": "euler", "scheduler": "simple", "seed": 552594972918839, "steps": 25, "width": 1080}
discoveries: [次要节点 `LayerUtility: PurgeVRAM V2` 知识库中没有该节点类型的任何知识, 次要节点 `Text Multiline` 知识库中没有该节点类型的任何知识]
---

# 图片生成/文生图/Flux.1-Krea-Dev文生图_1951218791621570562.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Flux.1-Krea-Dev文生图_1951218791621570562.json`

## 结构

**节点**（16 个）：
- `UNETLoader`
- `DualCLIPLoader`
- `VAELoader`
- `RH_Translator`
- `CLIPTextEncode`
- `easy showAnything`
- `ConditioningZeroOut`
- `LayerUtility: PurgeVRAM V2`
- `SaveImage`
- `EmptyLatentImage`
- `Note`
- `ApplyFBCacheAndSkipBlocks`
- `Note`
- `KSampler`
- `VAEDecode`
- `Text Multiline`

**识别到的模式**：text_to_image

## 关键参数

- `batch_size` = `1`
- `cfg` = `1`
- `denoise` = `1`
- `height` = `1920`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `seed` = `552594972918839`
- `steps` = `25`
- `width` = `1080`

## 知识

覆盖率 **69%**（11/16）

**有卡**：`UNETLoader`、`DualCLIPLoader`、`VAELoader`、`RH_Translator`、`CLIPTextEncode`、`easy showAnything`、`ConditioningZeroOut`、`LayerUtility: PurgeVRAM V2`、`SaveImage`、`EmptyLatentImage`、`Note`

**缺卡**（2）：`LayerUtility: PurgeVRAM V2`、`Text Multiline`

## 学习发现

- 次要节点 `LayerUtility: PurgeVRAM V2` 知识库中没有该节点类型的任何知识
- 次要节点 `Text Multiline` 知识库中没有该节点类型的任何知识

---
key: 图片生成/图生图/F.1图生图车身修复_2079052568524845058.json
name: F.1图生图车身修复_2079052568524845058
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/F.1图生图车身修复_2079052568524845058.json
hash: 17d3450127dffe14
coverage: 0.823529
learned_at: 2026-10-10 20:48:02
nodes: [DualCLIPLoader, VAELoader, ConditioningZeroOut, VAEDecode, UNETLoader, 图像缩放V2_孤海, Image Comparer (rgthree), CLIPTextEncode, KSampler, LoadImage, LoraLoaderModelOnly, AILab_QwenVL, easy showAnything, RepeatLatentBatch, RebatchLatents, VAEEncode, SaveImage]
patterns: [image_to_image]
missing: [图像缩放V2_孤海]
parameters: {"cfg": 1, "denoise": 0.5900000000000001, "sampler_name": "euler", "scheduler": "beta", "seed": 749508725332721, "steps": 25}
discoveries: [次要节点 `图像缩放V2_孤海` 知识库中没有该节点类型的任何知识]
---

# 图片生成/图生图/F.1图生图车身修复_2079052568524845058.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/F.1图生图车身修复_2079052568524845058.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Output → Other

**节点**（17 个）：
- `DualCLIPLoader`
- `VAELoader`
- `ConditioningZeroOut`
- `VAEDecode` ★核心
- `UNETLoader` ★核心
- `图像缩放V2_孤海`
- `Image Comparer (rgthree)`
- `CLIPTextEncode` ★核心
- `KSampler` ★核心
- `LoadImage`
- `LoraLoaderModelOnly` ★核心
- `AILab_QwenVL`
- `easy showAnything`
- `RepeatLatentBatch`
- `RebatchLatents`
- `VAEEncode` ★核心
- `SaveImage`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `749508725332721`
- `steps` = `25`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `beta`
- `denoise` = `0.5900000000000001`

## 知识

覆盖率 **82%**（14/17）

**有卡**：`DualCLIPLoader`、`VAELoader`、`ConditioningZeroOut`、`VAEDecode`、`UNETLoader`、`CLIPTextEncode`、`KSampler`、`LoadImage`、`LoraLoaderModelOnly`、`AILab_QwenVL`、`RepeatLatentBatch`、`RebatchLatents`、`VAEEncode`、`SaveImage`

**缺卡**（1）：`图像缩放V2_孤海`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、ConditioningZeroOut、LoadImage、UNETLoader

## 学习发现

- 次要节点 `图像缩放V2_孤海` 知识库中没有该节点类型的任何知识

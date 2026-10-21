---
key: 图片生成/图生图/Qwen Image 2.1图片编辑加角色定妆照，图生图角色一致性设计方案_2103556787147460610.json
name: Qwen Image 2.1图片编辑加角色定妆照，图生图角色一致性设计方案_2103556787147460610
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen Image 2.1图片编辑加角色定妆照，图生图角色一致性设计方案_2103556787147460610.json
hash: 4d0718de34f02824
coverage: 0.891304
learned_at: 2026-10-21 00:42:31
nodes: [KSampler, VAEDecode, TextEncodeQwenImage21, KSampler, VAEDecode, QwenImage21Cache, VAELoader, EmptyLatentImage, ImageScaleToTotalPixels, CLIPLoader, EmptyLatentImage, ImageStitch, SaveImage, ComfySwitchNode, LoadImage, TextEncodeQwenImage21, UNETLoader, 孤海注释, 孤海注释, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, KSampler, EmptyLatentImage, JjkText, CLIPTextEncode, CLIPTextEncode, solarL_SaveImagesToZip, VAEDecode, CLIPLoader, VAELoader, Note]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/Qwen Image 2.1图片编辑加角色定妆照，图生图角色一致性设计方案_2103556787147460610.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen Image 2.1图片编辑加角色定妆照，图生图角色一致性设计方案_2103556787147460610.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（46 个）：
- `KSampler` ★核心
- `VAEDecode` ★核心
- `TextEncodeQwenImage21`
- `KSampler` ★核心
- `VAEDecode` ★核心
- `QwenImage21Cache`
- `VAELoader`
- `EmptyLatentImage` ★核心
- `ImageScaleToTotalPixels`
- `CLIPLoader`
- `EmptyLatentImage` ★核心
- `ImageStitch`
- `SaveImage`
- `ComfySwitchNode`
- `LoadImage`
- `TextEncodeQwenImage21`
- `UNETLoader` ★核心
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

覆盖率 **89%**（41/46）

**有卡**：`KSampler`、`VAEDecode`、`TextEncodeQwenImage21`、`QwenImage21Cache`、`VAELoader`、`EmptyLatentImage`、`ImageScaleToTotalPixels`、`CLIPLoader`、`ImageStitch`、`SaveImage`、`LoadImage`、`UNETLoader`、`LoraLoaderModelOnly`、`CLIPTextEncode`、`solarL_SaveImagesToZip`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

---
key: 视频生成/图生视频/Minimax_H3_角色替换单人角色直接替换，多人分批次生成+_角色替换_Character_Swap_LoRA_2108742532661334018.json
name: Minimax_H3_角色替换单人角色直接替换，多人分批次生成+_角色替换_Character_Swap_LoRA_2108742532661334018
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/Minimax_H3_角色替换单人角色直接替换，多人分批次生成+_角色替换_Character_Swap_LoRA_2108742532661334018.json
hash: 75521741b5935fe3
coverage: 0.931034
learned_at: 2026-10-18 00:23:43
nodes: [LayerMask: MaskStroke, VAELoader, VAEDecode, TextEncodeQwenImage21, CLIPLoader, EmptyLatentImage, SaveImage, GetImageSize, GrowMaskWithBlur, ImageMaskPreview_Guhai, LoadImage, SaveImage, LayerMask: MaskPreview, KSampler, LoadImage, LoadImage, Int, ImageToMask, JjkText, SaveImage, LayerUtility: RestoreCropBox, UNETLoader, LoraLoaderModelOnly, QwenImage21Cache, LoraLoaderModelOnly, LayerUtility: ImageScaleByAspectRatio, LayerUtility: CropByMask V2, EmptyImage, PreviewImage]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 517684825281892, "steps": 6, "width": 1024}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/图生视频/Minimax_H3_角色替换单人角色直接替换，多人分批次生成+_角色替换_Character_Swap_LoRA_2108742532661334018.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/Minimax_H3_角色替换单人角色直接替换，多人分批次生成+_角色替换_Character_Swap_LoRA_2108742532661334018.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（29 个）：
- `LayerMask: MaskStroke`
- `VAELoader`
- `VAEDecode` ★核心
- `TextEncodeQwenImage21`
- `CLIPLoader`
- `EmptyLatentImage` ★核心
- `SaveImage`
- `GetImageSize`
- `GrowMaskWithBlur`
- `ImageMaskPreview_Guhai`
- `LoadImage`
- `SaveImage`
- `LayerMask: MaskPreview`
- `KSampler` ★核心
- `LoadImage`
- `LoadImage`
- `Int`
- `ImageToMask`
- `JjkText`
- `SaveImage`
- `LayerUtility: RestoreCropBox`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `QwenImage21Cache`
- `LoraLoaderModelOnly` ★核心
- `LayerUtility: ImageScaleByAspectRatio`
- `LayerUtility: CropByMask V2`
- `EmptyImage`
- `PreviewImage`

## 关键参数

- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`
- `seed` = `517684825281892`
- `steps` = `6`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **93%**（27/29）

**有卡**：`LayerMask: MaskStroke`、`VAELoader`、`VAEDecode`、`TextEncodeQwenImage21`、`CLIPLoader`、`EmptyLatentImage`、`SaveImage`、`GetImageSize`、`GrowMaskWithBlur`、`ImageMaskPreview_Guhai`、`LoadImage`、`LayerMask: MaskPreview`、`KSampler`、`Int`、`ImageToMask`、`LayerUtility: RestoreCropBox`、`UNETLoader`、`LoraLoaderModelOnly`、`QwenImage21Cache`、`LayerUtility: ImageScaleByAspectRatio`、`LayerUtility: CropByMask V2`、`EmptyImage`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、CLIPLoader、EmptyLatentImage、LoadImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

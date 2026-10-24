---
key: 图片生成/图生图/多角度转换-Qwen image2.1图像编辑_2108180448810725378.json
name: 多角度转换-Qwen image2.1图像编辑_2108180448810725378
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/多角度转换-Qwen image2.1图像编辑_2108180448810725378.json
hash: e232819d1537ef3c
coverage: 0.652174
learned_at: 2026-10-23 12:46:15
nodes: [GetNode, VAELoader, GetNode, TextEncodeQwenImage21, QwenImage21Cache, EmptyLatentImage, LoraLoaderModelOnly, LoraLoaderModelOnly, KSampler, VAEDecode, SaveImageAdvanced, ResolutionSelector, ImageResizeKJv2, SetNode, SetNode, SetNode, CR Text, CR Text Concatenate, ShowText|pysssss, GetNode, UNETLoader, CLIPLoader, GetNode, LayerUtility: ImageRemoveAlpha, SaveImage, Image Comparer (rgthree), ttN concat, CR Text, CR Text, CR Text, CR Text, CR Text, ImpactSwitch, ImpactSwitch, CR Text, CR Text, CR Text, CR Text, CR Text, ImpactSwitch, MarkdownNote, CR Text, MarkdownNote, MarkdownNote, MarkdownNote, LoadImage]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "deis_2m", "scheduler": "simple", "seed": 889866864724872, "steps": 40, "width": 1024}
---

# 图片生成/图生图/多角度转换-Qwen image2.1图像编辑_2108180448810725378.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/多角度转换-Qwen image2.1图像编辑_2108180448810725378.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（46 个）：
- `GetNode`
- `VAELoader`
- `GetNode`
- `TextEncodeQwenImage21`
- `QwenImage21Cache`
- `EmptyLatentImage` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `KSampler` ★核心
- `VAEDecode` ★核心
- `SaveImageAdvanced`
- `ResolutionSelector`
- `ImageResizeKJv2`
- `SetNode`
- `SetNode`
- `SetNode`
- `CR Text`
- `CR Text Concatenate`
- `ShowText|pysssss`
- `GetNode`
- `UNETLoader` ★核心
- `CLIPLoader`
- `GetNode`
- `LayerUtility: ImageRemoveAlpha`
- `SaveImage`
- `Image Comparer (rgthree)`
- `ttN concat`
- `CR Text`
- `CR Text`
- `CR Text`
- `CR Text`
- `CR Text`
- `ImpactSwitch`
- `ImpactSwitch`
- `CR Text`
- `CR Text`
- `CR Text`
- `CR Text`
- `CR Text`
- `ImpactSwitch`
- `MarkdownNote`
- `CR Text`
- `MarkdownNote`
- `MarkdownNote`
- `MarkdownNote`
- `LoadImage`

## 关键参数

- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`
- `seed` = `889866864724872`
- `steps` = `40`
- `cfg` = `1`
- `sampler_name` = `deis_2m`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **65%**（30/46）

**有卡**：`VAELoader`、`TextEncodeQwenImage21`、`QwenImage21Cache`、`EmptyLatentImage`、`LoraLoaderModelOnly`、`KSampler`、`VAEDecode`、`SaveImageAdvanced`、`ResolutionSelector`、`ImageResizeKJv2`、`CR Text`、`CR Text Concatenate`、`UNETLoader`、`CLIPLoader`、`LayerUtility: ImageRemoveAlpha`、`SaveImage`、`ttN concat`、`LoadImage`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、CLIPLoader、EmptyLatentImage、ResolutionSelector

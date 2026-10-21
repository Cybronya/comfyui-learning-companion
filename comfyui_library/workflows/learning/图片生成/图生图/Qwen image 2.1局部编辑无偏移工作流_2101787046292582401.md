---
key: 图片生成/图生图/Qwen image 2.1局部编辑无偏移工作流_2101787046292582401.json
name: Qwen image 2.1局部编辑无偏移工作流_2101787046292582401
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen image 2.1局部编辑无偏移工作流_2101787046292582401.json
hash: 44b7eeff2e3b1e95
coverage: 0.807692
learned_at: 2026-10-21 00:43:01
nodes: [ResizeMask, GetImageSize, VAEEncode, ImageScale, SetLatentNoiseMask, ImageScaleToMaxDimension, Image Comparer (rgthree), GetNode, VAEDecode, VAEEncode, UNETLoader, VAELoader, CLIPLoader, SetNode, GrowMaskWithBlur, Fast Groups Bypasser (rgthree), KSamplerAdvanced, ImpactInt, TextEncodeQwenImage21, Note, LoadImage, Text, LoadImage, LoadImage, VAEDecode, SaveImage]
patterns: []
missing: []
parameters: {"cfg": 30, "denoise": "simple", "sampler_name": 1, "scheduler": "euler", "seed": "enable", "steps": "randomize"}
---

# 图片生成/图生图/Qwen image 2.1局部编辑无偏移工作流_2101787046292582401.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen image 2.1局部编辑无偏移工作流_2101787046292582401.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（26 个）：
- `ResizeMask`
- `GetImageSize`
- `VAEEncode` ★核心
- `ImageScale`
- `SetLatentNoiseMask`
- `ImageScaleToMaxDimension`
- `Image Comparer (rgthree)`
- `GetNode`
- `VAEDecode` ★核心
- `VAEEncode` ★核心
- `UNETLoader` ★核心
- `VAELoader`
- `CLIPLoader`
- `SetNode`
- `GrowMaskWithBlur`
- `Fast Groups Bypasser (rgthree)`
- `KSamplerAdvanced` ★核心
- `ImpactInt`
- `TextEncodeQwenImage21`
- `Note`
- `LoadImage`
- `Text`
- `LoadImage`
- `LoadImage`
- `VAEDecode` ★核心
- `SaveImage`

## 关键参数

- `seed` = `enable`
- `steps` = `randomize`
- `cfg` = `30`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `simple`

## 知识

覆盖率 **81%**（21/26）

**有卡**：`ResizeMask`、`GetImageSize`、`VAEEncode`、`ImageScale`、`SetLatentNoiseMask`、`ImageScaleToMaxDimension`、`VAEDecode`、`UNETLoader`、`VAELoader`、`CLIPLoader`、`GrowMaskWithBlur`、`KSamplerAdvanced`、`ImpactInt`、`TextEncodeQwenImage21`、`LoadImage`、`Text`、`SaveImage`

**用到的条目**：VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、LoadImage、UNETLoader、KSamplerAdvanced、SetLatentNoiseMask

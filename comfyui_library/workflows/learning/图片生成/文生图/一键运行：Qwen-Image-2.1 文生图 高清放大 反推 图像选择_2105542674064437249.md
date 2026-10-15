---
key: 图片生成/文生图/一键运行：Qwen-Image-2.1 文生图 高清放大 反推 图像选择_2105542674064437249.json
name: 一键运行：Qwen-Image-2.1 文生图 高清放大 反推 图像选择_2105542674064437249
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/一键运行：Qwen-Image-2.1 文生图 高清放大 反推 图像选择_2105542674064437249.json
hash: a0e2d49db878d4ee
coverage: 0.617021
learned_at: 2026-10-15 23:01:59
nodes: [LayerFilter: HDREffects, SetNode, GetNode, SetNode, GetNode, GetNode, SetNode, GetNode, GetNode, SetNode, ImageCaptionNode, CR Seed, Note, CR Text Input Switch (4 way), KSampler (Efficient), SetNode, VAELoader, ConditioningZeroOut, CLIPLoader, ShowText|pysssss, Fast Groups Bypasser (rgthree), EmptySD3LatentImage, Note, Label (rgthree), Label (rgthree), VOSR2Upscale, VOSR2ModelLoader, Image Comparer (rgthree), SaveImage, ResolutionSelector, EmptySD3LatentImage, CR Latent Input Switch, LoadImage, PreviewImage, UNETLoader, LoraLoaderModelOnly, TESpeedQwenImage21, SplitImageWithAlpha, easy imageChooser, SaveImage, Text Multiline, SetNode, TextEncodeQwenImage21, GetNode, easy positive, TextGenerate, CLIPLoader]
patterns: []
missing: []
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 403214011463433, "steps": 25}
---

# 图片生成/文生图/一键运行：Qwen-Image-2.1 文生图 高清放大 反推 图像选择_2105542674064437249.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/一键运行：Qwen-Image-2.1 文生图 高清放大 反推 图像选择_2105542674064437249.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Process → Output → Other

**节点**（47 个）：
- `LayerFilter: HDREffects`
- `SetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `ImageCaptionNode`
- `CR Seed`
- `Note`
- `CR Text Input Switch (4 way)`
- `KSampler (Efficient)` ★核心
- `SetNode`
- `VAELoader`
- `ConditioningZeroOut`
- `CLIPLoader`
- `ShowText|pysssss`
- `Fast Groups Bypasser (rgthree)`
- `EmptySD3LatentImage`
- `Note`
- `Label (rgthree)`
- `Label (rgthree)`
- `VOSR2Upscale`
- `VOSR2ModelLoader`
- `Image Comparer (rgthree)`
- `SaveImage`
- `ResolutionSelector`
- `EmptySD3LatentImage`
- `CR Latent Input Switch`
- `LoadImage`
- `PreviewImage`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `TESpeedQwenImage21`
- `SplitImageWithAlpha`
- `easy imageChooser`
- `SaveImage`
- `Text Multiline`
- `SetNode`
- `TextEncodeQwenImage21`
- `GetNode`
- `easy positive`
- `TextGenerate`
- `CLIPLoader`

## 关键参数

- `seed` = `403214011463433`
- `steps` = `25`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **62%**（29/47）

**有卡**：`LayerFilter: HDREffects`、`ImageCaptionNode`、`CR Seed`、`CR Text Input Switch (4 way)`、`KSampler (Efficient)`、`VAELoader`、`ConditioningZeroOut`、`CLIPLoader`、`EmptySD3LatentImage`、`Label (rgthree)`、`VOSR2Upscale`、`VOSR2ModelLoader`、`SaveImage`、`ResolutionSelector`、`CR Latent Input Switch`、`LoadImage`、`UNETLoader`、`LoraLoaderModelOnly`、`TESpeedQwenImage21`、`SplitImageWithAlpha`、`easy imageChooser`、`Text Multiline`、`TextEncodeQwenImage21`、`easy positive`、`TextGenerate`

**用到的条目**：TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、CLIPLoader、ConditioningZeroOut、ResolutionSelector、LoadImage、UNETLoader

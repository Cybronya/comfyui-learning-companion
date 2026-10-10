---
key: 一键运行：Qwen-Image-2.1 文生图 高清放大 反推 图像选择_2105542674064437249.json
name: 一键运行：Qwen-Image-2.1 文生图 高清放大 反推 图像选择_2105542674064437249
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/一键运行：Qwen-Image-2.1 文生图 高清放大 反推 图像选择_2105542674064437249.json
hash: a0e2d49db878d4ee
coverage: 0.361702
learned_at: 2026-10-10 20:59:33
nodes: [LayerFilter: HDREffects, SetNode, GetNode, SetNode, GetNode, GetNode, SetNode, GetNode, GetNode, SetNode, ImageCaptionNode, CR Seed, Note, CR Text Input Switch (4 way), KSampler (Efficient), SetNode, VAELoader, ConditioningZeroOut, CLIPLoader, ShowText|pysssss, Fast Groups Bypasser (rgthree), EmptySD3LatentImage, Note, Label (rgthree), Label (rgthree), VOSR2Upscale, VOSR2ModelLoader, Image Comparer (rgthree), SaveImage, ResolutionSelector, EmptySD3LatentImage, CR Latent Input Switch, LoadImage, PreviewImage, UNETLoader, LoraLoaderModelOnly, TESpeedQwenImage21, SplitImageWithAlpha, easy imageChooser, SaveImage, Text Multiline, SetNode, TextEncodeQwenImage21, GetNode, easy positive, TextGenerate, CLIPLoader]
patterns: []
missing: [CR Text Input Switch (4 way), ImageCaptionNode, Label (rgthree), Label (rgthree), LayerFilter: HDREffects, TESpeedQwenImage21, Text Multiline, easy imageChooser, easy positive, KSampler (Efficient), CR Latent Input Switch, CR Seed]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 403214011463433, "steps": 25}
discoveries: [次要节点 `CR Text Input Switch (4 way)` 知识库中没有该节点类型的任何知识, 次要节点 `ImageCaptionNode` 知识库中没有该节点类型的任何知识, 次要节点 `Label (rgthree)` 知识库中没有该节点类型的任何知识, 次要节点 `Label (rgthree)` 知识库中没有该节点类型的任何知识, 次要节点 `LayerFilter: HDREffects` 知识库中没有该节点类型的任何知识, 次要节点 `TESpeedQwenImage21` 知识库中没有该节点类型的任何知识, 次要节点 `Text Multiline` 知识库中没有该节点类型的任何知识, 次要节点 `easy imageChooser` 知识库中没有该节点类型的任何知识, 次要节点 `easy positive` 知识库中没有该节点类型的任何知识, 核心节点 `KSampler (Efficient)` 仅有 KSampler 的通用知识，没有该节点自己的说明, 次要节点 `CR Latent Input Switch` 仅有 VAE 的通用知识，没有该节点自己的说明, 次要节点 `CR Seed` 仅有 KSampler 的通用知识，没有该节点自己的说明]
---

# 一键运行：Qwen-Image-2.1 文生图 高清放大 反推 图像选择_2105542674064437249.json

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

覆盖率 **36%**（17/47）

**有卡**：`VAELoader`、`ConditioningZeroOut`、`CLIPLoader`、`EmptySD3LatentImage`、`VOSR2Upscale`、`VOSR2ModelLoader`、`SaveImage`、`ResolutionSelector`、`LoadImage`、`UNETLoader`、`LoraLoaderModelOnly`、`SplitImageWithAlpha`、`TextEncodeQwenImage21`、`TextGenerate`

**缺卡**（12）：`CR Text Input Switch (4 way)`、`ImageCaptionNode`、`Label (rgthree)`、`Label (rgthree)`、`LayerFilter: HDREffects`、`TESpeedQwenImage21`、`Text Multiline`、`easy imageChooser`、`easy positive`、`KSampler (Efficient)`、`CR Latent Input Switch`、`CR Seed`

**用到的条目**：TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、CLIPLoader、ConditioningZeroOut、ResolutionSelector、LoadImage、UNETLoader

## 学习发现

- 次要节点 `CR Text Input Switch (4 way)` 知识库中没有该节点类型的任何知识
- 次要节点 `ImageCaptionNode` 知识库中没有该节点类型的任何知识
- 次要节点 `Label (rgthree)` 知识库中没有该节点类型的任何知识
- 次要节点 `Label (rgthree)` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerFilter: HDREffects` 知识库中没有该节点类型的任何知识
- 次要节点 `TESpeedQwenImage21` 知识库中没有该节点类型的任何知识
- 次要节点 `Text Multiline` 知识库中没有该节点类型的任何知识
- 次要节点 `easy imageChooser` 知识库中没有该节点类型的任何知识
- 次要节点 `easy positive` 知识库中没有该节点类型的任何知识
- 核心节点 `KSampler (Efficient)` 仅有 KSampler 的通用知识，没有该节点自己的说明
- 次要节点 `CR Latent Input Switch` 仅有 VAE 的通用知识，没有该节点自己的说明
- 次要节点 `CR Seed` 仅有 KSampler 的通用知识，没有该节点自己的说明

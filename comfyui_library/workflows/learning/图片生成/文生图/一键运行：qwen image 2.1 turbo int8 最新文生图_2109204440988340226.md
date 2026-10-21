---
key: 图片生成/文生图/一键运行：qwen image 2.1 turbo int8 最新文生图_2109204440988340226.json
name: 一键运行：qwen image 2.1 turbo int8 最新文生图_2109204440988340226
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/一键运行：qwen image 2.1 turbo int8 最新文生图_2109204440988340226.json
hash: 71b12e7f9d758262
coverage: 0.607843
learned_at: 2026-10-21 02:58:16
nodes: [LayerFilter: HDREffects, SetNode, SetNode, GetNode, GetNode, SetNode, GetNode, SetNode, GetNode, GetNode, SetNode, ImageCaptionNode, Note, CR Text Input Switch (4 way), SetNode, VAELoader, CLIPLoader, SetNode, ShowText|pysssss, Fast Groups Bypasser (rgthree), EmptySD3LatentImage, Note, Label (rgthree), Text Multiline, TextGenerate, easy positive, TextEncodeQwenImage21, VOSR2Upscale, VOSR2ModelLoader, Image Comparer (rgthree), SaveImage, GetNode, ResolutionSelector, EmptySD3LatentImage, CR Latent Input Switch, LoadImage, RandomNoise, KSamplerSelect, SamplerCustomAdvanced, ManualSigmas, VAEDecode, GetNode, PreviewTextNode, LoraLoaderModelOnly, CLIPLoader, BasicGuider, UNETLoader, PreviewImage, SplitImageWithAlpha, easy imageChooser, Label (rgthree)]
patterns: []
missing: []
---

# 图片生成/文生图/一键运行：qwen image 2.1 turbo int8 最新文生图_2109204440988340226.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/一键运行：qwen image 2.1 turbo int8 最新文生图_2109204440988340226.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（51 个）：
- `LayerFilter: HDREffects`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `ImageCaptionNode`
- `Note`
- `CR Text Input Switch (4 way)`
- `SetNode`
- `VAELoader`
- `CLIPLoader`
- `SetNode`
- `ShowText|pysssss`
- `Fast Groups Bypasser (rgthree)`
- `EmptySD3LatentImage`
- `Note`
- `Label (rgthree)`
- `Text Multiline`
- `TextGenerate`
- `easy positive`
- `TextEncodeQwenImage21`
- `VOSR2Upscale`
- `VOSR2ModelLoader`
- `Image Comparer (rgthree)`
- `SaveImage`
- `GetNode`
- `ResolutionSelector`
- `EmptySD3LatentImage`
- `CR Latent Input Switch`
- `LoadImage`
- `RandomNoise`
- `KSamplerSelect` ★核心
- `SamplerCustomAdvanced` ★核心
- `ManualSigmas`
- `VAEDecode` ★核心
- `GetNode`
- `PreviewTextNode`
- `LoraLoaderModelOnly` ★核心
- `CLIPLoader`
- `BasicGuider`
- `UNETLoader` ★核心
- `PreviewImage`
- `SplitImageWithAlpha`
- `easy imageChooser`
- `Label (rgthree)`

## 知识

覆盖率 **61%**（31/51）

**有卡**：`LayerFilter: HDREffects`、`ImageCaptionNode`、`CR Text Input Switch (4 way)`、`VAELoader`、`CLIPLoader`、`EmptySD3LatentImage`、`Label (rgthree)`、`Text Multiline`、`TextGenerate`、`easy positive`、`TextEncodeQwenImage21`、`VOSR2Upscale`、`VOSR2ModelLoader`、`SaveImage`、`ResolutionSelector`、`CR Latent Input Switch`、`LoadImage`、`RandomNoise`、`KSamplerSelect`、`SamplerCustomAdvanced`、`ManualSigmas`、`VAEDecode`、`PreviewTextNode`、`LoraLoaderModelOnly`、`BasicGuider`、`UNETLoader`、`SplitImageWithAlpha`、`easy imageChooser`

**用到的条目**：VAEDecode、TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、CLIPLoader、ResolutionSelector、LoadImage、UNETLoader

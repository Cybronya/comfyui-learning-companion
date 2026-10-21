---
key: 图片生成/文生图/001-flux3_klein_distilled-qwen2.1_2111797689225662466.json
name: 001-flux3_klein_distilled-qwen2.1_2111797689225662466
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/001-flux3_klein_distilled-qwen2.1_2111797689225662466.json
hash: 806db4c5138fbbcf
coverage: 0.659091
learned_at: 2026-10-21 02:50:48
nodes: [ResolutionSelector, Note, CreateBoundingBoxes, PreviewAny, Flux3LayoutPrompt, MarkdownNote, PrimitiveStringMultiline, PrimitiveStringMultiline, TextGenerate, PreviewAny, EmptyFlux2LatentImage, VAEDecode, KSamplerAdvanced, CR Seed, ModelAttentionBackend, RandomNoise, BasicGuider, TextEncodeQwenImage21, KSamplerSelect, SamplerCustomAdvanced, ManualSigmas, EmptyLatentImage, VAEDecode, ModelAttentionBackend, PreviewImage, Image Comparer (rgthree), PreviewImage, Image Comparer (rgthree), Image Comparer (rgthree), Image Comparer (rgthree), Image Comparer (rgthree), Image Comparer (rgthree), Image Comparer (rgthree), CLIPTextEncode, CLIPTextEncode, UNETLoader, CLIPLoader, VAELoader, CLIPLoader, UNETLoader, CLIPLoader, VAELoader, SaveImage, SaveImage]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 16, "denoise": "simple", "height": 1344, "sampler_name": 1, "scheduler": "euler", "seed": "enable", "steps": "fixed", "width": 960}
---

# 图片生成/文生图/001-flux3_klein_distilled-qwen2.1_2111797689225662466.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/001-flux3_klein_distilled-qwen2.1_2111797689225662466.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（44 个）：
- `ResolutionSelector`
- `Note`
- `CreateBoundingBoxes`
- `PreviewAny`
- `Flux3LayoutPrompt`
- `MarkdownNote`
- `PrimitiveStringMultiline`
- `PrimitiveStringMultiline`
- `TextGenerate`
- `PreviewAny`
- `EmptyFlux2LatentImage`
- `VAEDecode` ★核心
- `KSamplerAdvanced` ★核心
- `CR Seed`
- `ModelAttentionBackend`
- `RandomNoise`
- `BasicGuider`
- `TextEncodeQwenImage21`
- `KSamplerSelect` ★核心
- `SamplerCustomAdvanced` ★核心
- `ManualSigmas`
- `EmptyLatentImage` ★核心
- `VAEDecode` ★核心
- `ModelAttentionBackend`
- `PreviewImage`
- `Image Comparer (rgthree)`
- `PreviewImage`
- `Image Comparer (rgthree)`
- `Image Comparer (rgthree)`
- `Image Comparer (rgthree)`
- `Image Comparer (rgthree)`
- `Image Comparer (rgthree)`
- `Image Comparer (rgthree)`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `CLIPLoader`
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `SaveImage`
- `SaveImage`

## 关键参数

- `seed` = `enable`
- `steps` = `fixed`
- `cfg` = `16`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `simple`
- `width` = `960`
- `height` = `1344`
- `batch_size` = `1`

## 知识

覆盖率 **66%**（29/44）

**有卡**：`ResolutionSelector`、`CreateBoundingBoxes`、`Flux3LayoutPrompt`、`TextGenerate`、`EmptyFlux2LatentImage`、`VAEDecode`、`KSamplerAdvanced`、`CR Seed`、`ModelAttentionBackend`、`RandomNoise`、`BasicGuider`、`TextEncodeQwenImage21`、`KSamplerSelect`、`SamplerCustomAdvanced`、`ManualSigmas`、`EmptyLatentImage`、`CLIPTextEncode`、`UNETLoader`、`CLIPLoader`、`VAELoader`、`SaveImage`

**用到的条目**：VAEDecode、TextEncodeQwenImage21、VAELoader、UNETLoader、CLIPTextEncode、CLIPLoader、EmptyLatentImage、ResolutionSelector

---
key: 图片生成/图生图/Qwen Image 2.1文生图+图片编辑-实用版_2102374646296440834.json
name: Qwen Image 2.1文生图+图片编辑-实用版_2102374646296440834
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen Image 2.1文生图+图片编辑-实用版_2102374646296440834.json
hash: 4d172726e2b944a2
coverage: 0.858491
learned_at: 2026-10-15 22:25:16
nodes: [MarkdownNote, VAELoader, KSampler, CLIPLoader, VAELoader, KSampler, ConditioningZeroOut, EmptySD3LatentImage, VAELoader, CLIPLoader, EmptyLatentImage, VAEDecode, VAEDecode, VAEDecode, KSampler, UNETLoader, LoraLoaderModelOnly, CLIPTextEncode, ConditioningZeroOut, AddLabel, SaveImage, Seed (rgthree), ModelSamplingAuraFlow, UNETLoader, TextEncodeQwenImage21, AddLabel, BatchImagesNode, CLIPTextEncode, ImagesConcanateToGrid, AddLabel, ResolutionSelector, SaveImage, SaveImage, UNETLoader, CLIPLoader, easy promptList, TextGenerateLTX2Prompt, AILab_QwenVL, TextEncodeQwenImage21, EmptyLatentImage, KSampler, VAEDecode, PrimitiveStringMultiline, SaveImage, LoadImage, PreviewAny, MarkdownNote, Label (rgthree), Label (rgthree), Label (rgthree), Label (rgthree), CLIPLoader, UNETLoader, Label (rgthree), Label (rgthree), KSampler, QwenImage21Cache, CLIPLoader, TextEncodeQwenImage21, VAELoader, CLIPLoader, TextGenerateLTX2Prompt, GetImageSize, EmptyLatentImage, VAEDecode, SaveImage, Image Comparer (rgthree), Label (rgthree), Label (rgthree), UNETLoader, CLIPLoader, VAELoader, ResolutionSelector, CLIPLoader, SaveImage, PrimitiveStringMultiline, Note, easy anythingIndexSwitch, PreviewAny, ComfySwitchNode, PreviewAny, Label (rgthree), LoadImage, LoadImage, LoadImage, UNETLoader, CLIPLoader, VAELoader, PrimitiveStringMultiline, TextEncodeQwenImage21, GetImageSize, EmptyLatentImage, QwenImage21Cache, KSampler, VAEDecode, SaveImage, Image Comparer (rgthree), LoadImage, PrimitiveStringMultiline, BatchImagesNode, ResolutionSelector, LoadImage, LoadImage, PreviewAny, ComfySwitchNode, TextGenerateLTX2Prompt]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 965300904929997, "steps": 25, "width": 1024}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/Qwen Image 2.1文生图+图片编辑-实用版_2102374646296440834.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen Image 2.1文生图+图片编辑-实用版_2102374646296440834.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（106 个）：
- `MarkdownNote`
- `VAELoader`
- `KSampler` ★核心
- `CLIPLoader`
- `VAELoader`
- `KSampler` ★核心
- `ConditioningZeroOut`
- `EmptySD3LatentImage`
- `VAELoader`
- `CLIPLoader`
- `EmptyLatentImage` ★核心
- `VAEDecode` ★核心
- `VAEDecode` ★核心
- `VAEDecode` ★核心
- `KSampler` ★核心
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `CLIPTextEncode` ★核心
- `ConditioningZeroOut`
- `AddLabel`
- `SaveImage`
- `Seed (rgthree)`
- `ModelSamplingAuraFlow`
- `UNETLoader` ★核心
- `TextEncodeQwenImage21`
- `AddLabel`
- `BatchImagesNode`
- `CLIPTextEncode` ★核心
- `ImagesConcanateToGrid`
- `AddLabel`
- `ResolutionSelector`
- `SaveImage`
- `SaveImage`
- `UNETLoader` ★核心
- `CLIPLoader`
- `easy promptList`
- `TextGenerateLTX2Prompt`
- `AILab_QwenVL`
- `TextEncodeQwenImage21`
- `EmptyLatentImage` ★核心
- `KSampler` ★核心
- `VAEDecode` ★核心
- `PrimitiveStringMultiline`
- `SaveImage`
- `LoadImage`
- `PreviewAny`
- `MarkdownNote`
- `Label (rgthree)`
- `Label (rgthree)`
- `Label (rgthree)`
- `Label (rgthree)`
- `CLIPLoader`
- `UNETLoader` ★核心
- `Label (rgthree)`
- `Label (rgthree)`
- `KSampler` ★核心
- `QwenImage21Cache`
- `CLIPLoader`
- `TextEncodeQwenImage21`
- `VAELoader`
- `CLIPLoader`
- `TextGenerateLTX2Prompt`
- `GetImageSize`
- `EmptyLatentImage` ★核心
- `VAEDecode` ★核心
- `SaveImage`
- `Image Comparer (rgthree)`
- `Label (rgthree)`
- `Label (rgthree)`
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `ResolutionSelector`
- `CLIPLoader`
- `SaveImage`
- `PrimitiveStringMultiline`
- `Note`
- `easy anythingIndexSwitch`
- `PreviewAny`
- `ComfySwitchNode`
- `PreviewAny`
- `Label (rgthree)`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `PrimitiveStringMultiline`
- `TextEncodeQwenImage21`
- `GetImageSize`
- `EmptyLatentImage` ★核心
- `QwenImage21Cache`
- `KSampler` ★核心
- `VAEDecode` ★核心
- `SaveImage`
- `Image Comparer (rgthree)`
- `LoadImage`
- `PrimitiveStringMultiline`
- `BatchImagesNode`
- `ResolutionSelector`
- `LoadImage`
- `LoadImage`
- `PreviewAny`
- `ComfySwitchNode`
- `TextGenerateLTX2Prompt`

**识别到的模式**：text_to_image

## 关键参数

- `seed` = `965300904929997`
- `steps` = `25`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`
- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`

## 知识

覆盖率 **86%**（91/106）

**有卡**：`VAELoader`、`KSampler`、`CLIPLoader`、`ConditioningZeroOut`、`EmptySD3LatentImage`、`EmptyLatentImage`、`VAEDecode`、`UNETLoader`、`LoraLoaderModelOnly`、`CLIPTextEncode`、`AddLabel`、`SaveImage`、`Seed (rgthree)`、`ModelSamplingAuraFlow`、`TextEncodeQwenImage21`、`BatchImagesNode`、`ImagesConcanateToGrid`、`ResolutionSelector`、`easy promptList`、`TextGenerateLTX2Prompt`、`AILab_QwenVL`、`LoadImage`、`Label (rgthree)`、`QwenImage21Cache`、`GetImageSize`、`easy anythingIndexSwitch`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、ConditioningZeroOut

## 参数体检

发现 2 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

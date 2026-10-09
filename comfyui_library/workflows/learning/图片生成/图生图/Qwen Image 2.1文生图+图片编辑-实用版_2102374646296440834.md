---
key: 图片生成/图生图/Qwen Image 2.1文生图+图片编辑-实用版_2102374646296440834.json
name: Qwen Image 2.1文生图+图片编辑-实用版_2102374646296440834.json
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen Image 2.1文生图+图片编辑-实用版_2102374646296440834.json
hash: 4d172726e2b944a2
coverage: 0.745283
learned_at: 2026-10-09 22:27:12
nodes: [MarkdownNote, VAELoader, KSampler, CLIPLoader, VAELoader, KSampler, ConditioningZeroOut, EmptySD3LatentImage, VAELoader, CLIPLoader, EmptyLatentImage, VAEDecode, VAEDecode, VAEDecode, KSampler, UNETLoader, LoraLoaderModelOnly, CLIPTextEncode, ConditioningZeroOut, AddLabel, SaveImage, Seed (rgthree), ModelSamplingAuraFlow, UNETLoader, TextEncodeQwenImage21, AddLabel, BatchImagesNode, CLIPTextEncode, ImagesConcanateToGrid, AddLabel, ResolutionSelector, SaveImage, SaveImage, UNETLoader, CLIPLoader, easy promptList, TextGenerateLTX2Prompt, AILab_QwenVL, TextEncodeQwenImage21, EmptyLatentImage, KSampler, VAEDecode, PrimitiveStringMultiline, SaveImage, LoadImage, PreviewAny, MarkdownNote, Label (rgthree), Label (rgthree), Label (rgthree), Label (rgthree), CLIPLoader, UNETLoader, Label (rgthree), Label (rgthree), KSampler, QwenImage21Cache, CLIPLoader, TextEncodeQwenImage21, VAELoader, CLIPLoader, TextGenerateLTX2Prompt, GetImageSize, EmptyLatentImage, VAEDecode, SaveImage, Image Comparer (rgthree), Label (rgthree), Label (rgthree), UNETLoader, CLIPLoader, VAELoader, ResolutionSelector, CLIPLoader, SaveImage, PrimitiveStringMultiline, Note, easy anythingIndexSwitch, PreviewAny, ComfySwitchNode, PreviewAny, Label (rgthree), LoadImage, LoadImage, LoadImage, UNETLoader, CLIPLoader, VAELoader, PrimitiveStringMultiline, TextEncodeQwenImage21, GetImageSize, EmptyLatentImage, QwenImage21Cache, KSampler, VAEDecode, SaveImage, Image Comparer (rgthree), LoadImage, PrimitiveStringMultiline, BatchImagesNode, ResolutionSelector, LoadImage, LoadImage, PreviewAny, ComfySwitchNode, TextGenerateLTX2Prompt]
patterns: [text_to_image]
missing: [Label (rgthree), Label (rgthree), Label (rgthree), Label (rgthree), Label (rgthree), Label (rgthree), Label (rgthree), Label (rgthree), Label (rgthree), easy anythingIndexSwitch, Seed (rgthree), easy promptList]
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 965300904929997, "steps": 25, "width": 1024}
discoveries: [次要节点 `Label (rgthree)` 知识库中没有该节点类型的任何知识, 次要节点 `Label (rgthree)` 知识库中没有该节点类型的任何知识, 次要节点 `Label (rgthree)` 知识库中没有该节点类型的任何知识, 次要节点 `Label (rgthree)` 知识库中没有该节点类型的任何知识, 次要节点 `Label (rgthree)` 知识库中没有该节点类型的任何知识, 次要节点 `Label (rgthree)` 知识库中没有该节点类型的任何知识, 次要节点 `Label (rgthree)` 知识库中没有该节点类型的任何知识, 次要节点 `Label (rgthree)` 知识库中没有该节点类型的任何知识, 次要节点 `Label (rgthree)` 知识库中没有该节点类型的任何知识, 次要节点 `easy anythingIndexSwitch` 知识库中没有该节点类型的任何知识, 次要节点 `Seed (rgthree)` 仅有 KSampler 的通用知识，没有该节点自己的说明, 次要节点 `easy promptList` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/Qwen Image 2.1文生图+图片编辑-实用版_2102374646296440834.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/2102374646296440834.json`

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

覆盖率 **75%**（79/106）

**有卡**：`VAELoader`、`KSampler`、`CLIPLoader`、`ConditioningZeroOut`、`EmptySD3LatentImage`、`EmptyLatentImage`、`VAEDecode`、`UNETLoader`、`LoraLoaderModelOnly`、`CLIPTextEncode`、`AddLabel`、`SaveImage`、`ModelSamplingAuraFlow`、`TextEncodeQwenImage21`、`BatchImagesNode`、`ImagesConcanateToGrid`、`ResolutionSelector`、`TextGenerateLTX2Prompt`、`AILab_QwenVL`、`LoadImage`、`QwenImage21Cache`、`GetImageSize`

**缺卡**（12）：`Label (rgthree)`、`Label (rgthree)`、`Label (rgthree)`、`Label (rgthree)`、`Label (rgthree)`、`Label (rgthree)`、`Label (rgthree)`、`Label (rgthree)`、`Label (rgthree)`、`easy anythingIndexSwitch`、`Seed (rgthree)`、`easy promptList`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、ConditioningZeroOut

## 参数体检

发现 2 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- 次要节点 `Label (rgthree)` 知识库中没有该节点类型的任何知识
- 次要节点 `Label (rgthree)` 知识库中没有该节点类型的任何知识
- 次要节点 `Label (rgthree)` 知识库中没有该节点类型的任何知识
- 次要节点 `Label (rgthree)` 知识库中没有该节点类型的任何知识
- 次要节点 `Label (rgthree)` 知识库中没有该节点类型的任何知识
- 次要节点 `Label (rgthree)` 知识库中没有该节点类型的任何知识
- 次要节点 `Label (rgthree)` 知识库中没有该节点类型的任何知识
- 次要节点 `Label (rgthree)` 知识库中没有该节点类型的任何知识
- 次要节点 `Label (rgthree)` 知识库中没有该节点类型的任何知识
- 次要节点 `easy anythingIndexSwitch` 知识库中没有该节点类型的任何知识
- 次要节点 `Seed (rgthree)` 仅有 KSampler 的通用知识，没有该节点自己的说明
- 次要节点 `easy promptList` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

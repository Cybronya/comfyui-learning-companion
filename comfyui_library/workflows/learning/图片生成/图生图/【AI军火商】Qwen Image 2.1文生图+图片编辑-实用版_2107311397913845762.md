---
key: 图片生成/图生图/【AI军火商】Qwen Image 2.1文生图+图片编辑-实用版_2107311397913845762.json
name: 【AI军火商】Qwen Image 2.1文生图+图片编辑-实用版_2107311397913845762
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/【AI军火商】Qwen Image 2.1文生图+图片编辑-实用版_2107311397913845762.json
hash: 187a9df9957b66c4
coverage: 0.613208
learned_at: 2026-10-06 21:42:53
nodes: [MarkdownNote, VAELoader, KSampler, CLIPLoader, VAELoader, KSampler, ConditioningZeroOut, EmptySD3LatentImage, VAELoader, CLIPLoader, EmptyLatentImage, VAEDecode, VAEDecode, VAEDecode, KSampler, UNETLoader, LoraLoaderModelOnly, CLIPTextEncode, ConditioningZeroOut, AddLabel, SaveImage, Seed (rgthree), ModelSamplingAuraFlow, UNETLoader, TextEncodeQwenImage21, AddLabel, BatchImagesNode, CLIPTextEncode, ImagesConcanateToGrid, AddLabel, ResolutionSelector, SaveImage, SaveImage, UNETLoader, CLIPLoader, easy promptList, TextGenerateLTX2Prompt, AILab_QwenVL, TextEncodeQwenImage21, EmptyLatentImage, KSampler, VAEDecode, PrimitiveStringMultiline, SaveImage, LoadImage, PreviewAny, MarkdownNote, Label (rgthree), Label (rgthree), Label (rgthree), Label (rgthree), CLIPLoader, UNETLoader, Label (rgthree), KSampler, QwenImage21Cache, CLIPLoader, TextEncodeQwenImage21, VAELoader, CLIPLoader, TextGenerateLTX2Prompt, GetImageSize, EmptyLatentImage, VAEDecode, SaveImage, Image Comparer (rgthree), Label (rgthree), Label (rgthree), UNETLoader, CLIPLoader, VAELoader, ResolutionSelector, CLIPLoader, SaveImage, PrimitiveStringMultiline, Note, easy anythingIndexSwitch, PreviewAny, ComfySwitchNode, PreviewAny, Label (rgthree), LoadImage, LoadImage, UNETLoader, CLIPLoader, VAELoader, TextEncodeQwenImage21, GetImageSize, EmptyLatentImage, QwenImage21Cache, KSampler, VAEDecode, SaveImage, Image Comparer (rgthree), LoadImage, PrimitiveStringMultiline, BatchImagesNode, PreviewAny, ComfySwitchNode, TextGenerateLTX2Prompt, LoadImage, LoadImage, LoadImage, PrimitiveStringMultiline, Label (rgthree), ResolutionSelector]
patterns: [text_to_image]
missing: [AILab_QwenVL, AddLabel, AddLabel, AddLabel, BatchImagesNode, BatchImagesNode, ImagesConcanateToGrid, Label (rgthree), Label (rgthree), Label (rgthree), Label (rgthree), Label (rgthree), Label (rgthree), Label (rgthree), Label (rgthree), Label (rgthree), ModelSamplingAuraFlow, easy anythingIndexSwitch, GetImageSize, GetImageSize, PreviewAny, PreviewAny, PreviewAny, PreviewAny, Seed (rgthree), TextGenerateLTX2Prompt, TextGenerateLTX2Prompt, TextGenerateLTX2Prompt, easy promptList]
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 1124212234076821, "steps": 25, "width": 1024}
discoveries: [次要节点 `AILab_QwenVL` 知识库中没有该节点类型的任何知识, 次要节点 `AddLabel` 知识库中没有该节点类型的任何知识, 次要节点 `AddLabel` 知识库中没有该节点类型的任何知识, 次要节点 `AddLabel` 知识库中没有该节点类型的任何知识, 次要节点 `BatchImagesNode` 知识库中没有该节点类型的任何知识, 次要节点 `BatchImagesNode` 知识库中没有该节点类型的任何知识, 次要节点 `ImagesConcanateToGrid` 知识库中没有该节点类型的任何知识, 次要节点 `Label (rgthree)` 知识库中没有该节点类型的任何知识, 次要节点 `Label (rgthree)` 知识库中没有该节点类型的任何知识, 次要节点 `Label (rgthree)` 知识库中没有该节点类型的任何知识, 次要节点 `Label (rgthree)` 知识库中没有该节点类型的任何知识, 次要节点 `Label (rgthree)` 知识库中没有该节点类型的任何知识, 次要节点 `Label (rgthree)` 知识库中没有该节点类型的任何知识, 次要节点 `Label (rgthree)` 知识库中没有该节点类型的任何知识, 次要节点 `Label (rgthree)` 知识库中没有该节点类型的任何知识, 次要节点 `Label (rgthree)` 知识库中没有该节点类型的任何知识, 次要节点 `ModelSamplingAuraFlow` 知识库中没有该节点类型的任何知识, 次要节点 `easy anythingIndexSwitch` 知识库中没有该节点类型的任何知识, 次要节点 `GetImageSize` 仅有 Resolution 的通用知识，没有该节点自己的说明, 次要节点 `GetImageSize` 仅有 Resolution 的通用知识，没有该节点自己的说明, 次要节点 `PreviewAny` 仅有 SaveImage 的通用知识，没有该节点自己的说明, 次要节点 `PreviewAny` 仅有 SaveImage 的通用知识，没有该节点自己的说明, 次要节点 `PreviewAny` 仅有 SaveImage 的通用知识，没有该节点自己的说明, 次要节点 `PreviewAny` 仅有 SaveImage 的通用知识，没有该节点自己的说明, 次要节点 `Seed (rgthree)` 仅有 KSampler 的通用知识，没有该节点自己的说明, 次要节点 `TextGenerateLTX2Prompt` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明, 次要节点 `TextGenerateLTX2Prompt` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明, 次要节点 `TextGenerateLTX2Prompt` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明, 次要节点 `easy promptList` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/【AI军火商】Qwen Image 2.1文生图+图片编辑-实用版_2107311397913845762.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/【AI军火商】Qwen Image 2.1文生图+图片编辑-实用版_2107311397913845762.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

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
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
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
- `PreviewAny`
- `ComfySwitchNode`
- `TextGenerateLTX2Prompt`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `PrimitiveStringMultiline`
- `Label (rgthree)`
- `ResolutionSelector`

**识别到的模式**：text_to_image

## 关键参数

- `seed` = `1124212234076821`
- `steps` = `25`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`
- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`

## 知识

覆盖率 **61%**（65/106）

**有卡**：`VAELoader`、`KSampler`、`CLIPLoader`、`ConditioningZeroOut`、`EmptyLatentImage`、`VAEDecode`、`UNETLoader`、`LoraLoaderModelOnly`、`CLIPTextEncode`、`SaveImage`、`TextEncodeQwenImage21`、`ResolutionSelector`、`LoadImage`、`QwenImage21Cache`

**缺卡**（29）：`AILab_QwenVL`、`AddLabel`、`AddLabel`、`AddLabel`、`BatchImagesNode`、`BatchImagesNode`、`ImagesConcanateToGrid`、`Label (rgthree)`、`Label (rgthree)`、`Label (rgthree)`、`Label (rgthree)`、`Label (rgthree)`、`Label (rgthree)`、`Label (rgthree)`、`Label (rgthree)`、`Label (rgthree)`、`ModelSamplingAuraFlow`、`easy anythingIndexSwitch`、`GetImageSize`、`GetImageSize`、`PreviewAny`、`PreviewAny`、`PreviewAny`、`PreviewAny`、`Seed (rgthree)`、`TextGenerateLTX2Prompt`、`TextGenerateLTX2Prompt`、`TextGenerateLTX2Prompt`、`easy promptList`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、ConditioningZeroOut

## 参数体检

发现 2 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- 次要节点 `AILab_QwenVL` 知识库中没有该节点类型的任何知识
- 次要节点 `AddLabel` 知识库中没有该节点类型的任何知识
- 次要节点 `AddLabel` 知识库中没有该节点类型的任何知识
- 次要节点 `AddLabel` 知识库中没有该节点类型的任何知识
- 次要节点 `BatchImagesNode` 知识库中没有该节点类型的任何知识
- 次要节点 `BatchImagesNode` 知识库中没有该节点类型的任何知识
- 次要节点 `ImagesConcanateToGrid` 知识库中没有该节点类型的任何知识
- 次要节点 `Label (rgthree)` 知识库中没有该节点类型的任何知识
- 次要节点 `Label (rgthree)` 知识库中没有该节点类型的任何知识
- 次要节点 `Label (rgthree)` 知识库中没有该节点类型的任何知识
- 次要节点 `Label (rgthree)` 知识库中没有该节点类型的任何知识
- 次要节点 `Label (rgthree)` 知识库中没有该节点类型的任何知识
- 次要节点 `Label (rgthree)` 知识库中没有该节点类型的任何知识
- 次要节点 `Label (rgthree)` 知识库中没有该节点类型的任何知识
- 次要节点 `Label (rgthree)` 知识库中没有该节点类型的任何知识
- 次要节点 `Label (rgthree)` 知识库中没有该节点类型的任何知识
- 次要节点 `ModelSamplingAuraFlow` 知识库中没有该节点类型的任何知识
- 次要节点 `easy anythingIndexSwitch` 知识库中没有该节点类型的任何知识
- 次要节点 `GetImageSize` 仅有 Resolution 的通用知识，没有该节点自己的说明
- 次要节点 `GetImageSize` 仅有 Resolution 的通用知识，没有该节点自己的说明
- 次要节点 `PreviewAny` 仅有 SaveImage 的通用知识，没有该节点自己的说明
- 次要节点 `PreviewAny` 仅有 SaveImage 的通用知识，没有该节点自己的说明
- 次要节点 `PreviewAny` 仅有 SaveImage 的通用知识，没有该节点自己的说明
- 次要节点 `PreviewAny` 仅有 SaveImage 的通用知识，没有该节点自己的说明
- 次要节点 `Seed (rgthree)` 仅有 KSampler 的通用知识，没有该节点自己的说明
- 次要节点 `TextGenerateLTX2Prompt` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明
- 次要节点 `TextGenerateLTX2Prompt` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明
- 次要节点 `TextGenerateLTX2Prompt` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明
- 次要节点 `easy promptList` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

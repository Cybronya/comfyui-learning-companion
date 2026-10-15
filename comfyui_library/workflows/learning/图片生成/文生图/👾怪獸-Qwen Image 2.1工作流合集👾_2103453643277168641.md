---
key: 图片生成/文生图/👾怪獸-Qwen Image 2.1工作流合集👾_2103453643277168641.json
name: 👾怪獸-Qwen Image 2.1工作流合集👾_2103453643277168641
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/👾怪獸-Qwen Image 2.1工作流合集👾_2103453643277168641.json
hash: 9701d26739519daf
coverage: 0.652174
learned_at: 2026-10-10 21:00:01
nodes: [VAEDecode, easy showAnything, JjkText, PreviewImage, VAEDecode, SaveImage, ComfySwitchNode, GetNode, ResolutionSelector, SetNode, SetNode, CLIPLoader, VAELoader, Anything Everywhere3, AIO_Preprocessor, BatchImagesNode, GetNode, PreviewAny, EmptyLatentImage, MarkdownNote, LoadImage, Image Comparer (rgthree), GetNode, EmptyLatentImage, ComfySwitchNode, TextEncodeQwenImage21, ShowText|pysssss, LoadImage, ResolutionSelector, EmptyLatentImage, TextEncodeQwenImage21, TextGenerateLTX2Prompt, FastGroupsBypassSwitch, TextGenerateLTX2Prompt, ResolutionSelector, CR Text, VAEDecode, Fast Groups Bypasser (rgthree), LoadImage, LoadImage, LoadImage, CLIPLoader, PreviewAny, CR Text Concatenate, Qwen3VL_Advanced, DWPreprocessor, DepthAnythingPreprocessor, ImageBlend, PreviewImage, LoadImage, KSampler, KSampler, LoadImage, LoadImage, TextEncodeQwenImage21, TextGenerateLTX2Prompt, CR Prompt Text, CLIPLoader, UNETLoader, QwenImage21SageAttentionT8, LoraLoaderBypassModelOnly, KSampler, VAELoader, ComfySwitchNode, SaveImage, SaveImage, LoadImage, PreviewImage, Fast Groups Bypasser (rgthree)]
patterns: []
missing: [CR Text, CR Text Concatenate, CR Prompt Text]
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 454327193221583, "steps": 6, "width": 1024}
discoveries: [次要节点 `CR Text` 知识库中没有该节点类型的任何知识, 次要节点 `CR Text Concatenate` 知识库中没有该节点类型的任何知识, 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/文生图/👾怪獸-Qwen Image 2.1工作流合集👾_2103453643277168641.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/👾怪獸-Qwen Image 2.1工作流合集👾_2103453643277168641.json`

## 结构

**节点**（69 个）：
- `VAEDecode`
- `easy showAnything`
- `JjkText`
- `PreviewImage`
- `VAEDecode`
- `SaveImage`
- `ComfySwitchNode`
- `GetNode`
- `ResolutionSelector`
- `SetNode`
- `SetNode`
- `CLIPLoader`
- `VAELoader`
- `Anything Everywhere3`
- `AIO_Preprocessor`
- `BatchImagesNode`
- `GetNode`
- `PreviewAny`
- `EmptyLatentImage`
- `MarkdownNote`
- `LoadImage`
- `Image Comparer (rgthree)`
- `GetNode`
- `EmptyLatentImage`
- `ComfySwitchNode`
- `TextEncodeQwenImage21`
- `ShowText|pysssss`
- `LoadImage`
- `ResolutionSelector`
- `EmptyLatentImage`
- `TextEncodeQwenImage21`
- `TextGenerateLTX2Prompt`
- `FastGroupsBypassSwitch`
- `TextGenerateLTX2Prompt`
- `ResolutionSelector`
- `CR Text`
- `VAEDecode`
- `Fast Groups Bypasser (rgthree)`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `CLIPLoader`
- `PreviewAny`
- `CR Text Concatenate`
- `Qwen3VL_Advanced`
- `DWPreprocessor`
- `DepthAnythingPreprocessor`
- `ImageBlend`
- `PreviewImage`
- `LoadImage`
- `KSampler`
- `KSampler`
- `LoadImage`
- `LoadImage`
- `TextEncodeQwenImage21`
- `TextGenerateLTX2Prompt`
- `CR Prompt Text`
- `CLIPLoader`
- `UNETLoader`
- `QwenImage21SageAttentionT8`
- `LoraLoaderBypassModelOnly`
- `KSampler`
- `VAELoader`
- `ComfySwitchNode`
- `SaveImage`
- `SaveImage`
- `LoadImage`
- `PreviewImage`
- `Fast Groups Bypasser (rgthree)`

## 关键参数

- `batch_size` = `1`
- `cfg` = `1`
- `denoise` = `1`
- `height` = `1024`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `seed` = `454327193221583`
- `steps` = `6`
- `width` = `1024`

## 知识

覆盖率 **65%**（45/69）

**有卡**：`VAEDecode`、`easy showAnything`、`JjkText`、`PreviewImage`、`SaveImage`、`ComfySwitchNode`、`GetNode`、`ResolutionSelector`、`SetNode`、`CLIPLoader`、`VAELoader`、`Anything Everywhere3`、`AIO_Preprocessor`、`BatchImagesNode`、`PreviewAny`、`EmptyLatentImage`、`MarkdownNote`、`LoadImage`、`Image Comparer (rgthree)`、`TextEncodeQwenImage21`、`ShowText|pysssss`、`TextGenerateLTX2Prompt`、`FastGroupsBypassSwitch`、`CR Text`、`Fast Groups Bypasser (rgthree)`、`CR Text Concatenate`、`Qwen3VL_Advanced`

**缺卡**（3）：`CR Text`、`CR Text Concatenate`、`CR Prompt Text`

## 参数体检

发现 3 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- 次要节点 `CR Text` 知识库中没有该节点类型的任何知识
- 次要节点 `CR Text Concatenate` 知识库中没有该节点类型的任何知识
- 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

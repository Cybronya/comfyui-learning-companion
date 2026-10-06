---
key: 图片生成/文生图/👾怪獸-Qwen Image 2.1工作流合集👾_2103453643277168641.json
name: 👾怪獸-Qwen Image 2.1工作流合集👾_2103453643277168641
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/👾怪獸-Qwen Image 2.1工作流合集👾_2103453643277168641.json
hash: 9701d26739519daf
coverage: 0.608696
learned_at: 2026-10-07 02:03:51
nodes: [VAEDecode, easy showAnything, JjkText, PreviewImage, VAEDecode, SaveImage, ComfySwitchNode, GetNode, ResolutionSelector, SetNode, SetNode, CLIPLoader, VAELoader, Anything Everywhere3, AIO_Preprocessor, BatchImagesNode, GetNode, PreviewAny, EmptyLatentImage, MarkdownNote, LoadImage, Image Comparer (rgthree), GetNode, EmptyLatentImage, ComfySwitchNode, TextEncodeQwenImage21, ShowText|pysssss, LoadImage, ResolutionSelector, EmptyLatentImage, TextEncodeQwenImage21, TextGenerateLTX2Prompt, FastGroupsBypassSwitch, TextGenerateLTX2Prompt, ResolutionSelector, CR Text, VAEDecode, Fast Groups Bypasser (rgthree), LoadImage, LoadImage, LoadImage, CLIPLoader, PreviewAny, CR Text Concatenate, Qwen3VL_Advanced, DWPreprocessor, DepthAnythingPreprocessor, ImageBlend, PreviewImage, LoadImage, KSampler, KSampler, LoadImage, LoadImage, TextEncodeQwenImage21, TextGenerateLTX2Prompt, CR Prompt Text, CLIPLoader, UNETLoader, QwenImage21SageAttentionT8, LoraLoaderBypassModelOnly, KSampler, VAELoader, ComfySwitchNode, SaveImage, SaveImage, LoadImage, PreviewImage, Fast Groups Bypasser (rgthree)]
patterns: []
missing: [CR Text, CR Text Concatenate, DWPreprocessor, Qwen3VL_Advanced, CR Prompt Text, DepthAnythingPreprocessor]
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 454327193221583, "steps": 6, "width": 1024}
discoveries: [次要节点 `CR Text` 知识库中没有该节点类型的任何知识, 次要节点 `CR Text Concatenate` 知识库中没有该节点类型的任何知识, 次要节点 `DWPreprocessor` 知识库中没有该节点类型的任何知识, 次要节点 `Qwen3VL_Advanced` 知识库中没有该节点类型的任何知识, 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明, 次要节点 `DepthAnythingPreprocessor` 仅有 ControlNet 的通用知识，没有该节点自己的说明, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/文生图/👾怪獸-Qwen Image 2.1工作流合集👾_2103453643277168641.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/👾怪獸-Qwen Image 2.1工作流合集👾_2103453643277168641.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（69 个）：
- `VAEDecode` ★核心
- `easy showAnything`
- `JjkText`
- `PreviewImage`
- `VAEDecode` ★核心
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
- `EmptyLatentImage` ★核心
- `MarkdownNote`
- `LoadImage`
- `Image Comparer (rgthree)`
- `GetNode`
- `EmptyLatentImage` ★核心
- `ComfySwitchNode`
- `TextEncodeQwenImage21`
- `ShowText|pysssss`
- `LoadImage`
- `ResolutionSelector`
- `EmptyLatentImage` ★核心
- `TextEncodeQwenImage21`
- `TextGenerateLTX2Prompt`
- `FastGroupsBypassSwitch`
- `TextGenerateLTX2Prompt`
- `ResolutionSelector`
- `CR Text`
- `VAEDecode` ★核心
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
- `KSampler` ★核心
- `KSampler` ★核心
- `LoadImage`
- `LoadImage`
- `TextEncodeQwenImage21`
- `TextGenerateLTX2Prompt`
- `CR Prompt Text`
- `CLIPLoader`
- `UNETLoader` ★核心
- `QwenImage21SageAttentionT8`
- `LoraLoaderBypassModelOnly` ★核心
- `KSampler` ★核心
- `VAELoader`
- `ComfySwitchNode`
- `SaveImage`
- `SaveImage`
- `LoadImage`
- `PreviewImage`
- `Fast Groups Bypasser (rgthree)`

## 关键参数

- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`
- `seed` = `454327193221583`
- `steps` = `6`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **61%**（42/69）

**有卡**：`VAEDecode`、`SaveImage`、`ResolutionSelector`、`CLIPLoader`、`VAELoader`、`AIO_Preprocessor`、`BatchImagesNode`、`EmptyLatentImage`、`LoadImage`、`TextEncodeQwenImage21`、`TextGenerateLTX2Prompt`、`FastGroupsBypassSwitch`、`ImageBlend`、`KSampler`、`UNETLoader`、`QwenImage21SageAttentionT8`、`LoraLoaderBypassModelOnly`

**缺卡**（6）：`CR Text`、`CR Text Concatenate`、`DWPreprocessor`、`Qwen3VL_Advanced`、`CR Prompt Text`、`DepthAnythingPreprocessor`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、EmptyLatentImage、ResolutionSelector、LoadImage

## 参数体检

发现 3 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- 次要节点 `CR Text` 知识库中没有该节点类型的任何知识
- 次要节点 `CR Text Concatenate` 知识库中没有该节点类型的任何知识
- 次要节点 `DWPreprocessor` 知识库中没有该节点类型的任何知识
- 次要节点 `Qwen3VL_Advanced` 知识库中没有该节点类型的任何知识
- 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明
- 次要节点 `DepthAnythingPreprocessor` 仅有 ControlNet 的通用知识，没有该节点自己的说明
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

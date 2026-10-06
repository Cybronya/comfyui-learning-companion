---
key: 图片生成/文生图/Qwen image 2.1 文生与编辑加速工作流（双自动提示词）_2103765664929501185.json
name: Qwen image 2.1 文生与编辑加速工作流（双自动提示词）_2103765664929501185
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Qwen image 2.1 文生与编辑加速工作流（双自动提示词）_2103765664929501185.json
hash: 17f69d7cc0029fa8
coverage: 0.366667
learned_at: 2026-10-06 22:36:55
nodes: [CLIPLoader, VAELoader, VAEDecode, UNETLoader, EmptyLatentImage, KSampler, TextEncodeQwenImage21, VAEDecode, LoadImage, LoadImage, LoadImage, LoadImage, KSampler, SaveImage, QwenImage21Cache, 忽略多组孤海, 忽略多组孤海, CLIPLoader, StringConcatenate, TextGenerate, JsonExtractString, CLIPLoader, TextGenerate, JsonExtractString, BatchImagesNode, StringConcatenate, StringConcatenate, Any Switch (rgthree), PreviewAny, PreviewAny, llama_cpp_parameters, llama_cpp_instruct_adv, llama_cpp_instruct_adv, BatchImagesNode, Note, Note, Note, SetNode, GetNode, SetNode, GetNode, GetNode, GetNode, SetNode, GetNode, GetNode, SetNode, GetNode, SetNode, GetNode, SetNode, GetNode, SetNode, GetNode, SetNode, GetNode, SetNode, GetNode, SetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, SetNode, GetNode, GetNode, SetNode, GetNode, SetNode, GetNode, GetNode, GetNode, SetNode, GetNode, SetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, LoadImage, SetNode, GetNode, GetNode, GetNode, LoadImage, SetNode, GetNode, GetNode, GetNode, SetNode, GetNode, GetNode, GetNode, LoadImage, SetNode, GetNode, GetNode, GetNode, ImageScaleToMaxDimension, ImageScaleToMaxDimension, ImageScaleToMaxDimension, ImageScaleToMaxDimension, ImageScaleToMaxDimension, ImageScaleToMaxDimension, ImageScaleToMaxDimension, ImageScaleToMaxDimension, ImageScaleToMaxDimension, ImageScaleToMaxDimension, SetNode, GetNode, Image Comparer (rgthree), SetNode, GetNode, ComfySwitchNode, GetNode, ComfySwitchNode, GetNode, KSampler, ComfySwitchNode, SetNode, GetNode, SetNode, GetNode, GetNode, ComfySwitchNode, LoadImage, LoadImage, ResolutionSelector, PrimitiveBoolean, StringConcatenate, 忽略多组孤海, SetNode, TextEncodeQwenImage21, SaveImage, CR Prompt Text, LoadImage, PrimitiveBoolean, KSampler, LoraLoaderBypassModelOnly, Any Switch (rgthree), llama_cpp_model_loader]
patterns: []
missing: [忽略多组孤海, 忽略多组孤海, 忽略多组孤海, CR Prompt Text]
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 426982129804706, "steps": 6, "width": 1024}
discoveries: [次要节点 `忽略多组孤海` 知识库中没有该节点类型的任何知识, 次要节点 `忽略多组孤海` 知识库中没有该节点类型的任何知识, 次要节点 `忽略多组孤海` 知识库中没有该节点类型的任何知识, 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/文生图/Qwen image 2.1 文生与编辑加速工作流（双自动提示词）_2103765664929501185.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Qwen image 2.1 文生与编辑加速工作流（双自动提示词）_2103765664929501185.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（150 个）：
- `CLIPLoader`
- `VAELoader`
- `VAEDecode` ★核心
- `UNETLoader` ★核心
- `EmptyLatentImage` ★核心
- `KSampler` ★核心
- `TextEncodeQwenImage21`
- `VAEDecode` ★核心
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `KSampler` ★核心
- `SaveImage`
- `QwenImage21Cache`
- `忽略多组孤海`
- `忽略多组孤海`
- `CLIPLoader`
- `StringConcatenate`
- `TextGenerate`
- `JsonExtractString`
- `CLIPLoader`
- `TextGenerate`
- `JsonExtractString`
- `BatchImagesNode`
- `StringConcatenate`
- `StringConcatenate`
- `Any Switch (rgthree)`
- `PreviewAny`
- `PreviewAny`
- `llama_cpp_parameters`
- `llama_cpp_instruct_adv`
- `llama_cpp_instruct_adv`
- `BatchImagesNode`
- `Note`
- `Note`
- `Note`
- `SetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `LoadImage`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `LoadImage`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `LoadImage`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `ImageScaleToMaxDimension`
- `ImageScaleToMaxDimension`
- `ImageScaleToMaxDimension`
- `ImageScaleToMaxDimension`
- `ImageScaleToMaxDimension`
- `ImageScaleToMaxDimension`
- `ImageScaleToMaxDimension`
- `ImageScaleToMaxDimension`
- `ImageScaleToMaxDimension`
- `ImageScaleToMaxDimension`
- `SetNode`
- `GetNode`
- `Image Comparer (rgthree)`
- `SetNode`
- `GetNode`
- `ComfySwitchNode`
- `GetNode`
- `ComfySwitchNode`
- `GetNode`
- `KSampler` ★核心
- `ComfySwitchNode`
- `SetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `ComfySwitchNode`
- `LoadImage`
- `LoadImage`
- `ResolutionSelector`
- `PrimitiveBoolean`
- `StringConcatenate`
- `忽略多组孤海`
- `SetNode`
- `TextEncodeQwenImage21`
- `SaveImage`
- `CR Prompt Text`
- `LoadImage`
- `PrimitiveBoolean`
- `KSampler` ★核心
- `LoraLoaderBypassModelOnly` ★核心
- `Any Switch (rgthree)`
- `llama_cpp_model_loader`

## 关键参数

- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`
- `seed` = `426982129804706`
- `steps` = `6`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **37%**（55/150）

**有卡**：`CLIPLoader`、`VAELoader`、`VAEDecode`、`UNETLoader`、`EmptyLatentImage`、`KSampler`、`TextEncodeQwenImage21`、`LoadImage`、`SaveImage`、`QwenImage21Cache`、`StringConcatenate`、`TextGenerate`、`JsonExtractString`、`BatchImagesNode`、`llama_cpp_parameters`、`llama_cpp_instruct_adv`、`ImageScaleToMaxDimension`、`ResolutionSelector`、`PrimitiveBoolean`、`LoraLoaderBypassModelOnly`、`llama_cpp_model_loader`

**缺卡**（4）：`忽略多组孤海`、`忽略多组孤海`、`忽略多组孤海`、`CR Prompt Text`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、EmptyLatentImage、ResolutionSelector、LoadImage

## 参数体检

发现 2 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- 次要节点 `忽略多组孤海` 知识库中没有该节点类型的任何知识
- 次要节点 `忽略多组孤海` 知识库中没有该节点类型的任何知识
- 次要节点 `忽略多组孤海` 知识库中没有该节点类型的任何知识
- 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

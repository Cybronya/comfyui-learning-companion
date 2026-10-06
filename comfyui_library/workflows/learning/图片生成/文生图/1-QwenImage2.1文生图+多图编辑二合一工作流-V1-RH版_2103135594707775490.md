---
key: 图片生成/文生图/1-QwenImage2.1文生图+多图编辑二合一工作流-V1-RH版_2103135594707775490.json
name: 1-QwenImage2.1文生图+多图编辑二合一工作流-V1-RH版_2103135594707775490
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/1-QwenImage2.1文生图+多图编辑二合一工作流-V1-RH版_2103135594707775490.json
hash: 0d9fe1b8ef0d4b37
coverage: 0.367925
learned_at: 2026-10-07 02:04:36
nodes: [GetNode, GetNode, GetNode, SetNode, SetNode, SetNode, SetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, SetNode, SetNode, GetNode, PrimitiveStringMultiline, PrimitiveStringMultiline, GetNode, GetNode, SetNode, SetNode, SetNode, SetNode, easy cleanGpuUsed, TextGenerateLTX2Prompt, GetNode, GetNode, GetNode, SetNode, LoadAndResizeImage, GetNode, GetNode, GetNode, GetNode, TextEncodeQwenImage21, GetNode, LoadAndResizeImage, LoadAndResizeImage, LoadAndResizeImage, LoadAndResizeImage, LoadAndResizeImage, LoadAndResizeImage, SetNode, Any Switch (rgthree), SetNode, Fast Groups Bypasser (rgthree), Fast Bypasser (rgthree), SetNode, SetNode, GetNode, GetNode, CLIPLoader, CLIPLoader, MarkdownNote, EmptyLatentImage, ResolutionSelector, MarkdownNote, MarkdownNote, LoadAndResizeImage, Image Comparer (rgthree), SetNode, SetNode, LoadAndResizeImage, Fast Groups Bypasser (rgthree), PreviewImage, AIO_Preprocessor, GetNode, GetNode, GetNode, UNETLoader, CLIPLoader, VAELoader, LoadAndResizeImage, Fast Bypasser (rgthree), LoadAndResizeImage, PrimitiveStringMultiline, Fast Groups Bypasser (rgthree), Image Comparer (rgthree), KSampler, VAELoader, ResizeImageMaskNode, SeedVR2PostProcessing, SeedVR2Conditioning, SaveImage, UNETLoader, VAEEncodeTiled, VAEDecodeTiled, SeedVR2Preprocess, Note, LoraLoaderModelOnly, QwenImage21Cache, ComfySwitchNode, SetNode, Any Switch (rgthree), PreviewAny, SetNode, llama_cpp_parameters, Seed (rgthree), Note, KSampler, SetNode, llama_cpp_model_loader, llama_cpp_instruct_adv, VAEDecode, SaveImage]
patterns: []
missing: [Fast Bypasser (rgthree), Fast Bypasser (rgthree), easy cleanGpuUsed, Seed (rgthree)]
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1088, "sampler_name": "euler", "scheduler": "simple", "seed": 1083630546321884, "steps": 35, "width": 1920}
discoveries: [次要节点 `Fast Bypasser (rgthree)` 知识库中没有该节点类型的任何知识, 次要节点 `Fast Bypasser (rgthree)` 知识库中没有该节点类型的任何知识, 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识, 次要节点 `Seed (rgthree)` 仅有 KSampler 的通用知识，没有该节点自己的说明, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/文生图/1-QwenImage2.1文生图+多图编辑二合一工作流-V1-RH版_2103135594707775490.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/1-QwenImage2.1文生图+多图编辑二合一工作流-V1-RH版_2103135594707775490.json`

## 结构

**生成流程**：Model → Encode → Condition → Latent → Sampling → Decode → Output → Other

**节点**（106 个）：
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `PrimitiveStringMultiline`
- `PrimitiveStringMultiline`
- `GetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `easy cleanGpuUsed`
- `TextGenerateLTX2Prompt`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `LoadAndResizeImage`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `TextEncodeQwenImage21`
- `GetNode`
- `LoadAndResizeImage`
- `LoadAndResizeImage`
- `LoadAndResizeImage`
- `LoadAndResizeImage`
- `LoadAndResizeImage`
- `LoadAndResizeImage`
- `SetNode`
- `Any Switch (rgthree)`
- `SetNode`
- `Fast Groups Bypasser (rgthree)`
- `Fast Bypasser (rgthree)`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `CLIPLoader`
- `CLIPLoader`
- `MarkdownNote`
- `EmptyLatentImage` ★核心
- `ResolutionSelector`
- `MarkdownNote`
- `MarkdownNote`
- `LoadAndResizeImage`
- `Image Comparer (rgthree)`
- `SetNode`
- `SetNode`
- `LoadAndResizeImage`
- `Fast Groups Bypasser (rgthree)`
- `PreviewImage`
- `AIO_Preprocessor`
- `GetNode`
- `GetNode`
- `GetNode`
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `LoadAndResizeImage`
- `Fast Bypasser (rgthree)`
- `LoadAndResizeImage`
- `PrimitiveStringMultiline`
- `Fast Groups Bypasser (rgthree)`
- `Image Comparer (rgthree)`
- `KSampler` ★核心
- `VAELoader`
- `ResizeImageMaskNode`
- `SeedVR2PostProcessing`
- `SeedVR2Conditioning`
- `SaveImage`
- `UNETLoader` ★核心
- `VAEEncodeTiled` ★核心
- `VAEDecodeTiled` ★核心
- `SeedVR2Preprocess`
- `Note`
- `LoraLoaderModelOnly` ★核心
- `QwenImage21Cache`
- `ComfySwitchNode`
- `SetNode`
- `Any Switch (rgthree)`
- `PreviewAny`
- `SetNode`
- `llama_cpp_parameters`
- `Seed (rgthree)`
- `Note`
- `KSampler` ★核心
- `SetNode`
- `llama_cpp_model_loader`
- `llama_cpp_instruct_adv`
- `VAEDecode` ★核心
- `SaveImage`

## 关键参数

- `width` = `1920`
- `height` = `1088`
- `batch_size` = `1`
- `seed` = `1083630546321884`
- `steps` = `35`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **37%**（39/106）

**有卡**：`TextGenerateLTX2Prompt`、`LoadAndResizeImage`、`TextEncodeQwenImage21`、`CLIPLoader`、`EmptyLatentImage`、`ResolutionSelector`、`AIO_Preprocessor`、`UNETLoader`、`VAELoader`、`KSampler`、`ResizeImageMaskNode`、`SeedVR2PostProcessing`、`SeedVR2Conditioning`、`SaveImage`、`VAEEncodeTiled`、`VAEDecodeTiled`、`SeedVR2Preprocess`、`LoraLoaderModelOnly`、`QwenImage21Cache`、`llama_cpp_parameters`、`llama_cpp_model_loader`、`llama_cpp_instruct_adv`、`VAEDecode`

**缺卡**（4）：`Fast Bypasser (rgthree)`、`Fast Bypasser (rgthree)`、`easy cleanGpuUsed`、`Seed (rgthree)`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、CLIPLoader、EmptyLatentImage、ResolutionSelector

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- 次要节点 `Fast Bypasser (rgthree)` 知识库中没有该节点类型的任何知识
- 次要节点 `Fast Bypasser (rgthree)` 知识库中没有该节点类型的任何知识
- 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识
- 次要节点 `Seed (rgthree)` 仅有 KSampler 的通用知识，没有该节点自己的说明
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

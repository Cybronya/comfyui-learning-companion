---
key: 图片生成/图生图/Qwen Image 2.1好玩的LoRA工作流，风格迁移换脸其他创意处理工具_2107235837036556290.json
name: Qwen Image 2.1好玩的LoRA工作流，风格迁移换脸其他创意处理工具_2107235837036556290
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen Image 2.1好玩的LoRA工作流，风格迁移换脸其他创意处理工具_2107235837036556290.json
hash: 795d296fda5b3b48
coverage: 0.567164
learned_at: 2026-10-06 21:41:22
nodes: [SetNode, EmptyLatentImage, VAELoader, UNETLoader, VAEDecode, GetNode, GetNode, GetNode, GetNode, GetNode, TextEncodeQwenImage21, Image Comparer (rgthree), AddLabel, QwenImage21Cache, PreviewImage, CLIPLoader, LoadImage, GetNode, GetNode, easy showAnything, TTResolutionSelector, BatchImagesNode, ResolutionSelector, ImageConcatMulti, LoadImage, SetNode, TTResolutionSelector, ImageResizeKJv2, CR Prompt Text, CLIPLoader, KSampler, MuyeTextEditOutput, TextGenerate, ImageResizeKJv2, LoraLoaderModelOnly, SaveImage, SaveImageAdvanced, easy cleanGpuUsed, 孤海注释, 孤海注释, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, KSampler, EmptyLatentImage, JjkText, CLIPTextEncode, CLIPTextEncode, solarL_SaveImagesToZip, VAEDecode, CLIPLoader, VAELoader, Note]
patterns: [text_to_image]
missing: [AddLabel, BatchImagesNode, ImageConcatMulti, TextGenerate, easy cleanGpuUsed, CR Prompt Text, ImageResizeKJv2, ImageResizeKJv2, MuyeTextEditOutput, SaveImageAdvanced, TTResolutionSelector, TTResolutionSelector, solarL_SaveImagesToZip]
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [次要节点 `AddLabel` 知识库中没有该节点类型的任何知识, 次要节点 `BatchImagesNode` 知识库中没有该节点类型的任何知识, 次要节点 `ImageConcatMulti` 知识库中没有该节点类型的任何知识, 次要节点 `TextGenerate` 知识库中没有该节点类型的任何知识, 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识, 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明, 次要节点 `ImageResizeKJv2` 仅有 Resolution 的通用知识，没有该节点自己的说明, 次要节点 `ImageResizeKJv2` 仅有 Resolution 的通用知识，没有该节点自己的说明, 次要节点 `MuyeTextEditOutput` 仅有 SaveImage 的通用知识，没有该节点自己的说明, 次要节点 `SaveImageAdvanced` 仅有 SaveImage 的通用知识，没有该节点自己的说明, 次要节点 `TTResolutionSelector` 仅有 Resolution 的通用知识，没有该节点自己的说明, 次要节点 `TTResolutionSelector` 仅有 Resolution 的通用知识，没有该节点自己的说明, 次要节点 `solarL_SaveImagesToZip` 仅有 SaveImage 的通用知识，没有该节点自己的说明, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/Qwen Image 2.1好玩的LoRA工作流，风格迁移换脸其他创意处理工具_2107235837036556290.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen Image 2.1好玩的LoRA工作流，风格迁移换脸其他创意处理工具_2107235837036556290.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（67 个）：
- `SetNode`
- `EmptyLatentImage` ★核心
- `VAELoader`
- `UNETLoader` ★核心
- `VAEDecode` ★核心
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `TextEncodeQwenImage21`
- `Image Comparer (rgthree)`
- `AddLabel`
- `QwenImage21Cache`
- `PreviewImage`
- `CLIPLoader`
- `LoadImage`
- `GetNode`
- `GetNode`
- `easy showAnything`
- `TTResolutionSelector`
- `BatchImagesNode`
- `ResolutionSelector`
- `ImageConcatMulti`
- `LoadImage`
- `SetNode`
- `TTResolutionSelector`
- `ImageResizeKJv2`
- `CR Prompt Text`
- `CLIPLoader`
- `KSampler` ★核心
- `MuyeTextEditOutput`
- `TextGenerate`
- `ImageResizeKJv2`
- `LoraLoaderModelOnly` ★核心
- `SaveImage`
- `SaveImageAdvanced`
- `easy cleanGpuUsed`
- `孤海注释`
- `孤海注释`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `KSampler` ★核心
- `EmptyLatentImage` ★核心
- `JjkText`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `solarL_SaveImagesToZip`
- `VAEDecode` ★核心
- `CLIPLoader`
- `VAELoader`
- `Note`

**识别到的模式**：text_to_image

## 关键参数

- `width` = `80`
- `height` = `80`
- `batch_size` = `1`
- `seed` = `598626327129635`
- `steps` = `4`
- `cfg` = `4.5`
- `sampler_name` = `er_sde`
- `scheduler` = `beta`
- `denoise` = `1`

## 知识

覆盖率 **57%**（38/67）

**有卡**：`EmptyLatentImage`、`VAELoader`、`UNETLoader`、`VAEDecode`、`TextEncodeQwenImage21`、`QwenImage21Cache`、`CLIPLoader`、`LoadImage`、`ResolutionSelector`、`KSampler`、`LoraLoaderModelOnly`、`SaveImage`、`CLIPTextEncode`

**缺卡**（13）：`AddLabel`、`BatchImagesNode`、`ImageConcatMulti`、`TextGenerate`、`easy cleanGpuUsed`、`CR Prompt Text`、`ImageResizeKJv2`、`ImageResizeKJv2`、`MuyeTextEditOutput`、`SaveImageAdvanced`、`TTResolutionSelector`、`TTResolutionSelector`、`solarL_SaveImagesToZip`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- 次要节点 `AddLabel` 知识库中没有该节点类型的任何知识
- 次要节点 `BatchImagesNode` 知识库中没有该节点类型的任何知识
- 次要节点 `ImageConcatMulti` 知识库中没有该节点类型的任何知识
- 次要节点 `TextGenerate` 知识库中没有该节点类型的任何知识
- 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识
- 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明
- 次要节点 `ImageResizeKJv2` 仅有 Resolution 的通用知识，没有该节点自己的说明
- 次要节点 `ImageResizeKJv2` 仅有 Resolution 的通用知识，没有该节点自己的说明
- 次要节点 `MuyeTextEditOutput` 仅有 SaveImage 的通用知识，没有该节点自己的说明
- 次要节点 `SaveImageAdvanced` 仅有 SaveImage 的通用知识，没有该节点自己的说明
- 次要节点 `TTResolutionSelector` 仅有 Resolution 的通用知识，没有该节点自己的说明
- 次要节点 `TTResolutionSelector` 仅有 Resolution 的通用知识，没有该节点自己的说明
- 次要节点 `solarL_SaveImagesToZip` 仅有 SaveImage 的通用知识，没有该节点自己的说明
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

---
key: 图片生成/文生图/Qwen Image 2.1官流文生、编辑混合流_2106032439419301890.json
name: Qwen Image 2.1官流文生、编辑混合流_2106032439419301890
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Qwen Image 2.1官流文生、编辑混合流_2106032439419301890.json
hash: 863e73d60c069618
coverage: 0.361702
learned_at: 2026-10-06 21:48:31
nodes: [UNETLoader, VAELoader, EmptyLatentImage, VAEDecode, ComfySwitchNode, QwenImage21Cache, CLIPLoader, LoadImage, TextEncodeQwenImage21, CR Prompt Text, LoadImage, ImageResizeKJv2, LoadImage, ImageResizeKJv2, LoadImage, 孤海注释, ImageResizeKJv2, LoadImage, TTResolutionSelector, TTResolutionSelector, ImageResizeKJv2, TTResolutionSelector, CR Prompt Text, CLIPLoader, TTResolutionSelector, KSampler, CLIPLoader, easy showAnything, JWStringConcat, easy showAnything, easy showAnything, StringMergeNode, ResolutionSelector, SaveImageAdvanced, CR Prompt Text, Fast Groups Bypasser (rgthree), ImageResizeKJv2, CR Prompt Text, easy cleanGpuUsed, MuyeTextEditOutput, ZML_AnyTypeSwitch, TextGenerate, MuyeTextEditOutput, TextGenerate, TTResolutionSelector, BatchImagesNode, SaveImage]
patterns: []
missing: [BatchImagesNode, Fast Groups Bypasser (rgthree), JWStringConcat, StringMergeNode, TextGenerate, TextGenerate, ZML_AnyTypeSwitch, easy cleanGpuUsed, CR Prompt Text, CR Prompt Text, CR Prompt Text, CR Prompt Text, ImageResizeKJv2, ImageResizeKJv2, ImageResizeKJv2, ImageResizeKJv2, ImageResizeKJv2, MuyeTextEditOutput, MuyeTextEditOutput, SaveImageAdvanced, TTResolutionSelector, TTResolutionSelector, TTResolutionSelector, TTResolutionSelector, TTResolutionSelector]
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 55507293073990, "steps": 40, "width": 1024}
discoveries: [次要节点 `BatchImagesNode` 知识库中没有该节点类型的任何知识, 次要节点 `Fast Groups Bypasser (rgthree)` 知识库中没有该节点类型的任何知识, 次要节点 `JWStringConcat` 知识库中没有该节点类型的任何知识, 次要节点 `StringMergeNode` 知识库中没有该节点类型的任何知识, 次要节点 `TextGenerate` 知识库中没有该节点类型的任何知识, 次要节点 `TextGenerate` 知识库中没有该节点类型的任何知识, 次要节点 `ZML_AnyTypeSwitch` 知识库中没有该节点类型的任何知识, 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识, 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明, 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明, 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明, 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明, 次要节点 `ImageResizeKJv2` 仅有 Resolution 的通用知识，没有该节点自己的说明, 次要节点 `ImageResizeKJv2` 仅有 Resolution 的通用知识，没有该节点自己的说明, 次要节点 `ImageResizeKJv2` 仅有 Resolution 的通用知识，没有该节点自己的说明, 次要节点 `ImageResizeKJv2` 仅有 Resolution 的通用知识，没有该节点自己的说明, 次要节点 `ImageResizeKJv2` 仅有 Resolution 的通用知识，没有该节点自己的说明, 次要节点 `MuyeTextEditOutput` 仅有 SaveImage 的通用知识，没有该节点自己的说明, 次要节点 `MuyeTextEditOutput` 仅有 SaveImage 的通用知识，没有该节点自己的说明, 次要节点 `SaveImageAdvanced` 仅有 SaveImage 的通用知识，没有该节点自己的说明, 次要节点 `TTResolutionSelector` 仅有 Resolution 的通用知识，没有该节点自己的说明, 次要节点 `TTResolutionSelector` 仅有 Resolution 的通用知识，没有该节点自己的说明, 次要节点 `TTResolutionSelector` 仅有 Resolution 的通用知识，没有该节点自己的说明, 次要节点 `TTResolutionSelector` 仅有 Resolution 的通用知识，没有该节点自己的说明, 次要节点 `TTResolutionSelector` 仅有 Resolution 的通用知识，没有该节点自己的说明]
---

# 图片生成/文生图/Qwen Image 2.1官流文生、编辑混合流_2106032439419301890.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Qwen Image 2.1官流文生、编辑混合流_2106032439419301890.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（47 个）：
- `UNETLoader` ★核心
- `VAELoader`
- `EmptyLatentImage` ★核心
- `VAEDecode` ★核心
- `ComfySwitchNode`
- `QwenImage21Cache`
- `CLIPLoader`
- `LoadImage`
- `TextEncodeQwenImage21`
- `CR Prompt Text`
- `LoadImage`
- `ImageResizeKJv2`
- `LoadImage`
- `ImageResizeKJv2`
- `LoadImage`
- `孤海注释`
- `ImageResizeKJv2`
- `LoadImage`
- `TTResolutionSelector`
- `TTResolutionSelector`
- `ImageResizeKJv2`
- `TTResolutionSelector`
- `CR Prompt Text`
- `CLIPLoader`
- `TTResolutionSelector`
- `KSampler` ★核心
- `CLIPLoader`
- `easy showAnything`
- `JWStringConcat`
- `easy showAnything`
- `easy showAnything`
- `StringMergeNode`
- `ResolutionSelector`
- `SaveImageAdvanced`
- `CR Prompt Text`
- `Fast Groups Bypasser (rgthree)`
- `ImageResizeKJv2`
- `CR Prompt Text`
- `easy cleanGpuUsed`
- `MuyeTextEditOutput`
- `ZML_AnyTypeSwitch`
- `TextGenerate`
- `MuyeTextEditOutput`
- `TextGenerate`
- `TTResolutionSelector`
- `BatchImagesNode`
- `SaveImage`

## 关键参数

- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`
- `seed` = `55507293073990`
- `steps` = `40`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **36%**（17/47）

**有卡**：`UNETLoader`、`VAELoader`、`EmptyLatentImage`、`VAEDecode`、`QwenImage21Cache`、`CLIPLoader`、`LoadImage`、`TextEncodeQwenImage21`、`KSampler`、`ResolutionSelector`、`SaveImage`

**缺卡**（25）：`BatchImagesNode`、`Fast Groups Bypasser (rgthree)`、`JWStringConcat`、`StringMergeNode`、`TextGenerate`、`TextGenerate`、`ZML_AnyTypeSwitch`、`easy cleanGpuUsed`、`CR Prompt Text`、`CR Prompt Text`、`CR Prompt Text`、`CR Prompt Text`、`ImageResizeKJv2`、`ImageResizeKJv2`、`ImageResizeKJv2`、`ImageResizeKJv2`、`ImageResizeKJv2`、`MuyeTextEditOutput`、`MuyeTextEditOutput`、`SaveImageAdvanced`、`TTResolutionSelector`、`TTResolutionSelector`、`TTResolutionSelector`、`TTResolutionSelector`、`TTResolutionSelector`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、EmptyLatentImage、ResolutionSelector、SaveImage

## 学习发现

- 次要节点 `BatchImagesNode` 知识库中没有该节点类型的任何知识
- 次要节点 `Fast Groups Bypasser (rgthree)` 知识库中没有该节点类型的任何知识
- 次要节点 `JWStringConcat` 知识库中没有该节点类型的任何知识
- 次要节点 `StringMergeNode` 知识库中没有该节点类型的任何知识
- 次要节点 `TextGenerate` 知识库中没有该节点类型的任何知识
- 次要节点 `TextGenerate` 知识库中没有该节点类型的任何知识
- 次要节点 `ZML_AnyTypeSwitch` 知识库中没有该节点类型的任何知识
- 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识
- 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明
- 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明
- 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明
- 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明
- 次要节点 `ImageResizeKJv2` 仅有 Resolution 的通用知识，没有该节点自己的说明
- 次要节点 `ImageResizeKJv2` 仅有 Resolution 的通用知识，没有该节点自己的说明
- 次要节点 `ImageResizeKJv2` 仅有 Resolution 的通用知识，没有该节点自己的说明
- 次要节点 `ImageResizeKJv2` 仅有 Resolution 的通用知识，没有该节点自己的说明
- 次要节点 `ImageResizeKJv2` 仅有 Resolution 的通用知识，没有该节点自己的说明
- 次要节点 `MuyeTextEditOutput` 仅有 SaveImage 的通用知识，没有该节点自己的说明
- 次要节点 `MuyeTextEditOutput` 仅有 SaveImage 的通用知识，没有该节点自己的说明
- 次要节点 `SaveImageAdvanced` 仅有 SaveImage 的通用知识，没有该节点自己的说明
- 次要节点 `TTResolutionSelector` 仅有 Resolution 的通用知识，没有该节点自己的说明
- 次要节点 `TTResolutionSelector` 仅有 Resolution 的通用知识，没有该节点自己的说明
- 次要节点 `TTResolutionSelector` 仅有 Resolution 的通用知识，没有该节点自己的说明
- 次要节点 `TTResolutionSelector` 仅有 Resolution 的通用知识，没有该节点自己的说明
- 次要节点 `TTResolutionSelector` 仅有 Resolution 的通用知识，没有该节点自己的说明

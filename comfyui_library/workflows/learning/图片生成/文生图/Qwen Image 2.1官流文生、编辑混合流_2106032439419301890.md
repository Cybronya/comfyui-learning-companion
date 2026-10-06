---
key: 图片生成/文生图/Qwen Image 2.1官流文生、编辑混合流_2106032439419301890.json
name: Qwen Image 2.1官流文生、编辑混合流_2106032439419301890
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Qwen Image 2.1官流文生、编辑混合流_2106032439419301890.json
hash: 863e73d60c069618
coverage: 0.765957
learned_at: 2026-10-06 22:37:29
nodes: [UNETLoader, VAELoader, EmptyLatentImage, VAEDecode, ComfySwitchNode, QwenImage21Cache, CLIPLoader, LoadImage, TextEncodeQwenImage21, CR Prompt Text, LoadImage, ImageResizeKJv2, LoadImage, ImageResizeKJv2, LoadImage, 孤海注释, ImageResizeKJv2, LoadImage, TTResolutionSelector, TTResolutionSelector, ImageResizeKJv2, TTResolutionSelector, CR Prompt Text, CLIPLoader, TTResolutionSelector, KSampler, CLIPLoader, easy showAnything, JWStringConcat, easy showAnything, easy showAnything, StringMergeNode, ResolutionSelector, SaveImageAdvanced, CR Prompt Text, Fast Groups Bypasser (rgthree), ImageResizeKJv2, CR Prompt Text, easy cleanGpuUsed, MuyeTextEditOutput, ZML_AnyTypeSwitch, TextGenerate, MuyeTextEditOutput, TextGenerate, TTResolutionSelector, BatchImagesNode, SaveImage]
patterns: []
missing: [easy cleanGpuUsed, CR Prompt Text, CR Prompt Text, CR Prompt Text, CR Prompt Text]
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 55507293073990, "steps": 40, "width": 1024}
discoveries: [次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识, 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明, 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明, 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明, 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明]
---

# 图片生成/文生图/Qwen Image 2.1官流文生、编辑混合流_2106032439419301890.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Qwen Image 2.1官流文生、编辑混合流_2106032439419301890.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

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

覆盖率 **77%**（36/47）

**有卡**：`UNETLoader`、`VAELoader`、`EmptyLatentImage`、`VAEDecode`、`QwenImage21Cache`、`CLIPLoader`、`LoadImage`、`TextEncodeQwenImage21`、`ImageResizeKJv2`、`TTResolutionSelector`、`KSampler`、`JWStringConcat`、`StringMergeNode`、`ResolutionSelector`、`SaveImageAdvanced`、`MuyeTextEditOutput`、`ZML_AnyTypeSwitch`、`TextGenerate`、`BatchImagesNode`、`SaveImage`

**缺卡**（5）：`easy cleanGpuUsed`、`CR Prompt Text`、`CR Prompt Text`、`CR Prompt Text`、`CR Prompt Text`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、EmptyLatentImage、ResolutionSelector、SaveImage

## 学习发现

- 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识
- 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明
- 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明
- 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明
- 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明

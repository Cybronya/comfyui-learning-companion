---
key: 图片生成/图生图/Qwen+Image+2.1+多合一工作流小志版_2102085069686009857.json
name: Qwen+Image+2.1+多合一工作流小志版_2102085069686009857
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen+Image+2.1+多合一工作流小志版_2102085069686009857.json
hash: 498fa813d20437ad
coverage: 0.522388
learned_at: 2026-10-10 20:48:09
nodes: [ConditioningZeroOut, VAEDecode, QwenImage21ModelConfig_EditUtils, QwenImage21Cache, GetNode, GetNode, GetNode, CLIPLoader, SetNode, EditTextEncode_EditUtils, SetNode, SetNode, VAELoader, UNETLoader, CLIPLoader, SetNode, SetNode, CLIPLoader, BatchImagesNode, PrimitiveInt, Label (rgthree), Label (rgthree), Label (rgthree), EmptyLatentImage, GetNode, TextEncodeQwenImage21, PrimitiveInt, PrimitiveInt, MarkdownNote, Label (rgthree), KSampler, KSampler, MarkdownNote, PrimitiveInt, CropWithPadInfo_EditUtils, PrimitiveStringMultiline, ResolutionSelector, GetNode, GetNode, GetNode, GetNode, easy showAnything, Note, TextGenerateLTX2Prompt, Label (rgthree), LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, PrimitiveInt, TextGenerateLTX2Prompt, CropWithPadInfo_EditUtils, PrimitiveStringMultiline, QwenImage21ConfigPreparer_EditUtils, QwenImage21ConfigPreparer_EditUtils, QwenImage21ConfigPreparer_EditUtils, QwenImage21ConfigPreparer_EditUtils, QwenImage21ConfigPreparer_EditUtils, QwenImage21ConfigPreparer_EditUtils, SaveImage, Image Comparer (rgthree), Fast Groups Bypasser (rgthree), Fast Groups Bypasser (rgthree), VAEDecode, SaveImage]
patterns: []
missing: [Label (rgthree), Label (rgthree), Label (rgthree), Label (rgthree), Label (rgthree)]
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 484131308893510, "steps": 25, "width": 1024}
discoveries: [次要节点 `Label (rgthree)` 知识库中没有该节点类型的任何知识, 次要节点 `Label (rgthree)` 知识库中没有该节点类型的任何知识, 次要节点 `Label (rgthree)` 知识库中没有该节点类型的任何知识, 次要节点 `Label (rgthree)` 知识库中没有该节点类型的任何知识, 次要节点 `Label (rgthree)` 知识库中没有该节点类型的任何知识]
---

# 图片生成/图生图/Qwen+Image+2.1+多合一工作流小志版_2102085069686009857.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen+Image+2.1+多合一工作流小志版_2102085069686009857.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（67 个）：
- `ConditioningZeroOut`
- `VAEDecode` ★核心
- `QwenImage21ModelConfig_EditUtils`
- `QwenImage21Cache`
- `GetNode`
- `GetNode`
- `GetNode`
- `CLIPLoader`
- `SetNode`
- `EditTextEncode_EditUtils`
- `SetNode`
- `SetNode`
- `VAELoader`
- `UNETLoader` ★核心
- `CLIPLoader`
- `SetNode`
- `SetNode`
- `CLIPLoader`
- `BatchImagesNode`
- `PrimitiveInt`
- `Label (rgthree)`
- `Label (rgthree)`
- `Label (rgthree)`
- `EmptyLatentImage` ★核心
- `GetNode`
- `TextEncodeQwenImage21`
- `PrimitiveInt`
- `PrimitiveInt`
- `MarkdownNote`
- `Label (rgthree)`
- `KSampler` ★核心
- `KSampler` ★核心
- `MarkdownNote`
- `PrimitiveInt`
- `CropWithPadInfo_EditUtils`
- `PrimitiveStringMultiline`
- `ResolutionSelector`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `easy showAnything`
- `Note`
- `TextGenerateLTX2Prompt`
- `Label (rgthree)`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `PrimitiveInt`
- `TextGenerateLTX2Prompt`
- `CropWithPadInfo_EditUtils`
- `PrimitiveStringMultiline`
- `QwenImage21ConfigPreparer_EditUtils`
- `QwenImage21ConfigPreparer_EditUtils`
- `QwenImage21ConfigPreparer_EditUtils`
- `QwenImage21ConfigPreparer_EditUtils`
- `QwenImage21ConfigPreparer_EditUtils`
- `QwenImage21ConfigPreparer_EditUtils`
- `SaveImage`
- `Image Comparer (rgthree)`
- `Fast Groups Bypasser (rgthree)`
- `Fast Groups Bypasser (rgthree)`
- `VAEDecode` ★核心
- `SaveImage`

## 关键参数

- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`
- `seed` = `484131308893510`
- `steps` = `25`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **52%**（35/67）

**有卡**：`ConditioningZeroOut`、`VAEDecode`、`QwenImage21ModelConfig_EditUtils`、`QwenImage21Cache`、`CLIPLoader`、`EditTextEncode_EditUtils`、`VAELoader`、`UNETLoader`、`BatchImagesNode`、`EmptyLatentImage`、`TextEncodeQwenImage21`、`KSampler`、`CropWithPadInfo_EditUtils`、`ResolutionSelector`、`TextGenerateLTX2Prompt`、`LoadImage`、`QwenImage21ConfigPreparer_EditUtils`、`SaveImage`

**缺卡**（5）：`Label (rgthree)`、`Label (rgthree)`、`Label (rgthree)`、`Label (rgthree)`、`Label (rgthree)`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、ConditioningZeroOut、EmptyLatentImage、ResolutionSelector

## 学习发现

- 次要节点 `Label (rgthree)` 知识库中没有该节点类型的任何知识
- 次要节点 `Label (rgthree)` 知识库中没有该节点类型的任何知识
- 次要节点 `Label (rgthree)` 知识库中没有该节点类型的任何知识
- 次要节点 `Label (rgthree)` 知识库中没有该节点类型的任何知识
- 次要节点 `Label (rgthree)` 知识库中没有该节点类型的任何知识

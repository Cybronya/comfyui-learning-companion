---
key: 图片生成/图生图/Qwen Image 2.1 图片编辑（提示词反推）2609_2106049358109167617.json
name: Qwen Image 2.1 图片编辑（提示词反推）2609_2106049358109167617.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen Image 2.1 图片编辑（提示词反推）2609_2106049358109167617.json
hash: e210f808161eb7b8
coverage: 0.632653
learned_at: 2026-10-09 22:09:18
nodes: [UNETLoader, ModelAttentionBackend, llama_cpp_model_loader, QwenImage21Cache, easy ifElse, llama_cpp_instruct_adv, CLIPLoader, easy lengthAnything, easy forLoopStart, VAELoader, EmptyLatentImage, easy forLoopEnd, PreviewAny, PrimitiveStringMultiline, RepeatLatentBatch, ConditioningZeroOut, CropWithPadInfo_EditUtils, VAEDecode, EditTextEncode_EditUtils, RepeatLatentBatch, CropWithPadInfo_EditUtils, Image Comparer (rgthree), SaveImage, QwenImage21ConfigPreparer_EditUtils, easy ifElse, PrimitiveInt, TextEncodeQwenImage21, KSampler, easy imageSizeByLongerSide, easy indexAnything, QwenImage21ModelConfig_EditUtils, easy ifElse, easy ifElse, easy ifElse, easy ifElse, LoadImage, ComfyMathExpression, easy ifElse, PrimitiveBoolean, PrimitiveBoolean, easy makeImageList, LoadImage, LoadImage, LoadImage, PrimitiveInt, PrimitiveBoolean, LoadImage, LoadImage, ResolutionSelector]
patterns: []
missing: [easy forLoopEnd, easy forLoopStart, easy indexAnything, easy lengthAnything, easy makeImageList, easy imageSizeByLongerSide]
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "beta", "seed": 999, "steps": 25, "width": 1024}
discoveries: [次要节点 `easy forLoopEnd` 知识库中没有该节点类型的任何知识, 次要节点 `easy forLoopStart` 知识库中没有该节点类型的任何知识, 次要节点 `easy indexAnything` 知识库中没有该节点类型的任何知识, 次要节点 `easy lengthAnything` 知识库中没有该节点类型的任何知识, 次要节点 `easy makeImageList` 知识库中没有该节点类型的任何知识, 次要节点 `easy imageSizeByLongerSide` 仅有 Resolution 的通用知识，没有该节点自己的说明]
---

# 图片生成/图生图/Qwen Image 2.1 图片编辑（提示词反推）2609_2106049358109167617.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/2106049358109167617.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（49 个）：
- `UNETLoader` ★核心
- `ModelAttentionBackend`
- `llama_cpp_model_loader`
- `QwenImage21Cache`
- `easy ifElse`
- `llama_cpp_instruct_adv`
- `CLIPLoader`
- `easy lengthAnything`
- `easy forLoopStart`
- `VAELoader`
- `EmptyLatentImage` ★核心
- `easy forLoopEnd`
- `PreviewAny`
- `PrimitiveStringMultiline`
- `RepeatLatentBatch`
- `ConditioningZeroOut`
- `CropWithPadInfo_EditUtils`
- `VAEDecode` ★核心
- `EditTextEncode_EditUtils`
- `RepeatLatentBatch`
- `CropWithPadInfo_EditUtils`
- `Image Comparer (rgthree)`
- `SaveImage`
- `QwenImage21ConfigPreparer_EditUtils`
- `easy ifElse`
- `PrimitiveInt`
- `TextEncodeQwenImage21`
- `KSampler` ★核心
- `easy imageSizeByLongerSide`
- `easy indexAnything`
- `QwenImage21ModelConfig_EditUtils`
- `easy ifElse`
- `easy ifElse`
- `easy ifElse`
- `easy ifElse`
- `LoadImage`
- `ComfyMathExpression`
- `easy ifElse`
- `PrimitiveBoolean`
- `PrimitiveBoolean`
- `easy makeImageList`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `PrimitiveInt`
- `PrimitiveBoolean`
- `LoadImage`
- `LoadImage`
- `ResolutionSelector`

## 关键参数

- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`
- `seed` = `999`
- `steps` = `25`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `beta`
- `denoise` = `1`

## 知识

覆盖率 **63%**（31/49）

**有卡**：`UNETLoader`、`ModelAttentionBackend`、`llama_cpp_model_loader`、`QwenImage21Cache`、`llama_cpp_instruct_adv`、`CLIPLoader`、`VAELoader`、`EmptyLatentImage`、`RepeatLatentBatch`、`ConditioningZeroOut`、`CropWithPadInfo_EditUtils`、`VAEDecode`、`EditTextEncode_EditUtils`、`SaveImage`、`QwenImage21ConfigPreparer_EditUtils`、`TextEncodeQwenImage21`、`KSampler`、`QwenImage21ModelConfig_EditUtils`、`LoadImage`、`ComfyMathExpression`、`PrimitiveBoolean`、`ResolutionSelector`

**缺卡**（6）：`easy forLoopEnd`、`easy forLoopStart`、`easy indexAnything`、`easy lengthAnything`、`easy makeImageList`、`easy imageSizeByLongerSide`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、ConditioningZeroOut、EmptyLatentImage、ResolutionSelector

## 学习发现

- 次要节点 `easy forLoopEnd` 知识库中没有该节点类型的任何知识
- 次要节点 `easy forLoopStart` 知识库中没有该节点类型的任何知识
- 次要节点 `easy indexAnything` 知识库中没有该节点类型的任何知识
- 次要节点 `easy lengthAnything` 知识库中没有该节点类型的任何知识
- 次要节点 `easy makeImageList` 知识库中没有该节点类型的任何知识
- 次要节点 `easy imageSizeByLongerSide` 仅有 Resolution 的通用知识，没有该节点自己的说明

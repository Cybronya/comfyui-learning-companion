---
key: 图片生成/图生图/Qwen Image 2.1图片编辑一流通吃｜反推提示词加文生图图生图｜全能编辑器_2102250613080940546.json
name: Qwen Image 2.1图片编辑一流通吃｜反推提示词加文生图图生图｜全能编辑器_2102250613080940546
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen Image 2.1图片编辑一流通吃｜反推提示词加文生图图生图｜全能编辑器_2102250613080940546.json
hash: 255fb3c802461eaa
coverage: 0.76087
learned_at: 2026-10-10 20:48:06
nodes: [UNETLoader, ModelAttentionBackend, llama_cpp_model_loader, QwenImage21Cache, easy ifElse, llama_cpp_instruct_adv, CLIPLoader, easy lengthAnything, easy forLoopStart, VAELoader, ResolutionSelector, EmptyLatentImage, easy forLoopEnd, PreviewAny, PrimitiveStringMultiline, RepeatLatentBatch, ConditioningZeroOut, CropWithPadInfo_EditUtils, VAEDecode, EditTextEncode_EditUtils, RepeatLatentBatch, CropWithPadInfo_EditUtils, Image Comparer (rgthree), SaveImage, QwenImage21ConfigPreparer_EditUtils, easy ifElse, PrimitiveInt, TextEncodeQwenImage21, KSampler, easy imageSizeByLongerSide, easy indexAnything, QwenImage21ModelConfig_EditUtils, easy ifElse, easy ifElse, easy ifElse, easy ifElse, LoadImage, LoadImage, LoadImage, ComfyMathExpression, easy ifElse, PrimitiveBoolean, PrimitiveBoolean, PrimitiveBoolean, easy makeImageList, LoadImage, LoadImage, LoadImage, PrimitiveInt, 孤海注释, 孤海注释, UNETLoader, CLIPLoader, CLIPTextEncode, VAELoader, EmptyLatentImage, KSampler, VAEDecode, solarL_SaveImagesToZip, JjkText, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, CLIPTextEncode, Note]
patterns: [text_to_image]
missing: [easy forLoopEnd, easy forLoopStart, easy indexAnything, easy lengthAnything, easy makeImageList, easy imageSizeByLongerSide]
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [次要节点 `easy forLoopEnd` 知识库中没有该节点类型的任何知识, 次要节点 `easy forLoopStart` 知识库中没有该节点类型的任何知识, 次要节点 `easy indexAnything` 知识库中没有该节点类型的任何知识, 次要节点 `easy lengthAnything` 知识库中没有该节点类型的任何知识, 次要节点 `easy makeImageList` 知识库中没有该节点类型的任何知识, 次要节点 `easy imageSizeByLongerSide` 仅有 Resolution 的通用知识，没有该节点自己的说明, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/Qwen Image 2.1图片编辑一流通吃｜反推提示词加文生图图生图｜全能编辑器_2102250613080940546.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen Image 2.1图片编辑一流通吃｜反推提示词加文生图图生图｜全能编辑器_2102250613080940546.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（92 个）：
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
- `ResolutionSelector`
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
- `LoadImage`
- `LoadImage`
- `ComfyMathExpression`
- `easy ifElse`
- `PrimitiveBoolean`
- `PrimitiveBoolean`
- `PrimitiveBoolean`
- `easy makeImageList`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `PrimitiveInt`
- `孤海注释`
- `孤海注释`
- `UNETLoader` ★核心
- `CLIPLoader`
- `CLIPTextEncode` ★核心
- `VAELoader`
- `EmptyLatentImage` ★核心
- `KSampler` ★核心
- `VAEDecode` ★核心
- `solarL_SaveImagesToZip`
- `JjkText`
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
- `CLIPTextEncode` ★核心
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

覆盖率 **76%**（70/92）

**有卡**：`UNETLoader`、`ModelAttentionBackend`、`llama_cpp_model_loader`、`QwenImage21Cache`、`llama_cpp_instruct_adv`、`CLIPLoader`、`VAELoader`、`ResolutionSelector`、`EmptyLatentImage`、`RepeatLatentBatch`、`ConditioningZeroOut`、`CropWithPadInfo_EditUtils`、`VAEDecode`、`EditTextEncode_EditUtils`、`SaveImage`、`QwenImage21ConfigPreparer_EditUtils`、`TextEncodeQwenImage21`、`KSampler`、`QwenImage21ModelConfig_EditUtils`、`LoadImage`、`ComfyMathExpression`、`PrimitiveBoolean`、`CLIPTextEncode`、`solarL_SaveImagesToZip`、`LoraLoaderModelOnly`

**缺卡**（6）：`easy forLoopEnd`、`easy forLoopStart`、`easy indexAnything`、`easy lengthAnything`、`easy makeImageList`、`easy imageSizeByLongerSide`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、ConditioningZeroOut

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- 次要节点 `easy forLoopEnd` 知识库中没有该节点类型的任何知识
- 次要节点 `easy forLoopStart` 知识库中没有该节点类型的任何知识
- 次要节点 `easy indexAnything` 知识库中没有该节点类型的任何知识
- 次要节点 `easy lengthAnything` 知识库中没有该节点类型的任何知识
- 次要节点 `easy makeImageList` 知识库中没有该节点类型的任何知识
- 次要节点 `easy imageSizeByLongerSide` 仅有 Resolution 的通用知识，没有该节点自己的说明
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

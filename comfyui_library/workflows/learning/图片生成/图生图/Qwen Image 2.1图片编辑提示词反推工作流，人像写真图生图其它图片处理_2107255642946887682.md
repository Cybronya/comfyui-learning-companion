---
key: 图片生成/图生图/Qwen Image 2.1图片编辑提示词反推工作流，人像写真图生图其它图片处理_2107255642946887682.json
name: Qwen Image 2.1图片编辑提示词反推工作流，人像写真图生图其它图片处理_2107255642946887682
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen Image 2.1图片编辑提示词反推工作流，人像写真图生图其它图片处理_2107255642946887682.json
hash: b5e04c22ee5423a3
coverage: 0.525641
learned_at: 2026-10-06 21:41:14
nodes: [UNETLoader, ModelAttentionBackend, llama_cpp_model_loader, QwenImage21Cache, easy ifElse, llama_cpp_instruct_adv, CLIPLoader, easy lengthAnything, easy forLoopStart, VAELoader, EmptyLatentImage, easy forLoopEnd, PreviewAny, PrimitiveStringMultiline, RepeatLatentBatch, ConditioningZeroOut, CropWithPadInfo_EditUtils, VAEDecode, EditTextEncode_EditUtils, RepeatLatentBatch, CropWithPadInfo_EditUtils, Image Comparer (rgthree), SaveImage, QwenImage21ConfigPreparer_EditUtils, easy ifElse, PrimitiveInt, TextEncodeQwenImage21, KSampler, easy imageSizeByLongerSide, easy indexAnything, QwenImage21ModelConfig_EditUtils, easy ifElse, easy ifElse, easy ifElse, easy ifElse, LoadImage, ComfyMathExpression, easy ifElse, PrimitiveBoolean, PrimitiveBoolean, easy makeImageList, LoadImage, LoadImage, LoadImage, PrimitiveInt, PrimitiveBoolean, LoadImage, LoadImage, ResolutionSelector, 孤海注释, 孤海注释, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, KSampler, EmptyLatentImage, JjkText, CLIPTextEncode, CLIPTextEncode, solarL_SaveImagesToZip, VAEDecode, CLIPLoader, VAELoader, Note]
patterns: [text_to_image]
missing: [ComfyMathExpression, CropWithPadInfo_EditUtils, CropWithPadInfo_EditUtils, ModelAttentionBackend, PrimitiveBoolean, PrimitiveBoolean, PrimitiveBoolean, QwenImage21ConfigPreparer_EditUtils, QwenImage21ModelConfig_EditUtils, easy forLoopEnd, easy forLoopStart, easy indexAnything, easy lengthAnything, easy makeImageList, llama_cpp_instruct_adv, llama_cpp_model_loader, EditTextEncode_EditUtils, PreviewAny, RepeatLatentBatch, RepeatLatentBatch, easy imageSizeByLongerSide, solarL_SaveImagesToZip]
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [次要节点 `ComfyMathExpression` 知识库中没有该节点类型的任何知识, 次要节点 `CropWithPadInfo_EditUtils` 知识库中没有该节点类型的任何知识, 次要节点 `CropWithPadInfo_EditUtils` 知识库中没有该节点类型的任何知识, 次要节点 `ModelAttentionBackend` 知识库中没有该节点类型的任何知识, 次要节点 `PrimitiveBoolean` 知识库中没有该节点类型的任何知识, 次要节点 `PrimitiveBoolean` 知识库中没有该节点类型的任何知识, 次要节点 `PrimitiveBoolean` 知识库中没有该节点类型的任何知识, 次要节点 `QwenImage21ConfigPreparer_EditUtils` 知识库中没有该节点类型的任何知识, 次要节点 `QwenImage21ModelConfig_EditUtils` 知识库中没有该节点类型的任何知识, 次要节点 `easy forLoopEnd` 知识库中没有该节点类型的任何知识, 次要节点 `easy forLoopStart` 知识库中没有该节点类型的任何知识, 次要节点 `easy indexAnything` 知识库中没有该节点类型的任何知识, 次要节点 `easy lengthAnything` 知识库中没有该节点类型的任何知识, 次要节点 `easy makeImageList` 知识库中没有该节点类型的任何知识, 次要节点 `llama_cpp_instruct_adv` 知识库中没有该节点类型的任何知识, 次要节点 `llama_cpp_model_loader` 知识库中没有该节点类型的任何知识, 次要节点 `EditTextEncode_EditUtils` 仅有 VAE 的通用知识，没有该节点自己的说明, 次要节点 `PreviewAny` 仅有 SaveImage 的通用知识，没有该节点自己的说明, 次要节点 `RepeatLatentBatch` 仅有 VAE 的通用知识，没有该节点自己的说明, 次要节点 `RepeatLatentBatch` 仅有 VAE 的通用知识，没有该节点自己的说明, 次要节点 `easy imageSizeByLongerSide` 仅有 Resolution 的通用知识，没有该节点自己的说明, 次要节点 `solarL_SaveImagesToZip` 仅有 SaveImage 的通用知识，没有该节点自己的说明, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/Qwen Image 2.1图片编辑提示词反推工作流，人像写真图生图其它图片处理_2107255642946887682.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen Image 2.1图片编辑提示词反推工作流，人像写真图生图其它图片处理_2107255642946887682.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（78 个）：
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

覆盖率 **53%**（41/78）

**有卡**：`UNETLoader`、`QwenImage21Cache`、`CLIPLoader`、`VAELoader`、`EmptyLatentImage`、`ConditioningZeroOut`、`VAEDecode`、`SaveImage`、`TextEncodeQwenImage21`、`KSampler`、`LoadImage`、`ResolutionSelector`、`LoraLoaderModelOnly`、`CLIPTextEncode`

**缺卡**（22）：`ComfyMathExpression`、`CropWithPadInfo_EditUtils`、`CropWithPadInfo_EditUtils`、`ModelAttentionBackend`、`PrimitiveBoolean`、`PrimitiveBoolean`、`PrimitiveBoolean`、`QwenImage21ConfigPreparer_EditUtils`、`QwenImage21ModelConfig_EditUtils`、`easy forLoopEnd`、`easy forLoopStart`、`easy indexAnything`、`easy lengthAnything`、`easy makeImageList`、`llama_cpp_instruct_adv`、`llama_cpp_model_loader`、`EditTextEncode_EditUtils`、`PreviewAny`、`RepeatLatentBatch`、`RepeatLatentBatch`、`easy imageSizeByLongerSide`、`solarL_SaveImagesToZip`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、ConditioningZeroOut

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- 次要节点 `ComfyMathExpression` 知识库中没有该节点类型的任何知识
- 次要节点 `CropWithPadInfo_EditUtils` 知识库中没有该节点类型的任何知识
- 次要节点 `CropWithPadInfo_EditUtils` 知识库中没有该节点类型的任何知识
- 次要节点 `ModelAttentionBackend` 知识库中没有该节点类型的任何知识
- 次要节点 `PrimitiveBoolean` 知识库中没有该节点类型的任何知识
- 次要节点 `PrimitiveBoolean` 知识库中没有该节点类型的任何知识
- 次要节点 `PrimitiveBoolean` 知识库中没有该节点类型的任何知识
- 次要节点 `QwenImage21ConfigPreparer_EditUtils` 知识库中没有该节点类型的任何知识
- 次要节点 `QwenImage21ModelConfig_EditUtils` 知识库中没有该节点类型的任何知识
- 次要节点 `easy forLoopEnd` 知识库中没有该节点类型的任何知识
- 次要节点 `easy forLoopStart` 知识库中没有该节点类型的任何知识
- 次要节点 `easy indexAnything` 知识库中没有该节点类型的任何知识
- 次要节点 `easy lengthAnything` 知识库中没有该节点类型的任何知识
- 次要节点 `easy makeImageList` 知识库中没有该节点类型的任何知识
- 次要节点 `llama_cpp_instruct_adv` 知识库中没有该节点类型的任何知识
- 次要节点 `llama_cpp_model_loader` 知识库中没有该节点类型的任何知识
- 次要节点 `EditTextEncode_EditUtils` 仅有 VAE 的通用知识，没有该节点自己的说明
- 次要节点 `PreviewAny` 仅有 SaveImage 的通用知识，没有该节点自己的说明
- 次要节点 `RepeatLatentBatch` 仅有 VAE 的通用知识，没有该节点自己的说明
- 次要节点 `RepeatLatentBatch` 仅有 VAE 的通用知识，没有该节点自己的说明
- 次要节点 `easy imageSizeByLongerSide` 仅有 Resolution 的通用知识，没有该节点自己的说明
- 次要节点 `solarL_SaveImagesToZip` 仅有 SaveImage 的通用知识，没有该节点自己的说明
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

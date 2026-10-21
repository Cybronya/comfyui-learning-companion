---
key: 图片生成/文生图/Qwen Image 2.1多合一工作流 全能图像编辑方案_2109008831576625154.json
name: Qwen Image 2.1多合一工作流 全能图像编辑方案_2109008831576625154
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Qwen Image 2.1多合一工作流 全能图像编辑方案_2109008831576625154.json
hash: a551e75ab65b604f
coverage: 0.681818
learned_at: 2026-10-21 02:54:12
nodes: [ConditioningZeroOut, VAEDecode, QwenImage21ModelConfig_EditUtils, QwenImage21Cache, GetNode, GetNode, GetNode, CLIPLoader, SetNode, EditTextEncode_EditUtils, SetNode, SetNode, VAELoader, UNETLoader, CLIPLoader, SetNode, SetNode, CLIPLoader, BatchImagesNode, PrimitiveInt, EmptyLatentImage, GetNode, TextEncodeQwenImage21, PrimitiveInt, PrimitiveInt, KSampler, KSampler, PrimitiveInt, CropWithPadInfo_EditUtils, PrimitiveStringMultiline, ResolutionSelector, GetNode, GetNode, GetNode, GetNode, easy showAnything, TextGenerateLTX2Prompt, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, PrimitiveInt, TextGenerateLTX2Prompt, CropWithPadInfo_EditUtils, PrimitiveStringMultiline, QwenImage21ConfigPreparer_EditUtils, QwenImage21ConfigPreparer_EditUtils, QwenImage21ConfigPreparer_EditUtils, QwenImage21ConfigPreparer_EditUtils, QwenImage21ConfigPreparer_EditUtils, QwenImage21ConfigPreparer_EditUtils, SaveImage, Image Comparer (rgthree), Fast Groups Bypasser (rgthree), Fast Groups Bypasser (rgthree), VAEDecode, SaveImage, 孤海注释, 孤海注释, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, KSampler, EmptyLatentImage, JjkText, CLIPTextEncode, CLIPTextEncode, solarL_SaveImagesToZip, VAEDecode, CLIPLoader, VAELoader, Note]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/文生图/Qwen Image 2.1多合一工作流 全能图像编辑方案_2109008831576625154.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Qwen Image 2.1多合一工作流 全能图像编辑方案_2109008831576625154.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（88 个）：
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
- `EmptyLatentImage` ★核心
- `GetNode`
- `TextEncodeQwenImage21`
- `PrimitiveInt`
- `PrimitiveInt`
- `KSampler` ★核心
- `KSampler` ★核心
- `PrimitiveInt`
- `CropWithPadInfo_EditUtils`
- `PrimitiveStringMultiline`
- `ResolutionSelector`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `easy showAnything`
- `TextGenerateLTX2Prompt`
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

覆盖率 **68%**（60/88）

**有卡**：`ConditioningZeroOut`、`VAEDecode`、`QwenImage21ModelConfig_EditUtils`、`QwenImage21Cache`、`CLIPLoader`、`EditTextEncode_EditUtils`、`VAELoader`、`UNETLoader`、`BatchImagesNode`、`EmptyLatentImage`、`TextEncodeQwenImage21`、`KSampler`、`CropWithPadInfo_EditUtils`、`ResolutionSelector`、`TextGenerateLTX2Prompt`、`LoadImage`、`QwenImage21ConfigPreparer_EditUtils`、`SaveImage`、`LoraLoaderModelOnly`、`CLIPTextEncode`、`solarL_SaveImagesToZip`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、ConditioningZeroOut

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

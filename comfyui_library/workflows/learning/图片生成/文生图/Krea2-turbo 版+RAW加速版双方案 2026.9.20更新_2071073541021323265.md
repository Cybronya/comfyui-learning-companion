---
key: 图片生成/文生图/Krea2-turbo 版+RAW加速版双方案 2026.9.20更新_2071073541021323265.json
name: Krea2-turbo 版+RAW加速版双方案 2026.9.20更新_2071073541021323265
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Krea2-turbo 版+RAW加速版双方案 2026.9.20更新_2071073541021323265.json
hash: b4606ad7390fbcb7
coverage: 0.795455
learned_at: 2026-10-07 03:05:08
nodes: [VAELoader, CLIPTextEncode, ConditioningZeroOut, SeedVR2LoadVAEModel, ImageScaleBy, SeedVR2LoadDiTModel, VAEDecode, SaveImage, SaveImage, EmptyLatentImage, easy clearCacheAll, SeedVR2VideoUpscaler, Image Comparer (rgthree), CLIPTextEncode, ConditioningZeroOut, PrimitiveStringMultiline, VAEDecode, SaveImage, EmptyLatentImage, UNETLoader, VAELoader, CLIPLoader, LoraLoaderModelOnly, KSampler, KSampler, SaveImage, Image Comparer (rgthree), SeedVR2LoadVAEModel, ImageScaleBy, SeedVR2LoadDiTModel, easy clearCacheAll, SeedVR2VideoUpscaler, easy int, UNETLoader, CLIPLoader, easy int, CR Text Concatenate, Text, LoraLoaderModelOnly, Text, LoraLoaderModelOnly, Fast Groups Muter (rgthree), KSampler, KSampler]
patterns: [text_to_image]
missing: [CR Text Concatenate, easy clearCacheAll, easy clearCacheAll, easy int, easy int]
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1680, "sampler_name": "euler_ancestral", "scheduler": "beta57", "seed": 587786870124111, "steps": 8, "width": 1024}
discoveries: [次要节点 `CR Text Concatenate` 知识库中没有该节点类型的任何知识, 次要节点 `easy clearCacheAll` 知识库中没有该节点类型的任何知识, 次要节点 `easy clearCacheAll` 知识库中没有该节点类型的任何知识, 次要节点 `easy int` 知识库中没有该节点类型的任何知识, 次要节点 `easy int` 知识库中没有该节点类型的任何知识, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/文生图/Krea2-turbo 版+RAW加速版双方案 2026.9.20更新_2071073541021323265.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Krea2-turbo 版+RAW加速版双方案 2026.9.20更新_2071073541021323265.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（44 个）：
- `VAELoader`
- `CLIPTextEncode` ★核心
- `ConditioningZeroOut`
- `SeedVR2LoadVAEModel`
- `ImageScaleBy`
- `SeedVR2LoadDiTModel`
- `VAEDecode` ★核心
- `SaveImage`
- `SaveImage`
- `EmptyLatentImage` ★核心
- `easy clearCacheAll`
- `SeedVR2VideoUpscaler`
- `Image Comparer (rgthree)`
- `CLIPTextEncode` ★核心
- `ConditioningZeroOut`
- `PrimitiveStringMultiline`
- `VAEDecode` ★核心
- `SaveImage`
- `EmptyLatentImage` ★核心
- `UNETLoader` ★核心
- `VAELoader`
- `CLIPLoader`
- `LoraLoaderModelOnly` ★核心
- `KSampler` ★核心
- `KSampler` ★核心
- `SaveImage`
- `Image Comparer (rgthree)`
- `SeedVR2LoadVAEModel`
- `ImageScaleBy`
- `SeedVR2LoadDiTModel`
- `easy clearCacheAll`
- `SeedVR2VideoUpscaler`
- `easy int`
- `UNETLoader` ★核心
- `CLIPLoader`
- `easy int`
- `CR Text Concatenate`
- `Text`
- `LoraLoaderModelOnly` ★核心
- `Text`
- `LoraLoaderModelOnly` ★核心
- `Fast Groups Muter (rgthree)`
- `KSampler` ★核心
- `KSampler` ★核心

**识别到的模式**：text_to_image

## 关键参数

- `width` = `1024`
- `height` = `1680`
- `batch_size` = `1`
- `seed` = `587786870124111`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `euler_ancestral`
- `scheduler` = `beta57`
- `denoise` = `1`

## 知识

覆盖率 **80%**（35/44）

**有卡**：`VAELoader`、`CLIPTextEncode`、`ConditioningZeroOut`、`SeedVR2LoadVAEModel`、`ImageScaleBy`、`SeedVR2LoadDiTModel`、`VAEDecode`、`SaveImage`、`EmptyLatentImage`、`SeedVR2VideoUpscaler`、`UNETLoader`、`CLIPLoader`、`LoraLoaderModelOnly`、`KSampler`、`Text`

**缺卡**（5）：`CR Text Concatenate`、`easy clearCacheAll`、`easy clearCacheAll`、`easy int`、`easy int`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、EmptyLatentImage

## 参数体检

发现 4 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- 次要节点 `CR Text Concatenate` 知识库中没有该节点类型的任何知识
- 次要节点 `easy clearCacheAll` 知识库中没有该节点类型的任何知识
- 次要节点 `easy clearCacheAll` 知识库中没有该节点类型的任何知识
- 次要节点 `easy int` 知识库中没有该节点类型的任何知识
- 次要节点 `easy int` 知识库中没有该节点类型的任何知识
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

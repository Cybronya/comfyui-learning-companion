---
key: 图片生成/图生图/姿势迁移—FireRed-Image-Edit-1.1_2032383512262742018.json
name: 姿势迁移—FireRed-Image-Edit-1.1_2032383512262742018.json
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/姿势迁移—FireRed-Image-Edit-1.1_2032383512262742018.json
hash: d51a122633a0a51a
coverage: 0.661017
learned_at: 2026-10-09 22:19:25
nodes: [ImageConcanate, ConditioningZeroOut, VAEDecode, VAEEncode, KSampler, UnetLoaderGGUF, LayerUtility: PurgeVRAM, ImageScaleToTotalPixels, ModelSamplingAuraFlow, CFGNorm, PathchSageAttentionKJ, ConditioningZeroOut, EmptySD3LatentImage, easy imageSize, LoadImage, ShowText|pysssss, LayerUtility: PurgeVRAM, ImageScaleToTotalPixels, ImageScaleToTotalPixels, CLIPLoader, VAELoader, VAELoader, CLIPLoader, CR Text, CR Text, SDPoseOODLoader, LoadImage, CLIPTextEncode, UNETLoader, UNETLoader, VAEDecode, LayerUtility: PurgeVRAM, SaveImage, PreviewImage, Image Comparer (rgthree), ImageConcanate, SaveImageJPG_GH, PreviewImage, VAEDecode, LayerColor: ColorAdapter, KSampler, LoraLoaderModelOnly, workflow>123, LoraLoaderModelOnly, KSampler, SDPoseOODProcessor, PreviewImage, easy ifElse, PrimitiveBoolean, TextEncodeQwenImageEditPlus, ShowText|pysssss, Qwen3_VQA, SomethingToString, PrimitiveBoolean, easy ifElse, CR Text Concatenate, CR Text Concatenate, CR Text, CR Text]
patterns: [image_to_image]
missing: [CR Text, CR Text, CR Text, CR Text, CR Text Concatenate, CR Text Concatenate, LayerUtility: PurgeVRAM, LayerUtility: PurgeVRAM, LayerUtility: PurgeVRAM, workflow>123, LayerColor: ColorAdapter, easy imageSize]
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 668453903638432, "steps": 4}
discoveries: [次要节点 `CR Text` 知识库中没有该节点类型的任何知识, 次要节点 `CR Text` 知识库中没有该节点类型的任何知识, 次要节点 `CR Text` 知识库中没有该节点类型的任何知识, 次要节点 `CR Text` 知识库中没有该节点类型的任何知识, 次要节点 `CR Text Concatenate` 知识库中没有该节点类型的任何知识, 次要节点 `CR Text Concatenate` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: PurgeVRAM` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: PurgeVRAM` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: PurgeVRAM` 知识库中没有该节点类型的任何知识, 次要节点 `workflow>123` 知识库中没有该节点类型的任何知识, 次要节点 `LayerColor: ColorAdapter` 仅有 LoRA 的通用知识，没有该节点自己的说明, 次要节点 `easy imageSize` 仅有 Resolution 的通用知识，没有该节点自己的说明, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/姿势迁移—FireRed-Image-Edit-1.1_2032383512262742018.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/2032383512262742018.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（59 个）：
- `ImageConcanate`
- `ConditioningZeroOut`
- `VAEDecode` ★核心
- `VAEEncode` ★核心
- `KSampler` ★核心
- `UnetLoaderGGUF` ★核心
- `LayerUtility: PurgeVRAM`
- `ImageScaleToTotalPixels`
- `ModelSamplingAuraFlow`
- `CFGNorm`
- `PathchSageAttentionKJ`
- `ConditioningZeroOut`
- `EmptySD3LatentImage`
- `easy imageSize`
- `LoadImage`
- `ShowText|pysssss`
- `LayerUtility: PurgeVRAM`
- `ImageScaleToTotalPixels`
- `ImageScaleToTotalPixels`
- `CLIPLoader`
- `VAELoader`
- `VAELoader`
- `CLIPLoader`
- `CR Text`
- `CR Text`
- `SDPoseOODLoader`
- `LoadImage`
- `CLIPTextEncode` ★核心
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `VAEDecode` ★核心
- `LayerUtility: PurgeVRAM`
- `SaveImage`
- `PreviewImage`
- `Image Comparer (rgthree)`
- `ImageConcanate`
- `SaveImageJPG_GH`
- `PreviewImage`
- `VAEDecode` ★核心
- `LayerColor: ColorAdapter`
- `KSampler` ★核心
- `LoraLoaderModelOnly` ★核心
- `workflow>123`
- `LoraLoaderModelOnly` ★核心
- `KSampler` ★核心
- `SDPoseOODProcessor`
- `PreviewImage`
- `easy ifElse`
- `PrimitiveBoolean`
- `TextEncodeQwenImageEditPlus`
- `ShowText|pysssss`
- `Qwen3_VQA`
- `SomethingToString`
- `PrimitiveBoolean`
- `easy ifElse`
- `CR Text Concatenate`
- `CR Text Concatenate`
- `CR Text`
- `CR Text`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `668453903638432`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **66%**（39/59）

**有卡**：`ImageConcanate`、`ConditioningZeroOut`、`VAEDecode`、`VAEEncode`、`KSampler`、`UnetLoaderGGUF`、`ImageScaleToTotalPixels`、`ModelSamplingAuraFlow`、`CFGNorm`、`PathchSageAttentionKJ`、`EmptySD3LatentImage`、`LoadImage`、`CLIPLoader`、`VAELoader`、`SDPoseOODLoader`、`CLIPTextEncode`、`UNETLoader`、`SaveImage`、`SaveImageJPG_GH`、`LoraLoaderModelOnly`、`SDPoseOODProcessor`、`PrimitiveBoolean`、`TextEncodeQwenImageEditPlus`、`Qwen3_VQA`、`SomethingToString`

**缺卡**（12）：`CR Text`、`CR Text`、`CR Text`、`CR Text`、`CR Text Concatenate`、`CR Text Concatenate`、`LayerUtility: PurgeVRAM`、`LayerUtility: PurgeVRAM`、`LayerUtility: PurgeVRAM`、`workflow>123`、`LayerColor: ColorAdapter`、`easy imageSize`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、LoadImage

## 参数体检

发现 3 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- 次要节点 `CR Text` 知识库中没有该节点类型的任何知识
- 次要节点 `CR Text` 知识库中没有该节点类型的任何知识
- 次要节点 `CR Text` 知识库中没有该节点类型的任何知识
- 次要节点 `CR Text` 知识库中没有该节点类型的任何知识
- 次要节点 `CR Text Concatenate` 知识库中没有该节点类型的任何知识
- 次要节点 `CR Text Concatenate` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: PurgeVRAM` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: PurgeVRAM` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: PurgeVRAM` 知识库中没有该节点类型的任何知识
- 次要节点 `workflow>123` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerColor: ColorAdapter` 仅有 LoRA 的通用知识，没有该节点自己的说明
- 次要节点 `easy imageSize` 仅有 Resolution 的通用知识，没有该节点自己的说明
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

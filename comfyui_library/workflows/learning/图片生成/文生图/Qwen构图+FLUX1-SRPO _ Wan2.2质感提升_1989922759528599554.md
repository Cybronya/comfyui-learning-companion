---
key: Qwen构图+FLUX1-SRPO _ Wan2.2质感提升_1989922759528599554.json
name: Qwen构图+FLUX1-SRPO _ Wan2.2质感提升_1989922759528599554
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Qwen构图+FLUX1-SRPO _ Wan2.2质感提升_1989922759528599554.json
hash: accda06c5c33563d
coverage: 0.736842
learned_at: 2026-10-10 20:59:10
nodes: [ConditioningZeroOut, UNETLoader, UNETLoader, CLIPTextEncode, EmptySD3LatentImage, LoraLoader, PathchSageAttentionKJ, ModelSamplingSD3, CLIPTextEncode, VAEEncode, CLIPTextEncode, LoraLoader, LoraLoader, Text Concatenate, CLIPLoader, CLIPTextEncode, KSampler, SaveImage, Image Comparer (rgthree), VAELoader, Text Multiline, CLIPTextEncode, VAEEncode, FluxGuidance, DualCLIPLoader, VAELoader, UpscaleModelLoader, ImageScaleBy, RH_Translator, SaveImage, Image Comparer (rgthree), LayerUtility: LoadJoyCaptionBeta1Model, LayerUtility: JoyCaptionBeta1, LayerUtility: ImageReel, LayerUtility: ImageReelComposit, VAEDecode, VAEDecode, KSampler, PreviewImage, SaveImage, ModelSamplingAuraFlow, CLIPLoader, VAELoader, KSampler, VAEDecode, UNETLoader, LoraLoaderModelOnly, SaveImage, PreviewImage, LoraLoaderModelOnly, PreviewImage, ImageUpscaleWithModel, Reroute, Text Multiline, PreviewImage, LoadImage, ShowText|pysssss]
patterns: [image_to_image, lora]
missing: [LayerUtility: ImageReel, LayerUtility: ImageReelComposit, LayerUtility: JoyCaptionBeta1, LayerUtility: LoadJoyCaptionBeta1Model, Text Concatenate, Text Multiline, Text Multiline]
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "lora_name": "WAN2.2-LowNoise_SmartphoneSnapshotPhotoReality_v3_by-AI_Characters.safetensors", "sampler_name": "euler", "scheduler": "simple", "seed": 724802566875783, "steps": 8, "strength_clip": 0.7000000000000002, "strength_model": 0.7000000000000002}
discoveries: [次要节点 `LayerUtility: ImageReel` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: ImageReelComposit` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: JoyCaptionBeta1` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: LoadJoyCaptionBeta1Model` 知识库中没有该节点类型的任何知识, 次要节点 `Text Concatenate` 知识库中没有该节点类型的任何知识, 次要节点 `Text Multiline` 知识库中没有该节点类型的任何知识, 次要节点 `Text Multiline` 知识库中没有该节点类型的任何知识, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# Qwen构图+FLUX1-SRPO _ Wan2.2质感提升_1989922759528599554.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Qwen构图+FLUX1-SRPO _ Wan2.2质感提升_1989922759528599554.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（57 个）：
- `ConditioningZeroOut`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `CLIPTextEncode` ★核心
- `EmptySD3LatentImage`
- `LoraLoader` ★核心
- `PathchSageAttentionKJ`
- `ModelSamplingSD3`
- `CLIPTextEncode` ★核心
- `VAEEncode` ★核心
- `CLIPTextEncode` ★核心
- `LoraLoader` ★核心
- `LoraLoader` ★核心
- `Text Concatenate`
- `CLIPLoader`
- `CLIPTextEncode` ★核心
- `KSampler` ★核心
- `SaveImage`
- `Image Comparer (rgthree)`
- `VAELoader`
- `Text Multiline`
- `CLIPTextEncode` ★核心
- `VAEEncode` ★核心
- `FluxGuidance`
- `DualCLIPLoader`
- `VAELoader`
- `UpscaleModelLoader`
- `ImageScaleBy`
- `RH_Translator`
- `SaveImage`
- `Image Comparer (rgthree)`
- `LayerUtility: LoadJoyCaptionBeta1Model`
- `LayerUtility: JoyCaptionBeta1`
- `LayerUtility: ImageReel`
- `LayerUtility: ImageReelComposit`
- `VAEDecode` ★核心
- `VAEDecode` ★核心
- `KSampler` ★核心
- `PreviewImage`
- `SaveImage`
- `ModelSamplingAuraFlow`
- `CLIPLoader`
- `VAELoader`
- `KSampler` ★核心
- `VAEDecode` ★核心
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `SaveImage`
- `PreviewImage`
- `LoraLoaderModelOnly` ★核心
- `PreviewImage`
- `ImageUpscaleWithModel`
- `Reroute`
- `Text Multiline`
- `PreviewImage`
- `LoadImage`
- `ShowText|pysssss`

**识别到的模式**：image_to_image、lora

## 关键参数

- `lora_name` = `WAN2.2-LowNoise_SmartphoneSnapshotPhotoReality_v3_by-AI_Characters.safetensors`
- `strength_model` = `0.7000000000000002`
- `strength_clip` = `0.7000000000000002`
- `seed` = `724802566875783`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **74%**（42/57）

**有卡**：`ConditioningZeroOut`、`UNETLoader`、`CLIPTextEncode`、`EmptySD3LatentImage`、`LoraLoader`、`PathchSageAttentionKJ`、`ModelSamplingSD3`、`VAEEncode`、`CLIPLoader`、`KSampler`、`SaveImage`、`VAELoader`、`FluxGuidance`、`DualCLIPLoader`、`UpscaleModelLoader`、`ImageScaleBy`、`RH_Translator`、`VAEDecode`、`ModelSamplingAuraFlow`、`LoraLoaderModelOnly`、`ImageUpscaleWithModel`、`LoadImage`

**缺卡**（7）：`LayerUtility: ImageReel`、`LayerUtility: ImageReelComposit`、`LayerUtility: JoyCaptionBeta1`、`LayerUtility: LoadJoyCaptionBeta1Model`、`Text Concatenate`、`Text Multiline`、`Text Multiline`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPTextEncode、CLIPLoader、ConditioningZeroOut

## 参数体检

发现 2 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- 次要节点 `LayerUtility: ImageReel` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: ImageReelComposit` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: JoyCaptionBeta1` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: LoadJoyCaptionBeta1Model` 知识库中没有该节点类型的任何知识
- 次要节点 `Text Concatenate` 知识库中没有该节点类型的任何知识
- 次要节点 `Text Multiline` 知识库中没有该节点类型的任何知识
- 次要节点 `Text Multiline` 知识库中没有该节点类型的任何知识
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

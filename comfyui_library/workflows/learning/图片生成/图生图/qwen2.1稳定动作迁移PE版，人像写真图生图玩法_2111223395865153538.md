---
key: 图片生成/图生图/qwen2.1稳定动作迁移PE版，人像写真图生图玩法_2111223395865153538.json
name: qwen2.1稳定动作迁移PE版，人像写真图生图玩法_2111223395865153538
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/qwen2.1稳定动作迁移PE版，人像写真图生图玩法_2111223395865153538.json
hash: 386665ea3d046f66
coverage: 0.83871
learned_at: 2026-10-23 11:43:01
nodes: [CLIPLoader, VAELoader, PathchSageAttentionKJ, QwenImage21Cache, SDPoseKeypointExtractor, SDPoseDrawKeypoints, LoadImage, LayerUtility: ImageScaleByAspectRatio V2, GetImageSize, LayerUtility: NumberCalculator, easy showAnything, Text Multiline, TextGenerateLTX2Prompt, PreviewImage, LayerUtility: ImageScaleByAspectRatio V2, ComfyMathExpression, PrimitiveFloat, JoinStrings, easy positive, PrimitiveString, SaveImage, UNETLoader, CheckpointLoaderSimple, CLIPLoader, LoadImage, Image Comparer (rgthree), PreviewImage, BatchImagesNode, TextEncodeQwenImageEditPlus, VAEEncode, ConditioningZeroOut, VAEDecode, KSampler, 孤海注释, 孤海注释, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, KSampler, CLIPTextEncode, CLIPTextEncode, CLIPLoader, JjkText, VAEDecode, EmptyLatentImage, VAELoader, solarL_SaveImagesToZip, Note]
patterns: [text_to_image, image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "checkpoint": "sdpose_wholebody_fp16.safetensors", "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/qwen2.1稳定动作迁移PE版，人像写真图生图玩法_2111223395865153538.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/qwen2.1稳定动作迁移PE版，人像写真图生图玩法_2111223395865153538.json`

## 结构

**生成流程**：Model → Encode → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（62 个）：
- `CLIPLoader`
- `VAELoader`
- `PathchSageAttentionKJ`
- `QwenImage21Cache`
- `SDPoseKeypointExtractor`
- `SDPoseDrawKeypoints`
- `LoadImage`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `GetImageSize`
- `LayerUtility: NumberCalculator`
- `easy showAnything`
- `Text Multiline`
- `TextGenerateLTX2Prompt`
- `PreviewImage`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `ComfyMathExpression`
- `PrimitiveFloat`
- `JoinStrings`
- `easy positive`
- `PrimitiveString`
- `SaveImage`
- `UNETLoader` ★核心
- `CheckpointLoaderSimple` ★核心
- `CLIPLoader`
- `LoadImage`
- `Image Comparer (rgthree)`
- `PreviewImage`
- `BatchImagesNode`
- `TextEncodeQwenImageEditPlus`
- `VAEEncode` ★核心
- `ConditioningZeroOut`
- `VAEDecode` ★核心
- `KSampler` ★核心
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
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `CLIPLoader`
- `JjkText`
- `VAEDecode` ★核心
- `EmptyLatentImage` ★核心
- `VAELoader`
- `solarL_SaveImagesToZip`
- `Note`

**识别到的模式**：text_to_image、image_to_image

## 关键参数

- `checkpoint` = `sdpose_wholebody_fp16.safetensors`
- `seed` = `598626327129635`
- `steps` = `4`
- `cfg` = `4.5`
- `sampler_name` = `er_sde`
- `scheduler` = `beta`
- `denoise` = `1`
- `width` = `80`
- `height` = `80`
- `batch_size` = `1`

## 知识

覆盖率 **84%**（52/62）

**有卡**：`CLIPLoader`、`VAELoader`、`PathchSageAttentionKJ`、`QwenImage21Cache`、`SDPoseKeypointExtractor`、`SDPoseDrawKeypoints`、`LoadImage`、`LayerUtility: ImageScaleByAspectRatio V2`、`GetImageSize`、`LayerUtility: NumberCalculator`、`Text Multiline`、`TextGenerateLTX2Prompt`、`ComfyMathExpression`、`JoinStrings`、`easy positive`、`SaveImage`、`UNETLoader`、`CheckpointLoaderSimple`、`BatchImagesNode`、`TextEncodeQwenImageEditPlus`、`VAEEncode`、`ConditioningZeroOut`、`VAEDecode`、`KSampler`、`LoraLoaderModelOnly`、`CLIPTextEncode`、`EmptyLatentImage`、`solarL_SaveImagesToZip`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CheckpointLoaderSimple、UNETLoader、CLIPTextEncode、CLIPLoader

## 参数体检

发现 2 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

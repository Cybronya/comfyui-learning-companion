---
key: 图片生成/图生图/狂徒AIGC-高清AI人物素材库一键生成-线上发布版1.0_2052588956339978241.json
name: 狂徒AIGC-高清AI人物素材库一键生成-线上发布版1.0_2052588956339978241
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/狂徒AIGC-高清AI人物素材库一键生成-线上发布版1.0_2052588956339978241.json
hash: 3653e46a548c2904
coverage: 0.953488
learned_at: 2026-10-23 13:14:31
nodes: [CFGNorm, VAELoader, CLIPLoader, ConditioningZeroOut, FluxKontextMultiReferenceLatentMethod, FluxKontextMultiReferenceLatentMethod, VAEEncode, LoraLoaderModelOnly, KSampler, ModelSamplingAuraFlow, TextEncodeQwenImageEditPlus, RHUploadZip_V2, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, CheckpointLoaderSimple, VAEDecode, LayerUtility: PurgeVRAM, easy indexAnything, easy imageConcat, easy indexAnything, easy indexAnything, FL_SendToDiscordWebhook, FL_SendToDiscordWebhook, easy indexAnything, PreviewImage, easy imageConcat, easy batchAnything, easy cleanGpuUsed, easy lengthAnything, PreviewAny, easy forLoopStart, ImageListToBatch_, easy batchAnything, SaveImage, ImageBatchToList_, SaveImage, SaveImage, easy promptLine, easy indexAnything, LoadImage, easy forLoopEnd, TT_img_enc, ZML_AnyTypeSwitch]
patterns: [image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "checkpoint": "new_Qwen-Rapid-AIO-NSFW-v23.safetensors", "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 1054249299586202, "steps": 5}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/狂徒AIGC-高清AI人物素材库一键生成-线上发布版1.0_2052588956339978241.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/狂徒AIGC-高清AI人物素材库一键生成-线上发布版1.0_2052588956339978241.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（43 个）：
- `CFGNorm`
- `VAELoader`
- `CLIPLoader`
- `ConditioningZeroOut`
- `FluxKontextMultiReferenceLatentMethod`
- `FluxKontextMultiReferenceLatentMethod`
- `VAEEncode` ★核心
- `LoraLoaderModelOnly` ★核心
- `KSampler` ★核心
- `ModelSamplingAuraFlow`
- `TextEncodeQwenImageEditPlus`
- `RHUploadZip_V2`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `CheckpointLoaderSimple` ★核心
- `VAEDecode` ★核心
- `LayerUtility: PurgeVRAM`
- `easy indexAnything`
- `easy imageConcat`
- `easy indexAnything`
- `easy indexAnything`
- `FL_SendToDiscordWebhook`
- `FL_SendToDiscordWebhook`
- `easy indexAnything`
- `PreviewImage`
- `easy imageConcat`
- `easy batchAnything`
- `easy cleanGpuUsed`
- `easy lengthAnything`
- `PreviewAny`
- `easy forLoopStart`
- `ImageListToBatch_`
- `easy batchAnything`
- `SaveImage`
- `ImageBatchToList_`
- `SaveImage`
- `SaveImage`
- `easy promptLine`
- `easy indexAnything`
- `LoadImage`
- `easy forLoopEnd`
- `TT_img_enc`
- `ZML_AnyTypeSwitch`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `1054249299586202`
- `steps` = `5`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`
- `checkpoint` = `new_Qwen-Rapid-AIO-NSFW-v23.safetensors`

## 知识

覆盖率 **95%**（41/43）

**有卡**：`CFGNorm`、`VAELoader`、`CLIPLoader`、`ConditioningZeroOut`、`FluxKontextMultiReferenceLatentMethod`、`VAEEncode`、`LoraLoaderModelOnly`、`KSampler`、`ModelSamplingAuraFlow`、`TextEncodeQwenImageEditPlus`、`RHUploadZip_V2`、`LayerUtility: ImageScaleByAspectRatio V2`、`LoadImage`、`CheckpointLoaderSimple`、`VAEDecode`、`LayerUtility: PurgeVRAM`、`easy indexAnything`、`easy imageConcat`、`FL_SendToDiscordWebhook`、`easy batchAnything`、`easy cleanGpuUsed`、`easy lengthAnything`、`easy forLoopStart`、`ImageListToBatch_`、`SaveImage`、`ImageBatchToList_`、`easy promptLine`、`easy forLoopEnd`、`TT_img_enc`、`ZML_AnyTypeSwitch`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CheckpointLoaderSimple、CLIPLoader、ConditioningZeroOut、LoadImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

---
key: 平台全量/image-refiner 图像细化器 flux nf4 + dreamshaper xl_1863476584769368065.json
name: image-refiner 图像细化器 flux nf4 + dreamshaper xl_1863476584769368065
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/平台全量/image-refiner 图像细化器 flux nf4 + dreamshaper xl_1863476584769368065.json
hash: 7f8aa31c969d2b5b
coverage: 0.670886
learned_at: 2026-11-14 01:12:38
nodes: [LayerMask: LoadFlorence2Model, easy promptReplace, LayerUtility: Florence2Image2Prompt, CLIPTextEncode, GetNode, GetNode, GetImageSize, GetNode, easy imageSize, GetNode, ModelSamplingFlux, GetNode, Load Image Batch, ConstrainImage|pysssss, MathExpression|pysssss, CLIPTextEncode, GetNode, ImageUpscaleWithModel, MathExpression|pysssss, ImageScaleBy, MathExpression|pysssss, Note, MathExpression|pysssss, MathExpression|pysssss, TiledDiffusion, SeargePromptCombiner, ImpactQueueTriggerCountdown, ShowText|pysssss, FluxGuidance, SetNode, MathExpression|pysssss, ImageUpscaleWithModel, ImageScaleBy, CLIPSetLastLayer, LoraLoader, SaveImage, SetNode, SetNode, GetNode, ShowText|pysssss, SeargePromptCombiner, easy float, easy float, SetNode, easy float, Anything Everywhere, VAEDecodeTiled_TiledDiffusion, VAEEncodeTiled_TiledDiffusion, Note, Note, Note, Note, Note, easy promptReplace, UpscaleModelLoader, KSampler //Inspire, CheckpointLoaderSimple, Image Comparer (rgthree), Image Comparer (rgthree), LoadImage, GetNode, SaveImage, SaveImage, GetNode, CheckpointLoaderNF4, VAEEncode, easy float, ControlNetApply, SaveImage, VAEDecodeTiled_TiledDiffusion, CLIPTextEncode, CLIPTextEncode, TilePreprocessor, KSampler, ControlNetLoader, ControlNetApplyAdvanced, TiledDiffusion, PreviewImage, Image Comparer (rgthree)]
patterns: [image_to_image, controlnet, lora]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换]
parameters: {"cfg": 4, "checkpoint": "flux1-dev-bnb-nf4-v2.safetensors", "controlnet_strength": 1, "denoise": 1, "lora_name": "DetailedEyes_V3.safetensors", "sampler_name": "dpmpp_sde_gpu", "scheduler": "karras", "seed": 40282713074667, "steps": 8, "strength_clip": 1, "strength_model": 1}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换]
---

# 平台全量/image-refiner 图像细化器 flux nf4 + dreamshaper xl_1863476584769368065.json

> 来源文件 `comfyui_library/workflows/平台全量/image-refiner 图像细化器 flux nf4 + dreamshaper xl_1863476584769368065.json`

## 结构

**生成流程**：Model → Encode → Condition → Control → Sampling → Decode → Process → Output → Other

**节点**（79 个）：
- `LayerMask: LoadFlorence2Model`
- `easy promptReplace`
- `LayerUtility: Florence2Image2Prompt`
- `CLIPTextEncode` ★核心
- `GetNode`
- `GetNode`
- `GetImageSize`
- `GetNode`
- `easy imageSize`
- `GetNode`
- `ModelSamplingFlux`
- `GetNode`
- `Load Image Batch`
- `ConstrainImage|pysssss`
- `MathExpression|pysssss`
- `CLIPTextEncode` ★核心
- `GetNode`
- `ImageUpscaleWithModel`
- `MathExpression|pysssss`
- `ImageScaleBy`
- `MathExpression|pysssss`
- `Note`
- `MathExpression|pysssss`
- `MathExpression|pysssss`
- `TiledDiffusion`
- `SeargePromptCombiner`
- `ImpactQueueTriggerCountdown`
- `ShowText|pysssss`
- `FluxGuidance`
- `SetNode`
- `MathExpression|pysssss`
- `ImageUpscaleWithModel`
- `ImageScaleBy`
- `CLIPSetLastLayer`
- `LoraLoader` ★核心
- `SaveImage`
- `SetNode`
- `SetNode`
- `GetNode`
- `ShowText|pysssss`
- `SeargePromptCombiner`
- `easy float`
- `easy float`
- `SetNode`
- `easy float`
- `Anything Everywhere`
- `VAEDecodeTiled_TiledDiffusion` ★核心
- `VAEEncodeTiled_TiledDiffusion` ★核心
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `easy promptReplace`
- `UpscaleModelLoader`
- `KSampler //Inspire` ★核心
- `CheckpointLoaderSimple` ★核心
- `Image Comparer (rgthree)`
- `Image Comparer (rgthree)`
- `LoadImage`
- `GetNode`
- `SaveImage`
- `SaveImage`
- `GetNode`
- `CheckpointLoaderNF4` ★核心
- `VAEEncode` ★核心
- `easy float`
- `ControlNetApply` ★核心
- `SaveImage`
- `VAEDecodeTiled_TiledDiffusion` ★核心
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `TilePreprocessor`
- `KSampler` ★核心
- `ControlNetLoader`
- `ControlNetApplyAdvanced` ★核心
- `TiledDiffusion`
- `PreviewImage`
- `Image Comparer (rgthree)`

**识别到的模式**：image_to_image、controlnet、lora

## 关键参数

- `lora_name` = `DetailedEyes_V3.safetensors`
- `strength_model` = `1`
- `strength_clip` = `1`
- `seed` = `40282713074667`
- `steps` = `8`
- `cfg` = `4`
- `sampler_name` = `dpmpp_sde_gpu`
- `scheduler` = `karras`
- `denoise` = `1`
- `checkpoint` = `flux1-dev-bnb-nf4-v2.safetensors`
- `controlnet_strength` = `1`

## 知识

覆盖率 **67%**（53/79）

**有卡**：`LayerMask: LoadFlorence2Model`、`easy promptReplace`、`LayerUtility: Florence2Image2Prompt`、`CLIPTextEncode`、`GetImageSize`、`easy imageSize`、`ModelSamplingFlux`、`Load Image Batch`、`ConstrainImage|pysssss`、`MathExpression|pysssss`、`ImageUpscaleWithModel`、`ImageScaleBy`、`TiledDiffusion`、`SeargePromptCombiner`、`ImpactQueueTriggerCountdown`、`FluxGuidance`、`CLIPSetLastLayer`、`LoraLoader`、`SaveImage`、`easy float`、`VAEDecodeTiled_TiledDiffusion`、`VAEEncodeTiled_TiledDiffusion`、`UpscaleModelLoader`、`KSampler //Inspire`、`CheckpointLoaderSimple`、`LoadImage`、`CheckpointLoaderNF4`、`VAEEncode`、`ControlNetApply`、`TilePreprocessor`、`KSampler`、`ControlNetLoader`、`ControlNetApplyAdvanced`

**用到的条目**：KSampler、CheckpointLoaderSimple、CLIPTextEncode、LoadImage、ControlNetApply、ControlNetApplyAdvanced、ControlNetLoader、FluxGuidance

## 参数体检

发现 2 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换

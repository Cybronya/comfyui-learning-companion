---
key: 数字人/数字人/AI大宗主-SAM3.1+Animate人物替换，动作迁移-官方FOR循环版本（小白福音）_2054451280411676673.json
name: AI大宗主-SAM3.1+Animate人物替换，动作迁移-官方FOR循环版本（小白福音）_2054451280411676673
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/数字人/数字人/AI大宗主-SAM3.1+Animate人物替换，动作迁移-官方FOR循环版本（小白福音）_2054451280411676673.json
hash: 44ec5f9d86b64be7
coverage: 0.478947
learned_at: 2026-10-26 01:53:41
nodes: [SetNode, SetNode, SetNode, GetNode, GetNode, GetNode, GetNode, SetNode, SetNode, SetNode, GetNode, MaskToImage, GetNode, GetNode, GetNode, VHS_VideoCombine, BlockifyMask, LayerUtility: PurgeVRAM V2, SAM3_Detect, GetNode, GetNode, GetNode, GetNode, GetNode, VHS_VideoCombine, ImageCompositeMasked, SetNode, RTDETR_detect, GetNode, SetNode, SDPoseKeypointExtractor, VHS_VideoCombine, GetNode, SDPoseFaceBBoxes, GetNode, CLIPTextEncode, SetNode, JoinStrings, easy positive, SetNode, GetNode, GetNode, GetNode, GetNode, GetNode, SetNode, GetNode, GetNode, GetNode, GetNode, DrawMaskOnImage, SetNode, SetNode, SetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, MathExpression|pysssss, GetNode, SetNode, GetNode, SetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, KSampler, KSampler, GetNode, GetNode, GetNode, SetNode, SetNode, easy forLoopEnd, easy batchAnything, TrimVideoLatent, ImageFromBatch, VAEDecode, LayerUtility: PurgeVRAM V2, TrimVideoLatent, SetNode, MathExpression|pysssss, LayerUtility: PurgeVRAM V2, VAEDecode, GetNode, ImageFromBatch, MathExpression|pysssss, GetNode, MathExpression|pysssss, MathExpression|pysssss, GetNode, DeepTranslatorTextNode, CLIPTextEncode, VHS_LoadVideo, MarkdownNote, ShowText|pysssss, CLIPVisionEncode, GetNode, CLIPVisionLoader, CLIPLoader, VAELoader, CheckpointLoaderSimple, UNETLoader, CheckpointLoaderSimple, MathExpression|pysssss, MathExpression|pysssss, UNETLoader, SetNode, ModelPatchTorchSettings, CLIPTextEncode, Label (rgthree), Label (rgthree), easy int, easy int, GrowMask, easy int, easy int, GetNode, GetNode, GetNode, GetNode, GetNode, SDPoseDrawKeypoints, ImageFromBatch, ColorMatchV2, ImageFromBatch, GetNode, VHS_VideoCombine, SetNode, VHS_VideoCombine, GetNode, SetNode, SetNode, CM_IntToFloat, VHS_VideoCombine, GetNode, GetNode, easy int, GetNode, VHS_VideoCombine, easy int, Note, GetNode, GetNode, GetNode, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, ImageConcatMulti, GetNode, GetNode, PathchSageAttentionKJ, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, SetNode, ModelSamplingSD3, Label (rgthree), llama_cpp_model_loader, llama_cpp_parameters, GetNode, LayerUtility: PurgeVRAM V2, llama_cpp_instruct_adv, LayerUtility: PurgeVRAM V2, VHS_LoadVideo, easy int, easy positive, LoraLoaderModelOnly, VHS_VideoCombine, CropByBBoxes, easy showAnything, easy forLoopStart, easy showAnything, LoraLoaderModelOnly, WanAnimateToVideo, WanAnimateToVideo, VHS_VideoCombine, VHS_VideoCombine]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "checkpoint": "sdpose_wholebody_fp16.safetensors", "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 321544606044423, "steps": 6}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 数字人/数字人/AI大宗主-SAM3.1+Animate人物替换，动作迁移-官方FOR循环版本（小白福音）_2054451280411676673.json

> 来源文件 `comfyui_library/workflows/数字人/数字人/AI大宗主-SAM3.1+Animate人物替换，动作迁移-官方FOR循环版本（小白福音）_2054451280411676673.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（190 个）：
- `SetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `MaskToImage`
- `GetNode`
- `GetNode`
- `GetNode`
- `VHS_VideoCombine`
- `BlockifyMask`
- `LayerUtility: PurgeVRAM V2`
- `SAM3_Detect`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `VHS_VideoCombine`
- `ImageCompositeMasked`
- `SetNode`
- `RTDETR_detect`
- `GetNode`
- `SetNode`
- `SDPoseKeypointExtractor`
- `VHS_VideoCombine`
- `GetNode`
- `SDPoseFaceBBoxes`
- `GetNode`
- `CLIPTextEncode` ★核心
- `SetNode`
- `JoinStrings`
- `easy positive`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `DrawMaskOnImage`
- `SetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `MathExpression|pysssss`
- `GetNode`
- `SetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `KSampler` ★核心
- `KSampler` ★核心
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `easy forLoopEnd`
- `easy batchAnything`
- `TrimVideoLatent`
- `ImageFromBatch`
- `VAEDecode` ★核心
- `LayerUtility: PurgeVRAM V2`
- `TrimVideoLatent`
- `SetNode`
- `MathExpression|pysssss`
- `LayerUtility: PurgeVRAM V2`
- `VAEDecode` ★核心
- `GetNode`
- `ImageFromBatch`
- `MathExpression|pysssss`
- `GetNode`
- `MathExpression|pysssss`
- `MathExpression|pysssss`
- `GetNode`
- `DeepTranslatorTextNode`
- `CLIPTextEncode` ★核心
- `VHS_LoadVideo`
- `MarkdownNote`
- `ShowText|pysssss`
- `CLIPVisionEncode`
- `GetNode`
- `CLIPVisionLoader`
- `CLIPLoader`
- `VAELoader`
- `CheckpointLoaderSimple` ★核心
- `UNETLoader` ★核心
- `CheckpointLoaderSimple` ★核心
- `MathExpression|pysssss`
- `MathExpression|pysssss`
- `UNETLoader` ★核心
- `SetNode`
- `ModelPatchTorchSettings`
- `CLIPTextEncode` ★核心
- `Label (rgthree)`
- `Label (rgthree)`
- `easy int`
- `easy int`
- `GrowMask`
- `easy int`
- `easy int`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SDPoseDrawKeypoints`
- `ImageFromBatch`
- `ColorMatchV2`
- `ImageFromBatch`
- `GetNode`
- `VHS_VideoCombine`
- `SetNode`
- `VHS_VideoCombine`
- `GetNode`
- `SetNode`
- `SetNode`
- `CM_IntToFloat`
- `VHS_VideoCombine`
- `GetNode`
- `GetNode`
- `easy int`
- `GetNode`
- `VHS_VideoCombine`
- `easy int`
- `Note`
- `GetNode`
- `GetNode`
- `GetNode`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `ImageConcatMulti`
- `GetNode`
- `GetNode`
- `PathchSageAttentionKJ`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `SetNode`
- `ModelSamplingSD3`
- `Label (rgthree)`
- `llama_cpp_model_loader`
- `llama_cpp_parameters`
- `GetNode`
- `LayerUtility: PurgeVRAM V2`
- `llama_cpp_instruct_adv`
- `LayerUtility: PurgeVRAM V2`
- `VHS_LoadVideo`
- `easy int`
- `easy positive`
- `LoraLoaderModelOnly` ★核心
- `VHS_VideoCombine`
- `CropByBBoxes`
- `easy showAnything`
- `easy forLoopStart`
- `easy showAnything`
- `LoraLoaderModelOnly` ★核心
- `WanAnimateToVideo`
- `WanAnimateToVideo`
- `VHS_VideoCombine`
- `VHS_VideoCombine`

## 关键参数

- `seed` = `321544606044423`
- `steps` = `6`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`
- `checkpoint` = `sdpose_wholebody_fp16.safetensors`

## 知识

覆盖率 **48%**（91/190）

**有卡**：`MaskToImage`、`VHS_VideoCombine`、`BlockifyMask`、`LayerUtility: PurgeVRAM V2`、`SAM3_Detect`、`ImageCompositeMasked`、`RTDETR_detect`、`SDPoseKeypointExtractor`、`SDPoseFaceBBoxes`、`CLIPTextEncode`、`JoinStrings`、`easy positive`、`DrawMaskOnImage`、`MathExpression|pysssss`、`KSampler`、`easy forLoopEnd`、`easy batchAnything`、`TrimVideoLatent`、`ImageFromBatch`、`VAEDecode`、`DeepTranslatorTextNode`、`VHS_LoadVideo`、`CLIPVisionEncode`、`CLIPVisionLoader`、`CLIPLoader`、`VAELoader`、`CheckpointLoaderSimple`、`UNETLoader`、`ModelPatchTorchSettings`、`Label (rgthree)`、`easy int`、`GrowMask`、`SDPoseDrawKeypoints`、`ColorMatchV2`、`CM_IntToFloat`、`LayerUtility: ImageScaleByAspectRatio V2`、`LoadImage`、`ImageConcatMulti`、`PathchSageAttentionKJ`、`LoraLoaderModelOnly`、`ModelSamplingSD3`、`llama_cpp_model_loader`、`llama_cpp_parameters`、`llama_cpp_instruct_adv`、`CropByBBoxes`、`easy forLoopStart`、`WanAnimateToVideo`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CheckpointLoaderSimple、UNETLoader、CLIPTextEncode、CLIPLoader

## 参数体检

发现 2 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

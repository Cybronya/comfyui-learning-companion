---
key: 图片生成/图生图/黑白漫画上色方案——基于qwen2511——特调loraV4.0_2009612107720953858.json
name: 黑白漫画上色方案——基于qwen2511——特调loraV4.0_2009612107720953858
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/黑白漫画上色方案——基于qwen2511——特调loraV4.0_2009612107720953858.json
hash: faea1315ed20fc4e
coverage: 0.434783
learned_at: 2026-10-23 13:35:59
nodes: [SetNode, easy showAnything, easy imageCount, easy forLoopStart, SetNode, easy forLoopEnd, SetNode, GetNode, SetNode, Int, SetNode, Note, Note, Note, Note, SetNode, GetNode, TextEncodeQwenImageEditPlus, ReferenceLatent, GetNode, GetNode, GetNode, GetNode, VAEEncode, SetNode, GetNode, GetNode, GetNode, GetNode, ReferenceLatent, GetNode, SetLatentNoiseMask, GetNode, VAEDecode, GetNode, TextEncodeQwenImageEditPlus, GetNode, GetNode, GetNode, GetNode, SetNode, GetNode, GetNode, Note, LayerMask: MaskPreview, GetNode, GetNode, SetNode, Note, RHBatchImages:, RHExtractImage, PreviewImage, SetNode, LanPaint_MaskBlend, ControlNetLoader, ControlNetInpaintingAliMamaApply, VAELoader, Image Comparer (rgthree), LayerUtility: ImageScaleByAspectRatio V2, MaskBlur+, Note, LoadImage, GetNode, SetNode, InvertMask (segment anything), Note, SaveImage, Qwen3VL_Chat, ShowText|pysssss, Note, Note, SetNode, GrowMask, MaskBlur+, KSampler, CLIPLoader, LayerMask: YoloV8Detect, LayerMask: MaskPreview, GetNode, RHUploadZip, LayerUtility: PurgeVRAM V2, Bjornulf_ShowInt, GetNode, LoadImage, CR Text, Note, Note, LoraLoader, LoraLoader, UNETLoader, CheckpointLoaderSimple, LoraLoaderModelOnly]
patterns: [image_to_image, lora]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "checkpoint": "new_Qwen-Rapid-AIO-SFW-v19.safetensors", "denoise": 1, "lora_name": "qwen-2511-Escort_Colour_copy_000002000.safetensors", "sampler_name": "euler_ancestral", "scheduler": "beta57", "seed": 922914611490716, "steps": 4, "strength_clip": 1, "strength_model": 0.9000000000000001}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/黑白漫画上色方案——基于qwen2511——特调loraV4.0_2009612107720953858.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/黑白漫画上色方案——基于qwen2511——特调loraV4.0_2009612107720953858.json`

## 结构

**生成流程**：Model → Encode → Control → Sampling → Decode → Process → Output → Other

**节点**（92 个）：
- `SetNode`
- `easy showAnything`
- `easy imageCount`
- `easy forLoopStart`
- `SetNode`
- `easy forLoopEnd`
- `SetNode`
- `GetNode`
- `SetNode`
- `Int`
- `SetNode`
- `Note`
- `Note`
- `Note`
- `Note`
- `SetNode`
- `GetNode`
- `TextEncodeQwenImageEditPlus`
- `ReferenceLatent`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `VAEEncode` ★核心
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `ReferenceLatent`
- `GetNode`
- `SetLatentNoiseMask`
- `GetNode`
- `VAEDecode` ★核心
- `GetNode`
- `TextEncodeQwenImageEditPlus`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `Note`
- `LayerMask: MaskPreview`
- `GetNode`
- `GetNode`
- `SetNode`
- `Note`
- `RHBatchImages:`
- `RHExtractImage`
- `PreviewImage`
- `SetNode`
- `LanPaint_MaskBlend`
- `ControlNetLoader`
- `ControlNetInpaintingAliMamaApply`
- `VAELoader`
- `Image Comparer (rgthree)`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `MaskBlur+`
- `Note`
- `LoadImage`
- `GetNode`
- `SetNode`
- `InvertMask (segment anything)`
- `Note`
- `SaveImage`
- `Qwen3VL_Chat`
- `ShowText|pysssss`
- `Note`
- `Note`
- `SetNode`
- `GrowMask`
- `MaskBlur+`
- `KSampler` ★核心
- `CLIPLoader`
- `LayerMask: YoloV8Detect`
- `LayerMask: MaskPreview`
- `GetNode`
- `RHUploadZip`
- `LayerUtility: PurgeVRAM V2`
- `Bjornulf_ShowInt`
- `GetNode`
- `LoadImage`
- `CR Text`
- `Note`
- `Note`
- `LoraLoader` ★核心
- `LoraLoader` ★核心
- `UNETLoader` ★核心
- `CheckpointLoaderSimple` ★核心
- `LoraLoaderModelOnly` ★核心

**识别到的模式**：image_to_image、lora

## 关键参数

- `seed` = `922914611490716`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `euler_ancestral`
- `scheduler` = `beta57`
- `denoise` = `1`
- `lora_name` = `qwen-2511-Escort_Colour_copy_000002000.safetensors`
- `strength_model` = `0.9000000000000001`
- `strength_clip` = `1`
- `checkpoint` = `new_Qwen-Rapid-AIO-SFW-v19.safetensors`

## 知识

覆盖率 **43%**（40/92）

**有卡**：`easy imageCount`、`easy forLoopStart`、`easy forLoopEnd`、`Int`、`TextEncodeQwenImageEditPlus`、`ReferenceLatent`、`VAEEncode`、`SetLatentNoiseMask`、`VAEDecode`、`LayerMask: MaskPreview`、`RHBatchImages:`、`RHExtractImage`、`LanPaint_MaskBlend`、`ControlNetLoader`、`ControlNetInpaintingAliMamaApply`、`VAELoader`、`LayerUtility: ImageScaleByAspectRatio V2`、`MaskBlur+`、`LoadImage`、`InvertMask (segment anything)`、`SaveImage`、`Qwen3VL_Chat`、`GrowMask`、`KSampler`、`CLIPLoader`、`LayerMask: YoloV8Detect`、`RHUploadZip`、`LayerUtility: PurgeVRAM V2`、`Bjornulf_ShowInt`、`CR Text`、`LoraLoader`、`UNETLoader`、`CheckpointLoaderSimple`、`LoraLoaderModelOnly`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CheckpointLoaderSimple、UNETLoader、CLIPLoader、LoadImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

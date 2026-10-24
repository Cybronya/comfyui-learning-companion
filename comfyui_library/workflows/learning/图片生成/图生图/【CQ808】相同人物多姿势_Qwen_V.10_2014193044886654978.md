---
key: 图片生成/图生图/【CQ808】相同人物多姿势_Qwen_V.10_2014193044886654978.json
name: 【CQ808】相同人物多姿势_Qwen_V.10_2014193044886654978
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/【CQ808】相同人物多姿势_Qwen_V.10_2014193044886654978.json
hash: 32dfd7ba26230c20
coverage: 0.793103
learned_at: 2026-10-23 11:48:33
nodes: [CLIPLoader, VAELoader, easy anythingIndexSwitch, ProcessString, Int, LoraLoaderModelOnly, ModelSamplingAuraFlow, LoraLoaderModelOnly, easy anythingIndexSwitch, TextEncodeQwenImageEditPlus, ConditioningZeroOut, PrimitiveInt, Text Concatenate, JDCN_StringToList, Note, CFGNorm, VAEEncode, ImageScaleToTotalPixels, SetNode, GetNode, VAEDecode, VAEDecode, easy anythingIndexSwitch, easy imageCount, easy forLoopStart, easy forLoopEnd, easy showAnything, RHBatchImages:, VAEDecode, easy imageListToImageBatch, easy imageCount, Bjornulf_ShowInt, easy forLoopStart, easy forLoopEnd, easy showAnything, RHBatchImages:, easy imageListToImageBatch, DuckHideNode, LayerUtility: PurgeVRAM, TT_img_enc_v2, SaveImage, Fast Groups Bypasser (rgthree), CheckpointLoaderSimple, KSampler, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, Bjornulf_ShowInt, Fast Groups Bypasser (rgthree), Fast Groups Bypasser (rgthree), SaveImage, Note, Note, Note, LoadImage, CR Text, CR Prompt Text, SaveImage]
patterns: [image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "checkpoint": "e6093d0b626b2a046868f0fc1b5b98962608194df5d2dcbd3f2f737401897c47.safetensors", "denoise": 1, "sampler_name": "euler_ancestral", "scheduler": "beta", "seed": 754667695069507, "steps": 8}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/【CQ808】相同人物多姿势_Qwen_V.10_2014193044886654978.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/【CQ808】相同人物多姿势_Qwen_V.10_2014193044886654978.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（58 个）：
- `CLIPLoader`
- `VAELoader`
- `easy anythingIndexSwitch`
- `ProcessString`
- `Int`
- `LoraLoaderModelOnly` ★核心
- `ModelSamplingAuraFlow`
- `LoraLoaderModelOnly` ★核心
- `easy anythingIndexSwitch`
- `TextEncodeQwenImageEditPlus`
- `ConditioningZeroOut`
- `PrimitiveInt`
- `Text Concatenate`
- `JDCN_StringToList`
- `Note`
- `CFGNorm`
- `VAEEncode` ★核心
- `ImageScaleToTotalPixels`
- `SetNode`
- `GetNode`
- `VAEDecode` ★核心
- `VAEDecode` ★核心
- `easy anythingIndexSwitch`
- `easy imageCount`
- `easy forLoopStart`
- `easy forLoopEnd`
- `easy showAnything`
- `RHBatchImages:`
- `VAEDecode` ★核心
- `easy imageListToImageBatch`
- `easy imageCount`
- `Bjornulf_ShowInt`
- `easy forLoopStart`
- `easy forLoopEnd`
- `easy showAnything`
- `RHBatchImages:`
- `easy imageListToImageBatch`
- `DuckHideNode`
- `LayerUtility: PurgeVRAM`
- `TT_img_enc_v2`
- `SaveImage`
- `Fast Groups Bypasser (rgthree)`
- `CheckpointLoaderSimple` ★核心
- `KSampler` ★核心
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `Bjornulf_ShowInt`
- `Fast Groups Bypasser (rgthree)`
- `Fast Groups Bypasser (rgthree)`
- `SaveImage`
- `Note`
- `Note`
- `Note`
- `LoadImage`
- `CR Text`
- `CR Prompt Text`
- `SaveImage`

**识别到的模式**：image_to_image

## 关键参数

- `checkpoint` = `e6093d0b626b2a046868f0fc1b5b98962608194df5d2dcbd3f2f737401897c47.safetensors`
- `seed` = `754667695069507`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `euler_ancestral`
- `scheduler` = `beta`
- `denoise` = `1`

## 知识

覆盖率 **79%**（46/58）

**有卡**：`CLIPLoader`、`VAELoader`、`easy anythingIndexSwitch`、`ProcessString`、`Int`、`LoraLoaderModelOnly`、`ModelSamplingAuraFlow`、`TextEncodeQwenImageEditPlus`、`ConditioningZeroOut`、`Text Concatenate`、`JDCN_StringToList`、`CFGNorm`、`VAEEncode`、`ImageScaleToTotalPixels`、`VAEDecode`、`easy imageCount`、`easy forLoopStart`、`easy forLoopEnd`、`RHBatchImages:`、`easy imageListToImageBatch`、`Bjornulf_ShowInt`、`DuckHideNode`、`LayerUtility: PurgeVRAM`、`TT_img_enc_v2`、`SaveImage`、`CheckpointLoaderSimple`、`KSampler`、`UNETLoader`、`LoadImage`、`CR Text`、`CR Prompt Text`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CheckpointLoaderSimple、UNETLoader、CLIPLoader、ConditioningZeroOut

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

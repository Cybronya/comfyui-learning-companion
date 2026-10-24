---
key: 图片生成/图生图/产品单图编辑 ｜细节修复、修改文本… ｜+RefineAny 局部优化 LoRA｜Qwen-lmage-Edit-2511_2052579173188816897.json
name: 产品单图编辑 ｜细节修复、修改文本… ｜+RefineAny 局部优化 LoRA｜Qwen-lmage-Edit-2511_2052579173188816897
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/产品单图编辑 ｜细节修复、修改文本… ｜+RefineAny 局部优化 LoRA｜Qwen-lmage-Edit-2511_2052579173188816897.json
hash: 553a6d7135ec9c2e
coverage: 0.72
learned_at: 2026-10-23 12:07:03
nodes: [ModelSamplingAuraFlow, CFGNorm, FluxKontextMultiReferenceLatentMethod, VAEEncode, VAEDecode, VAELoader, RefineNodeReferenceImageProcess, RefineNodePreprocessMask, Note, Note, ConditioningZeroOut, Note, Note, KSampler, Image Comparer (rgthree), TextEncodeQwenImageEditPlus, LoadImage, LoraLoaderModelOnly, LoraLoaderModelOnly, CLIPLoader, UNETLoader, Note, Note, RefineNodePasteBack, SaveImage]
patterns: [image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 482930941659100, "steps": 4}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/产品单图编辑 ｜细节修复、修改文本… ｜+RefineAny 局部优化 LoRA｜Qwen-lmage-Edit-2511_2052579173188816897.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/产品单图编辑 ｜细节修复、修改文本… ｜+RefineAny 局部优化 LoRA｜Qwen-lmage-Edit-2511_2052579173188816897.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（25 个）：
- `ModelSamplingAuraFlow`
- `CFGNorm`
- `FluxKontextMultiReferenceLatentMethod`
- `VAEEncode` ★核心
- `VAEDecode` ★核心
- `VAELoader`
- `RefineNodeReferenceImageProcess`
- `RefineNodePreprocessMask`
- `Note`
- `Note`
- `ConditioningZeroOut`
- `Note`
- `Note`
- `KSampler` ★核心
- `Image Comparer (rgthree)`
- `TextEncodeQwenImageEditPlus`
- `LoadImage`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `CLIPLoader`
- `UNETLoader` ★核心
- `Note`
- `Note`
- `RefineNodePasteBack`
- `SaveImage`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `482930941659100`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **72%**（18/25）

**有卡**：`ModelSamplingAuraFlow`、`CFGNorm`、`FluxKontextMultiReferenceLatentMethod`、`VAEEncode`、`VAEDecode`、`VAELoader`、`RefineNodeReferenceImageProcess`、`RefineNodePreprocessMask`、`ConditioningZeroOut`、`KSampler`、`TextEncodeQwenImageEditPlus`、`LoadImage`、`LoraLoaderModelOnly`、`CLIPLoader`、`UNETLoader`、`RefineNodePasteBack`、`SaveImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPLoader、ConditioningZeroOut、LoadImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

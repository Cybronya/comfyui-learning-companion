---
key: 平台全量/产品单图编辑 + 1 张参考图（精细编辑）｜+RefineAny 局部优化 LoRA｜Qwen-lmage-Edit-2511_2052582687495475201.json
name: 产品单图编辑 + 1 张参考图（精细编辑）｜+RefineAny 局部优化 LoRA｜Qwen-lmage-Edit-2511_2052582687495475201
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/平台全量/产品单图编辑 + 1 张参考图（精细编辑）｜+RefineAny 局部优化 LoRA｜Qwen-lmage-Edit-2511_2052582687495475201.json
hash: 0b4956c14964b2bf
coverage: 0.689655
learned_at: 2026-11-14 01:34:51
nodes: [ModelSamplingAuraFlow, CFGNorm, VAEDecode, VAELoader, VAEEncode, PreviewImage, PreviewImage, ConditioningZeroOut, CLIPLoader, RefineNodeReferenceImageProcess, Note, LoadImage, RefineNodePreprocessMask, Note, Note, FluxKontextMultiReferenceLatentMethod, LoadImage, RefineNodePreprocessMask, KSampler, TextEncodeQwenImageEditPlus, Note, Note, LoraLoaderModelOnly, LoraLoaderModelOnly, UNETLoader, Note, Note, RefineNodePasteBack, SaveImage]
patterns: [image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 468908371904668, "steps": 4}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 平台全量/产品单图编辑 + 1 张参考图（精细编辑）｜+RefineAny 局部优化 LoRA｜Qwen-lmage-Edit-2511_2052582687495475201.json

> 来源文件 `comfyui_library/workflows/平台全量/产品单图编辑 + 1 张参考图（精细编辑）｜+RefineAny 局部优化 LoRA｜Qwen-lmage-Edit-2511_2052582687495475201.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（29 个）：
- `ModelSamplingAuraFlow`
- `CFGNorm`
- `VAEDecode` ★核心
- `VAELoader`
- `VAEEncode` ★核心
- `PreviewImage`
- `PreviewImage`
- `ConditioningZeroOut`
- `CLIPLoader`
- `RefineNodeReferenceImageProcess`
- `Note`
- `LoadImage`
- `RefineNodePreprocessMask`
- `Note`
- `Note`
- `FluxKontextMultiReferenceLatentMethod`
- `LoadImage`
- `RefineNodePreprocessMask`
- `KSampler` ★核心
- `TextEncodeQwenImageEditPlus`
- `Note`
- `Note`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `Note`
- `Note`
- `RefineNodePasteBack`
- `SaveImage`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `468908371904668`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **69%**（20/29）

**有卡**：`ModelSamplingAuraFlow`、`CFGNorm`、`VAEDecode`、`VAELoader`、`VAEEncode`、`ConditioningZeroOut`、`CLIPLoader`、`RefineNodeReferenceImageProcess`、`LoadImage`、`RefineNodePreprocessMask`、`FluxKontextMultiReferenceLatentMethod`、`KSampler`、`TextEncodeQwenImageEditPlus`、`LoraLoaderModelOnly`、`UNETLoader`、`RefineNodePasteBack`、`SaveImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPLoader、ConditioningZeroOut、LoadImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

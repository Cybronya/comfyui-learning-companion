---
key: 图片生成/图生图/Qwen-Image-Edit-2511-Multiple-Angles-LoRA单个镜头_2009066368041226242.json
name: Qwen-Image-Edit-2511-Multiple-Angles-LoRA单个镜头_2009066368041226242
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen-Image-Edit-2511-Multiple-Angles-LoRA单个镜头_2009066368041226242.json
hash: 14037bc33f369b33
coverage: 0.736842
learned_at: 2026-10-23 11:16:51
nodes: [ModelSamplingAuraFlow, LoraLoaderModelOnly, VAELoader, Anything Everywhere3, CLIPLoader, UNETLoader, CFGNorm, LoraLoaderModelOnly, Note, VAEEncode, Anything Everywhere3, TextEncodeQwenImageEdit, LoadImage, VAEDecode, ConditioningZeroOut, SaveImage, KSampler, PrimitiveStringMultiline, PreviewImage]
patterns: [image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "beta", "seed": 767446396265436, "steps": 8}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/Qwen-Image-Edit-2511-Multiple-Angles-LoRA单个镜头_2009066368041226242.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen-Image-Edit-2511-Multiple-Angles-LoRA单个镜头_2009066368041226242.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Output → Other

**节点**（19 个）：
- `ModelSamplingAuraFlow`
- `LoraLoaderModelOnly` ★核心
- `VAELoader`
- `Anything Everywhere3`
- `CLIPLoader`
- `UNETLoader` ★核心
- `CFGNorm`
- `LoraLoaderModelOnly` ★核心
- `Note`
- `VAEEncode` ★核心
- `Anything Everywhere3`
- `TextEncodeQwenImageEdit`
- `LoadImage`
- `VAEDecode` ★核心
- `ConditioningZeroOut`
- `SaveImage`
- `KSampler` ★核心
- `PrimitiveStringMultiline`
- `PreviewImage`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `767446396265436`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `beta`
- `denoise` = `1`

## 知识

覆盖率 **74%**（14/19）

**有卡**：`ModelSamplingAuraFlow`、`LoraLoaderModelOnly`、`VAELoader`、`CLIPLoader`、`UNETLoader`、`CFGNorm`、`VAEEncode`、`TextEncodeQwenImageEdit`、`LoadImage`、`VAEDecode`、`ConditioningZeroOut`、`SaveImage`、`KSampler`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、ConditioningZeroOut、LoadImage、UNETLoader

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

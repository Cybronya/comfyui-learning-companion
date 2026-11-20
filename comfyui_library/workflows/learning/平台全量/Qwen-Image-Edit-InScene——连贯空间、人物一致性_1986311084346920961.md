---
key: 平台全量/Qwen-Image-Edit-InScene——连贯空间、人物一致性_1986311084346920961.json
name: Qwen-Image-Edit-InScene——连贯空间、人物一致性_1986311084346920961
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/平台全量/Qwen-Image-Edit-InScene——连贯空间、人物一致性_1986311084346920961.json
hash: 52d5a7e50f6c1c8d
coverage: 0.85
learned_at: 2026-11-14 00:51:44
nodes: [LoraLoaderModelOnly, LoraLoaderModelOnly, UNETLoader, LoadImage, ImageConcanate, LayerUtility: ImageScaleByAspectRatio V2, VAEEncode, TextEncodeQwenImageEdit_lrzjason, KSampler, CFGNorm, ConditioningZeroOut, SaveImage, VAEDecode, ModelSamplingAuraFlow, CLIPLoader, VAELoader, PrimitiveStringMultiline, Note, MarkdownNote, SaveImage]
patterns: [image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 472575691907664, "steps": 8}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 平台全量/Qwen-Image-Edit-InScene——连贯空间、人物一致性_1986311084346920961.json

> 来源文件 `comfyui_library/workflows/平台全量/Qwen-Image-Edit-InScene——连贯空间、人物一致性_1986311084346920961.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（20 个）：
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `LoadImage`
- `ImageConcanate`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `VAEEncode` ★核心
- `TextEncodeQwenImageEdit_lrzjason`
- `KSampler` ★核心
- `CFGNorm`
- `ConditioningZeroOut`
- `SaveImage`
- `VAEDecode` ★核心
- `ModelSamplingAuraFlow`
- `CLIPLoader`
- `VAELoader`
- `PrimitiveStringMultiline`
- `Note`
- `MarkdownNote`
- `SaveImage`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `472575691907664`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **85%**（17/20）

**有卡**：`LoraLoaderModelOnly`、`UNETLoader`、`LoadImage`、`ImageConcanate`、`LayerUtility: ImageScaleByAspectRatio V2`、`VAEEncode`、`TextEncodeQwenImageEdit_lrzjason`、`KSampler`、`CFGNorm`、`ConditioningZeroOut`、`SaveImage`、`VAEDecode`、`ModelSamplingAuraFlow`、`CLIPLoader`、`VAELoader`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、ConditioningZeroOut、LoadImage、UNETLoader

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

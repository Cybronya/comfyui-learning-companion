---
key: 图片生成/图生图/批量多角度图片生成+qwen-edit-2511-multiple-angles-lora_2009835220324851714.json
name: 批量多角度图片生成+qwen-edit-2511-multiple-angles-lora_2009835220324851714
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/批量多角度图片生成+qwen-edit-2511-multiple-angles-lora_2009835220324851714.json
hash: 8ead97af0772098a
coverage: 0.869565
learned_at: 2026-10-23 12:54:27
nodes: [ModelSamplingAuraFlow, FluxKontextMultiReferenceLatentMethod, FluxKontextMultiReferenceLatentMethod, CFGNorm, TextEncodeQwenImageEditPlus, Note, VAEDecode, TextEncodeQwenImageEditPlus, LoadImage, KSampler, FluxKontextImageScale, VAEEncode, SaveImage, ShowText|pysssss, Text Multiline, CR Seed, LoraLoaderModelOnly, UNETLoader, LoraLoaderModelOnly, CLIPLoader, VAELoader, easy promptLine, Note]
patterns: [image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 293976170771154, "steps": 4}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/批量多角度图片生成+qwen-edit-2511-multiple-angles-lora_2009835220324851714.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/批量多角度图片生成+qwen-edit-2511-multiple-angles-lora_2009835220324851714.json`

## 结构

**生成流程**：Model → Encode → Sampling → Decode → Output → Other

**节点**（23 个）：
- `ModelSamplingAuraFlow`
- `FluxKontextMultiReferenceLatentMethod`
- `FluxKontextMultiReferenceLatentMethod`
- `CFGNorm`
- `TextEncodeQwenImageEditPlus`
- `Note`
- `VAEDecode` ★核心
- `TextEncodeQwenImageEditPlus`
- `LoadImage`
- `KSampler` ★核心
- `FluxKontextImageScale`
- `VAEEncode` ★核心
- `SaveImage`
- `ShowText|pysssss`
- `Text Multiline`
- `CR Seed`
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `CLIPLoader`
- `VAELoader`
- `easy promptLine`
- `Note`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `293976170771154`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **87%**（20/23）

**有卡**：`ModelSamplingAuraFlow`、`FluxKontextMultiReferenceLatentMethod`、`CFGNorm`、`TextEncodeQwenImageEditPlus`、`VAEDecode`、`LoadImage`、`KSampler`、`FluxKontextImageScale`、`VAEEncode`、`SaveImage`、`Text Multiline`、`CR Seed`、`LoraLoaderModelOnly`、`UNETLoader`、`CLIPLoader`、`VAELoader`、`easy promptLine`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPLoader、LoadImage、CFGNorm

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

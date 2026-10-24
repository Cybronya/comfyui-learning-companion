---
key: 图片生成/图生图/【遇见AI】Qwen-image controlnet lora版diffsynth_2050876883620909058.json
name: 【遇见AI】Qwen-image controlnet lora版diffsynth_2050876883620909058
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/【遇见AI】Qwen-image controlnet lora版diffsynth_2050876883620909058.json
hash: 1efd80a204568776
coverage: 0.9
learned_at: 2026-10-23 11:52:09
nodes: [CFGNorm, ModelSamplingAuraFlow, VAEDecode, SaveImage, KSampler, AIO_Preprocessor, TextEncodeQwenImageEditPlus, ReferenceLatent, TextEncodeQwenImageEditPlus, VAEEncode, PreviewImage, Note, ReferenceLatent, LoadImage, LoadImage, UNETLoader, CLIPLoader, VAELoader, LoadImage, LoraLoader]
patterns: [image_to_image, lora]
missing: []
parameters: {"cfg": 2.5, "denoise": 1, "lora_name": "Qwen\\qwen_image_union_diffsynth_lora.safetensors", "sampler_name": "euler", "scheduler": "simple", "seed": 891131941913746, "steps": 40, "strength_clip": 1, "strength_model": 1}
---

# 图片生成/图生图/【遇见AI】Qwen-image controlnet lora版diffsynth_2050876883620909058.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/【遇见AI】Qwen-image controlnet lora版diffsynth_2050876883620909058.json`

## 结构

**生成流程**：Model → Encode → Sampling → Decode → Output → Other

**节点**（20 个）：
- `CFGNorm`
- `ModelSamplingAuraFlow`
- `VAEDecode` ★核心
- `SaveImage`
- `KSampler` ★核心
- `AIO_Preprocessor`
- `TextEncodeQwenImageEditPlus`
- `ReferenceLatent`
- `TextEncodeQwenImageEditPlus`
- `VAEEncode` ★核心
- `PreviewImage`
- `Note`
- `ReferenceLatent`
- `LoadImage`
- `LoadImage`
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `LoadImage`
- `LoraLoader` ★核心

**识别到的模式**：image_to_image、lora

## 关键参数

- `seed` = `891131941913746`
- `steps` = `40`
- `cfg` = `2.5`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`
- `lora_name` = `Qwen\qwen_image_union_diffsynth_lora.safetensors`
- `strength_model` = `1`
- `strength_clip` = `1`

## 知识

覆盖率 **90%**（18/20）

**有卡**：`CFGNorm`、`ModelSamplingAuraFlow`、`VAEDecode`、`SaveImage`、`KSampler`、`AIO_Preprocessor`、`TextEncodeQwenImageEditPlus`、`ReferenceLatent`、`VAEEncode`、`LoadImage`、`UNETLoader`、`CLIPLoader`、`VAELoader`、`LoraLoader`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPLoader、LoadImage、UNETLoader、CFGNorm、ReferenceLatent

---
key: 图片生成/图生图/Qwen_EditV1.0_2001542701378093057.json
name: Qwen_EditV1.0_2001542701378093057
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen_EditV1.0_2001542701378093057.json
hash: 4b7519cb8dc038d2
coverage: 0.952381
learned_at: 2026-10-23 11:20:56
nodes: [ModelSamplingAuraFlow, CFGNorm, PrimitiveInt, VAEDecode, CLIPLoader, VAELoader, TextEncodeQwenImageEditPlus, TextEncodeQwenImageEditPlus, LoraLoaderModelOnly, UNETLoader, KSampler, SaveImage, VAEEncode, ImageScaleToTotalPixels, ImageResizeKJv2, ImageResizeKJv2, LoadImage, LoadImage, TextInput_, LoadImage, ImageResizeKJv2]
patterns: [image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "er_sde", "scheduler": "beta", "seed": 356886564754545, "steps": 3}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/Qwen_EditV1.0_2001542701378093057.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen_EditV1.0_2001542701378093057.json`

## 结构

**生成流程**：Model → Encode → Sampling → Decode → Process → Output → Other

**节点**（21 个）：
- `ModelSamplingAuraFlow`
- `CFGNorm`
- `PrimitiveInt`
- `VAEDecode` ★核心
- `CLIPLoader`
- `VAELoader`
- `TextEncodeQwenImageEditPlus`
- `TextEncodeQwenImageEditPlus`
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `KSampler` ★核心
- `SaveImage`
- `VAEEncode` ★核心
- `ImageScaleToTotalPixels`
- `ImageResizeKJv2`
- `ImageResizeKJv2`
- `LoadImage`
- `LoadImage`
- `TextInput_`
- `LoadImage`
- `ImageResizeKJv2`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `356886564754545`
- `steps` = `3`
- `cfg` = `1`
- `sampler_name` = `er_sde`
- `scheduler` = `beta`
- `denoise` = `1`

## 知识

覆盖率 **95%**（20/21）

**有卡**：`ModelSamplingAuraFlow`、`CFGNorm`、`VAEDecode`、`CLIPLoader`、`VAELoader`、`TextEncodeQwenImageEditPlus`、`LoraLoaderModelOnly`、`UNETLoader`、`KSampler`、`SaveImage`、`VAEEncode`、`ImageScaleToTotalPixels`、`ImageResizeKJv2`、`LoadImage`、`TextInput_`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、LoadImage、UNETLoader、CFGNorm

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

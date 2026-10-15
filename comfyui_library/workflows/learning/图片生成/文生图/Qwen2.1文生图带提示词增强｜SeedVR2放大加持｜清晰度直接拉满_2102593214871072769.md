---
key: 图片生成/文生图/Qwen2.1文生图带提示词增强｜SeedVR2放大加持｜清晰度直接拉满_2102593214871072769.json
name: Qwen2.1文生图带提示词增强｜SeedVR2放大加持｜清晰度直接拉满_2102593214871072769
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Qwen2.1文生图带提示词增强｜SeedVR2放大加持｜清晰度直接拉满_2102593214871072769.json
hash: 927062b6331b3b48
coverage: 0.90625
learned_at: 2026-10-10 20:59:07
nodes: [ConditioningZeroOut, CLIPLoader, TextGenerate, TextEncodeQwenImage21, CLIPLoader, VAELoader, UNETLoader, LoraLoaderModelOnly, StringConstantMultiline, ResolutionSelector, SeedVR2LoadVAEModel, SeedVR2LoadDiTModel, easy int, SaveImage, SaveImage, SeedVR2VideoUpscaler, VAEDecode, KSampler, ImageScaleBy, easy clearCacheAll, EmptyLatentImage, 孤海注释, 孤海注释, UNETLoader, CLIPLoader, CLIPTextEncode, VAELoader, EmptyLatentImage, KSampler, VAEDecode, solarL_SaveImagesToZip, JjkText, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, CLIPTextEncode, Note]
patterns: [text_to_image]
missing: [easy clearCacheAll, easy int]
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [次要节点 `easy clearCacheAll` 知识库中没有该节点类型的任何知识, 次要节点 `easy int` 知识库中没有该节点类型的任何知识, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/文生图/Qwen2.1文生图带提示词增强｜SeedVR2放大加持｜清晰度直接拉满_2102593214871072769.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Qwen2.1文生图带提示词增强｜SeedVR2放大加持｜清晰度直接拉满_2102593214871072769.json`

## 结构

**节点**（64 个）：
- `ConditioningZeroOut`
- `CLIPLoader`
- `TextGenerate`
- `TextEncodeQwenImage21`
- `CLIPLoader`
- `VAELoader`
- `UNETLoader`
- `LoraLoaderModelOnly`
- `StringConstantMultiline`
- `ResolutionSelector`
- `SeedVR2LoadVAEModel`
- `SeedVR2LoadDiTModel`
- `easy int`
- `SaveImage`
- `SaveImage`
- `SeedVR2VideoUpscaler`
- `VAEDecode`
- `KSampler`
- `ImageScaleBy`
- `easy clearCacheAll`
- `EmptyLatentImage`
- `孤海注释`
- `孤海注释`
- `UNETLoader`
- `CLIPLoader`
- `CLIPTextEncode`
- `VAELoader`
- `EmptyLatentImage`
- `KSampler`
- `VAEDecode`
- `solarL_SaveImagesToZip`
- `JjkText`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `CLIPTextEncode`
- `Note`

**识别到的模式**：text_to_image

## 关键参数

- `batch_size` = `1`
- `cfg` = `4.5`
- `denoise` = `1`
- `height` = `80`
- `sampler_name` = `er_sde`
- `scheduler` = `beta`
- `seed` = `598626327129635`
- `steps` = `4`
- `width` = `80`

## 知识

覆盖率 **91%**（58/64）

**有卡**：`ConditioningZeroOut`、`CLIPLoader`、`TextGenerate`、`TextEncodeQwenImage21`、`VAELoader`、`UNETLoader`、`LoraLoaderModelOnly`、`StringConstantMultiline`、`ResolutionSelector`、`SeedVR2LoadVAEModel`、`SeedVR2LoadDiTModel`、`easy int`、`SaveImage`、`SeedVR2VideoUpscaler`、`VAEDecode`、`KSampler`、`ImageScaleBy`、`easy clearCacheAll`、`EmptyLatentImage`、`孤海注释`、`CLIPTextEncode`、`solarL_SaveImagesToZip`、`JjkText`

**缺卡**（2）：`easy clearCacheAll`、`easy int`

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- 次要节点 `easy clearCacheAll` 知识库中没有该节点类型的任何知识
- 次要节点 `easy int` 知识库中没有该节点类型的任何知识
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

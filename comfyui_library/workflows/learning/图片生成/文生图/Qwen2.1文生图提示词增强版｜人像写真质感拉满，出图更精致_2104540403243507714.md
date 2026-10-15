---
key: 图片生成/文生图/Qwen2.1文生图提示词增强版｜人像写真质感拉满，出图更精致_2104540403243507714.json
name: Qwen2.1文生图提示词增强版｜人像写真质感拉满，出图更精致_2104540403243507714
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Qwen2.1文生图提示词增强版｜人像写真质感拉满，出图更精致_2104540403243507714.json
hash: e213dd12d0e2cb79
coverage: 0.913793
learned_at: 2026-10-10 20:59:07
nodes: [ConditioningZeroOut, VAELoader, CLIPLoader, VAEDecode, EmptyLatentImage, KSampler, CLIPLoader, easy clearCacheAll, TextEncodeQwenImage21, SaveImage, ResolutionSelector, UNETLoader, StringConstantMultiline, LoraLoaderModelOnly, TextGenerate, 孤海注释, 孤海注释, UNETLoader, CLIPLoader, CLIPTextEncode, VAELoader, EmptyLatentImage, KSampler, VAEDecode, solarL_SaveImagesToZip, JjkText, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, CLIPTextEncode, Note]
patterns: [text_to_image]
missing: [easy clearCacheAll]
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [次要节点 `easy clearCacheAll` 知识库中没有该节点类型的任何知识, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/文生图/Qwen2.1文生图提示词增强版｜人像写真质感拉满，出图更精致_2104540403243507714.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Qwen2.1文生图提示词增强版｜人像写真质感拉满，出图更精致_2104540403243507714.json`

## 结构

**节点**（58 个）：
- `ConditioningZeroOut`
- `VAELoader`
- `CLIPLoader`
- `VAEDecode`
- `EmptyLatentImage`
- `KSampler`
- `CLIPLoader`
- `easy clearCacheAll`
- `TextEncodeQwenImage21`
- `SaveImage`
- `ResolutionSelector`
- `UNETLoader`
- `StringConstantMultiline`
- `LoraLoaderModelOnly`
- `TextGenerate`
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

覆盖率 **91%**（53/58）

**有卡**：`ConditioningZeroOut`、`VAELoader`、`CLIPLoader`、`VAEDecode`、`EmptyLatentImage`、`KSampler`、`easy clearCacheAll`、`TextEncodeQwenImage21`、`SaveImage`、`ResolutionSelector`、`UNETLoader`、`StringConstantMultiline`、`LoraLoaderModelOnly`、`TextGenerate`、`孤海注释`、`CLIPTextEncode`、`solarL_SaveImagesToZip`、`JjkText`

**缺卡**（1）：`easy clearCacheAll`

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- 次要节点 `easy clearCacheAll` 知识库中没有该节点类型的任何知识
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

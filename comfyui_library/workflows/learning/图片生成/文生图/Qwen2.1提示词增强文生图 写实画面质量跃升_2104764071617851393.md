---
key: 图片生成/文生图/Qwen2.1提示词增强文生图 写实画面质量跃升_2104764071617851393.json
name: Qwen2.1提示词增强文生图 写实画面质量跃升_2104764071617851393
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Qwen2.1提示词增强文生图 写实画面质量跃升_2104764071617851393.json
hash: a3e241637b664152
coverage: 0.886364
learned_at: 2026-10-10 20:59:06
nodes: [ConditioningZeroOut, VAELoader, CLIPLoader, VAEDecode, EmptyLatentImage, KSampler, CLIPLoader, easy clearCacheAll, TextEncodeQwenImage21, SaveImage, UNETLoader, StringConstantMultiline, LoraLoaderModelOnly, TextGenerate, ResolutionSelector, 孤海注释, 孤海注释, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, KSampler, EmptyLatentImage, JjkText, CLIPTextEncode, CLIPTextEncode, solarL_SaveImagesToZip, VAEDecode, CLIPLoader, VAELoader, Note]
patterns: [text_to_image]
missing: [easy clearCacheAll]
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [次要节点 `easy clearCacheAll` 知识库中没有该节点类型的任何知识, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/文生图/Qwen2.1提示词增强文生图 写实画面质量跃升_2104764071617851393.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Qwen2.1提示词增强文生图 写实画面质量跃升_2104764071617851393.json`

## 结构

**节点**（44 个）：
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
- `UNETLoader`
- `StringConstantMultiline`
- `LoraLoaderModelOnly`
- `TextGenerate`
- `ResolutionSelector`
- `孤海注释`
- `孤海注释`
- `UNETLoader`
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
- `KSampler`
- `EmptyLatentImage`
- `JjkText`
- `CLIPTextEncode`
- `CLIPTextEncode`
- `solarL_SaveImagesToZip`
- `VAEDecode`
- `CLIPLoader`
- `VAELoader`
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

覆盖率 **89%**（39/44）

**有卡**：`ConditioningZeroOut`、`VAELoader`、`CLIPLoader`、`VAEDecode`、`EmptyLatentImage`、`KSampler`、`easy clearCacheAll`、`TextEncodeQwenImage21`、`SaveImage`、`UNETLoader`、`StringConstantMultiline`、`LoraLoaderModelOnly`、`TextGenerate`、`ResolutionSelector`、`孤海注释`、`JjkText`、`CLIPTextEncode`

**缺卡**（1）：`easy clearCacheAll`

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- 次要节点 `easy clearCacheAll` 知识库中没有该节点类型的任何知识
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

---
key: 图片生成/文生图/Qwen2.1提示词增强文生图 写实画面质量跃升_2104764071617851393.json
name: Qwen2.1提示词增强文生图 写实画面质量跃升_2104764071617851393
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Qwen2.1提示词增强文生图 写实画面质量跃升_2104764071617851393.json
hash: a3e241637b664152
coverage: 0.886364
learned_at: 2026-10-07 02:27:19
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

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（44 个）：
- `ConditioningZeroOut`
- `VAELoader`
- `CLIPLoader`
- `VAEDecode` ★核心
- `EmptyLatentImage` ★核心
- `KSampler` ★核心
- `CLIPLoader`
- `easy clearCacheAll`
- `TextEncodeQwenImage21`
- `SaveImage`
- `UNETLoader` ★核心
- `StringConstantMultiline`
- `LoraLoaderModelOnly` ★核心
- `TextGenerate`
- `ResolutionSelector`
- `孤海注释`
- `孤海注释`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `KSampler` ★核心
- `EmptyLatentImage` ★核心
- `JjkText`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `solarL_SaveImagesToZip`
- `VAEDecode` ★核心
- `CLIPLoader`
- `VAELoader`
- `Note`

**识别到的模式**：text_to_image

## 关键参数

- `width` = `80`
- `height` = `80`
- `batch_size` = `1`
- `seed` = `598626327129635`
- `steps` = `4`
- `cfg` = `4.5`
- `sampler_name` = `er_sde`
- `scheduler` = `beta`
- `denoise` = `1`

## 知识

覆盖率 **89%**（39/44）

**有卡**：`ConditioningZeroOut`、`VAELoader`、`CLIPLoader`、`VAEDecode`、`EmptyLatentImage`、`KSampler`、`TextEncodeQwenImage21`、`SaveImage`、`UNETLoader`、`StringConstantMultiline`、`LoraLoaderModelOnly`、`TextGenerate`、`ResolutionSelector`、`CLIPTextEncode`、`solarL_SaveImagesToZip`

**缺卡**（1）：`easy clearCacheAll`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、ConditioningZeroOut

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- 次要节点 `easy clearCacheAll` 知识库中没有该节点类型的任何知识
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

---
key: QwenImage2.1文生图搭配官方提示词助手，T2I自动扩写出图效率提升_2103196536837595138.json
name: QwenImage2.1文生图搭配官方提示词助手，T2I自动扩写出图效率提升_2103196536837595138
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/QwenImage2.1文生图搭配官方提示词助手，T2I自动扩写出图效率提升_2103196536837595138.json
hash: 3cc390ffd210b522
coverage: 0.8125
learned_at: 2026-10-10 20:59:07
nodes: [CLIPLoader, EmptyLatentImage, KSampler, ResolutionSelector, PrimitiveStringMultiline, VAEDecode, TextConcatenator, TextGenerate, CLIPLoader, JsonExtractString, VAELoader, Any Switch (rgthree), UNETLoader, SaveImageAdvanced, SaveImage, ShowAnything|Mie, TextEncodeQwenImage21, Fast Groups Bypasser (rgthree), PrimitiveStringMultiline, 孤海注释, 孤海注释, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, KSampler, EmptyLatentImage, JjkText, CLIPTextEncode, CLIPTextEncode, solarL_SaveImagesToZip, VAEDecode, CLIPLoader, VAELoader, Note]
patterns: [text_to_image]
missing: [ShowAnything|Mie]
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [次要节点 `ShowAnything|Mie` 知识库中没有该节点类型的任何知识, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# QwenImage2.1文生图搭配官方提示词助手，T2I自动扩写出图效率提升_2103196536837595138.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/QwenImage2.1文生图搭配官方提示词助手，T2I自动扩写出图效率提升_2103196536837595138.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（48 个）：
- `CLIPLoader`
- `EmptyLatentImage` ★核心
- `KSampler` ★核心
- `ResolutionSelector`
- `PrimitiveStringMultiline`
- `VAEDecode` ★核心
- `TextConcatenator`
- `TextGenerate`
- `CLIPLoader`
- `JsonExtractString`
- `VAELoader`
- `Any Switch (rgthree)`
- `UNETLoader` ★核心
- `SaveImageAdvanced`
- `SaveImage`
- `ShowAnything|Mie`
- `TextEncodeQwenImage21`
- `Fast Groups Bypasser (rgthree)`
- `PrimitiveStringMultiline`
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

覆盖率 **81%**（39/48）

**有卡**：`CLIPLoader`、`EmptyLatentImage`、`KSampler`、`ResolutionSelector`、`VAEDecode`、`TextConcatenator`、`TextGenerate`、`JsonExtractString`、`VAELoader`、`UNETLoader`、`SaveImageAdvanced`、`SaveImage`、`TextEncodeQwenImage21`、`LoraLoaderModelOnly`、`CLIPTextEncode`、`solarL_SaveImagesToZip`

**缺卡**（1）：`ShowAnything|Mie`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- 次要节点 `ShowAnything|Mie` 知识库中没有该节点类型的任何知识
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

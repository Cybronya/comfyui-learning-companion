---
key: 图片生成/文生图/通用QwenImage2.1方案，文生图图生图一站搞定_2111525886070706178.json
name: 通用QwenImage2.1方案，文生图图生图一站搞定_2111525886070706178
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/通用QwenImage2.1方案，文生图图生图一站搞定_2111525886070706178.json
hash: 403cf0381f9ea990
coverage: 0.790323
learned_at: 2026-10-21 03:03:12
nodes: [TextGenerate, easy showAnything, PrimitiveStringMultiline, easy showAnything, UNETLoader, CLIPLoader, VAELoader, KSampler, QwenImage21Cache, ComfySwitchNode, PrimitiveStringMultiline, CLIPLoader, CLIPLoader, easy isNone, JsonExtractString, TextConcatenator, ComfySwitchNode, easy showAnything, PrimitiveStringMultiline, EmptyLatentImage, SaveImage, VAEDecode, Any Switch (rgthree), LoadImage, LoadImage, LoadImage, LoadImage, TextEncodeQwenImage21, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, 孤海注释, 孤海注释, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, KSampler, CLIPTextEncode, CLIPTextEncode, CLIPLoader, JjkText, VAEDecode, EmptyLatentImage, VAELoader, solarL_SaveImagesToZip, Note]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/文生图/通用QwenImage2.1方案，文生图图生图一站搞定_2111525886070706178.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/通用QwenImage2.1方案，文生图图生图一站搞定_2111525886070706178.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（62 个）：
- `TextGenerate`
- `easy showAnything`
- `PrimitiveStringMultiline`
- `easy showAnything`
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `KSampler` ★核心
- `QwenImage21Cache`
- `ComfySwitchNode`
- `PrimitiveStringMultiline`
- `CLIPLoader`
- `CLIPLoader`
- `easy isNone`
- `JsonExtractString`
- `TextConcatenator`
- `ComfySwitchNode`
- `easy showAnything`
- `PrimitiveStringMultiline`
- `EmptyLatentImage` ★核心
- `SaveImage`
- `VAEDecode` ★核心
- `Any Switch (rgthree)`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `TextEncodeQwenImage21`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
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
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `CLIPLoader`
- `JjkText`
- `VAEDecode` ★核心
- `EmptyLatentImage` ★核心
- `VAELoader`
- `solarL_SaveImagesToZip`
- `Note`

**识别到的模式**：text_to_image

## 关键参数

- `seed` = `598626327129635`
- `steps` = `4`
- `cfg` = `4.5`
- `sampler_name` = `er_sde`
- `scheduler` = `beta`
- `denoise` = `1`
- `width` = `80`
- `height` = `80`
- `batch_size` = `1`

## 知识

覆盖率 **79%**（49/62）

**有卡**：`TextGenerate`、`UNETLoader`、`CLIPLoader`、`VAELoader`、`KSampler`、`QwenImage21Cache`、`easy isNone`、`JsonExtractString`、`TextConcatenator`、`EmptyLatentImage`、`SaveImage`、`VAEDecode`、`LoadImage`、`TextEncodeQwenImage21`、`LoraLoaderModelOnly`、`CLIPTextEncode`、`solarL_SaveImagesToZip`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

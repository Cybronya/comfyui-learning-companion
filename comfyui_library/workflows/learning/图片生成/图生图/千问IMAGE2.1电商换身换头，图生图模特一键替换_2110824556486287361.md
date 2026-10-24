---
key: 图片生成/图生图/千问IMAGE2.1电商换身换头，图生图模特一键替换_2110824556486287361.json
name: 千问IMAGE2.1电商换身换头，图生图模特一键替换_2110824556486287361
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/千问IMAGE2.1电商换身换头，图生图模特一键替换_2110824556486287361.json
hash: c5687579d9a9447e
coverage: 0.850746
learned_at: 2026-10-23 12:29:49
nodes: [Anything Everywhere, Anything Everywhere, Anything Everywhere, VAEDecode, Get resolution [Crystools], VAELoader, EmptyLatentImage, CLIPLoader, RegexReplace, CLIPLoader, StringConcatenate, UNETLoader, KSampler, TextGenerate, PreviewImage, VAEDecode, VAELoader, VAEEncode, ReferenceLatent, VAEDecode, PreviewImage, SaveImage, LoraLoaderModelOnly, TextEncodeQwenImage21, ConditioningZeroOut, CLIPLoader, TextEncodeQwenImage21, CLIPTextEncode, KSampler, LoraLoaderModelOnly, LoadImage, LoadImage, PrimitiveStringMultiline, EmptyLatentImage, UNETLoader, LoraLoaderModelOnly, KSamplerAdvanced, LoadImage, 孤海注释, 孤海注释, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, KSampler, CLIPTextEncode, CLIPTextEncode, CLIPLoader, JjkText, VAEDecode, EmptyLatentImage, VAELoader, solarL_SaveImagesToZip, Note]
patterns: [text_to_image, image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/千问IMAGE2.1电商换身换头，图生图模特一键替换_2110824556486287361.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/千问IMAGE2.1电商换身换头，图生图模特一键替换_2110824556486287361.json`

## 结构

**生成流程**：Model → Encode → Condition → Latent → Sampling → Decode → Output → Other

**节点**（67 个）：
- `Anything Everywhere`
- `Anything Everywhere`
- `Anything Everywhere`
- `VAEDecode` ★核心
- `Get resolution [Crystools]`
- `VAELoader`
- `EmptyLatentImage` ★核心
- `CLIPLoader`
- `RegexReplace`
- `CLIPLoader`
- `StringConcatenate`
- `UNETLoader` ★核心
- `KSampler` ★核心
- `TextGenerate`
- `PreviewImage`
- `VAEDecode` ★核心
- `VAELoader`
- `VAEEncode` ★核心
- `ReferenceLatent`
- `VAEDecode` ★核心
- `PreviewImage`
- `SaveImage`
- `LoraLoaderModelOnly` ★核心
- `TextEncodeQwenImage21`
- `ConditioningZeroOut`
- `CLIPLoader`
- `TextEncodeQwenImage21`
- `CLIPTextEncode` ★核心
- `KSampler` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoadImage`
- `LoadImage`
- `PrimitiveStringMultiline`
- `EmptyLatentImage` ★核心
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `KSamplerAdvanced` ★核心
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

**识别到的模式**：text_to_image、image_to_image

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

覆盖率 **85%**（57/67）

**有卡**：`VAEDecode`、`Get resolution [Crystools]`、`VAELoader`、`EmptyLatentImage`、`CLIPLoader`、`RegexReplace`、`StringConcatenate`、`UNETLoader`、`KSampler`、`TextGenerate`、`VAEEncode`、`ReferenceLatent`、`SaveImage`、`LoraLoaderModelOnly`、`TextEncodeQwenImage21`、`ConditioningZeroOut`、`CLIPTextEncode`、`LoadImage`、`KSamplerAdvanced`、`solarL_SaveImagesToZip`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、ConditioningZeroOut

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

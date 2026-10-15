---
key: 图片生成/文生图/Qwen Image 2.1文生图纯净官流40步无PE，搭配技能高质量文本出图方案_2103260563735400450.json
name: Qwen Image 2.1文生图纯净官流40步无PE，搭配技能高质量文本出图方案_2103260563735400450
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Qwen Image 2.1文生图纯净官流40步无PE，搭配技能高质量文本出图方案_2103260563735400450.json
hash: e6f98fd83cb08114
coverage: 0.878049
learned_at: 2026-10-10 20:58:54
nodes: [PixaromaRunTimer, UNETLoader, CLIPLoader, VAELoader, TextEncodeQwenImage21, EmptyLatentImage, KSampler, PixaromaSeed, PrimitiveStringMultiline, VAEDecode, SaveImage, ResolutionSelector, 孤海注释, 孤海注释, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, KSampler, EmptyLatentImage, JjkText, CLIPTextEncode, CLIPTextEncode, solarL_SaveImagesToZip, VAEDecode, CLIPLoader, VAELoader, Note]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/文生图/Qwen Image 2.1文生图纯净官流40步无PE，搭配技能高质量文本出图方案_2103260563735400450.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Qwen Image 2.1文生图纯净官流40步无PE，搭配技能高质量文本出图方案_2103260563735400450.json`

## 结构

**节点**（41 个）：
- `PixaromaRunTimer`
- `UNETLoader`
- `CLIPLoader`
- `VAELoader`
- `TextEncodeQwenImage21`
- `EmptyLatentImage`
- `KSampler`
- `PixaromaSeed`
- `PrimitiveStringMultiline`
- `VAEDecode`
- `SaveImage`
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

覆盖率 **88%**（36/41）

**有卡**：`PixaromaRunTimer`、`UNETLoader`、`CLIPLoader`、`VAELoader`、`TextEncodeQwenImage21`、`EmptyLatentImage`、`KSampler`、`PixaromaSeed`、`PrimitiveStringMultiline`、`VAEDecode`、`SaveImage`、`ResolutionSelector`、`孤海注释`、`LoraLoaderModelOnly`、`JjkText`、`CLIPTextEncode`

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

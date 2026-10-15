---
key: 图片生成/文生图/qwen-image-2.1官方原版｜纯净文生图像模型直出_2103085016224985090.json
name: qwen-image-2.1官方原版｜纯净文生图像模型直出_2103085016224985090
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/qwen-image-2.1官方原版｜纯净文生图像模型直出_2103085016224985090.json
hash: 834843cad4e44af3
coverage: 0.923077
learned_at: 2026-10-10 20:59:24
nodes: [UNETLoader, CLIPLoader, VAELoader, KSampler, ResolutionSelector, EmptyLatentImage, TextEncodeQwenImage21, VAEDecode, SaveImage, 孤海注释, 孤海注释, UNETLoader, CLIPLoader, CLIPTextEncode, VAELoader, EmptyLatentImage, KSampler, VAEDecode, solarL_SaveImagesToZip, JjkText, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, CLIPTextEncode, Note]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/文生图/qwen-image-2.1官方原版｜纯净文生图像模型直出_2103085016224985090.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/qwen-image-2.1官方原版｜纯净文生图像模型直出_2103085016224985090.json`

## 结构

**节点**（52 个）：
- `UNETLoader`
- `CLIPLoader`
- `VAELoader`
- `KSampler`
- `ResolutionSelector`
- `EmptyLatentImage`
- `TextEncodeQwenImage21`
- `VAEDecode`
- `SaveImage`
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

覆盖率 **92%**（48/52）

**有卡**：`UNETLoader`、`CLIPLoader`、`VAELoader`、`KSampler`、`ResolutionSelector`、`EmptyLatentImage`、`TextEncodeQwenImage21`、`VAEDecode`、`SaveImage`、`孤海注释`、`CLIPTextEncode`、`solarL_SaveImagesToZip`、`JjkText`、`LoraLoaderModelOnly`

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

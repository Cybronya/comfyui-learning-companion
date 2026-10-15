---
key: 图片生成/文生图/千问qwen image 2.1文生图工作流 高质量画面直出_2104994907697012737.json
name: 千问qwen image 2.1文生图工作流 高质量画面直出_2104994907697012737
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/千问qwen image 2.1文生图工作流 高质量画面直出_2104994907697012737.json
hash: 0971fec42e8dd160
coverage: 0.880952
learned_at: 2026-10-10 20:59:38
nodes: [ConditioningZeroOut, VAEDecode, SaveImage, UNETLoader, EmptyLatentImage, PreviewImage, CLIPLoader, KSampler, CLIPTextEncode, VAELoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, 孤海注释, 孤海注释, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, KSampler, EmptyLatentImage, JjkText, CLIPTextEncode, CLIPTextEncode, solarL_SaveImagesToZip, VAEDecode, CLIPLoader, VAELoader, Note]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/文生图/千问qwen image 2.1文生图工作流 高质量画面直出_2104994907697012737.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/千问qwen image 2.1文生图工作流 高质量画面直出_2104994907697012737.json`

## 结构

**节点**（42 个）：
- `ConditioningZeroOut`
- `VAEDecode`
- `SaveImage`
- `UNETLoader`
- `EmptyLatentImage`
- `PreviewImage`
- `CLIPLoader`
- `KSampler`
- `CLIPTextEncode`
- `VAELoader`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
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

覆盖率 **88%**（37/42）

**有卡**：`ConditioningZeroOut`、`VAEDecode`、`SaveImage`、`UNETLoader`、`EmptyLatentImage`、`PreviewImage`、`CLIPLoader`、`KSampler`、`CLIPTextEncode`、`VAELoader`、`LoraLoaderModelOnly`、`孤海注释`、`JjkText`

## 参数体检

发现 2 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

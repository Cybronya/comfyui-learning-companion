---
key: 图片生成/文生图/Qwen Image 2.1文生图加4步加速，高质量文本到图像生成工作流_2103932568507863042.json
name: Qwen Image 2.1文生图加4步加速，高质量文本到图像生成工作流_2103932568507863042
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Qwen Image 2.1文生图加4步加速，高质量文本到图像生成工作流_2103932568507863042.json
hash: 0b3dc807e5f455d0
coverage: 0.880952
learned_at: 2026-10-10 20:58:53
nodes: [VAELoader, ConditioningZeroOut, ModelAttentionBackend, CLIPLoader, KSampler, CLIPTextEncode, PreviewImage, LoraLoaderModelOnly, UNETLoader, EmptyLatentImage, SaveImageAdvanced, VAEDecode, SaveImage, 孤海注释, 孤海注释, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, KSampler, EmptyLatentImage, JjkText, CLIPTextEncode, CLIPTextEncode, solarL_SaveImagesToZip, VAEDecode, CLIPLoader, VAELoader, Note]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/文生图/Qwen Image 2.1文生图加4步加速，高质量文本到图像生成工作流_2103932568507863042.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Qwen Image 2.1文生图加4步加速，高质量文本到图像生成工作流_2103932568507863042.json`

## 结构

**节点**（42 个）：
- `VAELoader`
- `ConditioningZeroOut`
- `ModelAttentionBackend`
- `CLIPLoader`
- `KSampler`
- `CLIPTextEncode`
- `PreviewImage`
- `LoraLoaderModelOnly`
- `UNETLoader`
- `EmptyLatentImage`
- `SaveImageAdvanced`
- `VAEDecode`
- `SaveImage`
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

**有卡**：`VAELoader`、`ConditioningZeroOut`、`ModelAttentionBackend`、`CLIPLoader`、`KSampler`、`CLIPTextEncode`、`PreviewImage`、`LoraLoaderModelOnly`、`UNETLoader`、`EmptyLatentImage`、`SaveImageAdvanced`、`VAEDecode`、`SaveImage`、`孤海注释`、`JjkText`

## 参数体检

发现 2 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

---
key: 图片生成/图生图/LH-DMT版本-2.生图片类-048.Qwen一致性多角度写真摄影_2016524960361095169.json
name: LH-DMT版本-2.生图片类-048.Qwen一致性多角度写真摄影_2016524960361095169
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/LH-DMT版本-2.生图片类-048.Qwen一致性多角度写真摄影_2016524960361095169.json
hash: 4abaf5c9081adf64
coverage: 0.666667
learned_at: 2026-10-23 11:08:42
nodes: [Note, Note, TextEncodeQwenImageEditPlus, ModelSamplingAuraFlow, ImageScaleToTotalPixels, CLIPLoader, VAELoader, GetImageSize, CLIPTextEncode, EmptyLatentImage, PreviewImage, SaveImageKJ, MarkdownNote, PrimitiveString, PrimitiveString, Note, Note, easy promptLine, LoraLoaderModelOnly, UnetLoaderGGUF, KSampler, Note, LoraLoaderModelOnly, easy promptList, LoadImage, VAEDecode, SaveImage]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 512, "sampler_name": "euler", "scheduler": "beta", "seed": 37370598107871, "steps": 4, "width": 512}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/LH-DMT版本-2.生图片类-048.Qwen一致性多角度写真摄影_2016524960361095169.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/LH-DMT版本-2.生图片类-048.Qwen一致性多角度写真摄影_2016524960361095169.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（27 个）：
- `Note`
- `Note`
- `TextEncodeQwenImageEditPlus`
- `ModelSamplingAuraFlow`
- `ImageScaleToTotalPixels`
- `CLIPLoader`
- `VAELoader`
- `GetImageSize`
- `CLIPTextEncode` ★核心
- `EmptyLatentImage` ★核心
- `PreviewImage`
- `SaveImageKJ`
- `MarkdownNote`
- `PrimitiveString`
- `PrimitiveString`
- `Note`
- `Note`
- `easy promptLine`
- `LoraLoaderModelOnly` ★核心
- `UnetLoaderGGUF` ★核心
- `KSampler` ★核心
- `Note`
- `LoraLoaderModelOnly` ★核心
- `easy promptList`
- `LoadImage`
- `VAEDecode` ★核心
- `SaveImage`

**识别到的模式**：text_to_image

## 关键参数

- `width` = `512`
- `height` = `512`
- `batch_size` = `1`
- `seed` = `37370598107871`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `beta`
- `denoise` = `1`

## 知识

覆盖率 **67%**（18/27）

**有卡**：`TextEncodeQwenImageEditPlus`、`ModelSamplingAuraFlow`、`ImageScaleToTotalPixels`、`CLIPLoader`、`VAELoader`、`GetImageSize`、`CLIPTextEncode`、`EmptyLatentImage`、`SaveImageKJ`、`easy promptLine`、`LoraLoaderModelOnly`、`UnetLoaderGGUF`、`KSampler`、`easy promptList`、`LoadImage`、`VAEDecode`、`SaveImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage、LoadImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

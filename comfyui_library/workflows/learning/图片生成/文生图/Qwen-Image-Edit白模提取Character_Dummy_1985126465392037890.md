---
key: 图片生成/文生图/Qwen-Image-Edit白模提取Character_Dummy_1985126465392037890.json
name: Qwen-Image-Edit白模提取Character_Dummy_1985126465392037890.json
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Qwen-Image-Edit白模提取Character_Dummy_1985126465392037890.json
hash: 31bcfc723c6ed3b9
coverage: 0.782609
learned_at: 2026-10-09 20:13:10
nodes: [CFGNorm, KSampler, EmptySD3LatentImage, MarkdownNote, MarkdownNote, CLIPLoader, ImageConcatMulti, VAEDecode, ModelSamplingAuraFlow, TextEncodeQwenImageEditPlus, VAEEncode, ImageScaleToTotalPixels, MarkdownNote, MarkdownNote, SaveImage, SaveImage, TextEncodeQwenImageEditPlus, MarkdownNote, VAELoader, LoraLoaderModelOnly, UNETLoader, LoraLoaderModelOnly, LoadImage]
patterns: [image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 107383467143834, "steps": 4}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/文生图/Qwen-Image-Edit白模提取Character_Dummy_1985126465392037890.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/1985126465392037890.json`

## 结构

**生成流程**：Model → Encode → Sampling → Decode → Process → Output → Other

**节点**（23 个）：
- `CFGNorm`
- `KSampler` ★核心
- `EmptySD3LatentImage`
- `MarkdownNote`
- `MarkdownNote`
- `CLIPLoader`
- `ImageConcatMulti`
- `VAEDecode` ★核心
- `ModelSamplingAuraFlow`
- `TextEncodeQwenImageEditPlus`
- `VAEEncode` ★核心
- `ImageScaleToTotalPixels`
- `MarkdownNote`
- `MarkdownNote`
- `SaveImage`
- `SaveImage`
- `TextEncodeQwenImageEditPlus`
- `MarkdownNote`
- `VAELoader`
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoadImage`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `107383467143834`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **78%**（18/23）

**有卡**：`CFGNorm`、`KSampler`、`EmptySD3LatentImage`、`CLIPLoader`、`ImageConcatMulti`、`VAEDecode`、`ModelSamplingAuraFlow`、`TextEncodeQwenImageEditPlus`、`VAEEncode`、`ImageScaleToTotalPixels`、`SaveImage`、`VAELoader`、`LoraLoaderModelOnly`、`UNETLoader`、`LoadImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、LoadImage、UNETLoader、CFGNorm

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

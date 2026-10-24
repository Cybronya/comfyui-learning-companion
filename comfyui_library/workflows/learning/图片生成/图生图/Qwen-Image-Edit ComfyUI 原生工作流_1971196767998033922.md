---
key: 图片生成/图生图/Qwen-Image-Edit ComfyUI 原生工作流_1971196767998033922.json
name: Qwen-Image-Edit ComfyUI 原生工作流_1971196767998033922
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen-Image-Edit ComfyUI 原生工作流_1971196767998033922.json
hash: 4581f86bfccef7df
coverage: 0.694915
learned_at: 2026-10-23 11:16:44
nodes: [ModelSamplingAuraFlow, CFGNorm, CLIPLoader, VAEDecode, Image Comparer (rgthree), UNETLoader, MarkdownNote, LoadImage, Note, LoadImage, LoadImage, Note, Note, LoadImage, LoadImage, LoadImage, LoadImage, VAELoader, LoadImage, Note, LoadImage, LoadImage, Reroute, VAEEncode, VAEEncode, ReferenceLatent, LoadImage, LoadImage, Note, ReferenceLatent, ReferenceLatent, Note, LoadImage, Note, LoadImage, SaveImage, LoadImage, Note, LoadImage, Note, LoadImage, Note, LoadImage, Note, Note, LoadImage, ConditioningZeroOut, LoadImage, Note, Note, LoadImage, LoraLoaderModelOnly, LoraLoaderModelOnly, EmptyLatentImage, KSampler, VAEEncode, LoadImage, Note, TextEncodeQwenImageEditPlus]
patterns: [image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 768, "sampler_name": "euler", "scheduler": "simple", "seed": 591965062546751, "steps": 8, "width": 1680}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/Qwen-Image-Edit ComfyUI 原生工作流_1971196767998033922.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen-Image-Edit ComfyUI 原生工作流_1971196767998033922.json`

## 结构

**生成流程**：Model → Encode → Condition → Latent → Sampling → Decode → Output → Other

**节点**（59 个）：
- `ModelSamplingAuraFlow`
- `CFGNorm`
- `CLIPLoader`
- `VAEDecode` ★核心
- `Image Comparer (rgthree)`
- `UNETLoader` ★核心
- `MarkdownNote`
- `LoadImage`
- `Note`
- `LoadImage`
- `LoadImage`
- `Note`
- `Note`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `VAELoader`
- `LoadImage`
- `Note`
- `LoadImage`
- `LoadImage`
- `Reroute`
- `VAEEncode` ★核心
- `VAEEncode` ★核心
- `ReferenceLatent`
- `LoadImage`
- `LoadImage`
- `Note`
- `ReferenceLatent`
- `ReferenceLatent`
- `Note`
- `LoadImage`
- `Note`
- `LoadImage`
- `SaveImage`
- `LoadImage`
- `Note`
- `LoadImage`
- `Note`
- `LoadImage`
- `Note`
- `LoadImage`
- `Note`
- `Note`
- `LoadImage`
- `ConditioningZeroOut`
- `LoadImage`
- `Note`
- `Note`
- `LoadImage`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `EmptyLatentImage` ★核心
- `KSampler` ★核心
- `VAEEncode` ★核心
- `LoadImage`
- `Note`
- `TextEncodeQwenImageEditPlus`

**识别到的模式**：image_to_image

## 关键参数

- `width` = `1680`
- `height` = `768`
- `batch_size` = `1`
- `seed` = `591965062546751`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **69%**（41/59）

**有卡**：`ModelSamplingAuraFlow`、`CFGNorm`、`CLIPLoader`、`VAEDecode`、`UNETLoader`、`LoadImage`、`VAELoader`、`VAEEncode`、`ReferenceLatent`、`SaveImage`、`ConditioningZeroOut`、`LoraLoaderModelOnly`、`EmptyLatentImage`、`KSampler`、`TextEncodeQwenImageEditPlus`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、ConditioningZeroOut、EmptyLatentImage、LoadImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

---
key: 图片生成/图生图/Qwen Image Uinon ControlNet  lora（多合一）之 canny 工作流_1959598906571173889.json
name: Qwen Image Uinon ControlNet  lora（多合一）之 canny 工作流_1959598906571173889
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen Image Uinon ControlNet  lora（多合一）之 canny 工作流_1959598906571173889.json
hash: 884138f9c68c1833
coverage: 0.818182
learned_at: 2026-10-23 11:13:25
nodes: [CLIPTextEncode, Canny, ReferenceLatent, ReferenceLatent, VAEEncode, VAELoader, CLIPLoader, UNETLoader, ImageScaleToTotalPixels, MarkdownNote, MarkdownNote, ModelSamplingAuraFlow, VAEDecode, CLIPTextEncode, LoraLoaderModelOnly, LoraLoaderModelOnly, KSampler, PreviewImage, SaveImage, LoadImage, MarkdownNote, LoadImage]
patterns: [image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 1116105422743117, "steps": 4}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/Qwen Image Uinon ControlNet  lora（多合一）之 canny 工作流_1959598906571173889.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen Image Uinon ControlNet  lora（多合一）之 canny 工作流_1959598906571173889.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（22 个）：
- `CLIPTextEncode` ★核心
- `Canny`
- `ReferenceLatent`
- `ReferenceLatent`
- `VAEEncode` ★核心
- `VAELoader`
- `CLIPLoader`
- `UNETLoader` ★核心
- `ImageScaleToTotalPixels`
- `MarkdownNote`
- `MarkdownNote`
- `ModelSamplingAuraFlow`
- `VAEDecode` ★核心
- `CLIPTextEncode` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `KSampler` ★核心
- `PreviewImage`
- `SaveImage`
- `LoadImage`
- `MarkdownNote`
- `LoadImage`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `1116105422743117`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **82%**（18/22）

**有卡**：`CLIPTextEncode`、`Canny`、`ReferenceLatent`、`VAEEncode`、`VAELoader`、`CLIPLoader`、`UNETLoader`、`ImageScaleToTotalPixels`、`ModelSamplingAuraFlow`、`VAEDecode`、`LoraLoaderModelOnly`、`KSampler`、`SaveImage`、`LoadImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

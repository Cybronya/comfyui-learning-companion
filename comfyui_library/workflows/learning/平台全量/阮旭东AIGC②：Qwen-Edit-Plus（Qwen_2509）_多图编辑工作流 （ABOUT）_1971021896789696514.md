---
key: 平台全量/阮旭东AIGC②：Qwen-Edit-Plus（Qwen_2509）_多图编辑工作流 （ABOUT）_1971021896789696514.json
name: 阮旭东AIGC②：Qwen-Edit-Plus（Qwen_2509）_多图编辑工作流 （ABOUT）_1971021896789696514
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/平台全量/阮旭东AIGC②：Qwen-Edit-Plus（Qwen_2509）_多图编辑工作流 （ABOUT）_1971021896789696514.json
hash: 22eb44a9ef4c4510
coverage: 0.833333
learned_at: 2026-11-14 02:49:32
nodes: [CLIPLoader, VAELoader, ModelSamplingAuraFlow, TextEncodeQwenImageEditPlus, ConditioningZeroOut, UNETLoader, VAEDecode, LoraLoaderModelOnly, CFGNorm, ImageScaleToTotalPixels, ImageScaleToTotalPixels, ImageScaleToTotalPixels, KSampler, LoadImage, VAEEncode, SDXLEmptyLatentSizePicker+, Switch, MarkdownNote, LoadImage, LoadImage, MarkdownNote, ImageConcatMulti, ImageConcatMulti, SaveImage, SaveImage, LoadImage, LoadImage, PrimitiveStringMultiline, MarkdownNote, MarkdownNote]
patterns: [image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 0, "cfg": 1, "denoise": 1, "height": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 76002914723630, "steps": 4, "width": "832x1216 (0.68)"}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 平台全量/阮旭东AIGC②：Qwen-Edit-Plus（Qwen_2509）_多图编辑工作流 （ABOUT）_1971021896789696514.json

> 来源文件 `comfyui_library/workflows/平台全量/阮旭东AIGC②：Qwen-Edit-Plus（Qwen_2509）_多图编辑工作流 （ABOUT）_1971021896789696514.json`

## 结构

**生成流程**：Model → Encode → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（30 个）：
- `CLIPLoader`
- `VAELoader`
- `ModelSamplingAuraFlow`
- `TextEncodeQwenImageEditPlus`
- `ConditioningZeroOut`
- `UNETLoader` ★核心
- `VAEDecode` ★核心
- `LoraLoaderModelOnly` ★核心
- `CFGNorm`
- `ImageScaleToTotalPixels`
- `ImageScaleToTotalPixels`
- `ImageScaleToTotalPixels`
- `KSampler` ★核心
- `LoadImage`
- `VAEEncode` ★核心
- `SDXLEmptyLatentSizePicker+` ★核心
- `Switch`
- `MarkdownNote`
- `LoadImage`
- `LoadImage`
- `MarkdownNote`
- `ImageConcatMulti`
- `ImageConcatMulti`
- `SaveImage`
- `SaveImage`
- `LoadImage`
- `LoadImage`
- `PrimitiveStringMultiline`
- `MarkdownNote`
- `MarkdownNote`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `76002914723630`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`
- `width` = `832x1216 (0.68)`
- `height` = `1`
- `batch_size` = `0`

## 知识

覆盖率 **83%**（25/30）

**有卡**：`CLIPLoader`、`VAELoader`、`ModelSamplingAuraFlow`、`TextEncodeQwenImageEditPlus`、`ConditioningZeroOut`、`UNETLoader`、`VAEDecode`、`LoraLoaderModelOnly`、`CFGNorm`、`ImageScaleToTotalPixels`、`KSampler`、`LoadImage`、`VAEEncode`、`SDXLEmptyLatentSizePicker+`、`Switch`、`ImageConcatMulti`、`SaveImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPLoader、ConditioningZeroOut、LoadImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

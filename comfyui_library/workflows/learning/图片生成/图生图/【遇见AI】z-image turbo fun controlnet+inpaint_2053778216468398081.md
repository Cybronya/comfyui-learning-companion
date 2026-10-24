---
key: 图片生成/图生图/【遇见AI】z-image turbo fun controlnet+inpaint_2053778216468398081.json
name: 【遇见AI】z-image turbo fun controlnet+inpaint_2053778216468398081
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/【遇见AI】z-image turbo fun controlnet+inpaint_2053778216468398081.json
hash: 76d50d01382c155a
coverage: 0.833333
learned_at: 2026-10-23 11:52:29
nodes: [KSampler, EmptyLatentImage, VAEDecode, ZImageFunControlnet, Note, PreviewImage, SaveImage, LoadImage, AIO_Preprocessor, LoadImage, MarkdownNote, ConditioningZeroOut, CLIPTextEncode, LoadImage, UNETLoader, CLIPLoader, VAELoader, ModelPatchLoader]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 768, "sampler_name": "euler", "scheduler": "simple", "seed": 745033083450687, "steps": 8, "width": 512}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/【遇见AI】z-image turbo fun controlnet+inpaint_2053778216468398081.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/【遇见AI】z-image turbo fun controlnet+inpaint_2053778216468398081.json`

## 结构

**生成流程**：Model → Condition → Latent → Control → Sampling → Decode → Output → Other

**节点**（18 个）：
- `KSampler` ★核心
- `EmptyLatentImage` ★核心
- `VAEDecode` ★核心
- `ZImageFunControlnet`
- `Note`
- `PreviewImage`
- `SaveImage`
- `LoadImage`
- `AIO_Preprocessor`
- `LoadImage`
- `MarkdownNote`
- `ConditioningZeroOut`
- `CLIPTextEncode` ★核心
- `LoadImage`
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `ModelPatchLoader`

**识别到的模式**：text_to_image

## 关键参数

- `seed` = `745033083450687`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`
- `width` = `512`
- `height` = `768`
- `batch_size` = `1`

## 知识

覆盖率 **83%**（15/18）

**有卡**：`KSampler`、`EmptyLatentImage`、`VAEDecode`、`ZImageFunControlnet`、`SaveImage`、`LoadImage`、`AIO_Preprocessor`、`ConditioningZeroOut`、`CLIPTextEncode`、`UNETLoader`、`CLIPLoader`、`VAELoader`、`ModelPatchLoader`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、EmptyLatentImage、LoadImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

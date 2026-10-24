---
key: 图片生成/图生图/【遇见AI】z-image fun controlnet_2053781769182294018.json
name: 【遇见AI】z-image fun controlnet_2053781769182294018
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/【遇见AI】z-image fun controlnet_2053781769182294018.json
hash: f92e2771b1e1f6bf
coverage: 0.833333
learned_at: 2026-10-23 11:52:28
nodes: [EmptyLatentImage, VAEDecode, Note, PreviewImage, SaveImage, KSampler, AIO_Preprocessor, LoadImage, CLIPTextEncode, ZImageFunControlnet, CLIPTextEncode, LoadImage, MarkdownNote, LoadImage, CLIPLoader, VAELoader, ModelPatchLoader, UNETLoader]
patterns: [text_to_image]
missing: []
parameters: {"batch_size": 1, "cfg": 4, "denoise": 1, "height": 768, "sampler_name": "euler", "scheduler": "simple", "seed": 757391661074133, "steps": 28, "width": 512}
---

# 图片生成/图生图/【遇见AI】z-image fun controlnet_2053781769182294018.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/【遇见AI】z-image fun controlnet_2053781769182294018.json`

## 结构

**生成流程**：Model → Condition → Latent → Control → Sampling → Decode → Output → Other

**节点**（18 个）：
- `EmptyLatentImage` ★核心
- `VAEDecode` ★核心
- `Note`
- `PreviewImage`
- `SaveImage`
- `KSampler` ★核心
- `AIO_Preprocessor`
- `LoadImage`
- `CLIPTextEncode` ★核心
- `ZImageFunControlnet`
- `CLIPTextEncode` ★核心
- `LoadImage`
- `MarkdownNote`
- `LoadImage`
- `CLIPLoader`
- `VAELoader`
- `ModelPatchLoader`
- `UNETLoader` ★核心

**识别到的模式**：text_to_image

## 关键参数

- `width` = `512`
- `height` = `768`
- `batch_size` = `1`
- `seed` = `757391661074133`
- `steps` = `28`
- `cfg` = `4`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **83%**（15/18）

**有卡**：`EmptyLatentImage`、`VAEDecode`、`SaveImage`、`KSampler`、`AIO_Preprocessor`、`LoadImage`、`CLIPTextEncode`、`ZImageFunControlnet`、`CLIPLoader`、`VAELoader`、`ModelPatchLoader`、`UNETLoader`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、EmptyLatentImage、LoadImage、UNETLoader

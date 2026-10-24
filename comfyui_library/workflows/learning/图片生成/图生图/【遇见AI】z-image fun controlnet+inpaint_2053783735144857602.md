---
key: 图片生成/图生图/【遇见AI】z-image fun controlnet+inpaint_2053783735144857602.json
name: 【遇见AI】z-image fun controlnet+inpaint_2053783735144857602
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/【遇见AI】z-image fun controlnet+inpaint_2053783735144857602.json
hash: 2129ac5a21aadadf
coverage: 0.833333
learned_at: 2026-10-23 11:52:27
nodes: [VAEDecode, ZImageFunControlnet, Note, PreviewImage, SaveImage, AIO_Preprocessor, KSampler, LoadImage, LoadImage, MarkdownNote, LoadImage, CLIPLoader, VAELoader, EmptyLatentImage, CLIPTextEncode, UNETLoader, ModelPatchLoader, CLIPTextEncode]
patterns: [text_to_image]
missing: []
parameters: {"batch_size": 1, "cfg": 4, "denoise": 1, "height": 768, "sampler_name": "euler", "scheduler": "simple", "seed": 1040618850697003, "steps": 28, "width": 512}
---

# 图片生成/图生图/【遇见AI】z-image fun controlnet+inpaint_2053783735144857602.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/【遇见AI】z-image fun controlnet+inpaint_2053783735144857602.json`

## 结构

**生成流程**：Model → Condition → Latent → Control → Sampling → Decode → Output → Other

**节点**（18 个）：
- `VAEDecode` ★核心
- `ZImageFunControlnet`
- `Note`
- `PreviewImage`
- `SaveImage`
- `AIO_Preprocessor`
- `KSampler` ★核心
- `LoadImage`
- `LoadImage`
- `MarkdownNote`
- `LoadImage`
- `CLIPLoader`
- `VAELoader`
- `EmptyLatentImage` ★核心
- `CLIPTextEncode` ★核心
- `UNETLoader` ★核心
- `ModelPatchLoader`
- `CLIPTextEncode` ★核心

**识别到的模式**：text_to_image

## 关键参数

- `seed` = `1040618850697003`
- `steps` = `28`
- `cfg` = `4`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`
- `width` = `512`
- `height` = `768`
- `batch_size` = `1`

## 知识

覆盖率 **83%**（15/18）

**有卡**：`VAEDecode`、`ZImageFunControlnet`、`SaveImage`、`AIO_Preprocessor`、`KSampler`、`LoadImage`、`CLIPLoader`、`VAELoader`、`EmptyLatentImage`、`CLIPTextEncode`、`UNETLoader`、`ModelPatchLoader`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、EmptyLatentImage、LoadImage、UNETLoader

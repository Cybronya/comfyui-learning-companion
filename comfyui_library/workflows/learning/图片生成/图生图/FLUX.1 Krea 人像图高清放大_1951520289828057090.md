---
key: 图片生成/图生图/FLUX.1 Krea 人像图高清放大_1951520289828057090.json
name: FLUX.1 Krea 人像图高清放大_1951520289828057090
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/FLUX.1 Krea 人像图高清放大_1951520289828057090.json
hash: f3bb7b1522bfe780
coverage: 0.952381
learned_at: 2026-10-23 10:54:01
nodes: [ControlNetApplyAdvanced, CLIPTextEncode, ImageResize+, EmptyLatentImage, GetImageSize+, MathExpression|pysssss, CLIPTextEncode, ConditioningZeroOut, FluxGuidance, MathExpression|pysssss, Florence2Run, VAELoader, VAEDecode, KSampler, Image Comparer (rgthree), SaveImage, LoadImage, ControlNetLoader, UNETLoader, DualCLIPLoader, Florence2ModelLoader]
patterns: [text_to_image]
missing: []
parameters: {"batch_size": 1, "cfg": 1, "controlnet_strength": 0.8, "denoise": 1, "height": 1344, "sampler_name": "euler", "scheduler": "simple", "seed": 133821100340126, "steps": 20, "width": 1024}
---

# 图片生成/图生图/FLUX.1 Krea 人像图高清放大_1951520289828057090.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/FLUX.1 Krea 人像图高清放大_1951520289828057090.json`

## 结构

**生成流程**：Model → Condition → Latent → Control → Sampling → Decode → Process → Output → Other

**节点**（21 个）：
- `ControlNetApplyAdvanced` ★核心
- `CLIPTextEncode` ★核心
- `ImageResize+`
- `EmptyLatentImage` ★核心
- `GetImageSize+`
- `MathExpression|pysssss`
- `CLIPTextEncode` ★核心
- `ConditioningZeroOut`
- `FluxGuidance`
- `MathExpression|pysssss`
- `Florence2Run`
- `VAELoader`
- `VAEDecode` ★核心
- `KSampler` ★核心
- `Image Comparer (rgthree)`
- `SaveImage`
- `LoadImage`
- `ControlNetLoader`
- `UNETLoader` ★核心
- `DualCLIPLoader`
- `Florence2ModelLoader`

**识别到的模式**：text_to_image

## 关键参数

- `controlnet_strength` = `0.8`
- `width` = `1024`
- `height` = `1344`
- `batch_size` = `1`
- `seed` = `133821100340126`
- `steps` = `20`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **95%**（20/21）

**有卡**：`ControlNetApplyAdvanced`、`CLIPTextEncode`、`ImageResize+`、`EmptyLatentImage`、`GetImageSize+`、`MathExpression|pysssss`、`ConditioningZeroOut`、`FluxGuidance`、`Florence2Run`、`VAELoader`、`VAEDecode`、`KSampler`、`SaveImage`、`LoadImage`、`ControlNetLoader`、`UNETLoader`、`DualCLIPLoader`、`Florence2ModelLoader`

**用到的条目**：KSampler、VAEDecode、VAELoader、UNETLoader、CLIPTextEncode、ConditioningZeroOut、EmptyLatentImage、LoadImage

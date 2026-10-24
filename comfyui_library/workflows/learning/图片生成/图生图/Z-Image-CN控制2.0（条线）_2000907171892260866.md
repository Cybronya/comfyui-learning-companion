---
key: 图片生成/图生图/Z-Image-CN控制2.0（条线）_2000907171892260866.json
name: Z-Image-CN控制2.0（条线）_2000907171892260866
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Z-Image-CN控制2.0（条线）_2000907171892260866.json
hash: f0be02a404ab1257
coverage: 0.933333
learned_at: 2026-10-23 11:29:33
nodes: [CLIPLoader, UNETLoader, VAELoader, SaveImage, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, CLIPTextEncode, AIO_Preprocessor, ModelPatchLoader, QwenImageDiffsynthControlnet, EmptyLatentImage, PreviewImage, CLIPTextEncode, KSampler, VAEDecode]
patterns: [text_to_image]
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1280, "sampler_name": "euler", "scheduler": "simple", "seed": 691698995930672, "steps": 10, "width": 720}
---

# 图片生成/图生图/Z-Image-CN控制2.0（条线）_2000907171892260866.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Z-Image-CN控制2.0（条线）_2000907171892260866.json`

## 结构

**生成流程**：Model → Condition → Latent → Control → Sampling → Decode → Process → Output → Other

**节点**（15 个）：
- `CLIPLoader`
- `UNETLoader` ★核心
- `VAELoader`
- `SaveImage`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `CLIPTextEncode` ★核心
- `AIO_Preprocessor`
- `ModelPatchLoader`
- `QwenImageDiffsynthControlnet`
- `EmptyLatentImage` ★核心
- `PreviewImage`
- `CLIPTextEncode` ★核心
- `KSampler` ★核心
- `VAEDecode` ★核心

**识别到的模式**：text_to_image

## 关键参数

- `width` = `720`
- `height` = `1280`
- `batch_size` = `1`
- `seed` = `691698995930672`
- `steps` = `10`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **93%**（14/15）

**有卡**：`CLIPLoader`、`UNETLoader`、`VAELoader`、`SaveImage`、`LayerUtility: ImageScaleByAspectRatio V2`、`LoadImage`、`CLIPTextEncode`、`AIO_Preprocessor`、`ModelPatchLoader`、`QwenImageDiffsynthControlnet`、`EmptyLatentImage`、`KSampler`、`VAEDecode`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、EmptyLatentImage、LoadImage、UNETLoader

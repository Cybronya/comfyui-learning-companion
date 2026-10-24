---
key: 图片生成/图生图/Z-Image-CN控制（2.1）_2001999689794875393.json
name: Z-Image-CN控制（2.1）_2001999689794875393
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Z-Image-CN控制（2.1）_2001999689794875393.json
hash: 570c971882224a3d
coverage: 0.933333
learned_at: 2026-10-23 11:29:35
nodes: [CLIPLoader, VAEDecode, UNETLoader, VAELoader, SaveImage, EmptyLatentImage, KSampler, ModelPatchLoader, QwenImageDiffsynthControlnet, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, CLIPTextEncode, CLIPTextEncode, AIO_Preprocessor, PreviewImage]
patterns: [text_to_image]
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1280, "sampler_name": "euler", "scheduler": "simple", "seed": 732717027370709, "steps": 10, "width": 720}
---

# 图片生成/图生图/Z-Image-CN控制（2.1）_2001999689794875393.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Z-Image-CN控制（2.1）_2001999689794875393.json`

## 结构

**生成流程**：Model → Condition → Latent → Control → Sampling → Decode → Process → Output → Other

**节点**（15 个）：
- `CLIPLoader`
- `VAEDecode` ★核心
- `UNETLoader` ★核心
- `VAELoader`
- `SaveImage`
- `EmptyLatentImage` ★核心
- `KSampler` ★核心
- `ModelPatchLoader`
- `QwenImageDiffsynthControlnet`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `AIO_Preprocessor`
- `PreviewImage`

**识别到的模式**：text_to_image

## 关键参数

- `width` = `720`
- `height` = `1280`
- `batch_size` = `1`
- `seed` = `732717027370709`
- `steps` = `10`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **93%**（14/15）

**有卡**：`CLIPLoader`、`VAEDecode`、`UNETLoader`、`VAELoader`、`SaveImage`、`EmptyLatentImage`、`KSampler`、`ModelPatchLoader`、`QwenImageDiffsynthControlnet`、`LayerUtility: ImageScaleByAspectRatio V2`、`LoadImage`、`CLIPTextEncode`、`AIO_Preprocessor`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、EmptyLatentImage、LoadImage、UNETLoader

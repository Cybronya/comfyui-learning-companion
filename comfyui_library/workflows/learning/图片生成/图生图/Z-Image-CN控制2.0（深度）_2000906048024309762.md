---
key: 图片生成/图生图/Z-Image-CN控制2.0（深度）_2000906048024309762.json
name: Z-Image-CN控制2.0（深度）_2000906048024309762
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Z-Image-CN控制2.0（深度）_2000906048024309762.json
hash: 3d9d92a04866cb86
coverage: 0.933333
learned_at: 2026-10-23 11:29:33
nodes: [CLIPLoader, VAEDecode, UNETLoader, VAELoader, PreviewImage, SaveImage, LayerUtility: ImageScaleByAspectRatio V2, CLIPTextEncode, LoadImage, KSampler, ModelPatchLoader, EmptyLatentImage, CLIPTextEncode, AIO_Preprocessor, QwenImageDiffsynthControlnet]
patterns: [text_to_image]
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1280, "sampler_name": "euler", "scheduler": "simple", "seed": 526537047405043, "steps": 10, "width": 720}
---

# 图片生成/图生图/Z-Image-CN控制2.0（深度）_2000906048024309762.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Z-Image-CN控制2.0（深度）_2000906048024309762.json`

## 结构

**生成流程**：Model → Condition → Latent → Control → Sampling → Decode → Process → Output → Other

**节点**（15 个）：
- `CLIPLoader`
- `VAEDecode` ★核心
- `UNETLoader` ★核心
- `VAELoader`
- `PreviewImage`
- `SaveImage`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `CLIPTextEncode` ★核心
- `LoadImage`
- `KSampler` ★核心
- `ModelPatchLoader`
- `EmptyLatentImage` ★核心
- `CLIPTextEncode` ★核心
- `AIO_Preprocessor`
- `QwenImageDiffsynthControlnet`

**识别到的模式**：text_to_image

## 关键参数

- `seed` = `526537047405043`
- `steps` = `10`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`
- `width` = `720`
- `height` = `1280`
- `batch_size` = `1`

## 知识

覆盖率 **93%**（14/15）

**有卡**：`CLIPLoader`、`VAEDecode`、`UNETLoader`、`VAELoader`、`SaveImage`、`LayerUtility: ImageScaleByAspectRatio V2`、`CLIPTextEncode`、`LoadImage`、`KSampler`、`ModelPatchLoader`、`EmptyLatentImage`、`AIO_Preprocessor`、`QwenImageDiffsynthControlnet`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、EmptyLatentImage、LoadImage、UNETLoader

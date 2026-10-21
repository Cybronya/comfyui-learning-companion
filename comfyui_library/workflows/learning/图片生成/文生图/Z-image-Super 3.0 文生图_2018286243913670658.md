---
key: 图片生成/文生图/Z-image-Super 3.0 文生图_2018286243913670658.json
name: Z-image-Super 3.0 文生图_2018286243913670658
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Z-image-Super 3.0 文生图_2018286243913670658.json
hash: 1a43206a4ea5d6c0
coverage: 0.8
learned_at: 2026-10-19 22:30:03
nodes: [EmptyLatentImage, UNETLoader, PrimitiveNode, PrimitiveInt, PrimitiveInt, CLIPTextEncode, CLIPLoader, VAELoader, KSampler, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SaveImage, SeedVR2VideoUpscaler, LayerUtility: PurgeVRAM, VAEDecode, ImageScaleBy, Image Comparer (rgthree), CLIPTextEncode, SaveImage, CR Prompt Text]
patterns: [text_to_image]
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1920, "sampler_name": "euler", "scheduler": "simple", "seed": 369972456881499, "steps": 15, "width": 1080}
---

# 图片生成/文生图/Z-image-Super 3.0 文生图_2018286243913670658.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Z-image-Super 3.0 文生图_2018286243913670658.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（20 个）：
- `EmptyLatentImage` ★核心
- `UNETLoader` ★核心
- `PrimitiveNode`
- `PrimitiveInt`
- `PrimitiveInt`
- `CLIPTextEncode` ★核心
- `CLIPLoader`
- `VAELoader`
- `KSampler` ★核心
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SaveImage`
- `SeedVR2VideoUpscaler`
- `LayerUtility: PurgeVRAM`
- `VAEDecode` ★核心
- `ImageScaleBy`
- `Image Comparer (rgthree)`
- `CLIPTextEncode` ★核心
- `SaveImage`
- `CR Prompt Text`

**识别到的模式**：text_to_image

## 关键参数

- `width` = `1080`
- `height` = `1920`
- `batch_size` = `1`
- `seed` = `369972456881499`
- `steps` = `15`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **80%**（16/20）

**有卡**：`EmptyLatentImage`、`UNETLoader`、`CLIPTextEncode`、`CLIPLoader`、`VAELoader`、`KSampler`、`SeedVR2LoadDiTModel`、`SeedVR2LoadVAEModel`、`SaveImage`、`SeedVR2VideoUpscaler`、`LayerUtility: PurgeVRAM`、`VAEDecode`、`ImageScaleBy`、`CR Prompt Text`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、EmptyLatentImage、UNETLoader、SeedVR2LoadDiTModel

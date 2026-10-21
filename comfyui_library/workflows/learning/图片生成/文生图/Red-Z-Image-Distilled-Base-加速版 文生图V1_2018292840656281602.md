---
key: 图片生成/文生图/Red-Z-Image-Distilled-Base-加速版 文生图V1_2018292840656281602.json
name: Red-Z-Image-Distilled-Base-加速版 文生图V1_2018292840656281602
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Red-Z-Image-Distilled-Base-加速版 文生图V1_2018292840656281602.json
hash: 9dcd93b60b7f406b
coverage: 0.8
learned_at: 2026-10-19 22:29:51
nodes: [PrimitiveNode, CLIPTextEncode, EmptyLatentImage, CLIPTextEncode, KSampler, VAEDecode, LayerUtility: PurgeVRAM, SaveImage, PrimitiveInt, PrimitiveInt, ImageScaleBy, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, SaveImage, Image Comparer (rgthree), CLIPLoader, VAELoader, UNETLoader, CR Prompt Text]
patterns: [text_to_image]
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1920, "sampler_name": "euler", "scheduler": "simple", "seed": 843634065030824, "steps": 15, "width": 1080}
---

# 图片生成/文生图/Red-Z-Image-Distilled-Base-加速版 文生图V1_2018292840656281602.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Red-Z-Image-Distilled-Base-加速版 文生图V1_2018292840656281602.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（20 个）：
- `PrimitiveNode`
- `CLIPTextEncode` ★核心
- `EmptyLatentImage` ★核心
- `CLIPTextEncode` ★核心
- `KSampler` ★核心
- `VAEDecode` ★核心
- `LayerUtility: PurgeVRAM`
- `SaveImage`
- `PrimitiveInt`
- `PrimitiveInt`
- `ImageScaleBy`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `SaveImage`
- `Image Comparer (rgthree)`
- `CLIPLoader`
- `VAELoader`
- `UNETLoader` ★核心
- `CR Prompt Text`

**识别到的模式**：text_to_image

## 关键参数

- `width` = `1080`
- `height` = `1920`
- `batch_size` = `1`
- `seed` = `843634065030824`
- `steps` = `15`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **80%**（16/20）

**有卡**：`CLIPTextEncode`、`EmptyLatentImage`、`KSampler`、`VAEDecode`、`LayerUtility: PurgeVRAM`、`SaveImage`、`ImageScaleBy`、`SeedVR2LoadDiTModel`、`SeedVR2LoadVAEModel`、`SeedVR2VideoUpscaler`、`CLIPLoader`、`VAELoader`、`UNETLoader`、`CR Prompt Text`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、EmptyLatentImage、UNETLoader、SeedVR2LoadDiTModel

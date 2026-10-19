---
key: 图片生成/文生图/killer FLux出图+Contronet+Minicpmv4.5反推+4K高清修复v2.0_1999324967453982722.json
name: killer FLux出图+Contronet+Minicpmv4.5反推+4K高清修复v2.0_1999324967453982722
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/killer FLux出图+Contronet+Minicpmv4.5反推+4K高清修复v2.0_1999324967453982722.json
hash: 69263bee3ff140ff
coverage: 0.787879
learned_at: 2026-10-19 21:47:18
nodes: [ControlNetApplySD3, KSampler, AIO_Preprocessor, PreviewImage, SaveImage, CLIPTextEncode, MiniCPM_VQA, LoadImage, SetUnionControlNetType, ControlNetLoader, UNETLoader, DualCLIPLoader, CLIPTextEncode, VAELoader, Lora Loader, Lora Loader, Lora Loader, Lora Loader, VAEDecode, FluxGuidance, EmptyLatentImage, easy showAnything, CLIPTextEncode, Note, Note, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, PreviewImage, SeedVR2VideoUpscaler, Image Comparer (rgthree), Note, LoadImage, LoadImage]
patterns: [text_to_image]
missing: []
parameters: {"batch_size": 5, "cfg": 1, "controlnet_strength": 0.6500000000000001, "denoise": 1, "height": 1280, "sampler_name": "euler", "scheduler": "simple", "seed": 780703722385597, "steps": 25, "width": 840}
---

# 图片生成/文生图/killer FLux出图+Contronet+Minicpmv4.5反推+4K高清修复v2.0_1999324967453982722.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/killer FLux出图+Contronet+Minicpmv4.5反推+4K高清修复v2.0_1999324967453982722.json`

## 结构

**生成流程**：Model → Condition → Latent → Control → Sampling → Decode → Process → Output → Other

**节点**（33 个）：
- `ControlNetApplySD3` ★核心
- `KSampler` ★核心
- `AIO_Preprocessor`
- `PreviewImage`
- `SaveImage`
- `CLIPTextEncode` ★核心
- `MiniCPM_VQA`
- `LoadImage`
- `SetUnionControlNetType`
- `ControlNetLoader`
- `UNETLoader` ★核心
- `DualCLIPLoader`
- `CLIPTextEncode` ★核心
- `VAELoader`
- `Lora Loader`
- `Lora Loader`
- `Lora Loader`
- `Lora Loader`
- `VAEDecode` ★核心
- `FluxGuidance`
- `EmptyLatentImage` ★核心
- `easy showAnything`
- `CLIPTextEncode` ★核心
- `Note`
- `Note`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `PreviewImage`
- `SeedVR2VideoUpscaler`
- `Image Comparer (rgthree)`
- `Note`
- `LoadImage`
- `LoadImage`

**识别到的模式**：text_to_image

## 关键参数

- `controlnet_strength` = `0.6500000000000001`
- `seed` = `780703722385597`
- `steps` = `25`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`
- `width` = `840`
- `height` = `1280`
- `batch_size` = `5`

## 知识

覆盖率 **79%**（26/33）

**有卡**：`ControlNetApplySD3`、`KSampler`、`AIO_Preprocessor`、`SaveImage`、`CLIPTextEncode`、`MiniCPM_VQA`、`LoadImage`、`SetUnionControlNetType`、`ControlNetLoader`、`UNETLoader`、`DualCLIPLoader`、`VAELoader`、`Lora Loader`、`VAEDecode`、`FluxGuidance`、`EmptyLatentImage`、`SeedVR2LoadDiTModel`、`SeedVR2LoadVAEModel`、`SeedVR2VideoUpscaler`

**用到的条目**：KSampler、VAEDecode、VAELoader、UNETLoader、CLIPTextEncode、EmptyLatentImage、LoadImage、ControlNetLoader

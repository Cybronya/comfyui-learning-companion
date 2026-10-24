---
key: 图片生成/图生图/橘-Flux ControlNet-Union-Pro-2.0_1931564801863168002.json
name: 橘-Flux ControlNet-Union-Pro-2.0_1931564801863168002
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/橘-Flux ControlNet-Union-Pro-2.0_1931564801863168002.json
hash: cda4fdcf8b799b33
coverage: 0.862069
learned_at: 2026-10-23 13:10:53
nodes: [AIO_Preprocessor, SetUnionControlNetType, PreviewImage, PreviewImage, PreviewImage, FluxGuidance, CLIPTextEncode, SetUnionControlNetType, KSampler, PreviewImage, FluxGuidance, ControlNetApplySD3, ControlNetApplySD3, EmptySD3LatentImage, VAEDecode, VAEDecode, SaveImage, SaveImage, EmptySD3LatentImage, ControlNetLoader, CLIPTextEncode, LoadImage, CLIPTextEncode, CheckpointLoaderSimple, VAEEncode, ImpactImageInfo, AIO_Preprocessor, ImageResizeKJv2, KSampler]
patterns: [image_to_image]
missing: []
parameters: {"cfg": 1, "checkpoint": "flux1-dev-fp8-with_clip_vae.safetensors", "controlnet_strength": 1.0000000000000002, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 84694046412127, "steps": 20}
---

# 图片生成/图生图/橘-Flux ControlNet-Union-Pro-2.0_1931564801863168002.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/橘-Flux ControlNet-Union-Pro-2.0_1931564801863168002.json`

## 结构

**生成流程**：Model → Encode → Condition → Control → Sampling → Decode → Process → Output → Other

**节点**（29 个）：
- `AIO_Preprocessor`
- `SetUnionControlNetType`
- `PreviewImage`
- `PreviewImage`
- `PreviewImage`
- `FluxGuidance`
- `CLIPTextEncode` ★核心
- `SetUnionControlNetType`
- `KSampler` ★核心
- `PreviewImage`
- `FluxGuidance`
- `ControlNetApplySD3` ★核心
- `ControlNetApplySD3` ★核心
- `EmptySD3LatentImage`
- `VAEDecode` ★核心
- `VAEDecode` ★核心
- `SaveImage`
- `SaveImage`
- `EmptySD3LatentImage`
- `ControlNetLoader`
- `CLIPTextEncode` ★核心
- `LoadImage`
- `CLIPTextEncode` ★核心
- `CheckpointLoaderSimple` ★核心
- `VAEEncode` ★核心
- `ImpactImageInfo`
- `AIO_Preprocessor`
- `ImageResizeKJv2`
- `KSampler` ★核心

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `84694046412127`
- `steps` = `20`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`
- `controlnet_strength` = `1.0000000000000002`
- `checkpoint` = `flux1-dev-fp8-with_clip_vae.safetensors`

## 知识

覆盖率 **86%**（25/29）

**有卡**：`AIO_Preprocessor`、`SetUnionControlNetType`、`FluxGuidance`、`CLIPTextEncode`、`KSampler`、`ControlNetApplySD3`、`EmptySD3LatentImage`、`VAEDecode`、`SaveImage`、`ControlNetLoader`、`LoadImage`、`CheckpointLoaderSimple`、`VAEEncode`、`ImpactImageInfo`、`ImageResizeKJv2`

**用到的条目**：KSampler、VAEDecode、CheckpointLoaderSimple、CLIPTextEncode、LoadImage、ControlNetLoader、SetUnionControlNetType、ControlNetApplySD3

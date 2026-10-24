---
key: 图片生成/图生图/z-image-turbo_fun_controlnet_base_1996418811291115522.json
name: z-image-turbo_fun_controlnet_base_1996418811291115522
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/z-image-turbo_fun_controlnet_base_1996418811291115522.json
hash: 5af15d7644d14987
coverage: 0.85
learned_at: 2026-10-23 11:46:40
nodes: [UNETLoader, ModelSamplingAuraFlow, ModelPatchLoader, VAELoader, CLIPLoader, CLIPTextEncode, ConditioningZeroOut, PrimitiveNode, PrimitiveNode, EmptySD3LatentImage, KSamplerAdvanced, GetImageSize, DJZImageScaleToTotalPixels, PreviewImage, KSamplerAdvanced, QwenImageDiffsynthControlnet, AIO_Preprocessor, LoadImage, VAEDecode, SaveImage]
patterns: []
missing: []
parameters: {"cfg": 8, "denoise": "simple", "sampler_name": 1, "scheduler": "euler", "seed": "enable", "steps": "randomize"}
---

# 图片生成/图生图/z-image-turbo_fun_controlnet_base_1996418811291115522.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/z-image-turbo_fun_controlnet_base_1996418811291115522.json`

## 结构

**生成流程**：Model → Condition → Control → Sampling → Decode → Process → Output → Other

**节点**（20 个）：
- `UNETLoader` ★核心
- `ModelSamplingAuraFlow`
- `ModelPatchLoader`
- `VAELoader`
- `CLIPLoader`
- `CLIPTextEncode` ★核心
- `ConditioningZeroOut`
- `PrimitiveNode`
- `PrimitiveNode`
- `EmptySD3LatentImage`
- `KSamplerAdvanced` ★核心
- `GetImageSize`
- `DJZImageScaleToTotalPixels`
- `PreviewImage`
- `KSamplerAdvanced` ★核心
- `QwenImageDiffsynthControlnet`
- `AIO_Preprocessor`
- `LoadImage`
- `VAEDecode` ★核心
- `SaveImage`

## 关键参数

- `seed` = `enable`
- `steps` = `randomize`
- `cfg` = `8`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `simple`

## 知识

覆盖率 **85%**（17/20）

**有卡**：`UNETLoader`、`ModelSamplingAuraFlow`、`ModelPatchLoader`、`VAELoader`、`CLIPLoader`、`CLIPTextEncode`、`ConditioningZeroOut`、`EmptySD3LatentImage`、`KSamplerAdvanced`、`GetImageSize`、`DJZImageScaleToTotalPixels`、`QwenImageDiffsynthControlnet`、`AIO_Preprocessor`、`LoadImage`、`VAEDecode`、`SaveImage`

**用到的条目**：VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、LoadImage、UNETLoader、QwenImageDiffsynthControlnet

---
key: 图片生成/图生图/z-image-turbo_fun_controlnet_v2.0_1996424354097414146.json
name: z-image-turbo_fun_controlnet_v2.0_1996424354097414146
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/z-image-turbo_fun_controlnet_v2.0_1996424354097414146.json
hash: 126c850f21136695
coverage: 0.857143
learned_at: 2026-10-23 11:46:42
nodes: [CLIPLoader, ConditioningZeroOut, VAELoader, LoadImage, EmptySD3LatentImage, GetImageSize, VAEDecode, SaveImage, PrimitiveNode, CLIPTextEncode, UNETLoader, LoraLoaderModelOnly, AIO_Preprocessor, ModelSamplingAuraFlow, KSamplerAdvanced, PrimitiveNode, PreviewImage, QwenImageDiffsynthControlnet, ImageScaleToTotalPixels, KSamplerAdvanced, ModelPatchLoader]
patterns: []
missing: []
parameters: {"cfg": 8, "denoise": "simple", "sampler_name": 1, "scheduler": "euler", "seed": "enable", "steps": "randomize"}
---

# 图片生成/图生图/z-image-turbo_fun_controlnet_v2.0_1996424354097414146.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/z-image-turbo_fun_controlnet_v2.0_1996424354097414146.json`

## 结构

**生成流程**：Model → Condition → Control → Sampling → Decode → Process → Output → Other

**节点**（21 个）：
- `CLIPLoader`
- `ConditioningZeroOut`
- `VAELoader`
- `LoadImage`
- `EmptySD3LatentImage`
- `GetImageSize`
- `VAEDecode` ★核心
- `SaveImage`
- `PrimitiveNode`
- `CLIPTextEncode` ★核心
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `AIO_Preprocessor`
- `ModelSamplingAuraFlow`
- `KSamplerAdvanced` ★核心
- `PrimitiveNode`
- `PreviewImage`
- `QwenImageDiffsynthControlnet`
- `ImageScaleToTotalPixels`
- `KSamplerAdvanced` ★核心
- `ModelPatchLoader`

## 关键参数

- `seed` = `enable`
- `steps` = `randomize`
- `cfg` = `8`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `simple`

## 知识

覆盖率 **86%**（18/21）

**有卡**：`CLIPLoader`、`ConditioningZeroOut`、`VAELoader`、`LoadImage`、`EmptySD3LatentImage`、`GetImageSize`、`VAEDecode`、`SaveImage`、`CLIPTextEncode`、`UNETLoader`、`LoraLoaderModelOnly`、`AIO_Preprocessor`、`ModelSamplingAuraFlow`、`KSamplerAdvanced`、`QwenImageDiffsynthControlnet`、`ImageScaleToTotalPixels`、`ModelPatchLoader`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、LoadImage、UNETLoader

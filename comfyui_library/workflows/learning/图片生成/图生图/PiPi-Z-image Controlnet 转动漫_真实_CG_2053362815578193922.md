---
key: 图片生成/图生图/PiPi-Z-image Controlnet 转动漫_真实_CG_2053362815578193922.json
name: PiPi-Z-image Controlnet 转动漫_真实_CG_2053362815578193922
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/PiPi-Z-image Controlnet 转动漫_真实_CG_2053362815578193922.json
hash: cf97ef49fcad20b4
coverage: 0.931034
learned_at: 2026-10-23 11:10:50
nodes: [AIO_Preprocessor, AIO_Preprocessor, AIO_Preprocessor, AIO_Preprocessor, AIO_Preprocessor, AIO_Preprocessor, ConditioningZeroOut, LoadImage, VAELoader, AIO_Preprocessor, ModelSamplingAuraFlow, Image Comparer (rgthree), UNETLoader, LoraLoaderModelOnly, CLIPLoader, EmptySD3LatentImage, ModelPatchLoader, SaveImage, RH_Captioner, VAEDecode, JoinStrings, PreviewImage, KSampler, CLIPTextEncode, ImageUpscaleWithModel, UpscaleModelLoader, LayerUtility: ImageScaleByAspectRatio V2, Text, QwenImageDiffsynthControlnet]
patterns: []
missing: []
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 622747705204979, "steps": 15}
---

# 图片生成/图生图/PiPi-Z-image Controlnet 转动漫_真实_CG_2053362815578193922.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/PiPi-Z-image Controlnet 转动漫_真实_CG_2053362815578193922.json`

## 结构

**生成流程**：Model → Condition → Control → Sampling → Decode → Process → Output → Other

**节点**（29 个）：
- `AIO_Preprocessor`
- `AIO_Preprocessor`
- `AIO_Preprocessor`
- `AIO_Preprocessor`
- `AIO_Preprocessor`
- `AIO_Preprocessor`
- `ConditioningZeroOut`
- `LoadImage`
- `VAELoader`
- `AIO_Preprocessor`
- `ModelSamplingAuraFlow`
- `Image Comparer (rgthree)`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `CLIPLoader`
- `EmptySD3LatentImage`
- `ModelPatchLoader`
- `SaveImage`
- `RH_Captioner`
- `VAEDecode` ★核心
- `JoinStrings`
- `PreviewImage`
- `KSampler` ★核心
- `CLIPTextEncode` ★核心
- `ImageUpscaleWithModel`
- `UpscaleModelLoader`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `Text`
- `QwenImageDiffsynthControlnet`

## 关键参数

- `seed` = `622747705204979`
- `steps` = `15`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **93%**（27/29）

**有卡**：`AIO_Preprocessor`、`ConditioningZeroOut`、`LoadImage`、`VAELoader`、`ModelSamplingAuraFlow`、`UNETLoader`、`LoraLoaderModelOnly`、`CLIPLoader`、`EmptySD3LatentImage`、`ModelPatchLoader`、`SaveImage`、`RH_Captioner`、`VAEDecode`、`JoinStrings`、`KSampler`、`CLIPTextEncode`、`ImageUpscaleWithModel`、`UpscaleModelLoader`、`LayerUtility: ImageScaleByAspectRatio V2`、`Text`、`QwenImageDiffsynthControlnet`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、LoadImage

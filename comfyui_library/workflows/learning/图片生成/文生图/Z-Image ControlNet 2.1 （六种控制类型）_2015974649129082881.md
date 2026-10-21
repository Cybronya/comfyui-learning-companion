---
key: 图片生成/文生图/Z-Image ControlNet 2.1 （六种控制类型）_2015974649129082881.json
name: Z-Image ControlNet 2.1 （六种控制类型）_2015974649129082881
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Z-Image ControlNet 2.1 （六种控制类型）_2015974649129082881.json
hash: 09856d962f298aad
coverage: 0.913043
learned_at: 2026-10-19 22:15:22
nodes: [AIO_Preprocessor, AIO_Preprocessor, AIO_Preprocessor, AIO_Preprocessor, AIO_Preprocessor, AIO_Preprocessor, ConditioningZeroOut, VAELoader, EmptySD3LatentImage, CLIPLoader, AIO_Preprocessor, QwenImageDiffsynthControlnet, LoadImage, ModelPatchLoader, PreviewImage, CLIPTextEncode, UNETLoader, ModelSamplingAuraFlow, VAEDecode, LayerUtility: ImageScaleByAspectRatio V2, SaveImage, Image Comparer (rgthree), KSampler]
patterns: []
missing: []
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 162668668354250, "steps": 15}
---

# 图片生成/文生图/Z-Image ControlNet 2.1 （六种控制类型）_2015974649129082881.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Z-Image ControlNet 2.1 （六种控制类型）_2015974649129082881.json`

## 结构

**生成流程**：Model → Condition → Control → Sampling → Decode → Process → Output → Other

**节点**（23 个）：
- `AIO_Preprocessor`
- `AIO_Preprocessor`
- `AIO_Preprocessor`
- `AIO_Preprocessor`
- `AIO_Preprocessor`
- `AIO_Preprocessor`
- `ConditioningZeroOut`
- `VAELoader`
- `EmptySD3LatentImage`
- `CLIPLoader`
- `AIO_Preprocessor`
- `QwenImageDiffsynthControlnet`
- `LoadImage`
- `ModelPatchLoader`
- `PreviewImage`
- `CLIPTextEncode` ★核心
- `UNETLoader` ★核心
- `ModelSamplingAuraFlow`
- `VAEDecode` ★核心
- `LayerUtility: ImageScaleByAspectRatio V2`
- `SaveImage`
- `Image Comparer (rgthree)`
- `KSampler` ★核心

## 关键参数

- `seed` = `162668668354250`
- `steps` = `15`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **91%**（21/23）

**有卡**：`AIO_Preprocessor`、`ConditioningZeroOut`、`VAELoader`、`EmptySD3LatentImage`、`CLIPLoader`、`QwenImageDiffsynthControlnet`、`LoadImage`、`ModelPatchLoader`、`CLIPTextEncode`、`UNETLoader`、`ModelSamplingAuraFlow`、`VAEDecode`、`LayerUtility: ImageScaleByAspectRatio V2`、`SaveImage`、`KSampler`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、LoadImage、UNETLoader

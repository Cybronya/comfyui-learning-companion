---
key: 平台全量/z-image-turbo_fun_controlnet_1996823785732984833.json
name: z-image-turbo_fun_controlnet_1996823785732984833
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/z-image-turbo_fun_controlnet_1996823785732984833.json
hash: 7edc3b5391bbca11
coverage: 0.863636
learned_at: 2026-11-14 01:20:36
nodes: [UNETLoader, ModelSamplingAuraFlow, QwenImageDiffsynthControlnet, ModelPatchLoader, VAELoader, CLIPLoader, ConditioningZeroOut, PrimitiveNode, PrimitiveNode, EmptySD3LatentImage, KSamplerAdvanced, GetImageSize, DJZImageScaleToTotalPixels, PreviewImage, KSamplerAdvanced, VAEDecode, SaveImage, AIO_Preprocessor, LoadImage, AILab_QwenVL, CLIPTextEncode, LoadImage]
patterns: []
missing: []
parameters: {"cfg": 8, "denoise": "simple", "sampler_name": 1, "scheduler": "euler", "seed": "enable", "steps": "randomize"}
---

# 平台全量/z-image-turbo_fun_controlnet_1996823785732984833.json

> 来源文件 `comfyui_library/workflows/平台全量/z-image-turbo_fun_controlnet_1996823785732984833.json`

## 结构

**生成流程**：Model → Condition → Control → Sampling → Decode → Process → Output → Other

**节点**（22 个）：
- `UNETLoader` ★核心
- `ModelSamplingAuraFlow`
- `QwenImageDiffsynthControlnet`
- `ModelPatchLoader`
- `VAELoader`
- `CLIPLoader`
- `ConditioningZeroOut`
- `PrimitiveNode`
- `PrimitiveNode`
- `EmptySD3LatentImage`
- `KSamplerAdvanced` ★核心
- `GetImageSize`
- `DJZImageScaleToTotalPixels`
- `PreviewImage`
- `KSamplerAdvanced` ★核心
- `VAEDecode` ★核心
- `SaveImage`
- `AIO_Preprocessor`
- `LoadImage`
- `AILab_QwenVL`
- `CLIPTextEncode` ★核心
- `LoadImage`

## 关键参数

- `seed` = `enable`
- `steps` = `randomize`
- `cfg` = `8`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `simple`

## 知识

覆盖率 **86%**（19/22）

**有卡**：`UNETLoader`、`ModelSamplingAuraFlow`、`QwenImageDiffsynthControlnet`、`ModelPatchLoader`、`VAELoader`、`CLIPLoader`、`ConditioningZeroOut`、`EmptySD3LatentImage`、`KSamplerAdvanced`、`GetImageSize`、`DJZImageScaleToTotalPixels`、`VAEDecode`、`SaveImage`、`AIO_Preprocessor`、`LoadImage`、`AILab_QwenVL`、`CLIPTextEncode`

**用到的条目**：VAEDecode、VAELoader、CLIPLoader、CLIPTextEncode、ConditioningZeroOut、LoadImage、UNETLoader、QwenImageDiffsynthControlnet

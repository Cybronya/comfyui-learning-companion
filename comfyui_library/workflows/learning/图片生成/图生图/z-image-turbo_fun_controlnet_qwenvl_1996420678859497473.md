---
key: 图片生成/图生图/z-image-turbo_fun_controlnet_qwenvl_1996420678859497473.json
name: z-image-turbo_fun_controlnet_qwenvl_1996420678859497473
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/z-image-turbo_fun_controlnet_qwenvl_1996420678859497473.json
hash: 265278ed4abdc4df
coverage: 0.863636
learned_at: 2026-10-23 11:46:42
nodes: [UNETLoader, ModelSamplingAuraFlow, QwenImageDiffsynthControlnet, ModelPatchLoader, VAELoader, CLIPLoader, CLIPTextEncode, ConditioningZeroOut, PrimitiveNode, PrimitiveNode, EmptySD3LatentImage, KSamplerAdvanced, GetImageSize, DJZImageScaleToTotalPixels, PreviewImage, AIO_Preprocessor, AILab_QwenVL, LoadImage, LoadImage, KSamplerAdvanced, VAEDecode, SaveImage]
patterns: []
missing: []
parameters: {"cfg": 8, "denoise": "simple", "sampler_name": 1, "scheduler": "euler", "seed": "enable", "steps": "randomize"}
---

# 图片生成/图生图/z-image-turbo_fun_controlnet_qwenvl_1996420678859497473.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/z-image-turbo_fun_controlnet_qwenvl_1996420678859497473.json`

## 结构

**生成流程**：Model → Condition → Control → Sampling → Decode → Process → Output → Other

**节点**（22 个）：
- `UNETLoader` ★核心
- `ModelSamplingAuraFlow`
- `QwenImageDiffsynthControlnet`
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
- `AIO_Preprocessor`
- `AILab_QwenVL`
- `LoadImage`
- `LoadImage`
- `KSamplerAdvanced` ★核心
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

覆盖率 **86%**（19/22）

**有卡**：`UNETLoader`、`ModelSamplingAuraFlow`、`QwenImageDiffsynthControlnet`、`ModelPatchLoader`、`VAELoader`、`CLIPLoader`、`CLIPTextEncode`、`ConditioningZeroOut`、`EmptySD3LatentImage`、`KSamplerAdvanced`、`GetImageSize`、`DJZImageScaleToTotalPixels`、`AIO_Preprocessor`、`AILab_QwenVL`、`LoadImage`、`VAEDecode`、`SaveImage`

**用到的条目**：VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、LoadImage、UNETLoader、QwenImageDiffsynthControlnet

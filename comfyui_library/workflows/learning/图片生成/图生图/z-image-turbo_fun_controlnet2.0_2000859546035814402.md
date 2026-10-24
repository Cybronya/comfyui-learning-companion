---
key: 图片生成/图生图/z-image-turbo_fun_controlnet2.0_2000859546035814402.json
name: z-image-turbo_fun_controlnet2.0_2000859546035814402
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/z-image-turbo_fun_controlnet2.0_2000859546035814402.json
hash: aa0d3b05627622c6
coverage: 0.863636
learned_at: 2026-10-23 11:46:40
nodes: [UNETLoader, ModelSamplingAuraFlow, VAELoader, CLIPLoader, ConditioningZeroOut, EmptySD3LatentImage, KSamplerAdvanced, GetImageSize, DJZImageScaleToTotalPixels, KSamplerAdvanced, VAEDecode, SaveImage, AIO_Preprocessor, ModelPatchLoader, LoadImage, PrimitiveNode, PrimitiveNode, AILab_QwenVL, PreviewImage, QwenImageDiffsynthControlnet, LoadImage, CLIPTextEncode]
patterns: []
missing: []
parameters: {"cfg": 10, "denoise": "simple", "sampler_name": 1, "scheduler": "euler", "seed": "enable", "steps": "randomize"}
---

# 图片生成/图生图/z-image-turbo_fun_controlnet2.0_2000859546035814402.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/z-image-turbo_fun_controlnet2.0_2000859546035814402.json`

## 结构

**生成流程**：Model → Condition → Control → Sampling → Decode → Process → Output → Other

**节点**（22 个）：
- `UNETLoader` ★核心
- `ModelSamplingAuraFlow`
- `VAELoader`
- `CLIPLoader`
- `ConditioningZeroOut`
- `EmptySD3LatentImage`
- `KSamplerAdvanced` ★核心
- `GetImageSize`
- `DJZImageScaleToTotalPixels`
- `KSamplerAdvanced` ★核心
- `VAEDecode` ★核心
- `SaveImage`
- `AIO_Preprocessor`
- `ModelPatchLoader`
- `LoadImage`
- `PrimitiveNode`
- `PrimitiveNode`
- `AILab_QwenVL`
- `PreviewImage`
- `QwenImageDiffsynthControlnet`
- `LoadImage`
- `CLIPTextEncode` ★核心

## 关键参数

- `seed` = `enable`
- `steps` = `randomize`
- `cfg` = `10`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `simple`

## 知识

覆盖率 **86%**（19/22）

**有卡**：`UNETLoader`、`ModelSamplingAuraFlow`、`VAELoader`、`CLIPLoader`、`ConditioningZeroOut`、`EmptySD3LatentImage`、`KSamplerAdvanced`、`GetImageSize`、`DJZImageScaleToTotalPixels`、`VAEDecode`、`SaveImage`、`AIO_Preprocessor`、`ModelPatchLoader`、`LoadImage`、`AILab_QwenVL`、`QwenImageDiffsynthControlnet`、`CLIPTextEncode`

**用到的条目**：VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、LoadImage、UNETLoader、QwenImageDiffsynthControlnet

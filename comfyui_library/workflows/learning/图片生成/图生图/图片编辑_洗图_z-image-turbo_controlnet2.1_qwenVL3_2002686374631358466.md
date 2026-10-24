---
key: 图片生成/图生图/图片编辑_洗图_z-image-turbo_controlnet2.1_qwenVL3_2002686374631358466.json
name: 图片编辑_洗图_z-image-turbo_controlnet2.1_qwenVL3_2002686374631358466
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/图片编辑_洗图_z-image-turbo_controlnet2.1_qwenVL3_2002686374631358466.json
hash: d3c3c7028c8054f6
coverage: 0.482353
learned_at: 2026-10-23 12:41:28
nodes: [SetNode, SetNode, SetNode, SetNode, SetNode, easy int, SetNode, SetNode, GetNode, GetNode, GetNode, SetNode, GetNode, GetNode, easy int, SetNode, easy seed, GetNode, GetNode, GetNode, ConditioningZeroOut, CLIPTextEncode, SetNode, easy compare, ControlNetPreprocessorSelector, INTConstant, ControlNetPreprocessorSelector, easy compare, PreviewImage, easy ifElse, AIO_Preprocessor, GetNode, GetNode, easy ifElse, SetNode, INTConstant, ControlNetPreprocessorSelector, Note, Reroute, EmptySD3LatentImage, ModelSamplingAuraFlow, DifferentialDiffusion, GetNode, GetNode, GetNode, GetNode, easy int, VAEDecode, PreviewImage, ModelSamplingAuraFlow, Reroute, GetNode, UpscaleModelLoader, GetNode, Reroute, DifferentialDiffusion, KSamplerAdvanced, KSamplerAdvanced, CLIPLoader, VAELoader, ModelPatchLoader, SetNode, PreviewAny, LoadImage, ImageScaleToMaxDimension, GetImageSize, UltimateSDUpscale, Image Comparer (rgthree), GetNode, easy imageConcat, SaveImage, SeedVR2LoadVAEModel, PreviewImage, SeedVR2LoadDiTModel, Reroute, SeedVR2VideoUpscaler, GetNode, GetNode, ZImageFunControlnet, ModelSamplingAuraFlow, DifferentialDiffusion, UNETLoader, AILab_QwenVL, AILab_ImagePreview, Reroute]
patterns: []
missing: []
parameters: {"cfg": 8, "denoise": "simple", "sampler_name": 1, "scheduler": "euler", "seed": "disable", "steps": "fixed"}
---

# 图片生成/图生图/图片编辑_洗图_z-image-turbo_controlnet2.1_qwenVL3_2002686374631358466.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/图片编辑_洗图_z-image-turbo_controlnet2.1_qwenVL3_2002686374631358466.json`

## 结构

**生成流程**：Model → Condition → Control → Sampling → Decode → Process → Output → Other

**节点**（85 个）：
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `easy int`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `easy int`
- `SetNode`
- `easy seed`
- `GetNode`
- `GetNode`
- `GetNode`
- `ConditioningZeroOut`
- `CLIPTextEncode` ★核心
- `SetNode`
- `easy compare`
- `ControlNetPreprocessorSelector`
- `INTConstant`
- `ControlNetPreprocessorSelector`
- `easy compare`
- `PreviewImage`
- `easy ifElse`
- `AIO_Preprocessor`
- `GetNode`
- `GetNode`
- `easy ifElse`
- `SetNode`
- `INTConstant`
- `ControlNetPreprocessorSelector`
- `Note`
- `Reroute`
- `EmptySD3LatentImage`
- `ModelSamplingAuraFlow`
- `DifferentialDiffusion`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `easy int`
- `VAEDecode` ★核心
- `PreviewImage`
- `ModelSamplingAuraFlow`
- `Reroute`
- `GetNode`
- `UpscaleModelLoader`
- `GetNode`
- `Reroute`
- `DifferentialDiffusion`
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `CLIPLoader`
- `VAELoader`
- `ModelPatchLoader`
- `SetNode`
- `PreviewAny`
- `LoadImage`
- `ImageScaleToMaxDimension`
- `GetImageSize`
- `UltimateSDUpscale`
- `Image Comparer (rgthree)`
- `GetNode`
- `easy imageConcat`
- `SaveImage`
- `SeedVR2LoadVAEModel`
- `PreviewImage`
- `SeedVR2LoadDiTModel`
- `Reroute`
- `SeedVR2VideoUpscaler`
- `GetNode`
- `GetNode`
- `ZImageFunControlnet`
- `ModelSamplingAuraFlow`
- `DifferentialDiffusion`
- `UNETLoader` ★核心
- `AILab_QwenVL`
- `AILab_ImagePreview`
- `Reroute`

## 关键参数

- `seed` = `disable`
- `steps` = `fixed`
- `cfg` = `8`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `simple`

## 知识

覆盖率 **48%**（41/85）

**有卡**：`easy int`、`easy seed`、`ConditioningZeroOut`、`CLIPTextEncode`、`easy compare`、`ControlNetPreprocessorSelector`、`INTConstant`、`AIO_Preprocessor`、`EmptySD3LatentImage`、`ModelSamplingAuraFlow`、`DifferentialDiffusion`、`VAEDecode`、`UpscaleModelLoader`、`KSamplerAdvanced`、`CLIPLoader`、`VAELoader`、`ModelPatchLoader`、`LoadImage`、`ImageScaleToMaxDimension`、`GetImageSize`、`UltimateSDUpscale`、`easy imageConcat`、`SaveImage`、`SeedVR2LoadVAEModel`、`SeedVR2LoadDiTModel`、`SeedVR2VideoUpscaler`、`ZImageFunControlnet`、`UNETLoader`、`AILab_QwenVL`、`AILab_ImagePreview`

**用到的条目**：VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、LoadImage、UNETLoader、ZImageFunControlnet

---
key: 图片生成/图生图/图片编辑_局部重绘与外扩_z-image-turbo_controlnet_2003327006089543682.json
name: 图片编辑_局部重绘与外扩_z-image-turbo_controlnet_2003327006089543682
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/图片编辑_局部重绘与外扩_z-image-turbo_controlnet_2003327006089543682.json
hash: a38e81cf6d0ea53d
coverage: 0.573529
learned_at: 2026-10-23 12:41:28
nodes: [SetNode, SetNode, SetNode, SetNode, GetNode, GetNode, DifferentialDiffusion, GetNode, GetNode, ModelSamplingAuraFlow, PreviewImage, Reroute, KSampler, AILab_Preview, AIO_Preprocessor, ZImageFunControlnet, GetNode, GetNode, ModelSamplingAuraFlow, Reroute, UpscaleModelLoader, DifferentialDiffusion, Image Comparer (rgthree), Image Comparer (rgthree), VAEDecode, GetNode, GetNode, DifferentialDiffusion, GetNode, GetNode, ConditioningZeroOut, ModelSamplingAuraFlow, KSampler, Image Comparer (rgthree), VAEDecode, ZImageFunControlnet, AILab_Preview, Reroute, InpaintModelConditioning, InpaintModelConditioning, CLIPTextEncode, ImagePadForOutpaint, CLIPTextEncode, CLIPLoader, VAELoader, ModelPatchLoader, SeedVR2LoadVAEModel, PreviewImage, SeedVR2LoadDiTModel, Reroute, SeedVR2VideoUpscaler, Reroute, Reroute, Reroute, Reroute, easy imageConcat, SaveImage, UltimateSDUpscale, ConditioningZeroOut, GetNode, CLIPTextEncode, ConditioningZeroOut, AILab_ImagePreview, LoadImage, easy imageConcat, UNETLoader, GrowMaskWithBlur, Reroute]
patterns: []
missing: []
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 252184377496714, "steps": 10}
---

# 图片生成/图生图/图片编辑_局部重绘与外扩_z-image-turbo_controlnet_2003327006089543682.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/图片编辑_局部重绘与外扩_z-image-turbo_controlnet_2003327006089543682.json`

## 结构

**生成流程**：Model → Condition → Control → Sampling → Decode → Process → Output → Other

**节点**（68 个）：
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `DifferentialDiffusion`
- `GetNode`
- `GetNode`
- `ModelSamplingAuraFlow`
- `PreviewImage`
- `Reroute`
- `KSampler` ★核心
- `AILab_Preview`
- `AIO_Preprocessor`
- `ZImageFunControlnet`
- `GetNode`
- `GetNode`
- `ModelSamplingAuraFlow`
- `Reroute`
- `UpscaleModelLoader`
- `DifferentialDiffusion`
- `Image Comparer (rgthree)`
- `Image Comparer (rgthree)`
- `VAEDecode` ★核心
- `GetNode`
- `GetNode`
- `DifferentialDiffusion`
- `GetNode`
- `GetNode`
- `ConditioningZeroOut`
- `ModelSamplingAuraFlow`
- `KSampler` ★核心
- `Image Comparer (rgthree)`
- `VAEDecode` ★核心
- `ZImageFunControlnet`
- `AILab_Preview`
- `Reroute`
- `InpaintModelConditioning`
- `InpaintModelConditioning`
- `CLIPTextEncode` ★核心
- `ImagePadForOutpaint`
- `CLIPTextEncode` ★核心
- `CLIPLoader`
- `VAELoader`
- `ModelPatchLoader`
- `SeedVR2LoadVAEModel`
- `PreviewImage`
- `SeedVR2LoadDiTModel`
- `Reroute`
- `SeedVR2VideoUpscaler`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `easy imageConcat`
- `SaveImage`
- `UltimateSDUpscale`
- `ConditioningZeroOut`
- `GetNode`
- `CLIPTextEncode` ★核心
- `ConditioningZeroOut`
- `AILab_ImagePreview`
- `LoadImage`
- `easy imageConcat`
- `UNETLoader` ★核心
- `GrowMaskWithBlur`
- `Reroute`

## 关键参数

- `seed` = `252184377496714`
- `steps` = `10`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **57%**（39/68）

**有卡**：`DifferentialDiffusion`、`ModelSamplingAuraFlow`、`KSampler`、`AILab_Preview`、`AIO_Preprocessor`、`ZImageFunControlnet`、`UpscaleModelLoader`、`VAEDecode`、`ConditioningZeroOut`、`InpaintModelConditioning`、`CLIPTextEncode`、`ImagePadForOutpaint`、`CLIPLoader`、`VAELoader`、`ModelPatchLoader`、`SeedVR2LoadVAEModel`、`SeedVR2LoadDiTModel`、`SeedVR2VideoUpscaler`、`easy imageConcat`、`SaveImage`、`UltimateSDUpscale`、`AILab_ImagePreview`、`LoadImage`、`UNETLoader`、`GrowMaskWithBlur`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、LoadImage、UNETLoader

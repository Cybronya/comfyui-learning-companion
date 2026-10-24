---
key: 图片生成/图生图/LH-DMT版本-2.生图片类-025.Z_image深度控制洗图放大-高显存_2016493126872993793.json
name: LH-DMT版本-2.生图片类-025.Z_image深度控制洗图放大-高显存_2016493126872993793
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/LH-DMT版本-2.生图片类-025.Z_image深度控制洗图放大-高显存_2016493126872993793.json
hash: 0473fc9db646ca44
coverage: 0.530612
learned_at: 2026-10-23 11:08:39
nodes: [PreviewImage, EmptySD3LatentImage, Note, QwenImageDiffsynthControlnet, KSampler, VAEDecode, ConditioningZeroOut, SaveImage, CLIPLoader, UNETLoader, INTConstant, easy cleanGpuUsed, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, ImageScaleBy, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SaveImage, SeedVR2VideoUpscaler, Image Comparer (rgthree), Reroute, LayerUtility: ImageReel, LayerUtility: ImageReelComposit, easy cleanGpuUsed, PreviewImage, Reroute, Reroute, Reroute, ModelPatchLoader, ImageScaleToTotalPixels, AIO_Preprocessor, LayerUtility: ImageScaleByAspectRatio V2, VAELoader, Qwen3_VQA, ShowText|pysssss, CLIPTextEncode, Fast Groups Bypasser (rgthree), LoadImage]
patterns: []
missing: []
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "er_sde", "scheduler": "simple", "seed": 168967001473789, "steps": 10}
---

# 图片生成/图生图/LH-DMT版本-2.生图片类-025.Z_image深度控制洗图放大-高显存_2016493126872993793.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/LH-DMT版本-2.生图片类-025.Z_image深度控制洗图放大-高显存_2016493126872993793.json`

## 结构

**生成流程**：Model → Condition → Control → Sampling → Decode → Process → Output → Other

**节点**（49 个）：
- `PreviewImage`
- `EmptySD3LatentImage`
- `Note`
- `QwenImageDiffsynthControlnet`
- `KSampler` ★核心
- `VAEDecode` ★核心
- `ConditioningZeroOut`
- `SaveImage`
- `CLIPLoader`
- `UNETLoader` ★核心
- `INTConstant`
- `easy cleanGpuUsed`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `ImageScaleBy`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SaveImage`
- `SeedVR2VideoUpscaler`
- `Image Comparer (rgthree)`
- `Reroute`
- `LayerUtility: ImageReel`
- `LayerUtility: ImageReelComposit`
- `easy cleanGpuUsed`
- `PreviewImage`
- `Reroute`
- `Reroute`
- `Reroute`
- `ModelPatchLoader`
- `ImageScaleToTotalPixels`
- `AIO_Preprocessor`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `VAELoader`
- `Qwen3_VQA`
- `ShowText|pysssss`
- `CLIPTextEncode` ★核心
- `Fast Groups Bypasser (rgthree)`
- `LoadImage`

## 关键参数

- `seed` = `168967001473789`
- `steps` = `10`
- `cfg` = `1`
- `sampler_name` = `er_sde`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **53%**（26/49）

**有卡**：`EmptySD3LatentImage`、`QwenImageDiffsynthControlnet`、`KSampler`、`VAEDecode`、`ConditioningZeroOut`、`SaveImage`、`CLIPLoader`、`UNETLoader`、`INTConstant`、`easy cleanGpuUsed`、`ImageScaleBy`、`SeedVR2LoadDiTModel`、`SeedVR2LoadVAEModel`、`SeedVR2VideoUpscaler`、`LayerUtility: ImageReel`、`LayerUtility: ImageReelComposit`、`ModelPatchLoader`、`ImageScaleToTotalPixels`、`AIO_Preprocessor`、`LayerUtility: ImageScaleByAspectRatio V2`、`VAELoader`、`Qwen3_VQA`、`CLIPTextEncode`、`LoadImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、LoadImage、UNETLoader

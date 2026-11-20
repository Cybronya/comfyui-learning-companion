---
key: 平台全量/图片8倍精修高清放大(融合FlashVSR+SUPIR+SDUpscale+SeedVR2.5+模型_2000809892459970562.json
name: 图片8倍精修高清放大(融合FlashVSR+SUPIR+SDUpscale+SeedVR2.5+模型_2000809892459970562
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/图片8倍精修高清放大(融合FlashVSR+SUPIR+SDUpscale+SeedVR2.5+模型_2000809892459970562.json
hash: c6202196555ea5d5
coverage: 0.815789
learned_at: 2026-11-14 01:54:25
nodes: [Image Comparer (rgthree), SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, PrimitiveFloat, easy cleanGpuUsed, SUPIR_sample, SUPIR_model_loader_v2, Reroute, SUPIR_conditioner, SUPIR_encode, CheckpointLoaderSimple, GetNode, SUPIR_decode, CLIPTextEncode, CLIPTextEncode, SaveImage, easy cleanGpuUsed, UpscaleModelLoader, SeedVR2LoadDiTModel, SimpleMath+, easy imageSizeBySide, UltimateSDUpscale, SaveImage, UpscaleImageByUsingModel, SUPIR_first_stage, FlashVSRNode, LoadImage, SetNode, ColorMatch, Image Comparer (rgthree), GetImageSize+, ImageFromBatch+, FlashVSR_SM_KSampler, FlashVSR_SM_Model, PreviewImage, UpscaleModelLoader, SaveImage, LayerUtility: ImageScaleByAspectRatio V2]
patterns: []
missing: []
parameters: {"cfg": "fixed", "checkpoint": "1juggernautXL_juggXILightningByRD.safetensors", "denoise": 7, "sampler_name": 1, "scheduler": 3.5, "seed": 1472, "steps": 1837181187}
---

# 平台全量/图片8倍精修高清放大(融合FlashVSR+SUPIR+SDUpscale+SeedVR2.5+模型_2000809892459970562.json

> 来源文件 `comfyui_library/workflows/平台全量/图片8倍精修高清放大(融合FlashVSR+SUPIR+SDUpscale+SeedVR2.5+模型_2000809892459970562.json`

## 结构

**生成流程**：Model → Condition → Sampling → Process → Output → Other

**节点**（38 个）：
- `Image Comparer (rgthree)`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `PrimitiveFloat`
- `easy cleanGpuUsed`
- `SUPIR_sample`
- `SUPIR_model_loader_v2`
- `Reroute`
- `SUPIR_conditioner`
- `SUPIR_encode`
- `CheckpointLoaderSimple` ★核心
- `GetNode`
- `SUPIR_decode`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `SaveImage`
- `easy cleanGpuUsed`
- `UpscaleModelLoader`
- `SeedVR2LoadDiTModel`
- `SimpleMath+`
- `easy imageSizeBySide`
- `UltimateSDUpscale`
- `SaveImage`
- `UpscaleImageByUsingModel`
- `SUPIR_first_stage`
- `FlashVSRNode`
- `LoadImage`
- `SetNode`
- `ColorMatch`
- `Image Comparer (rgthree)`
- `GetImageSize+`
- `ImageFromBatch+`
- `FlashVSR_SM_KSampler` ★核心
- `FlashVSR_SM_Model`
- `PreviewImage`
- `UpscaleModelLoader`
- `SaveImage`
- `LayerUtility: ImageScaleByAspectRatio V2`

## 关键参数

- `checkpoint` = `1juggernautXL_juggXILightningByRD.safetensors`
- `seed` = `1472`
- `steps` = `1837181187`
- `cfg` = `fixed`
- `sampler_name` = `1`
- `scheduler` = `3.5`
- `denoise` = `7`

## 知识

覆盖率 **82%**（31/38）

**有卡**：`SeedVR2LoadVAEModel`、`SeedVR2VideoUpscaler`、`easy cleanGpuUsed`、`SUPIR_sample`、`SUPIR_model_loader_v2`、`SUPIR_conditioner`、`SUPIR_encode`、`CheckpointLoaderSimple`、`SUPIR_decode`、`CLIPTextEncode`、`SaveImage`、`UpscaleModelLoader`、`SeedVR2LoadDiTModel`、`SimpleMath+`、`easy imageSizeBySide`、`UltimateSDUpscale`、`UpscaleImageByUsingModel`、`SUPIR_first_stage`、`FlashVSRNode`、`LoadImage`、`ColorMatch`、`GetImageSize+`、`ImageFromBatch+`、`FlashVSR_SM_KSampler`、`FlashVSR_SM_Model`、`LayerUtility: ImageScaleByAspectRatio V2`

**用到的条目**：CheckpointLoaderSimple、CLIPTextEncode、LoadImage、FlashVSR_SM_KSampler、SeedVR2LoadDiTModel、SeedVR2LoadVAEModel、SeedVR2VideoUpscaler、SUPIR_decode

---
key: 平台全量/视频画质增强  视频高清放大 wan2.2 视频逐帧修复放大 SeedVR2 2.5 SeedVR2_2008011990899363841.json
name: 视频画质增强  视频高清放大 wan2.2 视频逐帧修复放大 SeedVR2 2.5 SeedVR2_2008011990899363841
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/视频画质增强  视频高清放大 wan2.2 视频逐帧修复放大 SeedVR2 2.5 SeedVR2_2008011990899363841.json
hash: 90099b48465ee59c
coverage: 0.702128
learned_at: 2026-11-14 02:40:12
nodes: [SetNode, SetNode, SetNode, SetNode, SetNode, SetNode, GetNode, GetNode, GetNode, VAEDecode, PathchSageAttentionKJ, CLIPLoader, ImageUpscaleWithModelBatched, RIFE VFI, CM_IntToFloat, VHS_VideoInfo, Int, GetNode, GetNode, VHS_VideoInfo, UNETLoader, LoraLoaderModelOnly, Display Any (rgthree), Display Any (rgthree), MathExpression|pysssss, GetNode, UpscaleModelLoader, LayerUtility: ImageScaleByAspectRatio V2, CLIPTextEncode, ModelSamplingSD3, VAEEncode, SeedVR2VideoUpscaler, LoraLoaderModelOnly, CLIPTextEncode, VAELoader, ClownsharKSampler_Beta, GetImageSizeAndCount, ImageFromBatch+, VHS_LoadVideo, Fast Groups Muter (rgthree), VHS_LoadVideo, Int, VHS_VideoCombine, VHS_VideoCombine, SeedVR2LoadVAEModel, SeedVR2LoadDiTModel, Fast Groups Muter (rgthree)]
patterns: []
missing: []
parameters: {"cfg": 4, "denoise": 1.0000000000000002, "sampler_name": -1, "scheduler": 0.20000000000000004, "seed": 0.5, "steps": "beta57"}
---

# 平台全量/视频画质增强  视频高清放大 wan2.2 视频逐帧修复放大 SeedVR2 2.5 SeedVR2_2008011990899363841.json

> 来源文件 `comfyui_library/workflows/平台全量/视频画质增强  视频高清放大 wan2.2 视频逐帧修复放大 SeedVR2 2.5 SeedVR2_2008011990899363841.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Other

**节点**（47 个）：
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `VAEDecode` ★核心
- `PathchSageAttentionKJ`
- `CLIPLoader`
- `ImageUpscaleWithModelBatched`
- `RIFE VFI`
- `CM_IntToFloat`
- `VHS_VideoInfo`
- `Int`
- `GetNode`
- `GetNode`
- `VHS_VideoInfo`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `Display Any (rgthree)`
- `Display Any (rgthree)`
- `MathExpression|pysssss`
- `GetNode`
- `UpscaleModelLoader`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `CLIPTextEncode` ★核心
- `ModelSamplingSD3`
- `VAEEncode` ★核心
- `SeedVR2VideoUpscaler`
- `LoraLoaderModelOnly` ★核心
- `CLIPTextEncode` ★核心
- `VAELoader`
- `ClownsharKSampler_Beta` ★核心
- `GetImageSizeAndCount`
- `ImageFromBatch+`
- `VHS_LoadVideo`
- `Fast Groups Muter (rgthree)`
- `VHS_LoadVideo`
- `Int`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `SeedVR2LoadVAEModel`
- `SeedVR2LoadDiTModel`
- `Fast Groups Muter (rgthree)`

## 关键参数

- `seed` = `0.5`
- `steps` = `beta57`
- `cfg` = `4`
- `sampler_name` = `-1`
- `scheduler` = `0.20000000000000004`
- `denoise` = `1.0000000000000002`

## 知识

覆盖率 **70%**（33/47）

**有卡**：`VAEDecode`、`PathchSageAttentionKJ`、`CLIPLoader`、`ImageUpscaleWithModelBatched`、`RIFE VFI`、`CM_IntToFloat`、`VHS_VideoInfo`、`Int`、`UNETLoader`、`LoraLoaderModelOnly`、`Display Any (rgthree)`、`MathExpression|pysssss`、`UpscaleModelLoader`、`LayerUtility: ImageScaleByAspectRatio V2`、`CLIPTextEncode`、`ModelSamplingSD3`、`VAEEncode`、`SeedVR2VideoUpscaler`、`VAELoader`、`ClownsharKSampler_Beta`、`GetImageSizeAndCount`、`ImageFromBatch+`、`VHS_LoadVideo`、`VHS_VideoCombine`、`SeedVR2LoadVAEModel`、`SeedVR2LoadDiTModel`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、CLIPTextEncode、UNETLoader、ClownsharKSampler_Beta、SeedVR2LoadDiTModel

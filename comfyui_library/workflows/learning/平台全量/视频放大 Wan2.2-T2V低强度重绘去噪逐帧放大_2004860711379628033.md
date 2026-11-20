---
key: 平台全量/视频放大 Wan2.2-T2V低强度重绘去噪逐帧放大_2004860711379628033.json
name: 视频放大 Wan2.2-T2V低强度重绘去噪逐帧放大_2004860711379628033
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/视频放大 Wan2.2-T2V低强度重绘去噪逐帧放大_2004860711379628033.json
hash: 4aabc0ff1b09b910
coverage: 0.66
learned_at: 2026-11-14 02:39:24
nodes: [SetNode, SetNode, SetNode, SetNode, SetNode, SetNode, GetNode, GetNode, GetNode, VAEDecode, Note, Int, Note, PathchSageAttentionKJ, CLIPLoader, ImageUpscaleWithModelBatched, RIFE VFI, CM_IntToFloat, GetImageSizeAndCount, ImageFromBatch+, VHS_VideoInfo, VHS_VideoCombine, VHS_LoadVideo, Fast Groups Muter (rgthree), SeedVR2VideoUpscaler, Int, GetNode, GetNode, VHS_VideoCombine, Note, VHS_VideoInfo, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, Fast Groups Muter (rgthree), Display Any (rgthree), Display Any (rgthree), MathExpression|pysssss, GetNode, UpscaleModelLoader, LayerUtility: ImageScaleByAspectRatio V2, CLIPTextEncode, CLIPTextEncode, ModelSamplingSD3, VAEEncode, VHS_LoadVideo, VAELoader, ClownsharKSampler_Beta]
patterns: []
missing: []
parameters: {"cfg": 4, "denoise": 1.0000000000000002, "sampler_name": -1, "scheduler": 0.20000000000000004, "seed": 0.5, "steps": "beta57"}
---

# 平台全量/视频放大 Wan2.2-T2V低强度重绘去噪逐帧放大_2004860711379628033.json

> 来源文件 `comfyui_library/workflows/平台全量/视频放大 Wan2.2-T2V低强度重绘去噪逐帧放大_2004860711379628033.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Other

**节点**（50 个）：
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
- `Note`
- `Int`
- `Note`
- `PathchSageAttentionKJ`
- `CLIPLoader`
- `ImageUpscaleWithModelBatched`
- `RIFE VFI`
- `CM_IntToFloat`
- `GetImageSizeAndCount`
- `ImageFromBatch+`
- `VHS_VideoInfo`
- `VHS_VideoCombine`
- `VHS_LoadVideo`
- `Fast Groups Muter (rgthree)`
- `SeedVR2VideoUpscaler`
- `Int`
- `GetNode`
- `GetNode`
- `VHS_VideoCombine`
- `Note`
- `VHS_VideoInfo`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `Fast Groups Muter (rgthree)`
- `Display Any (rgthree)`
- `Display Any (rgthree)`
- `MathExpression|pysssss`
- `GetNode`
- `UpscaleModelLoader`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `ModelSamplingSD3`
- `VAEEncode` ★核心
- `VHS_LoadVideo`
- `VAELoader`
- `ClownsharKSampler_Beta` ★核心

## 关键参数

- `seed` = `0.5`
- `steps` = `beta57`
- `cfg` = `4`
- `sampler_name` = `-1`
- `scheduler` = `0.20000000000000004`
- `denoise` = `1.0000000000000002`

## 知识

覆盖率 **66%**（33/50）

**有卡**：`VAEDecode`、`Int`、`PathchSageAttentionKJ`、`CLIPLoader`、`ImageUpscaleWithModelBatched`、`RIFE VFI`、`CM_IntToFloat`、`GetImageSizeAndCount`、`ImageFromBatch+`、`VHS_VideoInfo`、`VHS_VideoCombine`、`VHS_LoadVideo`、`SeedVR2VideoUpscaler`、`UNETLoader`、`LoraLoaderModelOnly`、`SeedVR2LoadDiTModel`、`SeedVR2LoadVAEModel`、`Display Any (rgthree)`、`MathExpression|pysssss`、`UpscaleModelLoader`、`LayerUtility: ImageScaleByAspectRatio V2`、`CLIPTextEncode`、`ModelSamplingSD3`、`VAEEncode`、`VAELoader`、`ClownsharKSampler_Beta`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、CLIPTextEncode、UNETLoader、ClownsharKSampler_Beta、SeedVR2LoadDiTModel

---
key: 平台全量/wan2.2 二次放大视频高清修复_1994312405784133634.json
name: wan2.2 二次放大视频高清修复_1994312405784133634
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/wan2.2 二次放大视频高清修复_1994312405784133634.json
hash: c9b249c2b19b8e35
coverage: 0.931034
learned_at: 2026-11-14 01:19:22
nodes: [PathchSageAttentionKJ, RIFE VFI, CLIPTextEncode, Note, VAEEncode, GetImageSizeAndCount, ImageUpscaleWithModelBatched, ImageFromBatch+, UNETLoader, MathExpression|pysssss, CM_IntToFloat, VHS_VideoInfoSource, Display Any (rgthree), LoraLoaderModelOnly, LoraLoaderModelOnly, CLIPLoader, ModelSamplingSD3, VAELoader, Note, LoraLoaderModelOnly, VAEDecode, UpscaleModelLoader, VHS_VideoCombine, VHS_VideoCombine, ClownsharKSampler_Beta, CLIPTextEncode, VHS_LoadVideo, Display Any (rgthree), ImageScale]
patterns: []
missing: []
parameters: {"cfg": 4, "denoise": 1.0000000000000002, "sampler_name": -1, "scheduler": 0.5300000000000001, "seed": 0.20000000000000004, "steps": "beta57"}
---

# 平台全量/wan2.2 二次放大视频高清修复_1994312405784133634.json

> 来源文件 `comfyui_library/workflows/平台全量/wan2.2 二次放大视频高清修复_1994312405784133634.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Other

**节点**（29 个）：
- `PathchSageAttentionKJ`
- `RIFE VFI`
- `CLIPTextEncode` ★核心
- `Note`
- `VAEEncode` ★核心
- `GetImageSizeAndCount`
- `ImageUpscaleWithModelBatched`
- `ImageFromBatch+`
- `UNETLoader` ★核心
- `MathExpression|pysssss`
- `CM_IntToFloat`
- `VHS_VideoInfoSource`
- `Display Any (rgthree)`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `CLIPLoader`
- `ModelSamplingSD3`
- `VAELoader`
- `Note`
- `LoraLoaderModelOnly` ★核心
- `VAEDecode` ★核心
- `UpscaleModelLoader`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `ClownsharKSampler_Beta` ★核心
- `CLIPTextEncode` ★核心
- `VHS_LoadVideo`
- `Display Any (rgthree)`
- `ImageScale`

## 关键参数

- `seed` = `0.20000000000000004`
- `steps` = `beta57`
- `cfg` = `4`
- `sampler_name` = `-1`
- `scheduler` = `0.5300000000000001`
- `denoise` = `1.0000000000000002`

## 知识

覆盖率 **93%**（27/29）

**有卡**：`PathchSageAttentionKJ`、`RIFE VFI`、`CLIPTextEncode`、`VAEEncode`、`GetImageSizeAndCount`、`ImageUpscaleWithModelBatched`、`ImageFromBatch+`、`UNETLoader`、`MathExpression|pysssss`、`CM_IntToFloat`、`VHS_VideoInfoSource`、`Display Any (rgthree)`、`LoraLoaderModelOnly`、`CLIPLoader`、`ModelSamplingSD3`、`VAELoader`、`VAEDecode`、`UpscaleModelLoader`、`VHS_VideoCombine`、`ClownsharKSampler_Beta`、`VHS_LoadVideo`、`ImageScale`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、CLIPTextEncode、UNETLoader、ClownsharKSampler_Beta、VAEEncode

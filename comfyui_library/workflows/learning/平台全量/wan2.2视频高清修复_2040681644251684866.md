---
key: 平台全量/wan2.2视频高清修复_2040681644251684866.json
name: wan2.2视频高清修复_2040681644251684866
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/wan2.2视频高清修复_2040681644251684866.json
hash: c731c5b915a70318
coverage: 0.9
learned_at: 2026-11-14 01:19:57
nodes: [PathchSageAttentionKJ, CLIPTextEncode, CLIPTextEncode, Note, VAEEncode, VAEDecode, GetImageSizeAndCount, VHS_VideoCombine, UpscaleModelLoader, ImageFromBatch+, UNETLoader, MathExpression|pysssss, VHS_VideoInfoSource, Display Any (rgthree), LoraLoaderModelOnly, LoraLoaderModelOnly, CLIPLoader, ModelSamplingSD3, VAELoader, Display Any (rgthree), Note, LayerUtility: ImageScaleByAspectRatio V2, Int, ClownsharKSampler_Beta, VHS_VideoCombine, Note, VHS_LoadVideo, ImageUpscaleWithModelBatched, CM_IntToFloat, RIFE VFI]
patterns: []
missing: []
parameters: {"cfg": 4, "denoise": 1.0000000000000002, "sampler_name": -1, "scheduler": 0.20000000000000004, "seed": 0.5, "steps": "beta57"}
---

# 平台全量/wan2.2视频高清修复_2040681644251684866.json

> 来源文件 `comfyui_library/workflows/平台全量/wan2.2视频高清修复_2040681644251684866.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Other

**节点**（30 个）：
- `PathchSageAttentionKJ`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `Note`
- `VAEEncode` ★核心
- `VAEDecode` ★核心
- `GetImageSizeAndCount`
- `VHS_VideoCombine`
- `UpscaleModelLoader`
- `ImageFromBatch+`
- `UNETLoader` ★核心
- `MathExpression|pysssss`
- `VHS_VideoInfoSource`
- `Display Any (rgthree)`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `CLIPLoader`
- `ModelSamplingSD3`
- `VAELoader`
- `Display Any (rgthree)`
- `Note`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `Int`
- `ClownsharKSampler_Beta` ★核心
- `VHS_VideoCombine`
- `Note`
- `VHS_LoadVideo`
- `ImageUpscaleWithModelBatched`
- `CM_IntToFloat`
- `RIFE VFI`

## 关键参数

- `seed` = `0.5`
- `steps` = `beta57`
- `cfg` = `4`
- `sampler_name` = `-1`
- `scheduler` = `0.20000000000000004`
- `denoise` = `1.0000000000000002`

## 知识

覆盖率 **90%**（27/30）

**有卡**：`PathchSageAttentionKJ`、`CLIPTextEncode`、`VAEEncode`、`VAEDecode`、`GetImageSizeAndCount`、`VHS_VideoCombine`、`UpscaleModelLoader`、`ImageFromBatch+`、`UNETLoader`、`MathExpression|pysssss`、`VHS_VideoInfoSource`、`Display Any (rgthree)`、`LoraLoaderModelOnly`、`CLIPLoader`、`ModelSamplingSD3`、`VAELoader`、`LayerUtility: ImageScaleByAspectRatio V2`、`Int`、`ClownsharKSampler_Beta`、`VHS_LoadVideo`、`ImageUpscaleWithModelBatched`、`CM_IntToFloat`、`RIFE VFI`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、CLIPTextEncode、UNETLoader、ClownsharKSampler_Beta、VAEEncode

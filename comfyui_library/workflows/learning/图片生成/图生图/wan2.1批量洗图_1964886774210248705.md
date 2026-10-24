---
key: 图片生成/图生图/wan2.1批量洗图_1964886774210248705.json
name: wan2.1批量洗图_1964886774210248705
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/wan2.1批量洗图_1964886774210248705.json
hash: 30f1a12de17d5cea
coverage: 0.862069
learned_at: 2026-10-23 11:45:51
nodes: [easy showAnything, UpscaleModelLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, CLIPTextEncode, PathchSageAttentionKJ, CLIPTextEncode, ImageUpscaleWithModel, VAEEncode, LayerUtility: ImageScaleRestore V2, Bjornulf_ShowInt, easy showAnything, RHExtractImage, SaveImage, RHUploadZip, RHBatchImages:, RHExtractImage, easy imageCount, PreviewImage, PreviewImage, easy forLoopStart, RH_Captioner, UNETLoader, CLIPLoader, VAELoader, SaveImage, easy forLoopEnd, KSampler, VAEDecode]
patterns: []
missing: []
parameters: {"cfg": 1, "denoise": 0.25000000000000006, "sampler_name": "uni_pc", "scheduler": "beta", "seed": 137393198808190, "steps": 10}
---

# 图片生成/图生图/wan2.1批量洗图_1964886774210248705.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/wan2.1批量洗图_1964886774210248705.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（29 个）：
- `easy showAnything`
- `UpscaleModelLoader`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `CLIPTextEncode` ★核心
- `PathchSageAttentionKJ`
- `CLIPTextEncode` ★核心
- `ImageUpscaleWithModel`
- `VAEEncode` ★核心
- `LayerUtility: ImageScaleRestore V2`
- `Bjornulf_ShowInt`
- `easy showAnything`
- `RHExtractImage`
- `SaveImage`
- `RHUploadZip`
- `RHBatchImages:`
- `RHExtractImage`
- `easy imageCount`
- `PreviewImage`
- `PreviewImage`
- `easy forLoopStart`
- `RH_Captioner`
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `SaveImage`
- `easy forLoopEnd`
- `KSampler` ★核心
- `VAEDecode` ★核心

## 关键参数

- `seed` = `137393198808190`
- `steps` = `10`
- `cfg` = `1`
- `sampler_name` = `uni_pc`
- `scheduler` = `beta`
- `denoise` = `0.25000000000000006`

## 知识

覆盖率 **86%**（25/29）

**有卡**：`UpscaleModelLoader`、`LoraLoaderModelOnly`、`CLIPTextEncode`、`PathchSageAttentionKJ`、`ImageUpscaleWithModel`、`VAEEncode`、`LayerUtility: ImageScaleRestore V2`、`Bjornulf_ShowInt`、`RHExtractImage`、`SaveImage`、`RHUploadZip`、`RHBatchImages:`、`easy imageCount`、`easy forLoopStart`、`RH_Captioner`、`UNETLoader`、`CLIPLoader`、`VAELoader`、`easy forLoopEnd`、`KSampler`、`VAEDecode`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、UNETLoader、VAEEncode

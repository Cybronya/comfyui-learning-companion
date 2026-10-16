---
key: 视频生成/图生视频/真王炸！wan2.2一键核爆_1955241155534340098.json
name: 真王炸！wan2.2一键核爆_1955241155534340098.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1955241155534340098.json
hash: 12feadea28dcdb57
coverage: 0.933333
learned_at: 2026-10-15 22:31:07
nodes: [PathchSageAttentionKJ, ModelSamplingSD3, PreviewImage, WanVideoNAG, CLIPLoader, ModelSamplingSD3, PathchSageAttentionKJ, WanImageToVideo, INTConstant, INTConstant, CLIPTextEncode, PreviewImage, ImageResizeKJv2, KSamplerAdvanced, KSamplerAdvanced, CLIPTextEncode, CR Text Replace, LoadImage, LoraLoaderModelOnly, LoraLoaderModelOnly, VAEDecode, LoraLoaderModelOnly, UNETLoader, VAELoader, UNETLoader, Display Any (rgthree), RH_Captioner, CR Text, GetImageRangeFromBatch, VHS_VideoCombine]
patterns: []
missing: []
parameters: {"cfg": 10, "denoise": "normal", "sampler_name": 1, "scheduler": "euler", "seed": "disable", "steps": "randomize"}
---

# 视频生成/图生视频/真王炸！wan2.2一键核爆_1955241155534340098.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1955241155534340098.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（30 个）：
- `PathchSageAttentionKJ`
- `ModelSamplingSD3`
- `PreviewImage`
- `WanVideoNAG`
- `CLIPLoader`
- `ModelSamplingSD3`
- `PathchSageAttentionKJ`
- `WanImageToVideo`
- `INTConstant`
- `INTConstant`
- `CLIPTextEncode` ★核心
- `PreviewImage`
- `ImageResizeKJv2`
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `CLIPTextEncode` ★核心
- `CR Text Replace`
- `LoadImage`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `VAEDecode` ★核心
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `VAELoader`
- `UNETLoader` ★核心
- `Display Any (rgthree)`
- `RH_Captioner`
- `CR Text`
- `GetImageRangeFromBatch`
- `VHS_VideoCombine`

## 关键参数

- `seed` = `disable`
- `steps` = `randomize`
- `cfg` = `10`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `normal`

## 知识

覆盖率 **93%**（28/30）

**有卡**：`PathchSageAttentionKJ`、`ModelSamplingSD3`、`WanVideoNAG`、`CLIPLoader`、`WanImageToVideo`、`INTConstant`、`CLIPTextEncode`、`ImageResizeKJv2`、`KSamplerAdvanced`、`CR Text Replace`、`LoadImage`、`LoraLoaderModelOnly`、`VAEDecode`、`UNETLoader`、`VAELoader`、`Display Any (rgthree)`、`RH_Captioner`、`CR Text`、`GetImageRangeFromBatch`、`VHS_VideoCombine`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerAdvanced

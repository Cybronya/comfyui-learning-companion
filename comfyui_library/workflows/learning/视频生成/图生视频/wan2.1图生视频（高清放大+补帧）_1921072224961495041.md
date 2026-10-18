---
key: 视频生成/图生视频/wan2.1图生视频（高清放大+补帧）_1921072224961495041.json
name: wan2.1图生视频（高清放大+补帧）_1921072224961495041.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/wan2.1图生视频（高清放大+补帧）_1921072224961495041.json
hash: 664e263d3c9f4ec3
coverage: 0.782609
learned_at: 2026-10-15 22:29:43
nodes: [Note, CLIPVisionEncode, CLIPVisionLoader, ImageUpscaleWithModel, UpscaleModelLoader, Note, PrimitiveInt, RIFE VFI, Note, VAEDecode, CLIPLoader, WanImageToVideo, LoadImage, LayerUtility: ImageScaleByAspectRatio V2, UNETLoader, Note, CLIPTextEncode, VAELoader, VHS_VideoCombine, CLIPTextEncode, KSampler, easy cleanGpuUsed, easy cleanGpuUsed]
patterns: []
missing: []
parameters: {"cfg": 6, "denoise": 1, "sampler_name": "uni_pc", "scheduler": "simple", "seed": 89821172915789, "steps": 20}
---

# 视频生成/图生视频/wan2.1图生视频（高清放大+补帧）_1921072224961495041.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1921072224961495041.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（23 个）：
- `Note`
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `ImageUpscaleWithModel`
- `UpscaleModelLoader`
- `Note`
- `PrimitiveInt`
- `RIFE VFI`
- `Note`
- `VAEDecode` ★核心
- `CLIPLoader`
- `WanImageToVideo`
- `LoadImage`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `UNETLoader` ★核心
- `Note`
- `CLIPTextEncode` ★核心
- `VAELoader`
- `VHS_VideoCombine`
- `CLIPTextEncode` ★核心
- `KSampler` ★核心
- `easy cleanGpuUsed`
- `easy cleanGpuUsed`

## 关键参数

- `seed` = `89821172915789`
- `steps` = `20`
- `cfg` = `6`
- `sampler_name` = `uni_pc`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **78%**（18/23）

**有卡**：`CLIPVisionEncode`、`CLIPVisionLoader`、`ImageUpscaleWithModel`、`UpscaleModelLoader`、`RIFE VFI`、`VAEDecode`、`CLIPLoader`、`WanImageToVideo`、`LoadImage`、`LayerUtility: ImageScaleByAspectRatio V2`、`UNETLoader`、`CLIPTextEncode`、`VAELoader`、`VHS_VideoCombine`、`KSampler`、`easy cleanGpuUsed`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、CLIPVisionEncode

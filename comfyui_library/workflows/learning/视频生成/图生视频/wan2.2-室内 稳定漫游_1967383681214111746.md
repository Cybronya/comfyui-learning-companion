---
key: 视频生成/图生视频/wan2.2-室内 稳定漫游_1967383681214111746.json
name: wan2.2-室内 稳定漫游_1967383681214111746.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/wan2.2-室内 稳定漫游_1967383681214111746.json
hash: 715ed24ce0dc83c1
coverage: 0.967742
learned_at: 2026-10-15 22:31:41
nodes: [CLIPVisionEncode, LayerUtility: ImageScaleByAspectRatio V2, easy int, VAELoader, CLIPVisionLoader, CLIPLoader, CLIPTextEncode, CLIPTextEncode, Text Concatenate, KSamplerAdvanced, ModelSamplingSD3, ModelSamplingSD3, UNETLoader, UNETLoader, SimpleMath+, LayerUtility: PurgeVRAM V2, easy showAnything, VAEDecode, LayerUtility: PurgeVRAM, LoadImage, RH_Captioner, Text Multiline, VHS_VideoCombine, ImageUpscaleWithModel, LayerUtility: ImageScaleByAspectRatio V2, UpscaleModelLoader, easy cleanGpuUsed, VHS_VideoCombine, WanImageToVideo, DF_Integer, KSamplerAdvanced]
patterns: []
missing: []
parameters: {"cfg": 30, "denoise": "simple", "sampler_name": 4, "scheduler": "euler", "seed": "disable", "steps": "fixed"}
---

# 视频生成/图生视频/wan2.2-室内 稳定漫游_1967383681214111746.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1967383681214111746.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（31 个）：
- `CLIPVisionEncode`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `easy int`
- `VAELoader`
- `CLIPVisionLoader`
- `CLIPLoader`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `Text Concatenate`
- `KSamplerAdvanced` ★核心
- `ModelSamplingSD3`
- `ModelSamplingSD3`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `SimpleMath+`
- `LayerUtility: PurgeVRAM V2`
- `easy showAnything`
- `VAEDecode` ★核心
- `LayerUtility: PurgeVRAM`
- `LoadImage`
- `RH_Captioner`
- `Text Multiline`
- `VHS_VideoCombine`
- `ImageUpscaleWithModel`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `UpscaleModelLoader`
- `easy cleanGpuUsed`
- `VHS_VideoCombine`
- `WanImageToVideo`
- `DF_Integer`
- `KSamplerAdvanced` ★核心

## 关键参数

- `seed` = `disable`
- `steps` = `fixed`
- `cfg` = `30`
- `sampler_name` = `4`
- `scheduler` = `euler`
- `denoise` = `simple`

## 知识

覆盖率 **97%**（30/31）

**有卡**：`CLIPVisionEncode`、`LayerUtility: ImageScaleByAspectRatio V2`、`easy int`、`VAELoader`、`CLIPVisionLoader`、`CLIPLoader`、`CLIPTextEncode`、`Text Concatenate`、`KSamplerAdvanced`、`ModelSamplingSD3`、`UNETLoader`、`SimpleMath+`、`LayerUtility: PurgeVRAM V2`、`VAEDecode`、`LayerUtility: PurgeVRAM`、`LoadImage`、`RH_Captioner`、`Text Multiline`、`VHS_VideoCombine`、`ImageUpscaleWithModel`、`UpscaleModelLoader`、`easy cleanGpuUsed`、`WanImageToVideo`、`DF_Integer`

**用到的条目**：VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerAdvanced、CLIPVisionEncode

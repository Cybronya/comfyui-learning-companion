---
key: 视频生成/图生视频/wan2.2 图生视频体验_1950070634309181442.json
name: wan2.2 图生视频体验_1950070634309181442.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/wan2.2 图生视频体验_1950070634309181442.json
hash: 4f671508201eed69
coverage: 0.84375
learned_at: 2026-10-15 22:30:52
nodes: [CLIPLoader, CLIPTextEncode, CLIPTextEncode, CLIPVisionEncode, SimpleMath+, WanImageToVideo, ModelSamplingSD3, KSamplerAdvanced, ModelSamplingSD3, VAEDecode, CLIPVisionLoader, easy cleanGpuUsed, VAELoader, PathchSageAttentionKJ, DF_Integer, LoadImage, LayerUtility: ImageScaleByAspectRatio V2, easy int, LayerUtility: PurgeVRAM, RH_Captioner, PatchModelPatcherOrder, TorchCompileModelWanVideoV2, UNETLoader, UNETLoader, KSamplerAdvanced, VHS_VideoCombine, JjkText, easy showAnything, PrimitiveBoolean, easy ifElse, JjkText, easy showAnything]
patterns: []
missing: []
parameters: {"cfg": 20, "denoise": "simple", "sampler_name": 3.5, "scheduler": "euler", "seed": "disable", "steps": "fixed"}
---

# 视频生成/图生视频/wan2.2 图生视频体验_1950070634309181442.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1950070634309181442.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（32 个）：
- `CLIPLoader`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `CLIPVisionEncode`
- `SimpleMath+`
- `WanImageToVideo`
- `ModelSamplingSD3`
- `KSamplerAdvanced` ★核心
- `ModelSamplingSD3`
- `VAEDecode` ★核心
- `CLIPVisionLoader`
- `easy cleanGpuUsed`
- `VAELoader`
- `PathchSageAttentionKJ`
- `DF_Integer`
- `LoadImage`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `easy int`
- `LayerUtility: PurgeVRAM`
- `RH_Captioner`
- `PatchModelPatcherOrder`
- `TorchCompileModelWanVideoV2`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `KSamplerAdvanced` ★核心
- `VHS_VideoCombine`
- `JjkText`
- `easy showAnything`
- `PrimitiveBoolean`
- `easy ifElse`
- `JjkText`
- `easy showAnything`

## 关键参数

- `seed` = `disable`
- `steps` = `fixed`
- `cfg` = `20`
- `sampler_name` = `3.5`
- `scheduler` = `euler`
- `denoise` = `simple`

## 知识

覆盖率 **84%**（27/32）

**有卡**：`CLIPLoader`、`CLIPTextEncode`、`CLIPVisionEncode`、`SimpleMath+`、`WanImageToVideo`、`ModelSamplingSD3`、`KSamplerAdvanced`、`VAEDecode`、`CLIPVisionLoader`、`easy cleanGpuUsed`、`VAELoader`、`PathchSageAttentionKJ`、`DF_Integer`、`LoadImage`、`LayerUtility: ImageScaleByAspectRatio V2`、`easy int`、`LayerUtility: PurgeVRAM`、`RH_Captioner`、`PatchModelPatcherOrder`、`TorchCompileModelWanVideoV2`、`UNETLoader`、`VHS_VideoCombine`、`PrimitiveBoolean`

**用到的条目**：VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerAdvanced、CLIPVisionEncode

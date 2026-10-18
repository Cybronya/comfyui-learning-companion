---
key: 视频生成/文生视频/【效果炸裂】wan2.2-14B最新稳定图生视频工作流_1950410149463769089.json
name: 【效果炸裂】wan2.2-14B最新稳定图生视频工作流_1950410149463769089.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/【效果炸裂】wan2.2-14B最新稳定图生视频工作流_1950410149463769089.json
hash: 66854b515a03afff
coverage: 0.885714
learned_at: 2026-10-15 22:43:35
nodes: [DF_Integer, easy showAnything, easy ifElse, TextBox, LayerUtility: PurgeVRAM, easy int, CLIPLoader, CLIPTextEncode, CLIPTextEncode, CLIPVisionEncode, SimpleMath+, WanImageToVideo, ModelSamplingSD3, KSamplerAdvanced, ModelSamplingSD3, KSamplerAdvanced, VAEDecode, CLIPVisionLoader, easy cleanGpuUsed, easy showAnything, CR Text Replace, RH_Captioner, VAELoader, PrimitiveBoolean, Note, LayerUtility: ImageScaleByAspectRatio V2, TorchCompileModelWanVideoV2, PathchSageAttentionKJ, TextBox, TextBox, LoadImage, VHS_VideoCombine, UNETLoader, UNETLoader, PatchModelPatcherOrder]
patterns: []
missing: []
parameters: {"cfg": 20, "denoise": "simple", "sampler_name": 3.5, "scheduler": "euler", "seed": "disable", "steps": "fixed"}
---

# 视频生成/文生视频/【效果炸裂】wan2.2-14B最新稳定图生视频工作流_1950410149463769089.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/1950410149463769089.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（35 个）：
- `DF_Integer`
- `easy showAnything`
- `easy ifElse`
- `TextBox`
- `LayerUtility: PurgeVRAM`
- `easy int`
- `CLIPLoader`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `CLIPVisionEncode`
- `SimpleMath+`
- `WanImageToVideo`
- `ModelSamplingSD3`
- `KSamplerAdvanced` ★核心
- `ModelSamplingSD3`
- `KSamplerAdvanced` ★核心
- `VAEDecode` ★核心
- `CLIPVisionLoader`
- `easy cleanGpuUsed`
- `easy showAnything`
- `CR Text Replace`
- `RH_Captioner`
- `VAELoader`
- `PrimitiveBoolean`
- `Note`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `TorchCompileModelWanVideoV2`
- `PathchSageAttentionKJ`
- `TextBox`
- `TextBox`
- `LoadImage`
- `VHS_VideoCombine`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `PatchModelPatcherOrder`

## 关键参数

- `seed` = `disable`
- `steps` = `fixed`
- `cfg` = `20`
- `sampler_name` = `3.5`
- `scheduler` = `euler`
- `denoise` = `simple`

## 知识

覆盖率 **89%**（31/35）

**有卡**：`DF_Integer`、`TextBox`、`LayerUtility: PurgeVRAM`、`easy int`、`CLIPLoader`、`CLIPTextEncode`、`CLIPVisionEncode`、`SimpleMath+`、`WanImageToVideo`、`ModelSamplingSD3`、`KSamplerAdvanced`、`VAEDecode`、`CLIPVisionLoader`、`easy cleanGpuUsed`、`CR Text Replace`、`RH_Captioner`、`VAELoader`、`PrimitiveBoolean`、`LayerUtility: ImageScaleByAspectRatio V2`、`TorchCompileModelWanVideoV2`、`PathchSageAttentionKJ`、`LoadImage`、`VHS_VideoCombine`、`UNETLoader`、`PatchModelPatcherOrder`

**用到的条目**：VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerAdvanced、CLIPVisionEncode

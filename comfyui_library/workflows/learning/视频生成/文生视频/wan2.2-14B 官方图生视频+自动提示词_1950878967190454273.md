---
key: 视频生成/文生视频/wan2.2-14B 官方图生视频+自动提示词_1950878967190454273.json
name: wan2.2-14B 官方图生视频+自动提示词_1950878967190454273
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/wan2.2-14B 官方图生视频+自动提示词_1950878967190454273.json
hash: c18058ce0bbeb0bf
coverage: 0.911765
learned_at: 2026-10-15 22:47:35
nodes: [DF_Integer, easy int, UNETLoader, UNETLoader, RH_Captioner, easy showAnything, easy showAnything, CR Text Replace, easy ifElse, TextBox, TextBox, PrimitiveBoolean, LayerUtility: ImageScaleByAspectRatio V2, PatchModelPatcherOrder, PathchSageAttentionKJ, TorchCompileModelWanVideoV2, CLIPLoader, easy cleanGpuUsed, CLIPVisionLoader, CLIPTextEncode, CLIPTextEncode, CLIPVisionEncode, VAELoader, SimpleMath+, WanImageToVideo, KSamplerAdvanced, ModelSamplingSD3, VHS_VideoCombine, LayerUtility: PurgeVRAM, KSamplerAdvanced, VAEDecode, ModelSamplingSD3, LoadImage, TextBox]
patterns: []
missing: []
parameters: {"cfg": 20, "denoise": "simple", "sampler_name": 3.5, "scheduler": "euler", "seed": "disable", "steps": "fixed"}
---

# 视频生成/文生视频/wan2.2-14B 官方图生视频+自动提示词_1950878967190454273.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/wan2.2-14B 官方图生视频+自动提示词_1950878967190454273.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（34 个）：
- `DF_Integer`
- `easy int`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `RH_Captioner`
- `easy showAnything`
- `easy showAnything`
- `CR Text Replace`
- `easy ifElse`
- `TextBox`
- `TextBox`
- `PrimitiveBoolean`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `PatchModelPatcherOrder`
- `PathchSageAttentionKJ`
- `TorchCompileModelWanVideoV2`
- `CLIPLoader`
- `easy cleanGpuUsed`
- `CLIPVisionLoader`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `CLIPVisionEncode`
- `VAELoader`
- `SimpleMath+`
- `WanImageToVideo`
- `KSamplerAdvanced` ★核心
- `ModelSamplingSD3`
- `VHS_VideoCombine`
- `LayerUtility: PurgeVRAM`
- `KSamplerAdvanced` ★核心
- `VAEDecode` ★核心
- `ModelSamplingSD3`
- `LoadImage`
- `TextBox`

## 关键参数

- `seed` = `disable`
- `steps` = `fixed`
- `cfg` = `20`
- `sampler_name` = `3.5`
- `scheduler` = `euler`
- `denoise` = `simple`

## 知识

覆盖率 **91%**（31/34）

**有卡**：`DF_Integer`、`easy int`、`UNETLoader`、`RH_Captioner`、`CR Text Replace`、`TextBox`、`PrimitiveBoolean`、`LayerUtility: ImageScaleByAspectRatio V2`、`PatchModelPatcherOrder`、`PathchSageAttentionKJ`、`TorchCompileModelWanVideoV2`、`CLIPLoader`、`easy cleanGpuUsed`、`CLIPVisionLoader`、`CLIPTextEncode`、`CLIPVisionEncode`、`VAELoader`、`SimpleMath+`、`WanImageToVideo`、`KSamplerAdvanced`、`ModelSamplingSD3`、`VHS_VideoCombine`、`LayerUtility: PurgeVRAM`、`VAEDecode`、`LoadImage`

**用到的条目**：VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerAdvanced、CLIPVisionEncode

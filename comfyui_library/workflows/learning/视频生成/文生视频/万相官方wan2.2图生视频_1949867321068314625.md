---
key: 视频生成/文生视频/万相官方wan2.2图生视频_1949867321068314625.json
name: 万相官方wan2.2图生视频_1949867321068314625.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/1949867321068314625.json
hash: ba8d636ce214655a
coverage: 0.891892
learned_at: 2026-10-15 22:43:33
nodes: [DF_Integer, LoadImage, easy showAnything, easy ifElse, TextBox, LayerUtility: PurgeVRAM, easy int, PathchSageAttentionKJ, PatchModelPatcherOrder, CLIPTextEncode, CLIPTextEncode, CLIPVisionEncode, SimpleMath+, WanImageToVideo, ModelSamplingSD3, KSamplerAdvanced, ModelSamplingSD3, KSamplerAdvanced, VAEDecode, VHS_VideoCombine, CLIPVisionLoader, easy cleanGpuUsed, easy showAnything, CR Text Replace, RH_Captioner, LayerUtility: ImageScaleByAspectRatio V2, VAELoader, TorchCompileModelWanVideoV2, TextBox, PrimitiveBoolean, Note, easy promptLine, UNETLoader, UNETLoader, easy promptLine, TextBox, CLIPLoader]
patterns: []
missing: []
parameters: {"cfg": 20, "denoise": "simple", "sampler_name": 3.5, "scheduler": "euler", "seed": "disable", "steps": "fixed"}
---

# 视频生成/文生视频/万相官方wan2.2图生视频_1949867321068314625.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/1949867321068314625.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（37 个）：
- `DF_Integer`
- `LoadImage`
- `easy showAnything`
- `easy ifElse`
- `TextBox`
- `LayerUtility: PurgeVRAM`
- `easy int`
- `PathchSageAttentionKJ`
- `PatchModelPatcherOrder`
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
- `VHS_VideoCombine`
- `CLIPVisionLoader`
- `easy cleanGpuUsed`
- `easy showAnything`
- `CR Text Replace`
- `RH_Captioner`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `VAELoader`
- `TorchCompileModelWanVideoV2`
- `TextBox`
- `PrimitiveBoolean`
- `Note`
- `easy promptLine`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `easy promptLine`
- `TextBox`
- `CLIPLoader`

## 关键参数

- `seed` = `disable`
- `steps` = `fixed`
- `cfg` = `20`
- `sampler_name` = `3.5`
- `scheduler` = `euler`
- `denoise` = `simple`

## 知识

覆盖率 **89%**（33/37）

**有卡**：`DF_Integer`、`LoadImage`、`TextBox`、`LayerUtility: PurgeVRAM`、`easy int`、`PathchSageAttentionKJ`、`PatchModelPatcherOrder`、`CLIPTextEncode`、`CLIPVisionEncode`、`SimpleMath+`、`WanImageToVideo`、`ModelSamplingSD3`、`KSamplerAdvanced`、`VAEDecode`、`VHS_VideoCombine`、`CLIPVisionLoader`、`easy cleanGpuUsed`、`CR Text Replace`、`RH_Captioner`、`LayerUtility: ImageScaleByAspectRatio V2`、`VAELoader`、`TorchCompileModelWanVideoV2`、`PrimitiveBoolean`、`easy promptLine`、`UNETLoader`、`CLIPLoader`

**用到的条目**：VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerAdvanced、CLIPVisionEncode

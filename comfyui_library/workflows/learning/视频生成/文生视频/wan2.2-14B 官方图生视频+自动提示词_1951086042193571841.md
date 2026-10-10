---
key: 视频生成/文生视频/wan2.2-14B 官方图生视频+自动提示词_1951086042193571841.json
name: wan2.2-14B 官方图生视频+自动提示词_1951086042193571841
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/wan2.2-14B 官方图生视频+自动提示词_1951086042193571841.json
hash: 902d7434c10588ff
coverage: 0.735294
learned_at: 2026-10-10 23:09:39
nodes: [DF_Integer, easy int, UNETLoader, UNETLoader, RH_Captioner, easy showAnything, easy showAnything, CR Text Replace, easy ifElse, TextBox, TextBox, PrimitiveBoolean, LayerUtility: ImageScaleByAspectRatio V2, PatchModelPatcherOrder, PathchSageAttentionKJ, TorchCompileModelWanVideoV2, CLIPLoader, easy cleanGpuUsed, CLIPVisionLoader, CLIPTextEncode, CLIPTextEncode, CLIPVisionEncode, VAELoader, SimpleMath+, WanImageToVideo, KSamplerAdvanced, ModelSamplingSD3, VHS_VideoCombine, LayerUtility: PurgeVRAM, KSamplerAdvanced, VAEDecode, ModelSamplingSD3, LoadImage, TextBox]
patterns: []
missing: [CR Text Replace, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: PurgeVRAM, SimpleMath+, easy cleanGpuUsed, easy int]
parameters: {"cfg": 20, "denoise": "simple", "sampler_name": 3.5, "scheduler": "euler", "seed": "disable", "steps": "fixed"}
discoveries: [次要节点 `CR Text Replace` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: PurgeVRAM` 知识库中没有该节点类型的任何知识, 次要节点 `SimpleMath+` 知识库中没有该节点类型的任何知识, 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识, 次要节点 `easy int` 知识库中没有该节点类型的任何知识]
---

# 视频生成/文生视频/wan2.2-14B 官方图生视频+自动提示词_1951086042193571841.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/wan2.2-14B 官方图生视频+自动提示词_1951086042193571841.json`

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

覆盖率 **74%**（25/34）

**有卡**：`DF_Integer`、`UNETLoader`、`RH_Captioner`、`TextBox`、`PrimitiveBoolean`、`PatchModelPatcherOrder`、`PathchSageAttentionKJ`、`TorchCompileModelWanVideoV2`、`CLIPLoader`、`CLIPVisionLoader`、`CLIPTextEncode`、`CLIPVisionEncode`、`VAELoader`、`WanImageToVideo`、`KSamplerAdvanced`、`ModelSamplingSD3`、`VHS_VideoCombine`、`VAEDecode`、`LoadImage`

**缺卡**（6）：`CR Text Replace`、`LayerUtility: ImageScaleByAspectRatio V2`、`LayerUtility: PurgeVRAM`、`SimpleMath+`、`easy cleanGpuUsed`、`easy int`

**用到的条目**：VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerAdvanced、CLIPVisionEncode

## 学习发现

- 次要节点 `CR Text Replace` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: PurgeVRAM` 知识库中没有该节点类型的任何知识
- 次要节点 `SimpleMath+` 知识库中没有该节点类型的任何知识
- 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识
- 次要节点 `easy int` 知识库中没有该节点类型的任何知识

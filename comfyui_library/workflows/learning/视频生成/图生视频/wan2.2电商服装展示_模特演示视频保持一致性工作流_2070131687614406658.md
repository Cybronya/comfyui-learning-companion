---
key: 视频生成/图生视频/wan2.2电商服装展示_模特演示视频保持一致性工作流_2070131687614406658.json
name: wan2.2电商服装展示_模特演示视频保持一致性工作流_2070131687614406658.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/wan2.2电商服装展示_模特演示视频保持一致性工作流_2070131687614406658.json
hash: 96e518847aa91aa0
coverage: 0.964286
learned_at: 2026-10-15 22:40:36
nodes: [PathchSageAttentionKJ, PathchSageAttentionKJ, ModelSamplingSD3, ModelSamplingSD3, PrimitiveInt, KSamplerAdvanced, KSamplerAdvanced, VAEDecode, CLIPTextEncode, CLIPTextEncode, SimpleMath+, INTConstant, UNETLoader, LoraLoaderModelOnly, VAELoader, CLIPLoader, PainterVRAM, WanImageToVideo, DownloadAndLoadGIMMVFIModel, GIMMVFI_interpolate, ImageConcatMulti, VHS_VideoCombine, LayerUtility: ImageScaleByAspectRatio V2, Int, UNETLoader, VHS_VideoCombine, Int, LoadImage]
patterns: []
missing: []
parameters: {"cfg": 12, "denoise": "simple", "sampler_name": 1, "scheduler": "euler", "seed": "disable", "steps": "fixed"}
---

# 视频生成/图生视频/wan2.2电商服装展示_模特演示视频保持一致性工作流_2070131687614406658.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2070131687614406658.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（28 个）：
- `PathchSageAttentionKJ`
- `PathchSageAttentionKJ`
- `ModelSamplingSD3`
- `ModelSamplingSD3`
- `PrimitiveInt`
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `VAEDecode` ★核心
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `SimpleMath+`
- `INTConstant`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `VAELoader`
- `CLIPLoader`
- `PainterVRAM`
- `WanImageToVideo`
- `DownloadAndLoadGIMMVFIModel`
- `GIMMVFI_interpolate`
- `ImageConcatMulti`
- `VHS_VideoCombine`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `Int`
- `UNETLoader` ★核心
- `VHS_VideoCombine`
- `Int`
- `LoadImage`

## 关键参数

- `seed` = `disable`
- `steps` = `fixed`
- `cfg` = `12`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `simple`

## 知识

覆盖率 **96%**（27/28）

**有卡**：`PathchSageAttentionKJ`、`ModelSamplingSD3`、`KSamplerAdvanced`、`VAEDecode`、`CLIPTextEncode`、`SimpleMath+`、`INTConstant`、`UNETLoader`、`LoraLoaderModelOnly`、`VAELoader`、`CLIPLoader`、`PainterVRAM`、`WanImageToVideo`、`DownloadAndLoadGIMMVFIModel`、`GIMMVFI_interpolate`、`ImageConcatMulti`、`VHS_VideoCombine`、`LayerUtility: ImageScaleByAspectRatio V2`、`Int`、`LoadImage`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerAdvanced

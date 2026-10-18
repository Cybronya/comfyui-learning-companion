---
key: 视频生成/图生视频/最强动漫模型DaSiWa8.1首帧中间帧和尾帧出视频_2009925117761032194.json
name: 最强动漫模型DaSiWa8.1首帧中间帧和尾帧出视频_2009925117761032194.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/最强动漫模型DaSiWa8.1首帧中间帧和尾帧出视频_2009925117761032194.json
hash: f3cc1be253582b77
coverage: 0.476923
learned_at: 2026-10-15 22:34:15
nodes: [PathchSageAttentionKJ, Note, easy showAnything, JoinStrings, ShowText|pysssss, Reroute, Reroute, ImageResizeKJv2, Reroute, ImageResizeKJv2, PathchSageAttentionKJ, Reroute, Reroute, Reroute, VAELoader, Reroute, Reroute, ModelPatchTorchSettings, Reroute, Reroute, ModelPatchTorchSettings, CLIPTextEncode, CLIPTextEncode, Reroute, Reroute, Reroute, Reroute, Reroute, Note, Reroute, Reroute, KSamplerAdvanced, KSamplerAdvanced, VAEDecode, Reroute, Reroute, Reroute, INTConstant, Note, Note, Reroute, INTConstant, TextInput_, Reroute, Reroute, VHS_VideoCombine, Int, Note, PrimitiveInt, LayerUtility: ImageScaleByAspectRatio V2, ImageBatchMulti, ImageConcatMulti, GetImagesFromBatchIndexed, PreviewImage, WanMultiFrameRefToVideo, Reroute, CLIPLoader, Fast Groups Bypasser (rgthree), UNETLoader, UNETLoader, RIFE VFI, LoadImage, LoadImage, LoadImage, Qwen3_VQA]
patterns: []
missing: []
parameters: {"cfg": 6, "denoise": "simple", "sampler_name": 1, "scheduler": "euler", "seed": "disable", "steps": "fixed"}
---

# 视频生成/图生视频/最强动漫模型DaSiWa8.1首帧中间帧和尾帧出视频_2009925117761032194.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2009925117761032194.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（65 个）：
- `PathchSageAttentionKJ`
- `Note`
- `easy showAnything`
- `JoinStrings`
- `ShowText|pysssss`
- `Reroute`
- `Reroute`
- `ImageResizeKJv2`
- `Reroute`
- `ImageResizeKJv2`
- `PathchSageAttentionKJ`
- `Reroute`
- `Reroute`
- `Reroute`
- `VAELoader`
- `Reroute`
- `Reroute`
- `ModelPatchTorchSettings`
- `Reroute`
- `Reroute`
- `ModelPatchTorchSettings`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Note`
- `Reroute`
- `Reroute`
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `VAEDecode` ★核心
- `Reroute`
- `Reroute`
- `Reroute`
- `INTConstant`
- `Note`
- `Note`
- `Reroute`
- `INTConstant`
- `TextInput_`
- `Reroute`
- `Reroute`
- `VHS_VideoCombine`
- `Int`
- `Note`
- `PrimitiveInt`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `ImageBatchMulti`
- `ImageConcatMulti`
- `GetImagesFromBatchIndexed`
- `PreviewImage`
- `WanMultiFrameRefToVideo`
- `Reroute`
- `CLIPLoader`
- `Fast Groups Bypasser (rgthree)`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `RIFE VFI`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `Qwen3_VQA`

## 关键参数

- `seed` = `disable`
- `steps` = `fixed`
- `cfg` = `6`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `simple`

## 知识

覆盖率 **48%**（31/65）

**有卡**：`PathchSageAttentionKJ`、`JoinStrings`、`ImageResizeKJv2`、`VAELoader`、`ModelPatchTorchSettings`、`CLIPTextEncode`、`KSamplerAdvanced`、`VAEDecode`、`INTConstant`、`TextInput_`、`VHS_VideoCombine`、`Int`、`LayerUtility: ImageScaleByAspectRatio V2`、`ImageBatchMulti`、`ImageConcatMulti`、`GetImagesFromBatchIndexed`、`WanMultiFrameRefToVideo`、`CLIPLoader`、`UNETLoader`、`RIFE VFI`、`LoadImage`、`Qwen3_VQA`

**用到的条目**：VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、LayerUtility: ImageScaleByAspectRatio V2、KSamplerAdvanced

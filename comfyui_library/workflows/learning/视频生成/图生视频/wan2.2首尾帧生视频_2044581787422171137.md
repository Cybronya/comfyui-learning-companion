---
key: 视频生成/图生视频/wan2.2首尾帧生视频_2044581787422171137.json
name: wan2.2首尾帧生视频_2044581787422171137.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2044581787422171137.json
hash: 83aa92ccfe3d1a15
coverage: 1
learned_at: 2026-10-15 22:36:39
nodes: [LoadImage, LoadImage, VAELoader, UNETLoader, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, PathchSageAttentionKJ, PathchSageAttentionKJ, ModelPatchTorchSettings, ModelPatchTorchSettings, CLIPVisionLoader, CLIPVisionEncode, CLIPVisionEncode, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: ImageScaleByAspectRatio V2, VAEDecode, WanMoeKSampler, WanFirstLastFrameToVideo, Int, CLIPLoader, VHS_VideoCombine, CLIPTextEncode, CLIPTextEncode]
patterns: []
missing: []
parameters: {"cfg": 3, "denoise": "euler_ancestral", "sampler_name": 1, "scheduler": 1, "seed": 0.875, "steps": "fixed"}
---

# 视频生成/图生视频/wan2.2首尾帧生视频_2044581787422171137.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2044581787422171137.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（24 个）：
- `LoadImage`
- `LoadImage`
- `VAELoader`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `PathchSageAttentionKJ`
- `PathchSageAttentionKJ`
- `ModelPatchTorchSettings`
- `ModelPatchTorchSettings`
- `CLIPVisionLoader`
- `CLIPVisionEncode`
- `CLIPVisionEncode`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `VAEDecode` ★核心
- `WanMoeKSampler` ★核心
- `WanFirstLastFrameToVideo`
- `Int`
- `CLIPLoader`
- `VHS_VideoCombine`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心

## 关键参数

- `seed` = `0.875`
- `steps` = `fixed`
- `cfg` = `3`
- `sampler_name` = `1`
- `scheduler` = `1`
- `denoise` = `euler_ancestral`

## 知识

覆盖率 **100%**（24/24）

**有卡**：`LoadImage`、`VAELoader`、`UNETLoader`、`LoraLoaderModelOnly`、`PathchSageAttentionKJ`、`ModelPatchTorchSettings`、`CLIPVisionLoader`、`CLIPVisionEncode`、`LayerUtility: ImageScaleByAspectRatio V2`、`VAEDecode`、`WanMoeKSampler`、`WanFirstLastFrameToVideo`、`Int`、`CLIPLoader`、`VHS_VideoCombine`、`CLIPTextEncode`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、WanMoeKSampler

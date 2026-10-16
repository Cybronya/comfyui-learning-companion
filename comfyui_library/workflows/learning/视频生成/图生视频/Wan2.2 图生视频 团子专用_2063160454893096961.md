---
key: 视频生成/图生视频/Wan2.2 图生视频 团子专用_2063160454893096961.json
name: Wan2.2 图生视频 团子专用_2063160454893096961.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2063160454893096961.json
hash: a4b7f8c36b01dfa4
coverage: 0.814815
learned_at: 2026-10-15 22:39:10
nodes: [VAELoader, WanImageToVideo, LoraLoaderModelOnly, EmptyHunyuanLatentVideo, PathchSageAttentionKJ, ModelPatchTorchSettings, PathchSageAttentionKJ, ModelPatchTorchSettings, CLIPLoader, LoraLoaderModelOnly, Note, LoadImage, LoraLoaderModelOnly, PreviewImage, UNETLoader, UNETLoader, FL_RIFE, Fast Groups Bypasser (rgthree), Fast Groups Bypasser (rgthree), VHS_VideoCombine, VAEDecode, PlaySound|pysssss, Note, LayerUtility: ImageScaleByAspectRatio V2, CLIPTextEncode, CLIPTextEncode, WanMoeKSampler]
patterns: []
missing: []
parameters: {"cfg": 6, "denoise": "euler_ancestral", "sampler_name": 1, "scheduler": 1, "seed": 0.9, "steps": "randomize"}
---

# 视频生成/图生视频/Wan2.2 图生视频 团子专用_2063160454893096961.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2063160454893096961.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（27 个）：
- `VAELoader`
- `WanImageToVideo`
- `LoraLoaderModelOnly` ★核心
- `EmptyHunyuanLatentVideo`
- `PathchSageAttentionKJ`
- `ModelPatchTorchSettings`
- `PathchSageAttentionKJ`
- `ModelPatchTorchSettings`
- `CLIPLoader`
- `LoraLoaderModelOnly` ★核心
- `Note`
- `LoadImage`
- `LoraLoaderModelOnly` ★核心
- `PreviewImage`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `FL_RIFE`
- `Fast Groups Bypasser (rgthree)`
- `Fast Groups Bypasser (rgthree)`
- `VHS_VideoCombine`
- `VAEDecode` ★核心
- `PlaySound|pysssss`
- `Note`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `WanMoeKSampler` ★核心

## 关键参数

- `seed` = `0.9`
- `steps` = `randomize`
- `cfg` = `6`
- `sampler_name` = `1`
- `scheduler` = `1`
- `denoise` = `euler_ancestral`

## 知识

覆盖率 **81%**（22/27）

**有卡**：`VAELoader`、`WanImageToVideo`、`LoraLoaderModelOnly`、`EmptyHunyuanLatentVideo`、`PathchSageAttentionKJ`、`ModelPatchTorchSettings`、`CLIPLoader`、`LoadImage`、`UNETLoader`、`FL_RIFE`、`VHS_VideoCombine`、`VAEDecode`、`PlaySound|pysssss`、`LayerUtility: ImageScaleByAspectRatio V2`、`CLIPTextEncode`、`WanMoeKSampler`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、WanMoeKSampler

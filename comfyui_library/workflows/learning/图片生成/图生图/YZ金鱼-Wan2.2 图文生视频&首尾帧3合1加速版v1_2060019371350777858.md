---
key: 图片生成/图生图/YZ金鱼-Wan2.2 图文生视频&首尾帧3合1加速版v1_2060019371350777858.json
name: YZ金鱼-Wan2.2 图文生视频&首尾帧3合1加速版v1_2060019371350777858
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/YZ金鱼-Wan2.2 图文生视频&首尾帧3合1加速版v1_2060019371350777858.json
hash: f1f6ec253f3e078c
coverage: 0.793103
learned_at: 2026-10-23 11:28:54
nodes: [VAELoader, WanImageToVideo, LoraLoaderModelOnly, EmptyHunyuanLatentVideo, PathchSageAttentionKJ, ModelPatchTorchSettings, PathchSageAttentionKJ, ModelPatchTorchSettings, VHS_VideoCombine, Note, VHS_VideoCombine, CLIPLoader, LoraLoaderModelOnly, CLIPTextEncode, Note, LoadImage, CLIPTextEncode, LoraLoaderModelOnly, MarkdownNote, PlaySound|pysssss, PreviewImage, WanMoeKSampler, UNETLoader, UNETLoader, VAEDecode, LayerUtility: ImageScaleByAspectRatio V2, FL_RIFE, Fast Groups Bypasser (rgthree), Fast Groups Bypasser (rgthree)]
patterns: []
missing: []
parameters: {"cfg": 6, "denoise": "euler_ancestral", "sampler_name": 1, "scheduler": 1, "seed": 0.9, "steps": "fixed"}
---

# 图片生成/图生图/YZ金鱼-Wan2.2 图文生视频&首尾帧3合1加速版v1_2060019371350777858.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/YZ金鱼-Wan2.2 图文生视频&首尾帧3合1加速版v1_2060019371350777858.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（29 个）：
- `VAELoader`
- `WanImageToVideo`
- `LoraLoaderModelOnly` ★核心
- `EmptyHunyuanLatentVideo`
- `PathchSageAttentionKJ`
- `ModelPatchTorchSettings`
- `PathchSageAttentionKJ`
- `ModelPatchTorchSettings`
- `VHS_VideoCombine`
- `Note`
- `VHS_VideoCombine`
- `CLIPLoader`
- `LoraLoaderModelOnly` ★核心
- `CLIPTextEncode` ★核心
- `Note`
- `LoadImage`
- `CLIPTextEncode` ★核心
- `LoraLoaderModelOnly` ★核心
- `MarkdownNote`
- `PlaySound|pysssss`
- `PreviewImage`
- `WanMoeKSampler` ★核心
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `VAEDecode` ★核心
- `LayerUtility: ImageScaleByAspectRatio V2`
- `FL_RIFE`
- `Fast Groups Bypasser (rgthree)`
- `Fast Groups Bypasser (rgthree)`

## 关键参数

- `seed` = `0.9`
- `steps` = `fixed`
- `cfg` = `6`
- `sampler_name` = `1`
- `scheduler` = `1`
- `denoise` = `euler_ancestral`

## 知识

覆盖率 **79%**（23/29）

**有卡**：`VAELoader`、`WanImageToVideo`、`LoraLoaderModelOnly`、`EmptyHunyuanLatentVideo`、`PathchSageAttentionKJ`、`ModelPatchTorchSettings`、`VHS_VideoCombine`、`CLIPLoader`、`CLIPTextEncode`、`LoadImage`、`PlaySound|pysssss`、`WanMoeKSampler`、`UNETLoader`、`VAEDecode`、`LayerUtility: ImageScaleByAspectRatio V2`、`FL_RIFE`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、WanMoeKSampler

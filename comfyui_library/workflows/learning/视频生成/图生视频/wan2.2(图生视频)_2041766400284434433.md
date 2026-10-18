---
key: 视频生成/图生视频/wan2.2(图生视频)_2041766400284434433.json
name: wan2.2(图生视频)_2041766400284434433.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/wan2.2(图生视频)_2041766400284434433.json
hash: 391be83e675f058a
coverage: 0.909091
learned_at: 2026-10-15 22:36:22
nodes: [UNETLoader, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, ModelPatchTorchSettings, ModelPatchTorchSettings, CLIPLoader, WanImageToVideo, VAELoader, VAEDecode, WanMoeKSampler, LayerUtility: ImageScaleByAspectRatio V2, Note, Note, CLIPTextEncode, LoadImage, CLIPTextEncode, PathchSageAttentionKJ, PathchSageAttentionKJ, EmptyHunyuanLatentVideo, PlaySound|pysssss, VHS_VideoCombine]
patterns: []
missing: []
parameters: {"cfg": 3, "denoise": "euler_ancestral", "sampler_name": 1, "scheduler": 1, "seed": 0.9, "steps": "fixed"}
---

# 视频生成/图生视频/wan2.2(图生视频)_2041766400284434433.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2041766400284434433.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（22 个）：
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `ModelPatchTorchSettings`
- `ModelPatchTorchSettings`
- `CLIPLoader`
- `WanImageToVideo`
- `VAELoader`
- `VAEDecode` ★核心
- `WanMoeKSampler` ★核心
- `LayerUtility: ImageScaleByAspectRatio V2`
- `Note`
- `Note`
- `CLIPTextEncode` ★核心
- `LoadImage`
- `CLIPTextEncode` ★核心
- `PathchSageAttentionKJ`
- `PathchSageAttentionKJ`
- `EmptyHunyuanLatentVideo`
- `PlaySound|pysssss`
- `VHS_VideoCombine`

## 关键参数

- `seed` = `0.9`
- `steps` = `fixed`
- `cfg` = `3`
- `sampler_name` = `1`
- `scheduler` = `1`
- `denoise` = `euler_ancestral`

## 知识

覆盖率 **91%**（20/22）

**有卡**：`UNETLoader`、`LoraLoaderModelOnly`、`ModelPatchTorchSettings`、`CLIPLoader`、`WanImageToVideo`、`VAELoader`、`VAEDecode`、`WanMoeKSampler`、`LayerUtility: ImageScaleByAspectRatio V2`、`CLIPTextEncode`、`LoadImage`、`PathchSageAttentionKJ`、`EmptyHunyuanLatentVideo`、`PlaySound|pysssss`、`VHS_VideoCombine`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、WanMoeKSampler

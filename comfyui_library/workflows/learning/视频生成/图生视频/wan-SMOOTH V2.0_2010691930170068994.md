---
key: 视频生成/图生视频/wan-SMOOTH V2.0_2010691930170068994.json
name: wan-SMOOTH V2.0_2010691930170068994.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2010691930170068994.json
hash: 6d960c9154f66ec1
coverage: 1
learned_at: 2026-10-15 22:34:18
nodes: [VAELoader, CLIPLoader, ModelSamplingSD3, ModelSamplingSD3, PathchSageAttentionKJ, CLIPTextEncode, CLIPTextEncode, VAEDecode, ImageListToBatch+, CLIPVisionLoader, CLIPVisionEncode, WanFirstLastFrameToVideo, UNETLoader, UNETLoader, LoraLoaderModelOnly, VHS_VideoCombine, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, PathchSageAttentionKJ, LoraLoaderModelOnly, WanMoeKSampler]
patterns: []
missing: []
parameters: {"cfg": 6, "denoise": "euler", "sampler_name": 1, "scheduler": 1, "seed": 0.9, "steps": "fixed"}
---

# 视频生成/图生视频/wan-SMOOTH V2.0_2010691930170068994.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2010691930170068994.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（21 个）：
- `VAELoader`
- `CLIPLoader`
- `ModelSamplingSD3`
- `ModelSamplingSD3`
- `PathchSageAttentionKJ`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `VAEDecode` ★核心
- `ImageListToBatch+`
- `CLIPVisionLoader`
- `CLIPVisionEncode`
- `WanFirstLastFrameToVideo`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `VHS_VideoCombine`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `PathchSageAttentionKJ`
- `LoraLoaderModelOnly` ★核心
- `WanMoeKSampler` ★核心

## 关键参数

- `seed` = `0.9`
- `steps` = `fixed`
- `cfg` = `6`
- `sampler_name` = `1`
- `scheduler` = `1`
- `denoise` = `euler`

## 知识

覆盖率 **100%**（21/21）

**有卡**：`VAELoader`、`CLIPLoader`、`ModelSamplingSD3`、`PathchSageAttentionKJ`、`CLIPTextEncode`、`VAEDecode`、`ImageListToBatch+`、`CLIPVisionLoader`、`CLIPVisionEncode`、`WanFirstLastFrameToVideo`、`UNETLoader`、`LoraLoaderModelOnly`、`VHS_VideoCombine`、`LayerUtility: ImageScaleByAspectRatio V2`、`LoadImage`、`WanMoeKSampler`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、WanMoeKSampler

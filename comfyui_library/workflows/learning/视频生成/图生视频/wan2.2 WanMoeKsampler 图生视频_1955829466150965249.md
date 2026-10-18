---
key: 视频生成/图生视频/wan2.2 WanMoeKsampler 图生视频_1955829466150965249.json
name: wan2.2 WanMoeKsampler 图生视频_1955829466150965249.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/wan2.2 WanMoeKsampler 图生视频_1955829466150965249.json
hash: 482ef746fa2c76f2
coverage: 1
learned_at: 2026-10-15 22:31:10
nodes: [CLIPTextEncode, CLIPTextEncode, LoraLoaderModelOnly, UNETLoader, WanImageToVideo, LoadImage, CLIPLoader, VAELoader, JWInteger, LayerUtility: ImageScaleByAspectRatio V2, PathchSageAttentionKJ, PathchSageAttentionKJ, ModelSamplingSD3, ModelSamplingSD3, VAEDecode, VHS_VideoCombine, LoraLoaderModelOnly, UNETLoader, CR Text, WanMoeKSampler]
patterns: []
missing: []
parameters: {"cfg": 10, "denoise": "euler", "sampler_name": 3.5, "scheduler": 1, "seed": 0.9, "steps": "randomize"}
---

# 视频生成/图生视频/wan2.2 WanMoeKsampler 图生视频_1955829466150965249.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1955829466150965249.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（20 个）：
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `WanImageToVideo`
- `LoadImage`
- `CLIPLoader`
- `VAELoader`
- `JWInteger`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `PathchSageAttentionKJ`
- `PathchSageAttentionKJ`
- `ModelSamplingSD3`
- `ModelSamplingSD3`
- `VAEDecode` ★核心
- `VHS_VideoCombine`
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `CR Text`
- `WanMoeKSampler` ★核心

## 关键参数

- `seed` = `0.9`
- `steps` = `randomize`
- `cfg` = `10`
- `sampler_name` = `3.5`
- `scheduler` = `1`
- `denoise` = `euler`

## 知识

覆盖率 **100%**（20/20）

**有卡**：`CLIPTextEncode`、`LoraLoaderModelOnly`、`UNETLoader`、`WanImageToVideo`、`LoadImage`、`CLIPLoader`、`VAELoader`、`JWInteger`、`LayerUtility: ImageScaleByAspectRatio V2`、`PathchSageAttentionKJ`、`ModelSamplingSD3`、`VAEDecode`、`VHS_VideoCombine`、`CR Text`、`WanMoeKSampler`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、WanMoeKSampler

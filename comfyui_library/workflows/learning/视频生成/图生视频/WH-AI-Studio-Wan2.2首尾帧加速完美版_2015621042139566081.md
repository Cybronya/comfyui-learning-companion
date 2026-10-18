---
key: 视频生成/图生视频/WH-AI-Studio-Wan2.2首尾帧加速完美版_2015621042139566081.json
name: WH-AI-Studio-Wan2.2首尾帧加速完美版_2015621042139566081.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/WH-AI-Studio-Wan2.2首尾帧加速完美版_2015621042139566081.json
hash: adbebb9dcfa67cc9
coverage: 0.969697
learned_at: 2026-10-15 22:34:39
nodes: [PathchSageAttentionKJ, ModelSamplingSD3, CLIPLoader, VAELoader, CLIPVisionLoader, CLIPTextEncode, CLIPVisionEncode, ModelSamplingSD3, ImpactInt, ImpactInt, ImpactInt, ImpactInt, PathchSageAttentionKJ, SimpleMath+, UNETLoader, Reroute, CLIPVisionEncode, ImageResizeKJv2, WanVideoNAG, ImageResizeKJ, WanFirstLastFrameToVideo, SimpleMath+, UNETLoader, CLIPTextEncode, LoraLoaderModelOnly, LoraLoaderModelOnly, KSamplerAdvanced, VAEDecode, LoadImage, LoadImage, VHS_VideoCombine, CR Text, KSamplerAdvanced]
patterns: []
missing: []
parameters: {"cfg": 8, "denoise": "simple", "sampler_name": 1, "scheduler": "lcm", "seed": "enable", "steps": "randomize"}
---

# 视频生成/图生视频/WH-AI-Studio-Wan2.2首尾帧加速完美版_2015621042139566081.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2015621042139566081.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（33 个）：
- `PathchSageAttentionKJ`
- `ModelSamplingSD3`
- `CLIPLoader`
- `VAELoader`
- `CLIPVisionLoader`
- `CLIPTextEncode` ★核心
- `CLIPVisionEncode`
- `ModelSamplingSD3`
- `ImpactInt`
- `ImpactInt`
- `ImpactInt`
- `ImpactInt`
- `PathchSageAttentionKJ`
- `SimpleMath+`
- `UNETLoader` ★核心
- `Reroute`
- `CLIPVisionEncode`
- `ImageResizeKJv2`
- `WanVideoNAG`
- `ImageResizeKJ`
- `WanFirstLastFrameToVideo`
- `SimpleMath+`
- `UNETLoader` ★核心
- `CLIPTextEncode` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `KSamplerAdvanced` ★核心
- `VAEDecode` ★核心
- `LoadImage`
- `LoadImage`
- `VHS_VideoCombine`
- `CR Text`
- `KSamplerAdvanced` ★核心

## 关键参数

- `seed` = `enable`
- `steps` = `randomize`
- `cfg` = `8`
- `sampler_name` = `1`
- `scheduler` = `lcm`
- `denoise` = `simple`

## 知识

覆盖率 **97%**（32/33）

**有卡**：`PathchSageAttentionKJ`、`ModelSamplingSD3`、`CLIPLoader`、`VAELoader`、`CLIPVisionLoader`、`CLIPTextEncode`、`CLIPVisionEncode`、`ImpactInt`、`SimpleMath+`、`UNETLoader`、`ImageResizeKJv2`、`WanVideoNAG`、`ImageResizeKJ`、`WanFirstLastFrameToVideo`、`LoraLoaderModelOnly`、`KSamplerAdvanced`、`VAEDecode`、`LoadImage`、`VHS_VideoCombine`、`CR Text`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerAdvanced

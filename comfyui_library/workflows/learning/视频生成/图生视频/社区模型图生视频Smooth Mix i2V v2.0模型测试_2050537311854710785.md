---
key: 视频生成/图生视频/社区模型图生视频Smooth Mix i2V v2.0模型测试_2050537311854710785.json
name: 社区模型图生视频Smooth Mix i2V v2.0模型测试_2050537311854710785.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/社区模型图生视频Smooth Mix i2V v2.0模型测试_2050537311854710785.json
hash: d7b0d85ebec66cde
coverage: 1
learned_at: 2026-10-15 22:37:18
nodes: [CLIPLoader, KSamplerAdvanced, ModelSamplingSD3, ModelSamplingSD3, KSamplerAdvanced, CLIPTextEncode, VAELoader, VAEDecode, VHS_VideoCombine, WanImageToVideo, UNETLoader, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LayerUtility: ImageScaleByAspectRatio V2, CLIPTextEncode, LoadImage]
patterns: []
missing: []
parameters: {"cfg": 6, "denoise": "simple", "sampler_name": 1, "scheduler": "euler", "seed": "disable", "steps": "randomize"}
---

# 视频生成/图生视频/社区模型图生视频Smooth Mix i2V v2.0模型测试_2050537311854710785.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2050537311854710785.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（17 个）：
- `CLIPLoader`
- `KSamplerAdvanced` ★核心
- `ModelSamplingSD3`
- `ModelSamplingSD3`
- `KSamplerAdvanced` ★核心
- `CLIPTextEncode` ★核心
- `VAELoader`
- `VAEDecode` ★核心
- `VHS_VideoCombine`
- `WanImageToVideo`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LayerUtility: ImageScaleByAspectRatio V2`
- `CLIPTextEncode` ★核心
- `LoadImage`

## 关键参数

- `seed` = `disable`
- `steps` = `randomize`
- `cfg` = `6`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `simple`

## 知识

覆盖率 **100%**（17/17）

**有卡**：`CLIPLoader`、`KSamplerAdvanced`、`ModelSamplingSD3`、`CLIPTextEncode`、`VAELoader`、`VAEDecode`、`VHS_VideoCombine`、`WanImageToVideo`、`UNETLoader`、`LoraLoaderModelOnly`、`LayerUtility: ImageScaleByAspectRatio V2`、`LoadImage`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerAdvanced

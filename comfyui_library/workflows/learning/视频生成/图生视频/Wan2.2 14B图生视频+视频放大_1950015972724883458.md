---
key: 视频生成/图生视频/Wan2.2 14B图生视频+视频放大_1950015972724883458.json
name: Wan2.2 14B图生视频+视频放大_1950015972724883458.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1950015972724883458.json
hash: 3414d9bf6c8d47dc
coverage: 1
learned_at: 2026-10-15 22:30:51
nodes: [ModelSamplingSD3, ModelSamplingSD3, UNETLoader, UNETLoader, CLIPTextEncode, LoadImage, CLIPLoader, KSamplerAdvanced, KSamplerAdvanced, VAELoader, CLIPTextEncode, VHS_VideoCombine, RIFE VFI, ImageUpscaleWithModel, UpscaleModelLoader, VHS_VideoCombine, VAEDecode, WanImageToVideo]
patterns: []
missing: []
parameters: {"cfg": 20, "denoise": "simple", "sampler_name": 3.5, "scheduler": "euler", "seed": "enable", "steps": "randomize"}
---

# 视频生成/图生视频/Wan2.2 14B图生视频+视频放大_1950015972724883458.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1950015972724883458.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（18 个）：
- `ModelSamplingSD3`
- `ModelSamplingSD3`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `CLIPTextEncode` ★核心
- `LoadImage`
- `CLIPLoader`
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `VAELoader`
- `CLIPTextEncode` ★核心
- `VHS_VideoCombine`
- `RIFE VFI`
- `ImageUpscaleWithModel`
- `UpscaleModelLoader`
- `VHS_VideoCombine`
- `VAEDecode` ★核心
- `WanImageToVideo`

## 关键参数

- `seed` = `enable`
- `steps` = `randomize`
- `cfg` = `20`
- `sampler_name` = `3.5`
- `scheduler` = `euler`
- `denoise` = `simple`

## 知识

覆盖率 **100%**（18/18）

**有卡**：`ModelSamplingSD3`、`UNETLoader`、`CLIPTextEncode`、`LoadImage`、`CLIPLoader`、`KSamplerAdvanced`、`VAELoader`、`VHS_VideoCombine`、`RIFE VFI`、`ImageUpscaleWithModel`、`UpscaleModelLoader`、`VAEDecode`、`WanImageToVideo`

**用到的条目**：VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerAdvanced、ImageUpscaleWithModel

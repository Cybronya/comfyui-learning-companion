---
key: 视频生成/图生视频/简单点wan2.2-remixv2-i2v图生视频_2044709107302670338.json
name: 简单点wan2.2-remixv2-i2v图生视频_2044709107302670338.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2044709107302670338.json
hash: 463eed382697ae9e
coverage: 0.675
learned_at: 2026-10-15 22:36:40
nodes: [PathchSageAttentionKJ, PathchSageAttentionKJ, ModelPatchTorchSettings, ModelPatchTorchSettings, VAELoader, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, easy cleanGpuUsed, Reroute, Reroute, VAEDecode, CLIPLoader, UNETLoader, UNETLoader, wanBlockSwap, wanBlockSwap, Note, Reroute, PreviewImage, ModelSamplingSD3, ModelSamplingSD3, CLIPTextEncode, VHS_VideoCombine, RIFE VFI, KSamplerAdvanced, KSamplerAdvanced, Reroute, ImageResizeKJv2, WanImageToVideo, Int, LayerUtility: ImageScaleByAspectRatio V2, Note, VHS_VideoCombine, CLIPTextEncode, LoadImage, Int]
patterns: []
missing: []
parameters: {"cfg": 6, "denoise": "normal", "sampler_name": 1, "scheduler": "euler", "seed": "disable", "steps": "fixed"}
---

# 视频生成/图生视频/简单点wan2.2-remixv2-i2v图生视频_2044709107302670338.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2044709107302670338.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（40 个）：
- `PathchSageAttentionKJ`
- `PathchSageAttentionKJ`
- `ModelPatchTorchSettings`
- `ModelPatchTorchSettings`
- `VAELoader`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `easy cleanGpuUsed`
- `Reroute`
- `Reroute`
- `VAEDecode` ★核心
- `CLIPLoader`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `wanBlockSwap`
- `wanBlockSwap`
- `Note`
- `Reroute`
- `PreviewImage`
- `ModelSamplingSD3`
- `ModelSamplingSD3`
- `CLIPTextEncode` ★核心
- `VHS_VideoCombine`
- `RIFE VFI`
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `Reroute`
- `ImageResizeKJv2`
- `WanImageToVideo`
- `Int`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `Note`
- `VHS_VideoCombine`
- `CLIPTextEncode` ★核心
- `LoadImage`
- `Int`

## 关键参数

- `seed` = `disable`
- `steps` = `fixed`
- `cfg` = `6`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `normal`

## 知识

覆盖率 **68%**（27/40）

**有卡**：`PathchSageAttentionKJ`、`ModelPatchTorchSettings`、`VAELoader`、`easy cleanGpuUsed`、`VAEDecode`、`CLIPLoader`、`UNETLoader`、`wanBlockSwap`、`ModelSamplingSD3`、`CLIPTextEncode`、`VHS_VideoCombine`、`RIFE VFI`、`KSamplerAdvanced`、`ImageResizeKJv2`、`WanImageToVideo`、`Int`、`LayerUtility: ImageScaleByAspectRatio V2`、`LoadImage`

**用到的条目**：VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、LayerUtility: ImageScaleByAspectRatio V2、KSamplerAdvanced

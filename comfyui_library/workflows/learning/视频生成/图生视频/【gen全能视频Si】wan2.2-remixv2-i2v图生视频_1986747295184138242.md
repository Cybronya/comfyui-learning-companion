---
key: 视频生成/图生视频/【gen全能视频Si】wan2.2-remixv2-i2v图生视频_1986747295184138242.json
name: 【gen全能视频Si】wan2.2-remixv2-i2v图生视频_1986747295184138242.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1986747295184138242.json
hash: d600455f341af827
coverage: 0.675
learned_at: 2026-10-15 22:32:56
nodes: [PathchSageAttentionKJ, PathchSageAttentionKJ, ModelPatchTorchSettings, ModelPatchTorchSettings, VAELoader, Reroute, Reroute, Reroute, Reroute, WanImageToVideo, Reroute, Reroute, easy cleanGpuUsed, Reroute, Reroute, VAEDecode, CLIPLoader, UNETLoader, LayerUtility: ImageScaleByAspectRatio V2, ImageResizeKJv2, UNETLoader, wanBlockSwap, wanBlockSwap, Note, Int, Note, Reroute, PreviewImage, ModelSamplingSD3, ModelSamplingSD3, CLIPTextEncode, CLIPTextEncode, LoadImage, VHS_VideoCombine, RIFE VFI, VHS_VideoCombine, KSamplerAdvanced, KSamplerAdvanced, Reroute, Int]
patterns: []
missing: []
parameters: {"cfg": 6, "denoise": "normal", "sampler_name": 1, "scheduler": "euler", "seed": "disable", "steps": "fixed"}
---

# 视频生成/图生视频/【gen全能视频Si】wan2.2-remixv2-i2v图生视频_1986747295184138242.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1986747295184138242.json`

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
- `WanImageToVideo`
- `Reroute`
- `Reroute`
- `easy cleanGpuUsed`
- `Reroute`
- `Reroute`
- `VAEDecode` ★核心
- `CLIPLoader`
- `UNETLoader` ★核心
- `LayerUtility: ImageScaleByAspectRatio V2`
- `ImageResizeKJv2`
- `UNETLoader` ★核心
- `wanBlockSwap`
- `wanBlockSwap`
- `Note`
- `Int`
- `Note`
- `Reroute`
- `PreviewImage`
- `ModelSamplingSD3`
- `ModelSamplingSD3`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `LoadImage`
- `VHS_VideoCombine`
- `RIFE VFI`
- `VHS_VideoCombine`
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `Reroute`
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

**有卡**：`PathchSageAttentionKJ`、`ModelPatchTorchSettings`、`VAELoader`、`WanImageToVideo`、`easy cleanGpuUsed`、`VAEDecode`、`CLIPLoader`、`UNETLoader`、`LayerUtility: ImageScaleByAspectRatio V2`、`ImageResizeKJv2`、`wanBlockSwap`、`Int`、`ModelSamplingSD3`、`CLIPTextEncode`、`LoadImage`、`VHS_VideoCombine`、`RIFE VFI`、`KSamplerAdvanced`

**用到的条目**：VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、LayerUtility: ImageScaleByAspectRatio V2、KSamplerAdvanced

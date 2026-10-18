---
key: 视频生成/图生视频/Smooth Mix Wan 2.2 超好用的图生视频大模型_1979525930601320449.json
name: Smooth Mix Wan 2.2 超好用的图生视频大模型_1979525930601320449.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/Smooth Mix Wan 2.2 超好用的图生视频大模型_1979525930601320449.json
hash: ef9322618aec7720
coverage: 0.964286
learned_at: 2026-10-15 22:32:23
nodes: [ModelSamplingSD3, UNETLoader, ModelSamplingSD3, CLIPLoader, VAELoader, wanBlockSwap, PathchSageAttentionKJ, ModelPatchTorchSettings, LoadImage, KSamplerAdvanced, wanBlockSwap, PathchSageAttentionKJ, ModelPatchTorchSettings, ImpactInt, ImpactInt, ImpactInt, UNETLoader, PrimitiveStringMultiline, CLIPTextEncode, CLIPTextEncode, VAEDecode, WanImageToVideo, KSamplerAdvanced, SimpleMath+, ImageResizeKJv2, CLIPVisionEncode, CLIPVisionLoader, VHS_VideoCombine]
patterns: []
missing: []
parameters: {"cfg": 6, "denoise": "simple", "sampler_name": 1, "scheduler": "euler_ancestral", "seed": "disable", "steps": "fixed"}
---

# 视频生成/图生视频/Smooth Mix Wan 2.2 超好用的图生视频大模型_1979525930601320449.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1979525930601320449.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（28 个）：
- `ModelSamplingSD3`
- `UNETLoader` ★核心
- `ModelSamplingSD3`
- `CLIPLoader`
- `VAELoader`
- `wanBlockSwap`
- `PathchSageAttentionKJ`
- `ModelPatchTorchSettings`
- `LoadImage`
- `KSamplerAdvanced` ★核心
- `wanBlockSwap`
- `PathchSageAttentionKJ`
- `ModelPatchTorchSettings`
- `ImpactInt`
- `ImpactInt`
- `ImpactInt`
- `UNETLoader` ★核心
- `PrimitiveStringMultiline`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `VAEDecode` ★核心
- `WanImageToVideo`
- `KSamplerAdvanced` ★核心
- `SimpleMath+`
- `ImageResizeKJv2`
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `VHS_VideoCombine`

## 关键参数

- `seed` = `disable`
- `steps` = `fixed`
- `cfg` = `6`
- `sampler_name` = `1`
- `scheduler` = `euler_ancestral`
- `denoise` = `simple`

## 知识

覆盖率 **96%**（27/28）

**有卡**：`ModelSamplingSD3`、`UNETLoader`、`CLIPLoader`、`VAELoader`、`wanBlockSwap`、`PathchSageAttentionKJ`、`ModelPatchTorchSettings`、`LoadImage`、`KSamplerAdvanced`、`ImpactInt`、`CLIPTextEncode`、`VAEDecode`、`WanImageToVideo`、`SimpleMath+`、`ImageResizeKJv2`、`CLIPVisionEncode`、`CLIPVisionLoader`、`VHS_VideoCombine`

**用到的条目**：VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerAdvanced、CLIPVisionEncode

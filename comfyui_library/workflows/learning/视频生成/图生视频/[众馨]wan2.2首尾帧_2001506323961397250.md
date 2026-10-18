---
key: 视频生成/图生视频/[众馨]wan2.2首尾帧_2001506323961397250.json
name: [众馨]wan2.2首尾帧_2001506323961397250.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/[众馨]wan2.2首尾帧_2001506323961397250.json
hash: 7de2f1ef35fae78e
coverage: 0.97561
learned_at: 2026-10-15 22:33:45
nodes: [wanBlockSwap, wanBlockSwap, Mute / Bypass Repeater (rgthree), PathchSageAttentionKJ, ModelPatchTorchSettings, Fast Bypasser (rgthree), PathchSageAttentionKJ, ModelSamplingSD3, ModelSamplingSD3, CLIPLoader, VAELoader, ModelPatchTorchSettings, ImpactInt, Seed (rgthree), VAEDecode, RIFE VFI, SimpleMath+, easy cleanGpuUsed, ImageScaleBy, CLIPTextEncode, easy cleanGpuUsed, Fast Bypasser (rgthree), Fast Bypasser (rgthree), CLIPTextEncode, KSamplerAdvanced, KSamplerAdvanced, PrimitiveStringMultiline, ImpactInt, ImpactInt, CLIPVisionLoader, WanFirstLastFrameToVideo, ImageResizeKJv2, ImageResizeKJv2, CLIPVisionEncode, CLIPVisionEncode, UNETLoader, UNETLoader, VHS_VideoCombine, VHS_VideoCombine, LoadImage, LoadImage]
patterns: []
missing: []
parameters: {"cfg": 6, "denoise": "simple", "sampler_name": 1, "scheduler": "euler_ancestral", "seed": "disable", "steps": "fixed"}
---

# 视频生成/图生视频/[众馨]wan2.2首尾帧_2001506323961397250.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2001506323961397250.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（41 个）：
- `wanBlockSwap`
- `wanBlockSwap`
- `Mute / Bypass Repeater (rgthree)`
- `PathchSageAttentionKJ`
- `ModelPatchTorchSettings`
- `Fast Bypasser (rgthree)`
- `PathchSageAttentionKJ`
- `ModelSamplingSD3`
- `ModelSamplingSD3`
- `CLIPLoader`
- `VAELoader`
- `ModelPatchTorchSettings`
- `ImpactInt`
- `Seed (rgthree)`
- `VAEDecode` ★核心
- `RIFE VFI`
- `SimpleMath+`
- `easy cleanGpuUsed`
- `ImageScaleBy`
- `CLIPTextEncode` ★核心
- `easy cleanGpuUsed`
- `Fast Bypasser (rgthree)`
- `Fast Bypasser (rgthree)`
- `CLIPTextEncode` ★核心
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `PrimitiveStringMultiline`
- `ImpactInt`
- `ImpactInt`
- `CLIPVisionLoader`
- `WanFirstLastFrameToVideo`
- `ImageResizeKJv2`
- `ImageResizeKJv2`
- `CLIPVisionEncode`
- `CLIPVisionEncode`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `LoadImage`
- `LoadImage`

## 关键参数

- `seed` = `disable`
- `steps` = `fixed`
- `cfg` = `6`
- `sampler_name` = `1`
- `scheduler` = `euler_ancestral`
- `denoise` = `simple`

## 知识

覆盖率 **98%**（40/41）

**有卡**：`wanBlockSwap`、`Mute / Bypass Repeater (rgthree)`、`PathchSageAttentionKJ`、`ModelPatchTorchSettings`、`Fast Bypasser (rgthree)`、`ModelSamplingSD3`、`CLIPLoader`、`VAELoader`、`ImpactInt`、`Seed (rgthree)`、`VAEDecode`、`RIFE VFI`、`SimpleMath+`、`easy cleanGpuUsed`、`ImageScaleBy`、`CLIPTextEncode`、`KSamplerAdvanced`、`CLIPVisionLoader`、`WanFirstLastFrameToVideo`、`ImageResizeKJv2`、`CLIPVisionEncode`、`UNETLoader`、`VHS_VideoCombine`、`LoadImage`

**用到的条目**：VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerAdvanced、Seed (rgthree)

---
key: 视频生成/图生视频/wan2.2 Smooth Mix 高动态电影质感 图生视频_2010998394537381889.json
name: wan2.2 Smooth Mix 高动态电影质感 图生视频_2010998394537381889.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2010998394537381889.json
hash: 46d99834433a7bf6
coverage: 0.975
learned_at: 2026-10-15 22:34:20
nodes: [wanBlockSwap, wanBlockSwap, Mute / Bypass Repeater (rgthree), ModelPatchTorchSettings, PathchSageAttentionKJ, CLIPLoader, VAELoader, ModelPatchTorchSettings, SimpleMath+, CLIPTextEncode, Fast Bypasser (rgthree), Seed (rgthree), easy cleanGpuUsed, ImageScaleBy, easy cleanGpuUsed, CLIPVisionLoader, VAEDecode, ImpactInt, ImpactInt, CLIPTextEncode, PathchSageAttentionKJ, Fast Bypasser (rgthree), Fast Bypasser (rgthree), KSamplerAdvanced, ImageResizeKJv2, KSamplerAdvanced, CLIPVisionEncode, WanImageToVideo, UNETLoader, UNETLoader, ModelSamplingSD3, ModelSamplingSD3, LoraLoaderModelOnly, LoraLoaderModelOnly, RIFE VFI, ImpactInt, VHS_VideoCombine, VHS_VideoCombine, LoadImage, PrimitiveStringMultiline]
patterns: []
missing: []
parameters: {"cfg": 6, "denoise": "simple", "sampler_name": 1, "scheduler": "euler_ancestral", "seed": "disable", "steps": "fixed"}
---

# 视频生成/图生视频/wan2.2 Smooth Mix 高动态电影质感 图生视频_2010998394537381889.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2010998394537381889.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（40 个）：
- `wanBlockSwap`
- `wanBlockSwap`
- `Mute / Bypass Repeater (rgthree)`
- `ModelPatchTorchSettings`
- `PathchSageAttentionKJ`
- `CLIPLoader`
- `VAELoader`
- `ModelPatchTorchSettings`
- `SimpleMath+`
- `CLIPTextEncode` ★核心
- `Fast Bypasser (rgthree)`
- `Seed (rgthree)`
- `easy cleanGpuUsed`
- `ImageScaleBy`
- `easy cleanGpuUsed`
- `CLIPVisionLoader`
- `VAEDecode` ★核心
- `ImpactInt`
- `ImpactInt`
- `CLIPTextEncode` ★核心
- `PathchSageAttentionKJ`
- `Fast Bypasser (rgthree)`
- `Fast Bypasser (rgthree)`
- `KSamplerAdvanced` ★核心
- `ImageResizeKJv2`
- `KSamplerAdvanced` ★核心
- `CLIPVisionEncode`
- `WanImageToVideo`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `ModelSamplingSD3`
- `ModelSamplingSD3`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `RIFE VFI`
- `ImpactInt`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `LoadImage`
- `PrimitiveStringMultiline`

## 关键参数

- `seed` = `disable`
- `steps` = `fixed`
- `cfg` = `6`
- `sampler_name` = `1`
- `scheduler` = `euler_ancestral`
- `denoise` = `simple`

## 知识

覆盖率 **98%**（39/40）

**有卡**：`wanBlockSwap`、`Mute / Bypass Repeater (rgthree)`、`ModelPatchTorchSettings`、`PathchSageAttentionKJ`、`CLIPLoader`、`VAELoader`、`SimpleMath+`、`CLIPTextEncode`、`Fast Bypasser (rgthree)`、`Seed (rgthree)`、`easy cleanGpuUsed`、`ImageScaleBy`、`CLIPVisionLoader`、`VAEDecode`、`ImpactInt`、`KSamplerAdvanced`、`ImageResizeKJv2`、`CLIPVisionEncode`、`WanImageToVideo`、`UNETLoader`、`ModelSamplingSD3`、`LoraLoaderModelOnly`、`RIFE VFI`、`VHS_VideoCombine`、`LoadImage`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerAdvanced

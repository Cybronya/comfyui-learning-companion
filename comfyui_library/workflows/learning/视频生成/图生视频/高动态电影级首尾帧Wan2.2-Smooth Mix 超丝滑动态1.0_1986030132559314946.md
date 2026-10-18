---
key: 视频生成/图生视频/高动态电影级首尾帧Wan2.2-Smooth Mix 超丝滑动态1.0_1986030132559314946.json
name: 高动态电影级首尾帧Wan2.2-Smooth Mix 超丝滑动态1.0_1986030132559314946.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/高动态电影级首尾帧Wan2.2-Smooth Mix 超丝滑动态1.0_1986030132559314946.json
hash: be049c7e51670f45
coverage: 0.97619
learned_at: 2026-10-15 22:32:53
nodes: [Mute / Bypass Repeater (rgthree), PathchSageAttentionKJ, ModelPatchTorchSettings, Fast Bypasser (rgthree), PathchSageAttentionKJ, ModelSamplingSD3, ModelSamplingSD3, CLIPLoader, VAELoader, ModelPatchTorchSettings, ImpactInt, Seed (rgthree), VAEDecode, RIFE VFI, SimpleMath+, easy cleanGpuUsed, ImageScaleBy, CLIPTextEncode, easy cleanGpuUsed, CLIPTextEncode, KSamplerAdvanced, KSamplerAdvanced, ImpactInt, ImpactInt, CLIPVisionLoader, WanFirstLastFrameToVideo, ImageResizeKJv2, ImageResizeKJv2, CLIPVisionEncode, CLIPVisionEncode, UNETLoader, UNETLoader, wanBlockSwap, wanBlockSwap, Fast Bypasser (rgthree), Fast Bypasser (rgthree), VHS_VideoCombine, VHS_VideoCombine, RHHiddenNodes, PrimitiveStringMultiline, LoadImage, LoadImage]
patterns: []
missing: []
parameters: {"cfg": 6, "denoise": "simple", "sampler_name": 1, "scheduler": "euler_ancestral", "seed": "disable", "steps": "fixed"}
---

# 视频生成/图生视频/高动态电影级首尾帧Wan2.2-Smooth Mix 超丝滑动态1.0_1986030132559314946.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1986030132559314946.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（42 个）：
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
- `CLIPTextEncode` ★核心
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
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
- `wanBlockSwap`
- `wanBlockSwap`
- `Fast Bypasser (rgthree)`
- `Fast Bypasser (rgthree)`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `RHHiddenNodes`
- `PrimitiveStringMultiline`
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

覆盖率 **98%**（41/42）

**有卡**：`Mute / Bypass Repeater (rgthree)`、`PathchSageAttentionKJ`、`ModelPatchTorchSettings`、`Fast Bypasser (rgthree)`、`ModelSamplingSD3`、`CLIPLoader`、`VAELoader`、`ImpactInt`、`Seed (rgthree)`、`VAEDecode`、`RIFE VFI`、`SimpleMath+`、`easy cleanGpuUsed`、`ImageScaleBy`、`CLIPTextEncode`、`KSamplerAdvanced`、`CLIPVisionLoader`、`WanFirstLastFrameToVideo`、`ImageResizeKJv2`、`CLIPVisionEncode`、`UNETLoader`、`wanBlockSwap`、`VHS_VideoCombine`、`RHHiddenNodes`、`LoadImage`

**用到的条目**：VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerAdvanced、Seed (rgthree)

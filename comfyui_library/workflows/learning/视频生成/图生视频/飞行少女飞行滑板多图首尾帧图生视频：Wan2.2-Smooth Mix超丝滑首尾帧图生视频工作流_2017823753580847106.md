---
key: 视频生成/图生视频/飞行少女飞行滑板多图首尾帧图生视频：Wan2.2-Smooth Mix超丝滑首尾帧图生视频工作流_2017823753580847106.json
name: 飞行少女飞行滑板多图首尾帧图生视频：Wan2.2-Smooth Mix超丝滑首尾帧图生视频工作流_2017823753580847106.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2017823753580847106.json
hash: 7b9a8d2ab9034f9d
coverage: 0.986667
learned_at: 2026-10-15 22:34:51
nodes: [Mute / Bypass Repeater (rgthree), PathchSageAttentionKJ, Fast Bypasser (rgthree), PathchSageAttentionKJ, ModelSamplingSD3, ModelSamplingSD3, easy cleanGpuUsed, UNETLoader, UNETLoader, wanBlockSwap, wanBlockSwap, Fast Bypasser (rgthree), Fast Bypasser (rgthree), SimpleMath+, ImageScaleBy, RIFE VFI, easy cleanGpuUsed, CLIPVisionEncode, WanFirstLastFrameToVideo, easy cleanGpuUsed, CLIPTextEncode, CLIPTextEncode, SimpleMath+, ImageScaleBy, RIFE VFI, easy cleanGpuUsed, KSamplerAdvanced, CLIPVisionEncode, CLIPVisionEncode, easy cleanGpuUsed, CLIPTextEncode, CLIPTextEncode, ImageResizeKJv2, SimpleMath+, ImageScaleBy, RIFE VFI, easy cleanGpuUsed, KSamplerAdvanced, CLIPVisionEncode, CLIPTextEncode, CLIPTextEncode, CLIPLoader, ImageResizeKJv2, ImageResizeKJv2, ImpactInt, ImpactInt, ImpactInt, VAEDecode, VAEDecode, VAEDecode, VAELoader, ImageResizeKJv2, CLIPVisionEncode, CLIPVisionEncode, CLIPVisionLoader, KSamplerAdvanced, ModelPatchTorchSettings, ModelPatchTorchSettings, ImageResizeKJv2, ImageResizeKJv2, WanAdvancedI2V, WanAdvancedI2V, WanAdvancedI2V, Seed (rgthree), KSamplerAdvanced, KSamplerAdvanced, KSamplerAdvanced, ImageBatchExtendWithOverlap, ImageBatchExtendWithOverlap, VHS_VideoCombine, PrimitiveStringMultiline, LoadImage, LoadImage, LoadImage, LoadImage]
patterns: []
missing: []
parameters: {"cfg": 6, "denoise": "simple", "sampler_name": 1, "scheduler": "euler_ancestral", "seed": "disable", "steps": "randomize"}
---

# 视频生成/图生视频/飞行少女飞行滑板多图首尾帧图生视频：Wan2.2-Smooth Mix超丝滑首尾帧图生视频工作流_2017823753580847106.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2017823753580847106.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（75 个）：
- `Mute / Bypass Repeater (rgthree)`
- `PathchSageAttentionKJ`
- `Fast Bypasser (rgthree)`
- `PathchSageAttentionKJ`
- `ModelSamplingSD3`
- `ModelSamplingSD3`
- `easy cleanGpuUsed`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `wanBlockSwap`
- `wanBlockSwap`
- `Fast Bypasser (rgthree)`
- `Fast Bypasser (rgthree)`
- `SimpleMath+`
- `ImageScaleBy`
- `RIFE VFI`
- `easy cleanGpuUsed`
- `CLIPVisionEncode`
- `WanFirstLastFrameToVideo`
- `easy cleanGpuUsed`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `SimpleMath+`
- `ImageScaleBy`
- `RIFE VFI`
- `easy cleanGpuUsed`
- `KSamplerAdvanced` ★核心
- `CLIPVisionEncode`
- `CLIPVisionEncode`
- `easy cleanGpuUsed`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `ImageResizeKJv2`
- `SimpleMath+`
- `ImageScaleBy`
- `RIFE VFI`
- `easy cleanGpuUsed`
- `KSamplerAdvanced` ★核心
- `CLIPVisionEncode`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `CLIPLoader`
- `ImageResizeKJv2`
- `ImageResizeKJv2`
- `ImpactInt`
- `ImpactInt`
- `ImpactInt`
- `VAEDecode` ★核心
- `VAEDecode` ★核心
- `VAEDecode` ★核心
- `VAELoader`
- `ImageResizeKJv2`
- `CLIPVisionEncode`
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `KSamplerAdvanced` ★核心
- `ModelPatchTorchSettings`
- `ModelPatchTorchSettings`
- `ImageResizeKJv2`
- `ImageResizeKJv2`
- `WanAdvancedI2V`
- `WanAdvancedI2V`
- `WanAdvancedI2V`
- `Seed (rgthree)`
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `ImageBatchExtendWithOverlap`
- `ImageBatchExtendWithOverlap`
- `VHS_VideoCombine`
- `PrimitiveStringMultiline`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`

## 关键参数

- `seed` = `disable`
- `steps` = `randomize`
- `cfg` = `6`
- `sampler_name` = `1`
- `scheduler` = `euler_ancestral`
- `denoise` = `simple`

## 知识

覆盖率 **99%**（74/75）

**有卡**：`Mute / Bypass Repeater (rgthree)`、`PathchSageAttentionKJ`、`Fast Bypasser (rgthree)`、`ModelSamplingSD3`、`easy cleanGpuUsed`、`UNETLoader`、`wanBlockSwap`、`SimpleMath+`、`ImageScaleBy`、`RIFE VFI`、`CLIPVisionEncode`、`WanFirstLastFrameToVideo`、`CLIPTextEncode`、`KSamplerAdvanced`、`ImageResizeKJv2`、`CLIPLoader`、`ImpactInt`、`VAEDecode`、`VAELoader`、`CLIPVisionLoader`、`ModelPatchTorchSettings`、`WanAdvancedI2V`、`Seed (rgthree)`、`ImageBatchExtendWithOverlap`、`VHS_VideoCombine`、`LoadImage`

**用到的条目**：VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerAdvanced、Seed (rgthree)

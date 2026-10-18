---
key: 视频生成/图生视频/Wan2.2-Smooth+Mix+转场电影探班++多图首尾帧_2009529023986147330.json
name: Wan2.2-Smooth+Mix+转场电影探班++多图首尾帧_2009529023986147330.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/Wan2.2-Smooth+Mix+转场电影探班++多图首尾帧_2009529023986147330.json
hash: 6d6d698af629ee9b
coverage: 0.979592
learned_at: 2026-10-15 22:34:13
nodes: [Mute / Bypass Repeater (rgthree), PathchSageAttentionKJ, ModelPatchTorchSettings, Fast Bypasser (rgthree), PathchSageAttentionKJ, ModelSamplingSD3, ModelSamplingSD3, CLIPLoader, VAELoader, ModelPatchTorchSettings, ImpactInt, Seed (rgthree), SimpleMath+, easy cleanGpuUsed, ImageScaleBy, CLIPTextEncode, easy cleanGpuUsed, CLIPTextEncode, ImpactInt, ImpactInt, CLIPVisionLoader, WanFirstLastFrameToVideo, CLIPVisionEncode, CLIPVisionEncode, UNETLoader, UNETLoader, wanBlockSwap, wanBlockSwap, Fast Bypasser (rgthree), Fast Bypasser (rgthree), VAEDecode, easy forLoopEnd, easy batchAnything, easy anythingIndexSwitch, easy forLoopStart, JWInteger, easy anythingIndexSwitch, ImageResizeKJv2, ImageResizeKJv2, VHS_VideoCombine, RIFE VFI, KSamplerAdvanced, KSamplerAdvanced, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, PrimitiveStringMultiline]
patterns: []
missing: []
parameters: {"cfg": 6, "denoise": "simple", "sampler_name": 1, "scheduler": "euler_ancestral", "seed": "disable", "steps": "fixed"}
---

# 视频生成/图生视频/Wan2.2-Smooth+Mix+转场电影探班++多图首尾帧_2009529023986147330.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2009529023986147330.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（49 个）：
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
- `SimpleMath+`
- `easy cleanGpuUsed`
- `ImageScaleBy`
- `CLIPTextEncode` ★核心
- `easy cleanGpuUsed`
- `CLIPTextEncode` ★核心
- `ImpactInt`
- `ImpactInt`
- `CLIPVisionLoader`
- `WanFirstLastFrameToVideo`
- `CLIPVisionEncode`
- `CLIPVisionEncode`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `wanBlockSwap`
- `wanBlockSwap`
- `Fast Bypasser (rgthree)`
- `Fast Bypasser (rgthree)`
- `VAEDecode` ★核心
- `easy forLoopEnd`
- `easy batchAnything`
- `easy anythingIndexSwitch`
- `easy forLoopStart`
- `JWInteger`
- `easy anythingIndexSwitch`
- `ImageResizeKJv2`
- `ImageResizeKJv2`
- `VHS_VideoCombine`
- `RIFE VFI`
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
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

覆盖率 **98%**（48/49）

**有卡**：`Mute / Bypass Repeater (rgthree)`、`PathchSageAttentionKJ`、`ModelPatchTorchSettings`、`Fast Bypasser (rgthree)`、`ModelSamplingSD3`、`CLIPLoader`、`VAELoader`、`ImpactInt`、`Seed (rgthree)`、`SimpleMath+`、`easy cleanGpuUsed`、`ImageScaleBy`、`CLIPTextEncode`、`CLIPVisionLoader`、`WanFirstLastFrameToVideo`、`CLIPVisionEncode`、`UNETLoader`、`wanBlockSwap`、`VAEDecode`、`easy forLoopEnd`、`easy batchAnything`、`easy anythingIndexSwitch`、`easy forLoopStart`、`JWInteger`、`ImageResizeKJv2`、`VHS_VideoCombine`、`RIFE VFI`、`KSamplerAdvanced`、`LoadImage`

**用到的条目**：VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerAdvanced、Seed (rgthree)

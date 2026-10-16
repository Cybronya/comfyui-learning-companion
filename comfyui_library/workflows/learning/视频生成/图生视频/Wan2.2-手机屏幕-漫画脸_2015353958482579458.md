---
key: 视频生成/图生视频/Wan2.2-手机屏幕-漫画脸_2015353958482579458.json
name: Wan2.2-手机屏幕-漫画脸_2015353958482579458.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2015353958482579458.json
hash: c3971581e9d3cf74
coverage: 0.983333
learned_at: 2026-10-15 22:34:38
nodes: [Mute / Bypass Repeater (rgthree), PathchSageAttentionKJ, ModelPatchTorchSettings, Fast Bypasser (rgthree), PathchSageAttentionKJ, ModelSamplingSD3, ModelSamplingSD3, CLIPLoader, VAELoader, ModelPatchTorchSettings, Seed (rgthree), SimpleMath+, easy cleanGpuUsed, CLIPVisionLoader, WanFirstLastFrameToVideo, CLIPVisionEncode, CLIPVisionEncode, UNETLoader, UNETLoader, wanBlockSwap, wanBlockSwap, Fast Bypasser (rgthree), Fast Bypasser (rgthree), easy batchAnything, easy forLoopStart, ImageResizeKJv2, ImageResizeKJv2, VAEDecode, VHS_VideoCombine, ImpactInt, ImpactInt, easy cleanGpuUsed, ImageScaleBy, easy forLoopEnd, CLIPTextEncode, RIFE VFI, KSamplerAdvanced, KSamplerAdvanced, CLIPTextEncode, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, easy anythingIndexSwitch, easy anythingIndexSwitch, JWInteger, RH_Nano_Banana2_Image2Image, PrimitiveStringMultiline, ImpactInt, SaveImage, LoadAudio, LoadImage]
patterns: []
missing: []
parameters: {"cfg": 16, "denoise": "simple", "sampler_name": 1, "scheduler": "euler", "seed": "enable", "steps": "randomize"}
---

# 视频生成/图生视频/Wan2.2-手机屏幕-漫画脸_2015353958482579458.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2015353958482579458.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（60 个）：
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
- `Seed (rgthree)`
- `SimpleMath+`
- `easy cleanGpuUsed`
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
- `easy batchAnything`
- `easy forLoopStart`
- `ImageResizeKJv2`
- `ImageResizeKJv2`
- `VAEDecode` ★核心
- `VHS_VideoCombine`
- `ImpactInt`
- `ImpactInt`
- `easy cleanGpuUsed`
- `ImageScaleBy`
- `easy forLoopEnd`
- `CLIPTextEncode` ★核心
- `RIFE VFI`
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `CLIPTextEncode` ★核心
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `easy anythingIndexSwitch`
- `easy anythingIndexSwitch`
- `JWInteger`
- `RH_Nano_Banana2_Image2Image`
- `PrimitiveStringMultiline`
- `ImpactInt`
- `SaveImage`
- `LoadAudio`
- `LoadImage`

## 关键参数

- `seed` = `enable`
- `steps` = `randomize`
- `cfg` = `16`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `simple`

## 知识

覆盖率 **98%**（59/60）

**有卡**：`Mute / Bypass Repeater (rgthree)`、`PathchSageAttentionKJ`、`ModelPatchTorchSettings`、`Fast Bypasser (rgthree)`、`ModelSamplingSD3`、`CLIPLoader`、`VAELoader`、`Seed (rgthree)`、`SimpleMath+`、`easy cleanGpuUsed`、`CLIPVisionLoader`、`WanFirstLastFrameToVideo`、`CLIPVisionEncode`、`UNETLoader`、`wanBlockSwap`、`easy batchAnything`、`easy forLoopStart`、`ImageResizeKJv2`、`VAEDecode`、`VHS_VideoCombine`、`ImpactInt`、`ImageScaleBy`、`easy forLoopEnd`、`CLIPTextEncode`、`RIFE VFI`、`KSamplerAdvanced`、`LoadImage`、`easy anythingIndexSwitch`、`JWInteger`、`RH_Nano_Banana2_Image2Image`、`SaveImage`、`LoadAudio`

**用到的条目**：VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerAdvanced、Seed (rgthree)

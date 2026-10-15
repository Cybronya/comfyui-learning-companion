---
key: 视频生成/文生视频/高动态电影探班短视频复刻首尾帧Wan2.2-Smooth Mix_1999803744537673729.json
name: 高动态电影探班短视频复刻首尾帧Wan2.2-Smooth Mix_1999803744537673729
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/高动态电影探班短视频复刻首尾帧Wan2.2-Smooth Mix_1999803744537673729.json
hash: 1ae38e881f160061
coverage: 0.981132
learned_at: 2026-10-15 22:49:07
nodes: [Mute / Bypass Repeater (rgthree), PathchSageAttentionKJ, ModelPatchTorchSettings, Fast Bypasser (rgthree), PathchSageAttentionKJ, ModelSamplingSD3, ModelSamplingSD3, CLIPLoader, VAELoader, ModelPatchTorchSettings, ImpactInt, Seed (rgthree), VAEDecode, RIFE VFI, SimpleMath+, easy cleanGpuUsed, ImageScaleBy, CLIPTextEncode, easy cleanGpuUsed, CLIPTextEncode, KSamplerAdvanced, KSamplerAdvanced, ImpactInt, ImpactInt, CLIPVisionLoader, WanFirstLastFrameToVideo, CLIPVisionEncode, CLIPVisionEncode, UNETLoader, UNETLoader, wanBlockSwap, wanBlockSwap, Fast Bypasser (rgthree), Fast Bypasser (rgthree), VHS_VideoCombine, VHS_VideoCombine, RHHiddenNodes, ImageResizeKJv2, ImageResizeKJv2, SaveImage, SaveImage, LoadImage, LoadImage, LoadImage, LoadImage, PrimitiveStringMultiline, RH_Translator, RH_Nano_Banana_Image2Image, RH_Translator, ImageResize+, RH_Nano_Banana_Image2Image, LoadImage, LoadImage]
patterns: []
missing: []
parameters: {"cfg": 6, "denoise": "simple", "sampler_name": 1, "scheduler": "euler_ancestral", "seed": "disable", "steps": "fixed"}
---

# 视频生成/文生视频/高动态电影探班短视频复刻首尾帧Wan2.2-Smooth Mix_1999803744537673729.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/高动态电影探班短视频复刻首尾帧Wan2.2-Smooth Mix_1999803744537673729.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（53 个）：
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
- `ImageResizeKJv2`
- `ImageResizeKJv2`
- `SaveImage`
- `SaveImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `PrimitiveStringMultiline`
- `RH_Translator`
- `RH_Nano_Banana_Image2Image`
- `RH_Translator`
- `ImageResize+`
- `RH_Nano_Banana_Image2Image`
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

覆盖率 **98%**（52/53）

**有卡**：`Mute / Bypass Repeater (rgthree)`、`PathchSageAttentionKJ`、`ModelPatchTorchSettings`、`Fast Bypasser (rgthree)`、`ModelSamplingSD3`、`CLIPLoader`、`VAELoader`、`ImpactInt`、`Seed (rgthree)`、`VAEDecode`、`RIFE VFI`、`SimpleMath+`、`easy cleanGpuUsed`、`ImageScaleBy`、`CLIPTextEncode`、`KSamplerAdvanced`、`CLIPVisionLoader`、`WanFirstLastFrameToVideo`、`CLIPVisionEncode`、`UNETLoader`、`wanBlockSwap`、`VHS_VideoCombine`、`RHHiddenNodes`、`ImageResizeKJv2`、`SaveImage`、`LoadImage`、`RH_Translator`、`RH_Nano_Banana_Image2Image`、`ImageResize+`

**用到的条目**：VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerAdvanced、Seed (rgthree)

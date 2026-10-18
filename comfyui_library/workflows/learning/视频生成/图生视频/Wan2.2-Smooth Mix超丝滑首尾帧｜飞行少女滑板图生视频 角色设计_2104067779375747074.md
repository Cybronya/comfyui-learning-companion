---
key: 视频生成/图生视频/Wan2.2-Smooth Mix超丝滑首尾帧｜飞行少女滑板图生视频 角色设计_2104067779375747074.json
name: Wan2.2-Smooth Mix超丝滑首尾帧｜飞行少女滑板图生视频 角色设计_2104067779375747074
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/Wan2.2-Smooth Mix超丝滑首尾帧｜飞行少女滑板图生视频 角色设计_2104067779375747074.json
hash: e982c547b38ccc8e
coverage: 0.957627
learned_at: 2026-10-17 02:29:29
nodes: [Mute / Bypass Repeater (rgthree), PathchSageAttentionKJ, Fast Bypasser (rgthree), PathchSageAttentionKJ, ModelSamplingSD3, ModelSamplingSD3, easy cleanGpuUsed, UNETLoader, UNETLoader, wanBlockSwap, wanBlockSwap, Fast Bypasser (rgthree), Fast Bypasser (rgthree), SimpleMath+, ImageScaleBy, RIFE VFI, easy cleanGpuUsed, LoadImage, CLIPVisionEncode, WanFirstLastFrameToVideo, easy cleanGpuUsed, CLIPTextEncode, CLIPTextEncode, SimpleMath+, ImageScaleBy, RIFE VFI, easy cleanGpuUsed, KSamplerAdvanced, CLIPVisionEncode, CLIPVisionEncode, easy cleanGpuUsed, CLIPTextEncode, CLIPTextEncode, ImageResizeKJv2, SimpleMath+, ImageScaleBy, RIFE VFI, easy cleanGpuUsed, KSamplerAdvanced, CLIPVisionEncode, CLIPTextEncode, CLIPTextEncode, CLIPLoader, ImageResizeKJv2, LoadImage, LoadImage, LoadImage, ImageResizeKJv2, ImpactInt, ImpactInt, ImpactInt, VAEDecode, VAEDecode, VAEDecode, VAELoader, ImageResizeKJv2, CLIPVisionEncode, CLIPVisionEncode, CLIPVisionLoader, KSamplerAdvanced, ModelPatchTorchSettings, ModelPatchTorchSettings, PrimitiveStringMultiline, ImageResizeKJv2, ImageResizeKJv2, WanAdvancedI2V, WanAdvancedI2V, WanAdvancedI2V, Seed (rgthree), KSamplerAdvanced, KSamplerAdvanced, KSamplerAdvanced, ImageBatchExtendWithOverlap, ImageBatchExtendWithOverlap, VHS_VideoCombine, 孤海注释, 孤海注释, UNETLoader, CLIPLoader, CLIPTextEncode, VAELoader, EmptyLatentImage, KSampler, VAEDecode, solarL_SaveImagesToZip, JjkText, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, CLIPTextEncode, Note]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/图生视频/Wan2.2-Smooth Mix超丝滑首尾帧｜飞行少女滑板图生视频 角色设计_2104067779375747074.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/Wan2.2-Smooth Mix超丝滑首尾帧｜飞行少女滑板图生视频 角色设计_2104067779375747074.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（118 个）：
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
- `LoadImage`
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
- `LoadImage`
- `LoadImage`
- `LoadImage`
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
- `PrimitiveStringMultiline`
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
- `孤海注释`
- `孤海注释`
- `UNETLoader` ★核心
- `CLIPLoader`
- `CLIPTextEncode` ★核心
- `VAELoader`
- `EmptyLatentImage` ★核心
- `KSampler` ★核心
- `VAEDecode` ★核心
- `solarL_SaveImagesToZip`
- `JjkText`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `CLIPTextEncode` ★核心
- `Note`

**识别到的模式**：text_to_image

## 关键参数

- `seed` = `598626327129635`
- `steps` = `4`
- `cfg` = `4.5`
- `sampler_name` = `er_sde`
- `scheduler` = `beta`
- `denoise` = `1`
- `width` = `80`
- `height` = `80`
- `batch_size` = `1`

## 知识

覆盖率 **96%**（113/118）

**有卡**：`Mute / Bypass Repeater (rgthree)`、`PathchSageAttentionKJ`、`Fast Bypasser (rgthree)`、`ModelSamplingSD3`、`easy cleanGpuUsed`、`UNETLoader`、`wanBlockSwap`、`SimpleMath+`、`ImageScaleBy`、`RIFE VFI`、`LoadImage`、`CLIPVisionEncode`、`WanFirstLastFrameToVideo`、`CLIPTextEncode`、`KSamplerAdvanced`、`ImageResizeKJv2`、`CLIPLoader`、`ImpactInt`、`VAEDecode`、`VAELoader`、`CLIPVisionLoader`、`ModelPatchTorchSettings`、`WanAdvancedI2V`、`Seed (rgthree)`、`ImageBatchExtendWithOverlap`、`VHS_VideoCombine`、`EmptyLatentImage`、`KSampler`、`solarL_SaveImagesToZip`、`LoraLoaderModelOnly`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage、LoadImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

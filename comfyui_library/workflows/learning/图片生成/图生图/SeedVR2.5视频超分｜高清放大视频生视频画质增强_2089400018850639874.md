---
key: 图片生成/图生图/SeedVR2.5视频超分｜高清放大视频生视频画质增强_2089400018850639874.json
name: SeedVR2.5视频超分｜高清放大视频生视频画质增强_2089400018850639874
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/SeedVR2.5视频超分｜高清放大视频生视频画质增强_2089400018850639874.json
hash: 9d2fbfe2738d345a
coverage: 0.77551
learned_at: 2026-10-23 11:25:10
nodes: [Reroute, Reroute, Reroute, SetNode, Reroute, ImageScaleToTotalPixels, VHS_VideoInfo, SeedVR2LoadVAEModel, SeedVR2ExtraArgs, PreviewImage, ImageScaleToTotalPixels, SeedVR2BlockSwap, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadDiTModel, INTConstant, SeedVR2, LoadImage, SeedVR2VideoUpscaler, VHS_VideoCombine, VHS_LoadVideo, Fast Groups Bypasser (rgthree), 孤海注释, 孤海注释, UNETLoader, CLIPLoader, CLIPTextEncode, VAELoader, EmptyLatentImage, KSampler, VAEDecode, JjkText, solarL_SaveImagesToZip, CLIPTextEncode, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, Note]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/SeedVR2.5视频超分｜高清放大视频生视频画质增强_2089400018850639874.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/SeedVR2.5视频超分｜高清放大视频生视频画质增强_2089400018850639874.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（49 个）：
- `Reroute`
- `Reroute`
- `Reroute`
- `SetNode`
- `Reroute`
- `ImageScaleToTotalPixels`
- `VHS_VideoInfo`
- `SeedVR2LoadVAEModel`
- `SeedVR2ExtraArgs`
- `PreviewImage`
- `ImageScaleToTotalPixels`
- `SeedVR2BlockSwap`
- `SaveImage`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadDiTModel`
- `INTConstant`
- `SeedVR2`
- `LoadImage`
- `SeedVR2VideoUpscaler`
- `VHS_VideoCombine`
- `VHS_LoadVideo`
- `Fast Groups Bypasser (rgthree)`
- `孤海注释`
- `孤海注释`
- `UNETLoader` ★核心
- `CLIPLoader`
- `CLIPTextEncode` ★核心
- `VAELoader`
- `EmptyLatentImage` ★核心
- `KSampler` ★核心
- `VAEDecode` ★核心
- `JjkText`
- `solarL_SaveImagesToZip`
- `CLIPTextEncode` ★核心
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
- `Note`

**识别到的模式**：text_to_image

## 关键参数

- `width` = `80`
- `height` = `80`
- `batch_size` = `1`
- `seed` = `598626327129635`
- `steps` = `4`
- `cfg` = `4.5`
- `sampler_name` = `er_sde`
- `scheduler` = `beta`
- `denoise` = `1`

## 知识

覆盖率 **78%**（38/49）

**有卡**：`ImageScaleToTotalPixels`、`VHS_VideoInfo`、`SeedVR2LoadVAEModel`、`SeedVR2ExtraArgs`、`SeedVR2BlockSwap`、`SaveImage`、`SeedVR2LoadDiTModel`、`INTConstant`、`SeedVR2`、`LoadImage`、`SeedVR2VideoUpscaler`、`VHS_VideoCombine`、`VHS_LoadVideo`、`UNETLoader`、`CLIPLoader`、`CLIPTextEncode`、`VAELoader`、`EmptyLatentImage`、`KSampler`、`VAEDecode`、`solarL_SaveImagesToZip`、`LoraLoaderModelOnly`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage、LoadImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

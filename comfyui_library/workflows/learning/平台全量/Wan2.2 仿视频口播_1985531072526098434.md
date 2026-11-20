---
key: 平台全量/Wan2.2 仿视频口播_1985531072526098434.json
name: Wan2.2 仿视频口播_1985531072526098434
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/Wan2.2 仿视频口播_1985531072526098434.json
hash: 1859fea3e22aed9a
coverage: 0.972973
learned_at: 2026-11-14 01:05:40
nodes: [FaceMaskFromPoseKeypoints, TorchCompileModelWanVideoV2, ModelPatchTorchSettings, PathchSageAttentionKJ, Fast Bypasser (rgthree), CLIPLoader, Mute / Bypass Repeater (rgthree), VAELoader, TrimVideoLatent, KSampler, CLIPVisionLoader, ModelSamplingSD3, VAEDecode, ImageConcatMulti, ImageConcatMulti, wanBlockSwap, CLIPVisionEncode, CLIPTextEncode, CLIPTextEncode, GetImageSizeAndCount, VHS_VideoCombine, VHS_VideoCombine, PixelPerfectResolution, DWPreprocessor, ImageCropByMaskAndResize, WanAnimateToVideo, ImageResizeKJv2, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, JWInteger, JWInteger, LoadImage, VHS_LoadVideo, JjkText]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "sa_solver", "scheduler": "beta", "seed": 95416241020747, "steps": 4}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 平台全量/Wan2.2 仿视频口播_1985531072526098434.json

> 来源文件 `comfyui_library/workflows/平台全量/Wan2.2 仿视频口播_1985531072526098434.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（37 个）：
- `FaceMaskFromPoseKeypoints`
- `TorchCompileModelWanVideoV2`
- `ModelPatchTorchSettings`
- `PathchSageAttentionKJ`
- `Fast Bypasser (rgthree)`
- `CLIPLoader`
- `Mute / Bypass Repeater (rgthree)`
- `VAELoader`
- `TrimVideoLatent`
- `KSampler` ★核心
- `CLIPVisionLoader`
- `ModelSamplingSD3`
- `VAEDecode` ★核心
- `ImageConcatMulti`
- `ImageConcatMulti`
- `wanBlockSwap`
- `CLIPVisionEncode`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `GetImageSizeAndCount`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `PixelPerfectResolution`
- `DWPreprocessor`
- `ImageCropByMaskAndResize`
- `WanAnimateToVideo`
- `ImageResizeKJv2`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `JWInteger`
- `JWInteger`
- `LoadImage`
- `VHS_LoadVideo`
- `JjkText`

## 关键参数

- `seed` = `95416241020747`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `sa_solver`
- `scheduler` = `beta`
- `denoise` = `1`

## 知识

覆盖率 **97%**（36/37）

**有卡**：`FaceMaskFromPoseKeypoints`、`TorchCompileModelWanVideoV2`、`ModelPatchTorchSettings`、`PathchSageAttentionKJ`、`Fast Bypasser (rgthree)`、`CLIPLoader`、`Mute / Bypass Repeater (rgthree)`、`VAELoader`、`TrimVideoLatent`、`KSampler`、`CLIPVisionLoader`、`ModelSamplingSD3`、`VAEDecode`、`ImageConcatMulti`、`wanBlockSwap`、`CLIPVisionEncode`、`CLIPTextEncode`、`GetImageSizeAndCount`、`VHS_VideoCombine`、`PixelPerfectResolution`、`DWPreprocessor`、`ImageCropByMaskAndResize`、`WanAnimateToVideo`、`ImageResizeKJv2`、`UNETLoader`、`LoraLoaderModelOnly`、`JWInteger`、`LoadImage`、`VHS_LoadVideo`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、CLIPTextEncode、LoadImage、UNETLoader

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

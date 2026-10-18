---
key: 视频生成/图生视频/Wan2.2 Animate  动作迁移_1992545014192427009.json
name: Wan2.2 Animate  动作迁移_1992545014192427009.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/Wan2.2 Animate  动作迁移_1992545014192427009.json
hash: 9305418dfd463b76
coverage: 0.947368
learned_at: 2026-10-15 22:33:16
nodes: [MarkdownNote, FaceMaskFromPoseKeypoints, TorchCompileModelWanVideoV2, ModelPatchTorchSettings, PathchSageAttentionKJ, Fast Bypasser (rgthree), CLIPLoader, Mute / Bypass Repeater (rgthree), VAELoader, TrimVideoLatent, CLIPVisionLoader, ModelSamplingSD3, VAEDecode, ImageConcatMulti, ImageConcatMulti, JjkText, wanBlockSwap, CLIPVisionEncode, CLIPTextEncode, GetImageSizeAndCount, PixelPerfectResolution, ImageCropByMaskAndResize, WanAnimateToVideo, ImageResizeKJv2, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, JWInteger, JWInteger, LoadImage, DWPreprocessor, KSampler, CLIPTextEncode, VHS_LoadVideo, VHS_VideoCombine, VHS_VideoCombine]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "sa_solver", "scheduler": "beta", "seed": 399210250609761, "steps": 4}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/图生视频/Wan2.2 Animate  动作迁移_1992545014192427009.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1992545014192427009.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（38 个）：
- `MarkdownNote`
- `FaceMaskFromPoseKeypoints`
- `TorchCompileModelWanVideoV2`
- `ModelPatchTorchSettings`
- `PathchSageAttentionKJ`
- `Fast Bypasser (rgthree)`
- `CLIPLoader`
- `Mute / Bypass Repeater (rgthree)`
- `VAELoader`
- `TrimVideoLatent`
- `CLIPVisionLoader`
- `ModelSamplingSD3`
- `VAEDecode` ★核心
- `ImageConcatMulti`
- `ImageConcatMulti`
- `JjkText`
- `wanBlockSwap`
- `CLIPVisionEncode`
- `CLIPTextEncode` ★核心
- `GetImageSizeAndCount`
- `PixelPerfectResolution`
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
- `DWPreprocessor`
- `KSampler` ★核心
- `CLIPTextEncode` ★核心
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `VHS_VideoCombine`

## 关键参数

- `seed` = `399210250609761`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `sa_solver`
- `scheduler` = `beta`
- `denoise` = `1`

## 知识

覆盖率 **95%**（36/38）

**有卡**：`FaceMaskFromPoseKeypoints`、`TorchCompileModelWanVideoV2`、`ModelPatchTorchSettings`、`PathchSageAttentionKJ`、`Fast Bypasser (rgthree)`、`CLIPLoader`、`Mute / Bypass Repeater (rgthree)`、`VAELoader`、`TrimVideoLatent`、`CLIPVisionLoader`、`ModelSamplingSD3`、`VAEDecode`、`ImageConcatMulti`、`wanBlockSwap`、`CLIPVisionEncode`、`CLIPTextEncode`、`GetImageSizeAndCount`、`PixelPerfectResolution`、`ImageCropByMaskAndResize`、`WanAnimateToVideo`、`ImageResizeKJv2`、`UNETLoader`、`LoraLoaderModelOnly`、`JWInteger`、`LoadImage`、`DWPreprocessor`、`KSampler`、`VHS_LoadVideo`、`VHS_VideoCombine`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

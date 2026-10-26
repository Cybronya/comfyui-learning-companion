---
key: 数字人/数字人/换装+换脸+换背景- Animate Wan2.2_1975014128706301953.json
name: 换装+换脸+换背景- Animate Wan2.2_1975014128706301953
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/数字人/数字人/换装+换脸+换背景- Animate Wan2.2_1975014128706301953.json
hash: 6c18227f1fcd58cb
coverage: 0.534247
learned_at: 2026-10-26 02:02:21
nodes: [GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, VAEDecode, GetNode, ImageResizeKJv2, SetNode, GetNode, GetNode, SetNode, GetNode, easy cleanGpuUsed, easy sleep, SetNode, SetNode, SetNode, VHS_VideoCombine, CLIPVisionLoader, CLIPVisionEncode, SetNode, CLIPLoader, UnetLoaderGGUF, TrimVideoLatent, SetNode, VAELoader, SetNode, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, wanBlockSwap, ModelSamplingSD3, TorchCompileModelWanVideoV2, PathchSageAttentionKJ, KSampler, WanAnimateToVideo, SetNode, SetNode, OnnxDetectionModelLoader, SimpleMath+, easy showAnything, StringToInt, SetNode, SetNode, LoadImage, CLIPTextEncode, PoseAndFaceDetection, DrawViTPose, SetNode, ImageResizeKJv2, SetNode, GetNode, GetNode, GetNode, VHS_LoadVideo, CLIPTextEncode, GetNode, GetNode, GetImageSizeAndCount, ImageConcatMulti, VHS_VideoCombine, Int, Fast Groups Bypasser (rgthree), DF_Integer, VHS_VideoCombine, MarkdownNote, LoadImage, VHS_VideoCombine]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "sa_solver", "scheduler": "beta", "seed": 303382830094583, "steps": 4}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 数字人/数字人/换装+换脸+换背景- Animate Wan2.2_1975014128706301953.json

> 来源文件 `comfyui_library/workflows/数字人/数字人/换装+换脸+换背景- Animate Wan2.2_1975014128706301953.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（73 个）：
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `VAEDecode` ★核心
- `GetNode`
- `ImageResizeKJv2`
- `SetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `easy cleanGpuUsed`
- `easy sleep`
- `SetNode`
- `SetNode`
- `SetNode`
- `VHS_VideoCombine`
- `CLIPVisionLoader`
- `CLIPVisionEncode`
- `SetNode`
- `CLIPLoader`
- `UnetLoaderGGUF` ★核心
- `TrimVideoLatent`
- `SetNode`
- `VAELoader`
- `SetNode`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `wanBlockSwap`
- `ModelSamplingSD3`
- `TorchCompileModelWanVideoV2`
- `PathchSageAttentionKJ`
- `KSampler` ★核心
- `WanAnimateToVideo`
- `SetNode`
- `SetNode`
- `OnnxDetectionModelLoader`
- `SimpleMath+`
- `easy showAnything`
- `StringToInt`
- `SetNode`
- `SetNode`
- `LoadImage`
- `CLIPTextEncode` ★核心
- `PoseAndFaceDetection`
- `DrawViTPose`
- `SetNode`
- `ImageResizeKJv2`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `VHS_LoadVideo`
- `CLIPTextEncode` ★核心
- `GetNode`
- `GetNode`
- `GetImageSizeAndCount`
- `ImageConcatMulti`
- `VHS_VideoCombine`
- `Int`
- `Fast Groups Bypasser (rgthree)`
- `DF_Integer`
- `VHS_VideoCombine`
- `MarkdownNote`
- `LoadImage`
- `VHS_VideoCombine`

## 关键参数

- `seed` = `303382830094583`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `sa_solver`
- `scheduler` = `beta`
- `denoise` = `1`

## 知识

覆盖率 **53%**（39/73）

**有卡**：`VAEDecode`、`ImageResizeKJv2`、`easy cleanGpuUsed`、`easy sleep`、`VHS_VideoCombine`、`CLIPVisionLoader`、`CLIPVisionEncode`、`CLIPLoader`、`UnetLoaderGGUF`、`TrimVideoLatent`、`VAELoader`、`LoraLoaderModelOnly`、`wanBlockSwap`、`ModelSamplingSD3`、`TorchCompileModelWanVideoV2`、`PathchSageAttentionKJ`、`KSampler`、`WanAnimateToVideo`、`OnnxDetectionModelLoader`、`SimpleMath+`、`StringToInt`、`LoadImage`、`CLIPTextEncode`、`PoseAndFaceDetection`、`DrawViTPose`、`VHS_LoadVideo`、`GetImageSizeAndCount`、`ImageConcatMulti`、`Int`、`DF_Integer`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、CLIPVisionEncode

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

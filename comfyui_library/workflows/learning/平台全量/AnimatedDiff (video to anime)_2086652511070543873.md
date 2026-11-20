---
key: 平台全量/AnimatedDiff (video to anime)_2086652511070543873.json
name: AnimatedDiff (video to anime)_2086652511070543873
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/AnimatedDiff (video to anime)_2086652511070543873.json
hash: 8db8b54bc36c057d
coverage: 0.97619
learned_at: 2026-11-14 00:18:23
nodes: [AnyLineArtPreprocessor_aux, ImageResize+, ADE_AnimateDiffUniformContextOptions, ADE_ApplyAnimateDiffModelSimple, SimpleMathInt+, DifferentialDiffusion, MaskToImage, RemapImageRange, ImageCompositeMasked, SetLatentNoiseMask, VAEEncode, ImageBlur, ImageToMask, ADE_UseEvolvedSampling, ShowText|pysssss, ADE_LoadAnimateDiffModel, DepthAnythingPreprocessor, ControlNetLoader, ControlNetLoader, DownloadAndLoadFlorence2Model, ImageFromBatch, CLIPTextEncode, KSampler, VAELoader, UpscaleModelLoader, VAELoader, VAEDecodeTiled, UpscaleImageByUsingModel, VHS_VideoCombine, RMBG, RemapImageRange, CheckpointLoaderSimpleWithNoiseSelect, SimpleMathBoolean+, Florence2Run, FreeU_V2, ACN_AdvancedControlNetApply_v2, ACN_AdvancedControlNetApply_v2, SimpleMathDual+, VHS_LoadVideo, Text Multiline, SimpleCondition+, CLIPTextEncode]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换]
parameters: {"cfg": 4, "checkpoint": "Colorful Anime Kawa 彩璃二次元 _v3.0.safetensors", "controlnet_strength": 0.9000000000000001, "denoise": 1, "sampler_name": "euler", "scheduler": "sgm_uniform", "seed": 1081164106885654, "steps": 8}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换]
---

# 平台全量/AnimatedDiff (video to anime)_2086652511070543873.json

> 来源文件 `comfyui_library/workflows/平台全量/AnimatedDiff (video to anime)_2086652511070543873.json`

## 结构

**生成流程**：Model → Encode → Condition → Control → Sampling → Decode → Process → Other

**节点**（42 个）：
- `AnyLineArtPreprocessor_aux`
- `ImageResize+`
- `ADE_AnimateDiffUniformContextOptions`
- `ADE_ApplyAnimateDiffModelSimple`
- `SimpleMathInt+`
- `DifferentialDiffusion`
- `MaskToImage`
- `RemapImageRange`
- `ImageCompositeMasked`
- `SetLatentNoiseMask`
- `VAEEncode` ★核心
- `ImageBlur`
- `ImageToMask`
- `ADE_UseEvolvedSampling`
- `ShowText|pysssss`
- `ADE_LoadAnimateDiffModel`
- `DepthAnythingPreprocessor`
- `ControlNetLoader`
- `ControlNetLoader`
- `DownloadAndLoadFlorence2Model`
- `ImageFromBatch`
- `CLIPTextEncode` ★核心
- `KSampler` ★核心
- `VAELoader`
- `UpscaleModelLoader`
- `VAELoader`
- `VAEDecodeTiled` ★核心
- `UpscaleImageByUsingModel`
- `VHS_VideoCombine`
- `RMBG`
- `RemapImageRange`
- `CheckpointLoaderSimpleWithNoiseSelect` ★核心
- `SimpleMathBoolean+`
- `Florence2Run`
- `FreeU_V2`
- `ACN_AdvancedControlNetApply_v2` ★核心
- `ACN_AdvancedControlNetApply_v2` ★核心
- `SimpleMathDual+`
- `VHS_LoadVideo`
- `Text Multiline`
- `SimpleCondition+`
- `CLIPTextEncode` ★核心

## 关键参数

- `seed` = `1081164106885654`
- `steps` = `8`
- `cfg` = `4`
- `sampler_name` = `euler`
- `scheduler` = `sgm_uniform`
- `denoise` = `1`
- `checkpoint` = `Colorful Anime Kawa 彩璃二次元 _v3.0.safetensors`
- `controlnet_strength` = `0.9000000000000001`

## 知识

覆盖率 **98%**（41/42）

**有卡**：`AnyLineArtPreprocessor_aux`、`ImageResize+`、`ADE_AnimateDiffUniformContextOptions`、`ADE_ApplyAnimateDiffModelSimple`、`SimpleMathInt+`、`DifferentialDiffusion`、`MaskToImage`、`RemapImageRange`、`ImageCompositeMasked`、`SetLatentNoiseMask`、`VAEEncode`、`ImageBlur`、`ImageToMask`、`ADE_UseEvolvedSampling`、`ADE_LoadAnimateDiffModel`、`DepthAnythingPreprocessor`、`ControlNetLoader`、`DownloadAndLoadFlorence2Model`、`ImageFromBatch`、`CLIPTextEncode`、`KSampler`、`VAELoader`、`UpscaleModelLoader`、`VAEDecodeTiled`、`UpscaleImageByUsingModel`、`VHS_VideoCombine`、`RMBG`、`CheckpointLoaderSimpleWithNoiseSelect`、`SimpleMathBoolean+`、`Florence2Run`、`FreeU_V2`、`ACN_AdvancedControlNetApply_v2`、`SimpleMathDual+`、`VHS_LoadVideo`、`Text Multiline`、`SimpleCondition+`

**用到的条目**：KSampler、VAELoader、CLIPTextEncode、ACN_AdvancedControlNetApply_v2、ControlNetLoader、DepthAnythingPreprocessor、SetLatentNoiseMask、VAEDecodeTiled

## 参数体检

发现 2 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换

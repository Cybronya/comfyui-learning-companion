---
key: 平台全量/wan2.1 fun 视频转绘_1919990746303102978.json
name: wan2.1 fun 视频转绘_1919990746303102978
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/wan2.1 fun 视频转绘_1919990746303102978.json
hash: 754716b49a009b1c
coverage: 0.967742
learned_at: 2026-11-14 01:19:03
nodes: [easy showAnything, UNETLoader, LoraLoaderModelOnly, SkipLayerGuidanceWanVideo, WanVideoTeaCacheKJ, CLIPLoader, CLIPTextEncode, CLIPTextEncode, Florence2ModelLoader, Florence2Run, OpenposePreprocessor, CLIPVisionLoader, AIO_Preprocessor, AIO_Preprocessor, ImageBlend, ImageResizeKJ, ModelSamplingSD3, KSampler, VAEDecodeTiled, VHS_VideoCombine, VHS_VideoCombine, VAELoader, WanFunControlToVideo, INTConstant, INTConstant, ImageResizeKJ, CLIPVisionEncode, LoadImage, EmptyHunyuanLatentVideo, INTConstant, VHS_LoadVideo]
patterns: []
missing: []
problems: [[high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换]
parameters: {"cfg": 5, "denoise": 1, "sampler_name": "euler", "scheduler": "normal", "seed": 782022367296196, "steps": 20}
discoveries: [[high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换]
---

# 平台全量/wan2.1 fun 视频转绘_1919990746303102978.json

> 来源文件 `comfyui_library/workflows/平台全量/wan2.1 fun 视频转绘_1919990746303102978.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（31 个）：
- `easy showAnything`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `SkipLayerGuidanceWanVideo`
- `WanVideoTeaCacheKJ`
- `CLIPLoader`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `Florence2ModelLoader`
- `Florence2Run`
- `OpenposePreprocessor`
- `CLIPVisionLoader`
- `AIO_Preprocessor`
- `AIO_Preprocessor`
- `ImageBlend`
- `ImageResizeKJ`
- `ModelSamplingSD3`
- `KSampler` ★核心
- `VAEDecodeTiled` ★核心
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `VAELoader`
- `WanFunControlToVideo`
- `INTConstant`
- `INTConstant`
- `ImageResizeKJ`
- `CLIPVisionEncode`
- `LoadImage`
- `EmptyHunyuanLatentVideo`
- `INTConstant`
- `VHS_LoadVideo`

## 关键参数

- `seed` = `782022367296196`
- `steps` = `20`
- `cfg` = `5`
- `sampler_name` = `euler`
- `scheduler` = `normal`
- `denoise` = `1`

## 知识

覆盖率 **97%**（30/31）

**有卡**：`UNETLoader`、`LoraLoaderModelOnly`、`SkipLayerGuidanceWanVideo`、`WanVideoTeaCacheKJ`、`CLIPLoader`、`CLIPTextEncode`、`Florence2ModelLoader`、`Florence2Run`、`OpenposePreprocessor`、`CLIPVisionLoader`、`AIO_Preprocessor`、`ImageBlend`、`ImageResizeKJ`、`ModelSamplingSD3`、`KSampler`、`VAEDecodeTiled`、`VHS_VideoCombine`、`VAELoader`、`WanFunControlToVideo`、`INTConstant`、`CLIPVisionEncode`、`LoadImage`、`EmptyHunyuanLatentVideo`、`VHS_LoadVideo`

**用到的条目**：KSampler、VAELoader、LoraLoaderModelOnly、CLIPLoader、CLIPTextEncode、LoadImage、UNETLoader、OpenposePreprocessor

## 参数体检

发现 1 个问题：
- [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换

## 学习发现

- [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换

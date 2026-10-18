---
key: 视频生成/图生视频/Furry AI Dance Generator｜KSK Custom Edition_2072998868763320320.json
name: Furry AI Dance Generator｜KSK Custom Edition_2072998868763320320.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/Furry AI Dance Generator｜KSK Custom Edition_2072998868763320320.json
hash: d1db127149a6e1c5
coverage: 0.827586
learned_at: 2026-10-15 22:41:00
nodes: [CLIPTextEncode, VAELoader, Reroute, ModelSamplingSD3, ModelPatchTorchSettings, PathchSageAttentionKJ, TrimVideoLatent, VAEDecode, ComfyEverAnimateTrimImages, easy forLoopStart, ComfyEverAnimate, TrimVideoLatent, VAEDecode, ComfyEverAnimateTrimImages, ImageBatch, easy forLoopEnd, KSampler, INTConstant, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, CLIPLoader, ComfyMathExpression, CLIPTextEncode, VHS_VideoCombine, WD14Tagger|pysssss, WanChunkFeedForward, ModelMemoryUsageFactorOverride, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Note, INTConstant, VHS_LoadVideo, INTConstant, INTConstant, ImageResizeKJv2, GetImageSizeAndCount, OnnxDetectionModelLoader, DrawViTPose, PoseAndFaceDetection, VHS_VideoInfo, LoadImage, INTConstant, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, ComfyEverAnimate, KSampler]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "lcm", "scheduler": "normal", "seed": 42, "steps": 4}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/图生视频/Furry AI Dance Generator｜KSK Custom Edition_2072998868763320320.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2072998868763320320.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（58 个）：
- `CLIPTextEncode` ★核心
- `VAELoader`
- `Reroute`
- `ModelSamplingSD3`
- `ModelPatchTorchSettings`
- `PathchSageAttentionKJ`
- `TrimVideoLatent`
- `VAEDecode` ★核心
- `ComfyEverAnimateTrimImages`
- `easy forLoopStart`
- `ComfyEverAnimate`
- `TrimVideoLatent`
- `VAEDecode` ★核心
- `ComfyEverAnimateTrimImages`
- `ImageBatch`
- `easy forLoopEnd`
- `KSampler` ★核心
- `INTConstant`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `CLIPLoader`
- `ComfyMathExpression`
- `CLIPTextEncode` ★核心
- `VHS_VideoCombine`
- `WD14Tagger|pysssss`
- `WanChunkFeedForward`
- `ModelMemoryUsageFactorOverride`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Note`
- `INTConstant`
- `VHS_LoadVideo`
- `INTConstant`
- `INTConstant`
- `ImageResizeKJv2`
- `GetImageSizeAndCount`
- `OnnxDetectionModelLoader`
- `DrawViTPose`
- `PoseAndFaceDetection`
- `VHS_VideoInfo`
- `LoadImage`
- `INTConstant`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `ComfyEverAnimate`
- `KSampler` ★核心

## 关键参数

- `seed` = `42`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `lcm`
- `scheduler` = `normal`
- `denoise` = `1`

## 知识

覆盖率 **83%**（48/58）

**有卡**：`CLIPTextEncode`、`VAELoader`、`ModelSamplingSD3`、`ModelPatchTorchSettings`、`PathchSageAttentionKJ`、`TrimVideoLatent`、`VAEDecode`、`ComfyEverAnimateTrimImages`、`easy forLoopStart`、`ComfyEverAnimate`、`ImageBatch`、`easy forLoopEnd`、`KSampler`、`INTConstant`、`UNETLoader`、`LoraLoaderModelOnly`、`CLIPLoader`、`ComfyMathExpression`、`VHS_VideoCombine`、`WD14Tagger|pysssss`、`WanChunkFeedForward`、`ModelMemoryUsageFactorOverride`、`VHS_LoadVideo`、`ImageResizeKJv2`、`GetImageSizeAndCount`、`OnnxDetectionModelLoader`、`DrawViTPose`、`PoseAndFaceDetection`、`VHS_VideoInfo`、`LoadImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader

## 参数体检

发现 2 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

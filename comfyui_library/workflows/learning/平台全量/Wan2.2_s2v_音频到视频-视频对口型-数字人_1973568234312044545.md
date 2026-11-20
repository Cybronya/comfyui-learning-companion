---
key: 平台全量/Wan2.2_s2v_音频到视频-视频对口型-数字人_1973568234312044545.json
name: Wan2.2_s2v_音频到视频-视频对口型-数字人_1973568234312044545
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/Wan2.2_s2v_音频到视频-视频对口型-数字人_1973568234312044545.json
hash: 9c2709ec5c79565e
coverage: 0.935484
learned_at: 2026-11-14 01:06:15
nodes: [UNETLoader, CLIPLoader, ModelSamplingSD3, AudioEncoderEncode, VHS_VideoInfoLoaded, easy showAnything, WanSoundImageToVideo, VAELoader, PrimitiveStringMultiline, KSampler, LoraLoaderModelOnly, CLIPTextEncode, CLIPTextEncode, MathExpression|pysssss, floatToInt _O, AudioEncoderLoader, VHS_VideoInfoLoaded, GetImageRangeFromBatch, ImageConcanate, VHS_VideoCombine, VAEDecode, ColorMatch, GetImageRangeFromBatch, ReverseImageBatch, easy imageCount, JWIntegerSub, ReplaceImagesInBatch, ReverseImageBatch, VHS_VideoCombine, VHS_LoadVideo, VHS_LoadVideo]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "uni_pc", "scheduler": "simple", "seed": 356834028351479, "steps": 8}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 平台全量/Wan2.2_s2v_音频到视频-视频对口型-数字人_1973568234312044545.json

> 来源文件 `comfyui_library/workflows/平台全量/Wan2.2_s2v_音频到视频-视频对口型-数字人_1973568234312044545.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（31 个）：
- `UNETLoader` ★核心
- `CLIPLoader`
- `ModelSamplingSD3`
- `AudioEncoderEncode`
- `VHS_VideoInfoLoaded`
- `easy showAnything`
- `WanSoundImageToVideo`
- `VAELoader`
- `PrimitiveStringMultiline`
- `KSampler` ★核心
- `LoraLoaderModelOnly` ★核心
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `MathExpression|pysssss`
- `floatToInt _O`
- `AudioEncoderLoader`
- `VHS_VideoInfoLoaded`
- `GetImageRangeFromBatch`
- `ImageConcanate`
- `VHS_VideoCombine`
- `VAEDecode` ★核心
- `ColorMatch`
- `GetImageRangeFromBatch`
- `ReverseImageBatch`
- `easy imageCount`
- `JWIntegerSub`
- `ReplaceImagesInBatch`
- `ReverseImageBatch`
- `VHS_VideoCombine`
- `VHS_LoadVideo`
- `VHS_LoadVideo`

## 关键参数

- `seed` = `356834028351479`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `uni_pc`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **94%**（29/31）

**有卡**：`UNETLoader`、`CLIPLoader`、`ModelSamplingSD3`、`AudioEncoderEncode`、`VHS_VideoInfoLoaded`、`WanSoundImageToVideo`、`VAELoader`、`KSampler`、`LoraLoaderModelOnly`、`CLIPTextEncode`、`MathExpression|pysssss`、`floatToInt _O`、`AudioEncoderLoader`、`GetImageRangeFromBatch`、`ImageConcanate`、`VHS_VideoCombine`、`VAEDecode`、`ColorMatch`、`ReverseImageBatch`、`easy imageCount`、`JWIntegerSub`、`ReplaceImagesInBatch`、`VHS_LoadVideo`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、CLIPTextEncode、UNETLoader、AudioEncoderEncode

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

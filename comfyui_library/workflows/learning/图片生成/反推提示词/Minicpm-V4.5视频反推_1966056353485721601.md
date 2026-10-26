---
key: 图片生成/反推提示词/Minicpm-V4.5视频反推_1966056353485721601.json
name: Minicpm-V4.5视频反推_1966056353485721601
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/反推提示词/Minicpm-V4.5视频反推_1966056353485721601.json
hash: 4be85a1fb287ce57
coverage: 0.740741
learned_at: 2026-10-26 01:45:45
nodes: [CLIPTextEncode, ModelSamplingSD3, CLIPVisionLoader, CLIPVisionEncode, CLIPTextEncode, Note, easy clearCacheAll, KSampler, easy showAnything, Text Concatenate, VHS_VideoCombine, VAEDecode, VHS_VideoCombine, easy showAnything, WanImageToVideo, AILab_MiniCPM_4_V_Advanced, LoadVideo, CheckpointLoaderSimple, PrimitiveStringMultiline, GetVideoComponents, GetImageRangeFromBatch, LayerUtility: ImageScaleByAspectRatio V2, PrimitiveInt, PrimitiveInt, Primitive integer [Crystools], MathExpression|pysssss, easy showAnything]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "checkpoint": "wan2.2-t2v-rapid-aio-v9.safetensors", "denoise": 1, "sampler_name": "sa_solver", "scheduler": "beta", "seed": 685184510319810, "steps": 4}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/反推提示词/Minicpm-V4.5视频反推_1966056353485721601.json

> 来源文件 `comfyui_library/workflows/图片生成/反推提示词/Minicpm-V4.5视频反推_1966056353485721601.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（27 个）：
- `CLIPTextEncode` ★核心
- `ModelSamplingSD3`
- `CLIPVisionLoader`
- `CLIPVisionEncode`
- `CLIPTextEncode` ★核心
- `Note`
- `easy clearCacheAll`
- `KSampler` ★核心
- `easy showAnything`
- `Text Concatenate`
- `VHS_VideoCombine`
- `VAEDecode` ★核心
- `VHS_VideoCombine`
- `easy showAnything`
- `WanImageToVideo`
- `AILab_MiniCPM_4_V_Advanced`
- `LoadVideo`
- `CheckpointLoaderSimple` ★核心
- `PrimitiveStringMultiline`
- `GetVideoComponents`
- `GetImageRangeFromBatch`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `PrimitiveInt`
- `PrimitiveInt`
- `Primitive integer [Crystools]`
- `MathExpression|pysssss`
- `easy showAnything`

## 关键参数

- `seed` = `685184510319810`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `sa_solver`
- `scheduler` = `beta`
- `denoise` = `1`
- `checkpoint` = `wan2.2-t2v-rapid-aio-v9.safetensors`

## 知识

覆盖率 **74%**（20/27）

**有卡**：`CLIPTextEncode`、`ModelSamplingSD3`、`CLIPVisionLoader`、`CLIPVisionEncode`、`easy clearCacheAll`、`KSampler`、`Text Concatenate`、`VHS_VideoCombine`、`VAEDecode`、`WanImageToVideo`、`AILab_MiniCPM_4_V_Advanced`、`LoadVideo`、`CheckpointLoaderSimple`、`GetVideoComponents`、`GetImageRangeFromBatch`、`LayerUtility: ImageScaleByAspectRatio V2`、`Primitive integer [Crystools]`、`MathExpression|pysssss`

**用到的条目**：KSampler、VAEDecode、CheckpointLoaderSimple、CLIPTextEncode、CLIPVisionEncode、CLIPVisionLoader、GetImageRangeFromBatch、GetVideoComponents

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

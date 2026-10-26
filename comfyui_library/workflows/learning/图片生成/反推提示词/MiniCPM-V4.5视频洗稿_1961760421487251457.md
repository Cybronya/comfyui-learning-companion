---
key: 图片生成/反推提示词/MiniCPM-V4.5视频洗稿_1961760421487251457.json
name: MiniCPM-V4.5视频洗稿_1961760421487251457
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/反推提示词/MiniCPM-V4.5视频洗稿_1961760421487251457.json
hash: 33f4a328ea580d96
coverage: 0.740741
learned_at: 2026-10-26 01:45:39
nodes: [PrimitiveInt, PrimitiveInt, CLIPTextEncode, Primitive integer [Crystools], CheckpointLoaderSimple, ModelSamplingSD3, GetVideoComponents, GetImageRangeFromBatch, Get Image Size, CLIPVisionLoader, CLIPVisionEncode, CLIPTextEncode, Note, easy clearCacheAll, LoadVideo, KSampler, easy showAnything, MathExpression|pysssss, easy showAnything, Text Concatenate, PrimitiveStringMultiline, VHS_VideoCombine, VAEDecode, VHS_VideoCombine, easy showAnything, WanImageToVideo, AILab_MiniCPM_4_V_Advanced]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "checkpoint": "wan2.2-t2v-rapid-aio-v9.safetensors", "denoise": 1, "sampler_name": "sa_solver", "scheduler": "beta", "seed": 736122614882519, "steps": 4}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/反推提示词/MiniCPM-V4.5视频洗稿_1961760421487251457.json

> 来源文件 `comfyui_library/workflows/图片生成/反推提示词/MiniCPM-V4.5视频洗稿_1961760421487251457.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（27 个）：
- `PrimitiveInt`
- `PrimitiveInt`
- `CLIPTextEncode` ★核心
- `Primitive integer [Crystools]`
- `CheckpointLoaderSimple` ★核心
- `ModelSamplingSD3`
- `GetVideoComponents`
- `GetImageRangeFromBatch`
- `Get Image Size`
- `CLIPVisionLoader`
- `CLIPVisionEncode`
- `CLIPTextEncode` ★核心
- `Note`
- `easy clearCacheAll`
- `LoadVideo`
- `KSampler` ★核心
- `easy showAnything`
- `MathExpression|pysssss`
- `easy showAnything`
- `Text Concatenate`
- `PrimitiveStringMultiline`
- `VHS_VideoCombine`
- `VAEDecode` ★核心
- `VHS_VideoCombine`
- `easy showAnything`
- `WanImageToVideo`
- `AILab_MiniCPM_4_V_Advanced`

## 关键参数

- `checkpoint` = `wan2.2-t2v-rapid-aio-v9.safetensors`
- `seed` = `736122614882519`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `sa_solver`
- `scheduler` = `beta`
- `denoise` = `1`

## 知识

覆盖率 **74%**（20/27）

**有卡**：`CLIPTextEncode`、`Primitive integer [Crystools]`、`CheckpointLoaderSimple`、`ModelSamplingSD3`、`GetVideoComponents`、`GetImageRangeFromBatch`、`Get Image Size`、`CLIPVisionLoader`、`CLIPVisionEncode`、`easy clearCacheAll`、`LoadVideo`、`KSampler`、`MathExpression|pysssss`、`Text Concatenate`、`VHS_VideoCombine`、`VAEDecode`、`WanImageToVideo`、`AILab_MiniCPM_4_V_Advanced`

**用到的条目**：KSampler、VAEDecode、CheckpointLoaderSimple、CLIPTextEncode、CLIPVisionEncode、CLIPVisionLoader、Get Image Size、GetImageRangeFromBatch

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

---
key: 平台全量/MiniCPM-V4.5视频洗稿_1973417503571447810.json
name: MiniCPM-V4.5视频洗稿_1973417503571447810
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/MiniCPM-V4.5视频洗稿_1973417503571447810.json
hash: 2916fe7acc65c360
coverage: 0.823529
learned_at: 2026-11-14 00:40:38
nodes: [ModelSamplingSD3, CLIPVisionLoader, CLIPVisionEncode, easy clearCacheAll, KSampler, Text Concatenate, WanImageToVideo, CLIPTextEncode, CLIPTextEncode, CheckpointLoaderSimple, MathExpression|pysssss, ImageConcatMulti, easy showAnything, VHS_VideoCombine, VHS_VideoCombine, AddLabel, AddLabel, PrimitiveStringMultiline, ImageFromBatch+, Reroute, VAEDecode, GetImageRangeFromBatch, Get Image Size, ImageResize+, easy showAnything, CreateVideo, MathExpression|pysssss, AILab_MiniCPM_4_V_Advanced, CM_FloatToInt, PrimitiveInt, PrimitiveInt, VHS_LoadVideo, FloatConstant, Primitive integer [Crystools]]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "checkpoint": "wan2.2-t2v-rapid-aio-v10.safetensors", "denoise": 1, "sampler_name": "sa_solver", "scheduler": "beta", "seed": 472984712272768, "steps": 4}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 平台全量/MiniCPM-V4.5视频洗稿_1973417503571447810.json

> 来源文件 `comfyui_library/workflows/平台全量/MiniCPM-V4.5视频洗稿_1973417503571447810.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（34 个）：
- `ModelSamplingSD3`
- `CLIPVisionLoader`
- `CLIPVisionEncode`
- `easy clearCacheAll`
- `KSampler` ★核心
- `Text Concatenate`
- `WanImageToVideo`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `CheckpointLoaderSimple` ★核心
- `MathExpression|pysssss`
- `ImageConcatMulti`
- `easy showAnything`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `AddLabel`
- `AddLabel`
- `PrimitiveStringMultiline`
- `ImageFromBatch+`
- `Reroute`
- `VAEDecode` ★核心
- `GetImageRangeFromBatch`
- `Get Image Size`
- `ImageResize+`
- `easy showAnything`
- `CreateVideo`
- `MathExpression|pysssss`
- `AILab_MiniCPM_4_V_Advanced`
- `CM_FloatToInt`
- `PrimitiveInt`
- `PrimitiveInt`
- `VHS_LoadVideo`
- `FloatConstant`
- `Primitive integer [Crystools]`

## 关键参数

- `seed` = `472984712272768`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `sa_solver`
- `scheduler` = `beta`
- `denoise` = `1`
- `checkpoint` = `wan2.2-t2v-rapid-aio-v10.safetensors`

## 知识

覆盖率 **82%**（28/34）

**有卡**：`ModelSamplingSD3`、`CLIPVisionLoader`、`CLIPVisionEncode`、`easy clearCacheAll`、`KSampler`、`Text Concatenate`、`WanImageToVideo`、`CLIPTextEncode`、`CheckpointLoaderSimple`、`MathExpression|pysssss`、`ImageConcatMulti`、`VHS_VideoCombine`、`AddLabel`、`ImageFromBatch+`、`VAEDecode`、`GetImageRangeFromBatch`、`Get Image Size`、`ImageResize+`、`CreateVideo`、`AILab_MiniCPM_4_V_Advanced`、`CM_FloatToInt`、`VHS_LoadVideo`、`FloatConstant`、`Primitive integer [Crystools]`

**用到的条目**：KSampler、VAEDecode、CheckpointLoaderSimple、CLIPTextEncode、CLIPVisionEncode、CLIPVisionLoader、Get Image Size、ImageResize+

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

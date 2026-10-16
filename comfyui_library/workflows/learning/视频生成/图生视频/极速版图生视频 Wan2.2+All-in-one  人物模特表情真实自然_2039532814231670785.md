---
key: 视频生成/图生视频/极速版图生视频 Wan2.2+All-in-one  人物模特表情真实自然_2039532814231670785.json
name: 极速版图生视频 Wan2.2+All-in-one  人物模特表情真实自然_2039532814231670785.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2039532814231670785.json
hash: 413d8c72d40f7929
coverage: 1
learned_at: 2026-10-15 22:36:09
nodes: [CLIPVisionEncode, WanImageToVideo, CLIPTextEncode, MathExpression|pysssss, CLIPLoader, CLIPTextEncode, CheckpointLoaderSimple, JWInteger, JWInteger, LoraLoaderModelOnly, PathchSageAttentionKJ, LayerUtility: ImageScaleByAspectRatio V2, CLIPVisionLoader, JWFloat, VAEDecode, KSampler, ModelSamplingSD3, JWInteger, CR Prompt Text, VHS_VideoCombine, LoadImage]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "checkpoint": "wan2.2-i2v-rapid-aio-v10-nsfw.safetensors", "denoise": 1, "sampler_name": "sa_solver", "scheduler": "beta", "seed": 467586487966044, "steps": 4}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/图生视频/极速版图生视频 Wan2.2+All-in-one  人物模特表情真实自然_2039532814231670785.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2039532814231670785.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（21 个）：
- `CLIPVisionEncode`
- `WanImageToVideo`
- `CLIPTextEncode` ★核心
- `MathExpression|pysssss`
- `CLIPLoader`
- `CLIPTextEncode` ★核心
- `CheckpointLoaderSimple` ★核心
- `JWInteger`
- `JWInteger`
- `LoraLoaderModelOnly` ★核心
- `PathchSageAttentionKJ`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `CLIPVisionLoader`
- `JWFloat`
- `VAEDecode` ★核心
- `KSampler` ★核心
- `ModelSamplingSD3`
- `JWInteger`
- `CR Prompt Text`
- `VHS_VideoCombine`
- `LoadImage`

## 关键参数

- `checkpoint` = `wan2.2-i2v-rapid-aio-v10-nsfw.safetensors`
- `seed` = `467586487966044`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `sa_solver`
- `scheduler` = `beta`
- `denoise` = `1`

## 知识

覆盖率 **100%**（21/21）

**有卡**：`CLIPVisionEncode`、`WanImageToVideo`、`CLIPTextEncode`、`MathExpression|pysssss`、`CLIPLoader`、`CheckpointLoaderSimple`、`JWInteger`、`LoraLoaderModelOnly`、`PathchSageAttentionKJ`、`LayerUtility: ImageScaleByAspectRatio V2`、`CLIPVisionLoader`、`JWFloat`、`VAEDecode`、`KSampler`、`ModelSamplingSD3`、`CR Prompt Text`、`VHS_VideoCombine`、`LoadImage`

**用到的条目**：KSampler、VAEDecode、LoraLoaderModelOnly、CheckpointLoaderSimple、CLIPTextEncode、CLIPLoader、LoadImage、CLIPVisionEncode

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

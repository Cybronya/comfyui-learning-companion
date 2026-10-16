---
key: 视频生成/图生视频/图生视频极速版+人物表情真实自然+Wan2.2+All-in-one_2046422966447116289.json
name: 图生视频极速版+人物表情真实自然+Wan2.2+All-in-one_2046422966447116289.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2046422966447116289.json
hash: fd5e92d8883e7ba7
coverage: 1
learned_at: 2026-10-15 22:36:57
nodes: [CLIPVisionEncode, WanImageToVideo, CLIPTextEncode, MathExpression|pysssss, CLIPLoader, CLIPTextEncode, CheckpointLoaderSimple, JWInteger, JWInteger, LoraLoaderModelOnly, PathchSageAttentionKJ, LayerUtility: ImageScaleByAspectRatio V2, CLIPVisionLoader, JWFloat, VAEDecode, KSampler, ModelSamplingSD3, JWInteger, VHS_VideoCombine, LoadImage, CR Prompt Text]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "checkpoint": "wan2.2-i2v-rapid-aio-v10-nsfw.safetensors", "denoise": 1, "sampler_name": "sa_solver", "scheduler": "beta", "seed": 1013556653486393, "steps": 4}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/图生视频/图生视频极速版+人物表情真实自然+Wan2.2+All-in-one_2046422966447116289.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2046422966447116289.json`

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
- `VHS_VideoCombine`
- `LoadImage`
- `CR Prompt Text`

## 关键参数

- `checkpoint` = `wan2.2-i2v-rapid-aio-v10-nsfw.safetensors`
- `seed` = `1013556653486393`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `sa_solver`
- `scheduler` = `beta`
- `denoise` = `1`

## 知识

覆盖率 **100%**（21/21）

**有卡**：`CLIPVisionEncode`、`WanImageToVideo`、`CLIPTextEncode`、`MathExpression|pysssss`、`CLIPLoader`、`CheckpointLoaderSimple`、`JWInteger`、`LoraLoaderModelOnly`、`PathchSageAttentionKJ`、`LayerUtility: ImageScaleByAspectRatio V2`、`CLIPVisionLoader`、`JWFloat`、`VAEDecode`、`KSampler`、`ModelSamplingSD3`、`VHS_VideoCombine`、`LoadImage`、`CR Prompt Text`

**用到的条目**：KSampler、VAEDecode、LoraLoaderModelOnly、CheckpointLoaderSimple、CLIPTextEncode、CLIPLoader、LoadImage、CLIPVisionEncode

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

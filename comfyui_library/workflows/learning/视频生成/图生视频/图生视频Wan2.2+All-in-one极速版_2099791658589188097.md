---
key: 视频生成/图生视频/图生视频Wan2.2+All-in-one极速版_2099791658589188097.json
name: 图生视频Wan2.2+All-in-one极速版_2099791658589188097
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/图生视频Wan2.2+All-in-one极速版_2099791658589188097.json
hash: ef79b7de0ba5360f
coverage: 1
learned_at: 2026-10-17 01:59:51
nodes: [WanImageToVideo, CLIPTextEncode, MathExpression|pysssss, CLIPLoader, CLIPTextEncode, LoadLatent, VAEDecode, VHS_VideoCombine, VAELoader, CR Prompt Text, CheckpointLoaderSimple, JWInteger, JWInteger, LoraLoaderModelOnly, PathchSageAttentionKJ, LayerUtility: ImageScaleByAspectRatio V2, CLIPVisionLoader, JWFloat, VAEDecode, KSampler, ModelSamplingSD3, VHS_VideoCombine, JWInteger, CLIPVisionEncode, LoadImage]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "checkpoint": "wan2.2-i2v-rapid-aio-v10-nsfw.safetensors", "denoise": 1, "sampler_name": "sa_solver", "scheduler": "beta", "seed": 105529880925581, "steps": 4}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/图生视频/图生视频Wan2.2+All-in-one极速版_2099791658589188097.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/图生视频Wan2.2+All-in-one极速版_2099791658589188097.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（25 个）：
- `WanImageToVideo`
- `CLIPTextEncode` ★核心
- `MathExpression|pysssss`
- `CLIPLoader`
- `CLIPTextEncode` ★核心
- `LoadLatent`
- `VAEDecode` ★核心
- `VHS_VideoCombine`
- `VAELoader`
- `CR Prompt Text`
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
- `VHS_VideoCombine`
- `JWInteger`
- `CLIPVisionEncode`
- `LoadImage`

## 关键参数

- `checkpoint` = `wan2.2-i2v-rapid-aio-v10-nsfw.safetensors`
- `seed` = `105529880925581`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `sa_solver`
- `scheduler` = `beta`
- `denoise` = `1`

## 知识

覆盖率 **100%**（25/25）

**有卡**：`WanImageToVideo`、`CLIPTextEncode`、`MathExpression|pysssss`、`CLIPLoader`、`LoadLatent`、`VAEDecode`、`VHS_VideoCombine`、`VAELoader`、`CR Prompt Text`、`CheckpointLoaderSimple`、`JWInteger`、`LoraLoaderModelOnly`、`PathchSageAttentionKJ`、`LayerUtility: ImageScaleByAspectRatio V2`、`CLIPVisionLoader`、`JWFloat`、`KSampler`、`ModelSamplingSD3`、`CLIPVisionEncode`、`LoadImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CheckpointLoaderSimple、CLIPTextEncode、CLIPLoader、LoadImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

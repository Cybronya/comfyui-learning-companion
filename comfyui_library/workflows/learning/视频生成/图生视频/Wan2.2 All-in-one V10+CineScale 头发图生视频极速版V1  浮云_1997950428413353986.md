---
key: 视频生成/图生视频/Wan2.2 All-in-one V10+CineScale 头发图生视频极速版V1  浮云_1997950428413353986.json
name: Wan2.2 All-in-one V10+CineScale 头发图生视频极速版V1  浮云_1997950428413353986.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1997950428413353986.json
hash: 3f6587432b33086f
coverage: 1
learned_at: 2026-10-15 22:33:31
nodes: [CLIPVisionEncode, WanImageToVideo, ModelSamplingSD3, JWInteger, CLIPTextEncode, KSampler, LoraLoaderModelOnly, PathchSageAttentionKJ, CLIPTextEncode, CLIPLoader, JWInteger, SaveLatent, LayerUtility: ImageScaleByAspectRatio V2, CLIPVisionLoader, CheckpointLoaderSimple, VAEDecode, VHS_VideoCombine, CR Prompt Text, JWInteger, LoadImage]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "checkpoint": "wan2.2-i2v-rapid-aio-v10-nsfw.safetensors", "denoise": 1, "sampler_name": "sa_solver", "scheduler": "beta", "seed": 51451820664742, "steps": 4}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/图生视频/Wan2.2 All-in-one V10+CineScale 头发图生视频极速版V1  浮云_1997950428413353986.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1997950428413353986.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（20 个）：
- `CLIPVisionEncode`
- `WanImageToVideo`
- `ModelSamplingSD3`
- `JWInteger`
- `CLIPTextEncode` ★核心
- `KSampler` ★核心
- `LoraLoaderModelOnly` ★核心
- `PathchSageAttentionKJ`
- `CLIPTextEncode` ★核心
- `CLIPLoader`
- `JWInteger`
- `SaveLatent`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `CLIPVisionLoader`
- `CheckpointLoaderSimple` ★核心
- `VAEDecode` ★核心
- `VHS_VideoCombine`
- `CR Prompt Text`
- `JWInteger`
- `LoadImage`

## 关键参数

- `seed` = `51451820664742`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `sa_solver`
- `scheduler` = `beta`
- `denoise` = `1`
- `checkpoint` = `wan2.2-i2v-rapid-aio-v10-nsfw.safetensors`

## 知识

覆盖率 **100%**（20/20）

**有卡**：`CLIPVisionEncode`、`WanImageToVideo`、`ModelSamplingSD3`、`JWInteger`、`CLIPTextEncode`、`KSampler`、`LoraLoaderModelOnly`、`PathchSageAttentionKJ`、`CLIPLoader`、`SaveLatent`、`LayerUtility: ImageScaleByAspectRatio V2`、`CLIPVisionLoader`、`CheckpointLoaderSimple`、`VAEDecode`、`VHS_VideoCombine`、`CR Prompt Text`、`LoadImage`

**用到的条目**：KSampler、VAEDecode、LoraLoaderModelOnly、CheckpointLoaderSimple、CLIPTextEncode、CLIPLoader、LoadImage、SaveLatent

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

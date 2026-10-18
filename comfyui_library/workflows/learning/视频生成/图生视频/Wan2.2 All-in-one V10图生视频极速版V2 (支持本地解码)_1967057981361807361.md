---
key: 视频生成/图生视频/Wan2.2 All-in-one V10图生视频极速版V2 (支持本地解码)_1967057981361807361.json
name: Wan2.2 All-in-one V10图生视频极速版V2 (支持本地解码)_1967057981361807361.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/Wan2.2 All-in-one V10图生视频极速版V2 (支持本地解码)_1967057981361807361.json
hash: a3fea393b2edb9bc
coverage: 1
learned_at: 2026-10-15 22:31:40
nodes: [CLIPVisionEncode, WanImageToVideo, CLIPTextEncode, KSampler, PathchSageAttentionKJ, CLIPLoader, JWInteger, JWInteger, CLIPVisionLoader, LoraLoaderModelOnly, TT_img_enc, SaveImage, LoadImage, CLIPTextEncode, JWInteger, LayerUtility: ImageScaleByAspectRatio V2, CR Prompt Text, VAEDecode, ModelSamplingSD3, CheckpointLoaderSimple, VHS_VideoCombine]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "checkpoint": "wan2.2-i2v-rapid-aio-v10-nsfw.safetensors", "denoise": 1, "sampler_name": "sa_solver", "scheduler": "beta", "seed": 499827512192862, "steps": 4}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/图生视频/Wan2.2 All-in-one V10图生视频极速版V2 (支持本地解码)_1967057981361807361.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1967057981361807361.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（21 个）：
- `CLIPVisionEncode`
- `WanImageToVideo`
- `CLIPTextEncode` ★核心
- `KSampler` ★核心
- `PathchSageAttentionKJ`
- `CLIPLoader`
- `JWInteger`
- `JWInteger`
- `CLIPVisionLoader`
- `LoraLoaderModelOnly` ★核心
- `TT_img_enc`
- `SaveImage`
- `LoadImage`
- `CLIPTextEncode` ★核心
- `JWInteger`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `CR Prompt Text`
- `VAEDecode` ★核心
- `ModelSamplingSD3`
- `CheckpointLoaderSimple` ★核心
- `VHS_VideoCombine`

## 关键参数

- `seed` = `499827512192862`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `sa_solver`
- `scheduler` = `beta`
- `denoise` = `1`
- `checkpoint` = `wan2.2-i2v-rapid-aio-v10-nsfw.safetensors`

## 知识

覆盖率 **100%**（21/21）

**有卡**：`CLIPVisionEncode`、`WanImageToVideo`、`CLIPTextEncode`、`KSampler`、`PathchSageAttentionKJ`、`CLIPLoader`、`JWInteger`、`CLIPVisionLoader`、`LoraLoaderModelOnly`、`TT_img_enc`、`SaveImage`、`LoadImage`、`LayerUtility: ImageScaleByAspectRatio V2`、`CR Prompt Text`、`VAEDecode`、`ModelSamplingSD3`、`CheckpointLoaderSimple`、`VHS_VideoCombine`

**用到的条目**：KSampler、VAEDecode、LoraLoaderModelOnly、CheckpointLoaderSimple、CLIPTextEncode、CLIPLoader、LoadImage、CLIPVisionEncode

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

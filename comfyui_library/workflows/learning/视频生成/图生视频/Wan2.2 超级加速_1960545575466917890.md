---
key: 视频生成/图生视频/Wan2.2 超级加速_1960545575466917890.json
name: Wan2.2 超级加速_1960545575466917890.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1960545575466917890.json
hash: 9feea3acc0ada6f5
coverage: 1
learned_at: 2026-10-15 22:31:26
nodes: [CLIPVisionLoader, CLIPVisionEncode, CLIPTextEncode, PathchSageAttentionKJ, WanImageToVideo, ModelSamplingSD3, CLIPTextEncode, LayerUtility: ImageScaleByAspectRatio V2, JWInteger, LoadImage, JWInteger, CheckpointLoaderSimple, KSampler, RandomInt, VAEDecode, ImageFromBatch+, VHS_VideoCombine]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "checkpoint": "wan2.2-i2v-rapid-aio-v10-nsfw.safetensors", "denoise": 1, "sampler_name": "sa_solver", "scheduler": "beta", "seed": 3026735746437, "steps": 4}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/图生视频/Wan2.2 超级加速_1960545575466917890.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1960545575466917890.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（17 个）：
- `CLIPVisionLoader`
- `CLIPVisionEncode`
- `CLIPTextEncode` ★核心
- `PathchSageAttentionKJ`
- `WanImageToVideo`
- `ModelSamplingSD3`
- `CLIPTextEncode` ★核心
- `LayerUtility: ImageScaleByAspectRatio V2`
- `JWInteger`
- `LoadImage`
- `JWInteger`
- `CheckpointLoaderSimple` ★核心
- `KSampler` ★核心
- `RandomInt`
- `VAEDecode` ★核心
- `ImageFromBatch+`
- `VHS_VideoCombine`

## 关键参数

- `checkpoint` = `wan2.2-i2v-rapid-aio-v10-nsfw.safetensors`
- `seed` = `3026735746437`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `sa_solver`
- `scheduler` = `beta`
- `denoise` = `1`

## 知识

覆盖率 **100%**（17/17）

**有卡**：`CLIPVisionLoader`、`CLIPVisionEncode`、`CLIPTextEncode`、`PathchSageAttentionKJ`、`WanImageToVideo`、`ModelSamplingSD3`、`LayerUtility: ImageScaleByAspectRatio V2`、`JWInteger`、`LoadImage`、`CheckpointLoaderSimple`、`KSampler`、`RandomInt`、`VAEDecode`、`ImageFromBatch+`、`VHS_VideoCombine`

**用到的条目**：KSampler、VAEDecode、CheckpointLoaderSimple、CLIPTextEncode、LoadImage、CLIPVisionEncode、CLIPVisionLoader、ModelSamplingSD3

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

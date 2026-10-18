---
key: 视频生成/图生视频/Wan2.2 All-in-one V7图生视频高动态极速版V2_1955969682358632450.json
name: Wan2.2 All-in-one V7图生视频高动态极速版V2_1955969682358632450.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/Wan2.2 All-in-one V7图生视频高动态极速版V2_1955969682358632450.json
hash: fc2f2032f85f97c7
coverage: 1
learned_at: 2026-10-15 22:31:11
nodes: [JWInteger, CheckpointLoaderSimple, CLIPVisionLoader, CLIPVisionEncode, CLIPTextEncode, CLIPTextEncode, PathchSageAttentionKJ, LoadImage, LayerUtility: ImageScaleByAspectRatio V2, WanImageToVideo, ModelSamplingSD3, KSampler, VAEDecode, JWInteger, VHS_VideoCombine, ImageFromBatch+]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "checkpoint": "wan2.2-i2v-rapid-aio-v7.safetensors", "denoise": 1, "sampler_name": "sa_solver", "scheduler": "beta", "seed": 192054346835142, "steps": 4}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/图生视频/Wan2.2 All-in-one V7图生视频高动态极速版V2_1955969682358632450.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1955969682358632450.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（16 个）：
- `JWInteger`
- `CheckpointLoaderSimple` ★核心
- `CLIPVisionLoader`
- `CLIPVisionEncode`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `PathchSageAttentionKJ`
- `LoadImage`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `WanImageToVideo`
- `ModelSamplingSD3`
- `KSampler` ★核心
- `VAEDecode` ★核心
- `JWInteger`
- `VHS_VideoCombine`
- `ImageFromBatch+`

## 关键参数

- `checkpoint` = `wan2.2-i2v-rapid-aio-v7.safetensors`
- `seed` = `192054346835142`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `sa_solver`
- `scheduler` = `beta`
- `denoise` = `1`

## 知识

覆盖率 **100%**（16/16）

**有卡**：`JWInteger`、`CheckpointLoaderSimple`、`CLIPVisionLoader`、`CLIPVisionEncode`、`CLIPTextEncode`、`PathchSageAttentionKJ`、`LoadImage`、`LayerUtility: ImageScaleByAspectRatio V2`、`WanImageToVideo`、`ModelSamplingSD3`、`KSampler`、`VAEDecode`、`VHS_VideoCombine`、`ImageFromBatch+`

**用到的条目**：KSampler、VAEDecode、CheckpointLoaderSimple、CLIPTextEncode、LoadImage、CLIPVisionEncode、CLIPVisionLoader、ModelSamplingSD3

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

---
key: 视频生成/图生视频/Wan2.2 All-in-one V8图生视频高动态极速版V2_1958143493149511681.json
name: Wan2.2 All-in-one V8图生视频高动态极速版V2_1958143493149511681.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/Wan2.2 All-in-one V8图生视频高动态极速版V2_1958143493149511681.json
hash: ef239a51fbb2902e
coverage: 1
learned_at: 2026-10-15 22:31:21
nodes: [JWInteger, CLIPVisionLoader, CLIPVisionEncode, CLIPTextEncode, PathchSageAttentionKJ, LayerUtility: ImageScaleByAspectRatio V2, WanImageToVideo, ModelSamplingSD3, VAEDecode, JWInteger, LoadImage, CheckpointLoaderSimple, ImageFromBatch+, VHS_VideoCombine, CLIPTextEncode, KSampler]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "checkpoint": "wan2.2-i2v-rapid-aio-v8.safetensors", "denoise": 1, "sampler_name": "euler_ancestral", "scheduler": "beta", "seed": 192054346835142, "steps": 4}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/图生视频/Wan2.2 All-in-one V8图生视频高动态极速版V2_1958143493149511681.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1958143493149511681.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（16 个）：
- `JWInteger`
- `CLIPVisionLoader`
- `CLIPVisionEncode`
- `CLIPTextEncode` ★核心
- `PathchSageAttentionKJ`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `WanImageToVideo`
- `ModelSamplingSD3`
- `VAEDecode` ★核心
- `JWInteger`
- `LoadImage`
- `CheckpointLoaderSimple` ★核心
- `ImageFromBatch+`
- `VHS_VideoCombine`
- `CLIPTextEncode` ★核心
- `KSampler` ★核心

## 关键参数

- `checkpoint` = `wan2.2-i2v-rapid-aio-v8.safetensors`
- `seed` = `192054346835142`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `euler_ancestral`
- `scheduler` = `beta`
- `denoise` = `1`

## 知识

覆盖率 **100%**（16/16）

**有卡**：`JWInteger`、`CLIPVisionLoader`、`CLIPVisionEncode`、`CLIPTextEncode`、`PathchSageAttentionKJ`、`LayerUtility: ImageScaleByAspectRatio V2`、`WanImageToVideo`、`ModelSamplingSD3`、`VAEDecode`、`LoadImage`、`CheckpointLoaderSimple`、`ImageFromBatch+`、`VHS_VideoCombine`、`KSampler`

**用到的条目**：KSampler、VAEDecode、CheckpointLoaderSimple、CLIPTextEncode、LoadImage、CLIPVisionEncode、CLIPVisionLoader、ModelSamplingSD3

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

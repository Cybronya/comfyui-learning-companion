---
key: 视频生成/图生视频/Wan2.2 All-in-one图生视频--超级快速_1962517255911288834.json
name: Wan2.2 All-in-one图生视频--超级快速_1962517255911288834.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1962517255911288834.json
hash: 47bf9eb701dbd293
coverage: 1
learned_at: 2026-10-15 22:31:31
nodes: [CLIPVisionEncode, ModelSamplingSD3, PathchSageAttentionKJ, WanImageToVideo, KSampler, CLIPTextEncode, VHS_VideoCombine, CLIPTextEncode, CheckpointLoaderSimple, LoraLoaderModelOnly, CLIPLoader, VAEDecode, SaveImage, CLIPVisionLoader, ImageResizeKJv2, LoadImage]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "checkpoint": "wan2.2-i2v-rapid-aio-nsfw-v9.2.safetensors", "denoise": 1, "sampler_name": "sa_solver", "scheduler": "beta", "seed": 878180124149112, "steps": 4}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/图生视频/Wan2.2 All-in-one图生视频--超级快速_1962517255911288834.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1962517255911288834.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（16 个）：
- `CLIPVisionEncode`
- `ModelSamplingSD3`
- `PathchSageAttentionKJ`
- `WanImageToVideo`
- `KSampler` ★核心
- `CLIPTextEncode` ★核心
- `VHS_VideoCombine`
- `CLIPTextEncode` ★核心
- `CheckpointLoaderSimple` ★核心
- `LoraLoaderModelOnly` ★核心
- `CLIPLoader`
- `VAEDecode` ★核心
- `SaveImage`
- `CLIPVisionLoader`
- `ImageResizeKJv2`
- `LoadImage`

## 关键参数

- `seed` = `878180124149112`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `sa_solver`
- `scheduler` = `beta`
- `denoise` = `1`
- `checkpoint` = `wan2.2-i2v-rapid-aio-nsfw-v9.2.safetensors`

## 知识

覆盖率 **100%**（16/16）

**有卡**：`CLIPVisionEncode`、`ModelSamplingSD3`、`PathchSageAttentionKJ`、`WanImageToVideo`、`KSampler`、`CLIPTextEncode`、`VHS_VideoCombine`、`CheckpointLoaderSimple`、`LoraLoaderModelOnly`、`CLIPLoader`、`VAEDecode`、`SaveImage`、`CLIPVisionLoader`、`ImageResizeKJv2`、`LoadImage`

**用到的条目**：KSampler、VAEDecode、LoraLoaderModelOnly、CheckpointLoaderSimple、CLIPTextEncode、CLIPLoader、LoadImage、CLIPVisionEncode

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

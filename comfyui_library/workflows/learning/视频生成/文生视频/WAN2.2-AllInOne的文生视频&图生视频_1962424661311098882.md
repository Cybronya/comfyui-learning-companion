---
key: 视频生成/文生视频/WAN2.2-AllInOne的文生视频&图生视频_1962424661311098882.json
name: WAN2.2-AllInOne的文生视频&图生视频_1962424661311098882
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/WAN2.2-AllInOne的文生视频&图生视频_1962424661311098882.json
hash: 6293e7ef4b7efbcd
coverage: 1
learned_at: 2026-10-10 23:05:59
nodes: [CLIPTextEncode, VHS_VideoCombine, CLIPTextEncode, EmptyHunyuanLatentVideo, KSampler, ModelSamplingSD3, VAEDecode, CheckpointLoaderSimple, VHS_VideoCombine, KSampler, ModelSamplingSD3, VAEDecode, CLIPVisionEncode, CLIPTextEncode, WanImageToVideo, CLIPTextEncode, LoadImage, CheckpointLoaderSimple, CLIPVisionLoader]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "checkpoint": "wan2.2-i2v-rapid-aio-nsfw-v9.2.safetensors", "denoise": 1, "sampler_name": "sa_solver", "scheduler": "beta", "seed": 192054346835137, "steps": 4}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/文生视频/WAN2.2-AllInOne的文生视频&图生视频_1962424661311098882.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/WAN2.2-AllInOne的文生视频&图生视频_1962424661311098882.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Other

**节点**（19 个）：
- `CLIPTextEncode` ★核心
- `VHS_VideoCombine`
- `CLIPTextEncode` ★核心
- `EmptyHunyuanLatentVideo`
- `KSampler` ★核心
- `ModelSamplingSD3`
- `VAEDecode` ★核心
- `CheckpointLoaderSimple` ★核心
- `VHS_VideoCombine`
- `KSampler` ★核心
- `ModelSamplingSD3`
- `VAEDecode` ★核心
- `CLIPVisionEncode`
- `CLIPTextEncode` ★核心
- `WanImageToVideo`
- `CLIPTextEncode` ★核心
- `LoadImage`
- `CheckpointLoaderSimple` ★核心
- `CLIPVisionLoader`

## 关键参数

- `seed` = `192054346835137`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `sa_solver`
- `scheduler` = `beta`
- `denoise` = `1`
- `checkpoint` = `wan2.2-i2v-rapid-aio-nsfw-v9.2.safetensors`

## 知识

覆盖率 **100%**（19/19）

**有卡**：`CLIPTextEncode`、`VHS_VideoCombine`、`EmptyHunyuanLatentVideo`、`KSampler`、`ModelSamplingSD3`、`VAEDecode`、`CheckpointLoaderSimple`、`CLIPVisionEncode`、`WanImageToVideo`、`LoadImage`、`CLIPVisionLoader`

**用到的条目**：KSampler、VAEDecode、CheckpointLoaderSimple、CLIPTextEncode、LoadImage、CLIPVisionEncode、EmptyHunyuanLatentVideo、CLIPVisionLoader

## 参数体检

发现 2 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

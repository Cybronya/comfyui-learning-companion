---
key: 视频生成/文生视频/MEGA Merge-WAN2.2-AllInOne-图生视频_1968252013240832002.json
name: MEGA Merge-WAN2.2-AllInOne-图生视频_1968252013240832002
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/MEGA Merge-WAN2.2-AllInOne-图生视频_1968252013240832002.json
hash: 94e5a3144f74749c
coverage: 1
learned_at: 2026-10-10 23:00:43
nodes: [LoadImage, WanVideoVACEStartToEndFrame, INTConstant, ImageResizeKJv2, INTConstant, ImageRepeat, TrimVideoLatent, VAEDecode, CLIPTextEncode, VHS_VideoCombine, CheckpointLoaderSimple, KSampler, ModelSamplingSD3, WanVaceToVideo, CLIPTextEncode, GetImageSizeAndCount]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "checkpoint": "wan2.2-rapid-mega-aio-v1.safetensors", "denoise": 1, "sampler_name": "euler", "scheduler": "beta", "seed": 192054346835137, "steps": 6}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/文生视频/MEGA Merge-WAN2.2-AllInOne-图生视频_1968252013240832002.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/MEGA Merge-WAN2.2-AllInOne-图生视频_1968252013240832002.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（16 个）：
- `LoadImage`
- `WanVideoVACEStartToEndFrame`
- `INTConstant`
- `ImageResizeKJv2`
- `INTConstant`
- `ImageRepeat`
- `TrimVideoLatent`
- `VAEDecode` ★核心
- `CLIPTextEncode` ★核心
- `VHS_VideoCombine`
- `CheckpointLoaderSimple` ★核心
- `KSampler` ★核心
- `ModelSamplingSD3`
- `WanVaceToVideo`
- `CLIPTextEncode` ★核心
- `GetImageSizeAndCount`

## 关键参数

- `checkpoint` = `wan2.2-rapid-mega-aio-v1.safetensors`
- `seed` = `192054346835137`
- `steps` = `6`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `beta`
- `denoise` = `1`

## 知识

覆盖率 **100%**（16/16）

**有卡**：`LoadImage`、`WanVideoVACEStartToEndFrame`、`INTConstant`、`ImageResizeKJv2`、`ImageRepeat`、`TrimVideoLatent`、`VAEDecode`、`CLIPTextEncode`、`VHS_VideoCombine`、`CheckpointLoaderSimple`、`KSampler`、`ModelSamplingSD3`、`WanVaceToVideo`、`GetImageSizeAndCount`

**用到的条目**：KSampler、VAEDecode、CheckpointLoaderSimple、CLIPTextEncode、LoadImage、TrimVideoLatent、GetImageSizeAndCount、ImageResizeKJv2

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

---
key: 视频生成/文生视频/MEGA Merge-WAN2.2-AllInOne-首尾帧_1968252973186994178.json
name: MEGA Merge-WAN2.2-AllInOne-首尾帧_1968252973186994178
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/MEGA Merge-WAN2.2-AllInOne-首尾帧_1968252973186994178.json
hash: ecdd95c4b622044b
coverage: 1
learned_at: 2026-10-10 23:00:45
nodes: [TrimVideoLatent, VAEDecode, KSampler, ModelSamplingSD3, CheckpointLoaderSimple, INTConstant, ImageResizeKJv2, GetImageSizeAndCount, WanVideoVACEStartToEndFrame, INTConstant, LoadImage, ImageResizeKJv2, LoadImage, VHS_VideoCombine, WanVaceToVideo, CLIPTextEncode, CLIPTextEncode]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "checkpoint": "wan2.2-rapid-mega-aio-v1.safetensors", "denoise": 1, "sampler_name": "euler", "scheduler": "beta", "seed": 192054346835137, "steps": 6}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/文生视频/MEGA Merge-WAN2.2-AllInOne-首尾帧_1968252973186994178.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/MEGA Merge-WAN2.2-AllInOne-首尾帧_1968252973186994178.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（17 个）：
- `TrimVideoLatent`
- `VAEDecode` ★核心
- `KSampler` ★核心
- `ModelSamplingSD3`
- `CheckpointLoaderSimple` ★核心
- `INTConstant`
- `ImageResizeKJv2`
- `GetImageSizeAndCount`
- `WanVideoVACEStartToEndFrame`
- `INTConstant`
- `LoadImage`
- `ImageResizeKJv2`
- `LoadImage`
- `VHS_VideoCombine`
- `WanVaceToVideo`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心

## 关键参数

- `seed` = `192054346835137`
- `steps` = `6`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `beta`
- `denoise` = `1`
- `checkpoint` = `wan2.2-rapid-mega-aio-v1.safetensors`

## 知识

覆盖率 **100%**（17/17）

**有卡**：`TrimVideoLatent`、`VAEDecode`、`KSampler`、`ModelSamplingSD3`、`CheckpointLoaderSimple`、`INTConstant`、`ImageResizeKJv2`、`GetImageSizeAndCount`、`WanVideoVACEStartToEndFrame`、`LoadImage`、`VHS_VideoCombine`、`WanVaceToVideo`、`CLIPTextEncode`

**用到的条目**：KSampler、VAEDecode、CheckpointLoaderSimple、CLIPTextEncode、LoadImage、TrimVideoLatent、GetImageSizeAndCount、ImageResizeKJv2

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

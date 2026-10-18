---
key: 视频生成/图生视频/首尾帧视频-MEGA_V3-WAN2.2-AllInOne_1969995701813977090.json
name: 首尾帧视频-MEGA_V3-WAN2.2-AllInOne_1969995701813977090.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/首尾帧视频-MEGA_V3-WAN2.2-AllInOne_1969995701813977090.json
hash: 0727d1cd3a285566
coverage: 0.947368
learned_at: 2026-10-15 22:31:51
nodes: [KSampler, GetImageSizeAndCount, WanVideoVACEStartToEndFrame, CLIPTextEncode, WanVaceToVideo, TrimVideoLatent, VAEDecode, ModelSamplingSD3, INTConstant, INTConstant, INTConstant, ImageResizeKJv2, ImageResizeKJv2, LoadImage, LoadImage, CLIPTextEncode, VHS_VideoCombine, CheckpointLoaderSimple, PrimitiveStringMultiline]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "checkpoint": "wan2.2-rapid-mega-aio-v3.safetensors", "denoise": 1, "sampler_name": "euler", "scheduler": "beta", "seed": 192054346835137, "steps": 6}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/图生视频/首尾帧视频-MEGA_V3-WAN2.2-AllInOne_1969995701813977090.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1969995701813977090.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（19 个）：
- `KSampler` ★核心
- `GetImageSizeAndCount`
- `WanVideoVACEStartToEndFrame`
- `CLIPTextEncode` ★核心
- `WanVaceToVideo`
- `TrimVideoLatent`
- `VAEDecode` ★核心
- `ModelSamplingSD3`
- `INTConstant`
- `INTConstant`
- `INTConstant`
- `ImageResizeKJv2`
- `ImageResizeKJv2`
- `LoadImage`
- `LoadImage`
- `CLIPTextEncode` ★核心
- `VHS_VideoCombine`
- `CheckpointLoaderSimple` ★核心
- `PrimitiveStringMultiline`

## 关键参数

- `seed` = `192054346835137`
- `steps` = `6`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `beta`
- `denoise` = `1`
- `checkpoint` = `wan2.2-rapid-mega-aio-v3.safetensors`

## 知识

覆盖率 **95%**（18/19）

**有卡**：`KSampler`、`GetImageSizeAndCount`、`WanVideoVACEStartToEndFrame`、`CLIPTextEncode`、`WanVaceToVideo`、`TrimVideoLatent`、`VAEDecode`、`ModelSamplingSD3`、`INTConstant`、`ImageResizeKJv2`、`LoadImage`、`VHS_VideoCombine`、`CheckpointLoaderSimple`

**用到的条目**：KSampler、VAEDecode、CheckpointLoaderSimple、CLIPTextEncode、LoadImage、TrimVideoLatent、GetImageSizeAndCount、ImageResizeKJv2

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

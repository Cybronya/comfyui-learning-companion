---
key: 视频生成/文生视频/MEGA Merge-WAN2.2-AllInOne-双图参考_2072999566997495808.json
name: MEGA Merge-WAN2.2-AllInOne-双图参考_2072999566997495808
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/MEGA Merge-WAN2.2-AllInOne-双图参考_2072999566997495808.json
hash: e3348a7b4671d4d3
coverage: 1
learned_at: 2026-10-15 22:45:22
nodes: [TrimVideoLatent, VAEDecode, KSampler, ModelSamplingSD3, CheckpointLoaderSimple, VHS_VideoCombine, CLIPTextEncode, INTConstant, WanVaceToVideo, CLIPTextEncode, ImageConcanate, INTConstant, INTConstant, Image Rembg (Remove Background), Image Rembg (Remove Background), TTP_Expand_And_Mask, TTP_Expand_And_Mask, LoadImage, LoadImage]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "checkpoint": "wan2.2-rapid-mega-aio-v1.safetensors", "denoise": 1, "sampler_name": "euler", "scheduler": "beta", "seed": 192054346835137, "steps": 6}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/文生视频/MEGA Merge-WAN2.2-AllInOne-双图参考_2072999566997495808.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/MEGA Merge-WAN2.2-AllInOne-双图参考_2072999566997495808.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（19 个）：
- `TrimVideoLatent`
- `VAEDecode` ★核心
- `KSampler` ★核心
- `ModelSamplingSD3`
- `CheckpointLoaderSimple` ★核心
- `VHS_VideoCombine`
- `CLIPTextEncode` ★核心
- `INTConstant`
- `WanVaceToVideo`
- `CLIPTextEncode` ★核心
- `ImageConcanate`
- `INTConstant`
- `INTConstant`
- `Image Rembg (Remove Background)`
- `Image Rembg (Remove Background)`
- `TTP_Expand_And_Mask`
- `TTP_Expand_And_Mask`
- `LoadImage`
- `LoadImage`

## 关键参数

- `seed` = `192054346835137`
- `steps` = `6`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `beta`
- `denoise` = `1`
- `checkpoint` = `wan2.2-rapid-mega-aio-v1.safetensors`

## 知识

覆盖率 **100%**（19/19）

**有卡**：`TrimVideoLatent`、`VAEDecode`、`KSampler`、`ModelSamplingSD3`、`CheckpointLoaderSimple`、`VHS_VideoCombine`、`CLIPTextEncode`、`INTConstant`、`WanVaceToVideo`、`ImageConcanate`、`Image Rembg (Remove Background)`、`TTP_Expand_And_Mask`、`LoadImage`

**用到的条目**：KSampler、VAEDecode、CheckpointLoaderSimple、CLIPTextEncode、LoadImage、TrimVideoLatent、ImageConcanate、INTConstant

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

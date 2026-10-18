---
key: 视频生成/图生视频/Wan2.2 Rapid-AIO-Mega V6图生视频极速版_1975830949797695489.json
name: Wan2.2 Rapid-AIO-Mega V6图生视频极速版_1975830949797695489.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/Wan2.2 Rapid-AIO-Mega V6图生视频极速版_1975830949797695489.json
hash: 8887f844870eaba4
coverage: 0.833333
learned_at: 2026-10-15 22:32:09
nodes: [ModelSamplingSD3, CLIPTextEncode, WanVaceToVideo, Note, WanVideoVACEStartToEndFrame, ApplySageAttention, Note, Note, CLIPTextEncode, LoadImage, CR Prompt Text, JWInteger, LayerUtility: ImageScaleByAspectRatio V2, JWInteger, VAEDecode, VHS_VideoCombine, CheckpointLoaderSimple, KSampler]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "checkpoint": "wan2.2-rapid-mega-aio-v6.safetensors", "denoise": 1, "sampler_name": "sa_solver", "scheduler": "beta", "seed": 343116326427420, "steps": 4}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/图生视频/Wan2.2 Rapid-AIO-Mega V6图生视频极速版_1975830949797695489.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1975830949797695489.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（18 个）：
- `ModelSamplingSD3`
- `CLIPTextEncode` ★核心
- `WanVaceToVideo`
- `Note`
- `WanVideoVACEStartToEndFrame`
- `ApplySageAttention`
- `Note`
- `Note`
- `CLIPTextEncode` ★核心
- `LoadImage`
- `CR Prompt Text`
- `JWInteger`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `JWInteger`
- `VAEDecode` ★核心
- `VHS_VideoCombine`
- `CheckpointLoaderSimple` ★核心
- `KSampler` ★核心

## 关键参数

- `checkpoint` = `wan2.2-rapid-mega-aio-v6.safetensors`
- `seed` = `343116326427420`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `sa_solver`
- `scheduler` = `beta`
- `denoise` = `1`

## 知识

覆盖率 **83%**（15/18）

**有卡**：`ModelSamplingSD3`、`CLIPTextEncode`、`WanVaceToVideo`、`WanVideoVACEStartToEndFrame`、`ApplySageAttention`、`LoadImage`、`CR Prompt Text`、`JWInteger`、`LayerUtility: ImageScaleByAspectRatio V2`、`VAEDecode`、`VHS_VideoCombine`、`CheckpointLoaderSimple`、`KSampler`

**用到的条目**：KSampler、VAEDecode、CheckpointLoaderSimple、CLIPTextEncode、LoadImage、CR Prompt Text、ModelSamplingSD3、VHS_VideoCombine

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

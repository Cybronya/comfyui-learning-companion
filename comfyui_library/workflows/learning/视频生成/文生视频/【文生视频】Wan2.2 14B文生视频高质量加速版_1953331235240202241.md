---
key: 视频生成/文生视频/【文生视频】Wan2.2 14B文生视频高质量加速版_1953331235240202241.json
name: 【文生视频】Wan2.2 14B文生视频高质量加速版_1953331235240202241.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/1953331235240202241.json
hash: 41442636fbbb2bc3
coverage: 0.923077
learned_at: 2026-10-15 22:43:38
nodes: [CLIPTextEncode, KSampler, VAEDecode, VAELoader, VAELoader, VAEDecode, UNETLoader, CLIPTextEncode, ModelSamplingSD3, CLIPLoader, WanImageToVideo, EmptyHunyuanLatentVideo, CLIPLoader, LoraLoader, LoraLoader, UNETLoader, LoadImage, CLIPTextEncode, Fast Groups Bypasser (rgthree), CLIPTextEncode, KSampler, LoraLoader, VHS_VideoCombine, ModelSamplingSD3, VHS_VideoCombine, Fast Groups Bypasser (rgthree)]
patterns: [lora]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "lora_name": "t2v韩国女SeoullinaComplete.AkCZ.safetensors", "sampler_name": "sa_solver", "scheduler": "beta", "seed": 0, "steps": 4, "strength_clip": 1, "strength_model": 1}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/文生视频/【文生视频】Wan2.2 14B文生视频高质量加速版_1953331235240202241.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/1953331235240202241.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Other

**节点**（26 个）：
- `CLIPTextEncode` ★核心
- `KSampler` ★核心
- `VAEDecode` ★核心
- `VAELoader`
- `VAELoader`
- `VAEDecode` ★核心
- `UNETLoader` ★核心
- `CLIPTextEncode` ★核心
- `ModelSamplingSD3`
- `CLIPLoader`
- `WanImageToVideo`
- `EmptyHunyuanLatentVideo`
- `CLIPLoader`
- `LoraLoader` ★核心
- `LoraLoader` ★核心
- `UNETLoader` ★核心
- `LoadImage`
- `CLIPTextEncode` ★核心
- `Fast Groups Bypasser (rgthree)`
- `CLIPTextEncode` ★核心
- `KSampler` ★核心
- `LoraLoader` ★核心
- `VHS_VideoCombine`
- `ModelSamplingSD3`
- `VHS_VideoCombine`
- `Fast Groups Bypasser (rgthree)`

**识别到的模式**：lora

## 关键参数

- `seed` = `0`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `sa_solver`
- `scheduler` = `beta`
- `denoise` = `1`
- `lora_name` = `t2v韩国女SeoullinaComplete.AkCZ.safetensors`
- `strength_model` = `1`
- `strength_clip` = `1`

## 知识

覆盖率 **92%**（24/26）

**有卡**：`CLIPTextEncode`、`KSampler`、`VAEDecode`、`VAELoader`、`UNETLoader`、`ModelSamplingSD3`、`CLIPLoader`、`WanImageToVideo`、`EmptyHunyuanLatentVideo`、`LoraLoader`、`LoadImage`、`VHS_VideoCombine`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、EmptyHunyuanLatentVideo

## 参数体检

发现 2 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

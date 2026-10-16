---
key: 视频生成/图生视频/ai有娃了-Wan2.1原始节点（非KJ节点）-FusionX加速_1937704868792418306.json
name: ai有娃了-Wan2.1原始节点（非KJ节点）-FusionX加速_1937704868792418306.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1937704868792418306.json
hash: f1bae626ceb633c8
coverage: 1
learned_at: 2026-10-15 22:30:29
nodes: [KSampler, TrimVideoLatent, easy cleanGpuUsed, ImageResizeKJv2, WanVaceToVideo, ModelSamplingSD3, CLIPTextEncode, CLIPTextEncode, StringFunction|pysssss, LoraLoader, LoraLoader, LoadImage, CLIPLoader, VAEDecode, VAELoader, VHS_VideoCombine, UnetLoaderGGUF]
patterns: [lora]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "lora_name": "Wan21_AccVid_I2V_480P_14B_lora_rank32_fp16.safetensors", "sampler_name": "uni_pc", "scheduler": "simple", "seed": 712231674651547, "steps": 8, "strength_clip": 1, "strength_model": 1}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/图生视频/ai有娃了-Wan2.1原始节点（非KJ节点）-FusionX加速_1937704868792418306.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1937704868792418306.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（17 个）：
- `KSampler` ★核心
- `TrimVideoLatent`
- `easy cleanGpuUsed`
- `ImageResizeKJv2`
- `WanVaceToVideo`
- `ModelSamplingSD3`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `StringFunction|pysssss`
- `LoraLoader` ★核心
- `LoraLoader` ★核心
- `LoadImage`
- `CLIPLoader`
- `VAEDecode` ★核心
- `VAELoader`
- `VHS_VideoCombine`
- `UnetLoaderGGUF` ★核心

**识别到的模式**：lora

## 关键参数

- `seed` = `712231674651547`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `uni_pc`
- `scheduler` = `simple`
- `denoise` = `1`
- `lora_name` = `Wan21_AccVid_I2V_480P_14B_lora_rank32_fp16.safetensors`
- `strength_model` = `1`
- `strength_clip` = `1`

## 知识

覆盖率 **100%**（17/17）

**有卡**：`KSampler`、`TrimVideoLatent`、`easy cleanGpuUsed`、`ImageResizeKJv2`、`WanVaceToVideo`、`ModelSamplingSD3`、`CLIPTextEncode`、`StringFunction|pysssss`、`LoraLoader`、`LoadImage`、`CLIPLoader`、`VAEDecode`、`VAELoader`、`VHS_VideoCombine`、`UnetLoaderGGUF`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、LoadImage、TrimVideoLatent、LoraLoader

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

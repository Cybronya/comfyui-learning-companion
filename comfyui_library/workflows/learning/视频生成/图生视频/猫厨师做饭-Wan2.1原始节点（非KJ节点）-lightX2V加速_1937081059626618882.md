---
key: 视频生成/图生视频/猫厨师做饭-Wan2.1原始节点（非KJ节点）-lightX2V加速_1937081059626618882.json
name: 猫厨师做饭-Wan2.1原始节点（非KJ节点）-lightX2V加速_1937081059626618882.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1937081059626618882.json
hash: b216bc6afd1bb24f
coverage: 1
learned_at: 2026-10-15 22:30:28
nodes: [TrimVideoLatent, easy cleanGpuUsed, WanVaceToVideo, ImageResizeKJv2, CLIPTextEncode, CLIPTextEncode, KSampler, ModelSamplingSD3, Text Multiline, CLIPLoader, AV_LoraLoader, LoadImage, VAELoader, VAEDecode, VHS_VideoCombine, UnetLoaderGGUF]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "lora_name": "Wan21_T2V_14B_lightx2v_cfg_step_distill_lora_rank32.safetensors", "sampler_name": "lcm", "scheduler": "simple", "seed": 548547462515155, "steps": 5, "strength_clip": 1, "strength_model": 1}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/图生视频/猫厨师做饭-Wan2.1原始节点（非KJ节点）-lightX2V加速_1937081059626618882.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1937081059626618882.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（16 个）：
- `TrimVideoLatent`
- `easy cleanGpuUsed`
- `WanVaceToVideo`
- `ImageResizeKJv2`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `KSampler` ★核心
- `ModelSamplingSD3`
- `Text Multiline`
- `CLIPLoader`
- `AV_LoraLoader` ★核心
- `LoadImage`
- `VAELoader`
- `VAEDecode` ★核心
- `VHS_VideoCombine`
- `UnetLoaderGGUF` ★核心

## 关键参数

- `seed` = `548547462515155`
- `steps` = `5`
- `cfg` = `1`
- `sampler_name` = `lcm`
- `scheduler` = `simple`
- `denoise` = `1`
- `lora_name` = `Wan21_T2V_14B_lightx2v_cfg_step_distill_lora_rank32.safetensors`
- `strength_model` = `1`
- `strength_clip` = `1`

## 知识

覆盖率 **100%**（16/16）

**有卡**：`TrimVideoLatent`、`easy cleanGpuUsed`、`WanVaceToVideo`、`ImageResizeKJv2`、`CLIPTextEncode`、`KSampler`、`ModelSamplingSD3`、`Text Multiline`、`CLIPLoader`、`AV_LoraLoader`、`LoadImage`、`VAELoader`、`VAEDecode`、`VHS_VideoCombine`、`UnetLoaderGGUF`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、LoadImage、TrimVideoLatent、AV_LoraLoader

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

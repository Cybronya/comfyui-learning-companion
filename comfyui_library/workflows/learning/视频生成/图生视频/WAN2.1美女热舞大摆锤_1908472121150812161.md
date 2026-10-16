---
key: 视频生成/图生视频/WAN2.1美女热舞大摆锤_1908472121150812161.json
name: WAN2.1美女热舞大摆锤_1908472121150812161.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1908472121150812161.json
hash: a7ed70ebfed1fc0a
coverage: 1
learned_at: 2026-10-15 22:29:28
nodes: [VHS_VideoCombine, CLIPTextEncode, CLIPVisionEncode, CLIPVisionLoader, UNETLoader, KSampler, VAEDecodeTiled, VAELoader, CLIPTextEncode, LoadImage, CLIPLoader, LoraLoader, WanImageToVideo, TeaCache]
patterns: [lora]
missing: []
problems: [[high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换]
parameters: {"cfg": 6, "denoise": 1, "lora_name": "dbc.safetensors", "sampler_name": "uni_pc", "scheduler": "simple", "seed": 1096302494255295, "steps": 20, "strength_clip": 1, "strength_model": 1}
discoveries: [[high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换]
---

# 视频生成/图生视频/WAN2.1美女热舞大摆锤_1908472121150812161.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1908472121150812161.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Other

**节点**（14 个）：
- `VHS_VideoCombine`
- `CLIPTextEncode` ★核心
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `UNETLoader` ★核心
- `KSampler` ★核心
- `VAEDecodeTiled` ★核心
- `VAELoader`
- `CLIPTextEncode` ★核心
- `LoadImage`
- `CLIPLoader`
- `LoraLoader` ★核心
- `WanImageToVideo`
- `TeaCache`

**识别到的模式**：lora

## 关键参数

- `seed` = `1096302494255295`
- `steps` = `20`
- `cfg` = `6`
- `sampler_name` = `uni_pc`
- `scheduler` = `simple`
- `denoise` = `1`
- `lora_name` = `dbc.safetensors`
- `strength_model` = `1`
- `strength_clip` = `1`

## 知识

覆盖率 **100%**（14/14）

**有卡**：`VHS_VideoCombine`、`CLIPTextEncode`、`CLIPVisionEncode`、`CLIPVisionLoader`、`UNETLoader`、`KSampler`、`VAEDecodeTiled`、`VAELoader`、`LoadImage`、`CLIPLoader`、`LoraLoader`、`WanImageToVideo`、`TeaCache`

**用到的条目**：KSampler、VAELoader、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、VAEDecodeTiled、CLIPVisionEncode

## 参数体检

发现 1 个问题：
- [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换

## 学习发现

- [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换

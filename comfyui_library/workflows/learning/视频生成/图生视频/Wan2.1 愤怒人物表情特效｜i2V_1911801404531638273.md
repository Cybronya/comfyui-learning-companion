---
key: 视频生成/图生视频/Wan2.1 愤怒人物表情特效｜i2V_1911801404531638273.json
name: Wan2.1 愤怒人物表情特效｜i2V_1911801404531638273.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1911801404531638273.json
hash: fd80b068d0bdc623
coverage: 1
learned_at: 2026-10-15 22:29:31
nodes: [CLIPTextEncode, KSampler, VAELoader, VAEDecodeTiled, CLIPVisionEncode, WanImageToVideo, TeaCache, CLIPVisionLoader, CLIPLoader, ImageResizeKJ, UnetLoaderGGUF, CLIPTextEncode, Joy_caption, Joy_caption_load, VHS_VideoCombine, LoadImage, ConcatTextOfUtils, LoraLoader]
patterns: [lora]
missing: []
problems: [[high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换]
parameters: {"cfg": 6, "denoise": 1, "lora_name": "angry+adapter_model.safetensors", "sampler_name": "uni_pc", "scheduler": "simple", "seed": 304891622707005, "steps": 20, "strength_clip": 1, "strength_model": 1}
discoveries: [[high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换]
---

# 视频生成/图生视频/Wan2.1 愤怒人物表情特效｜i2V_1911801404531638273.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1911801404531638273.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（18 个）：
- `CLIPTextEncode` ★核心
- `KSampler` ★核心
- `VAELoader`
- `VAEDecodeTiled` ★核心
- `CLIPVisionEncode`
- `WanImageToVideo`
- `TeaCache`
- `CLIPVisionLoader`
- `CLIPLoader`
- `ImageResizeKJ`
- `UnetLoaderGGUF` ★核心
- `CLIPTextEncode` ★核心
- `Joy_caption`
- `Joy_caption_load`
- `VHS_VideoCombine`
- `LoadImage`
- `ConcatTextOfUtils`
- `LoraLoader` ★核心

**识别到的模式**：lora

## 关键参数

- `seed` = `304891622707005`
- `steps` = `20`
- `cfg` = `6`
- `sampler_name` = `uni_pc`
- `scheduler` = `simple`
- `denoise` = `1`
- `lora_name` = `angry+adapter_model.safetensors`
- `strength_model` = `1`
- `strength_clip` = `1`

## 知识

覆盖率 **100%**（18/18）

**有卡**：`CLIPTextEncode`、`KSampler`、`VAELoader`、`VAEDecodeTiled`、`CLIPVisionEncode`、`WanImageToVideo`、`TeaCache`、`CLIPVisionLoader`、`CLIPLoader`、`ImageResizeKJ`、`UnetLoaderGGUF`、`Joy_caption`、`Joy_caption_load`、`VHS_VideoCombine`、`LoadImage`、`ConcatTextOfUtils`、`LoraLoader`

**用到的条目**：KSampler、VAELoader、CLIPTextEncode、CLIPLoader、LoadImage、VAEDecodeTiled、CLIPVisionEncode、LoraLoader

## 参数体检

发现 1 个问题：
- [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换

## 学习发现

- [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换

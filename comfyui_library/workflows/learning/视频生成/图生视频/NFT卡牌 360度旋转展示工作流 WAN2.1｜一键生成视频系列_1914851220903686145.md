---
key: 视频生成/图生视频/NFT卡牌 360度旋转展示工作流 WAN2.1｜一键生成视频系列_1914851220903686145.json
name: NFT卡牌 360度旋转展示工作流 WAN2.1｜一键生成视频系列_1914851220903686145.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1914851220903686145.json
hash: 1b37802cd15dfde8
coverage: 1
learned_at: 2026-10-15 22:29:37
nodes: [CLIPTextEncode, KSampler, VAELoader, VAEDecodeTiled, CLIPVisionEncode, WanImageToVideo, TeaCache, CLIPVisionLoader, CLIPLoader, LoraLoader, UnetLoaderGGUF, CLIPTextEncode, Joy_caption, Joy_caption_load, LoadImage, ImageResizeKJ, ConcatTextOfUtils, VHS_VideoCombine]
patterns: [lora]
missing: []
problems: [[high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换]
parameters: {"cfg": 6, "denoise": 1, "lora_name": "360_epoch20.safetensors", "sampler_name": "uni_pc", "scheduler": "simple", "seed": 646746185982057, "steps": 20, "strength_clip": 1, "strength_model": 1}
discoveries: [[high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换]
---

# 视频生成/图生视频/NFT卡牌 360度旋转展示工作流 WAN2.1｜一键生成视频系列_1914851220903686145.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1914851220903686145.json`

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
- `LoraLoader` ★核心
- `UnetLoaderGGUF` ★核心
- `CLIPTextEncode` ★核心
- `Joy_caption`
- `Joy_caption_load`
- `LoadImage`
- `ImageResizeKJ`
- `ConcatTextOfUtils`
- `VHS_VideoCombine`

**识别到的模式**：lora

## 关键参数

- `seed` = `646746185982057`
- `steps` = `20`
- `cfg` = `6`
- `sampler_name` = `uni_pc`
- `scheduler` = `simple`
- `denoise` = `1`
- `lora_name` = `360_epoch20.safetensors`
- `strength_model` = `1`
- `strength_clip` = `1`

## 知识

覆盖率 **100%**（18/18）

**有卡**：`CLIPTextEncode`、`KSampler`、`VAELoader`、`VAEDecodeTiled`、`CLIPVisionEncode`、`WanImageToVideo`、`TeaCache`、`CLIPVisionLoader`、`CLIPLoader`、`LoraLoader`、`UnetLoaderGGUF`、`Joy_caption`、`Joy_caption_load`、`LoadImage`、`ImageResizeKJ`、`ConcatTextOfUtils`、`VHS_VideoCombine`

**用到的条目**：KSampler、VAELoader、CLIPTextEncode、CLIPLoader、LoadImage、VAEDecodeTiled、CLIPVisionEncode、LoraLoader

## 参数体检

发现 1 个问题：
- [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换

## 学习发现

- [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换

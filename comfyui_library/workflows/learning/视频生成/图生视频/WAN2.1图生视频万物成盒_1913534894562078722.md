---
key: 视频生成/图生视频/WAN2.1图生视频万物成盒_1913534894562078722.json
name: WAN2.1图生视频万物成盒_1913534894562078722.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1913534894562078722.json
hash: 85fc24dc3f7df0d4
coverage: 1
learned_at: 2026-10-15 22:29:34
nodes: [VHS_VideoCombine, CLIPTextEncode, CLIPVisionEncode, CLIPVisionLoader, UNETLoader, TeaCache, KSampler, VAELoader, VAEDecodeTiled, CLIPLoader, LoraLoader, LoadImage, WanImageToVideo, CLIPTextEncode]
patterns: [lora]
missing: []
problems: [[high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换]
parameters: {"cfg": 6, "denoise": 1, "lora_name": "万物成盒.safetensors", "sampler_name": "uni_pc", "scheduler": "simple", "seed": 808759423656025, "steps": 20, "strength_clip": 1, "strength_model": 1}
discoveries: [[high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换]
---

# 视频生成/图生视频/WAN2.1图生视频万物成盒_1913534894562078722.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1913534894562078722.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Other

**节点**（14 个）：
- `VHS_VideoCombine`
- `CLIPTextEncode` ★核心
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `UNETLoader` ★核心
- `TeaCache`
- `KSampler` ★核心
- `VAELoader`
- `VAEDecodeTiled` ★核心
- `CLIPLoader`
- `LoraLoader` ★核心
- `LoadImage`
- `WanImageToVideo`
- `CLIPTextEncode` ★核心

**识别到的模式**：lora

## 关键参数

- `seed` = `808759423656025`
- `steps` = `20`
- `cfg` = `6`
- `sampler_name` = `uni_pc`
- `scheduler` = `simple`
- `denoise` = `1`
- `lora_name` = `万物成盒.safetensors`
- `strength_model` = `1`
- `strength_clip` = `1`

## 知识

覆盖率 **100%**（14/14）

**有卡**：`VHS_VideoCombine`、`CLIPTextEncode`、`CLIPVisionEncode`、`CLIPVisionLoader`、`UNETLoader`、`TeaCache`、`KSampler`、`VAELoader`、`VAEDecodeTiled`、`CLIPLoader`、`LoraLoader`、`LoadImage`、`WanImageToVideo`

**用到的条目**：KSampler、VAELoader、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、VAEDecodeTiled、CLIPVisionEncode

## 参数体检

发现 1 个问题：
- [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换

## 学习发现

- [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换

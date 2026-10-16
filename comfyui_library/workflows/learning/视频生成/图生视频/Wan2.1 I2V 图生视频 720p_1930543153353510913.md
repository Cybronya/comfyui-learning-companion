---
key: 视频生成/图生视频/Wan2.1 I2V 图生视频 720p_1930543153353510913.json
name: Wan2.1 I2V 图生视频 720p_1930543153353510913.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1930543153353510913.json
hash: 5c73b2b1a18ea505
coverage: 1
learned_at: 2026-10-15 22:30:07
nodes: [CLIPLoader, UNETLoader, CLIPTextEncode, CLIPTextEncode, CLIPVisionEncode, KSampler, VAELoader, WanImageToVideo, VAEDecode, VHS_VideoCombine, LoadImage, CLIPVisionLoader]
patterns: []
missing: []
parameters: {"cfg": 6, "denoise": 1, "sampler_name": "uni_pc", "scheduler": "simple", "seed": 811882019142269, "steps": 20}
---

# 视频生成/图生视频/Wan2.1 I2V 图生视频 720p_1930543153353510913.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1930543153353510913.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Other

**节点**（12 个）：
- `CLIPLoader`
- `UNETLoader` ★核心
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `CLIPVisionEncode`
- `KSampler` ★核心
- `VAELoader`
- `WanImageToVideo`
- `VAEDecode` ★核心
- `VHS_VideoCombine`
- `LoadImage`
- `CLIPVisionLoader`

## 关键参数

- `seed` = `811882019142269`
- `steps` = `20`
- `cfg` = `6`
- `sampler_name` = `uni_pc`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **100%**（12/12）

**有卡**：`CLIPLoader`、`UNETLoader`、`CLIPTextEncode`、`CLIPVisionEncode`、`KSampler`、`VAELoader`、`WanImageToVideo`、`VAEDecode`、`VHS_VideoCombine`、`LoadImage`、`CLIPVisionLoader`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、CLIPVisionEncode

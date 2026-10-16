---
key: 视频生成/图生视频/Wan2.1图生视频_2008112193308467202.json
name: Wan2.1图生视频_2008112193308467202.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2008112193308467202.json
hash: a600204eecb044f0
coverage: 1
learned_at: 2026-10-15 22:34:06
nodes: [CLIPLoader, UNETLoader, VAELoader, CLIPVisionLoader, VAEDecode, VHS_VideoCombine, KSampler, CLIPTextEncode, CLIPVisionEncode, LoadImage, ImageResizeKJ, WanImageToVideo, CLIPTextEncode]
patterns: []
missing: []
parameters: {"cfg": 8, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 882182939405724, "steps": 20}
---

# 视频生成/图生视频/Wan2.1图生视频_2008112193308467202.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2008112193308467202.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（13 个）：
- `CLIPLoader`
- `UNETLoader` ★核心
- `VAELoader`
- `CLIPVisionLoader`
- `VAEDecode` ★核心
- `VHS_VideoCombine`
- `KSampler` ★核心
- `CLIPTextEncode` ★核心
- `CLIPVisionEncode`
- `LoadImage`
- `ImageResizeKJ`
- `WanImageToVideo`
- `CLIPTextEncode` ★核心

## 关键参数

- `seed` = `882182939405724`
- `steps` = `20`
- `cfg` = `8`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **100%**（13/13）

**有卡**：`CLIPLoader`、`UNETLoader`、`VAELoader`、`CLIPVisionLoader`、`VAEDecode`、`VHS_VideoCombine`、`KSampler`、`CLIPTextEncode`、`CLIPVisionEncode`、`LoadImage`、`ImageResizeKJ`、`WanImageToVideo`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、CLIPVisionEncode

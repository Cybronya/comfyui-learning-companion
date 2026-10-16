---
key: 视频生成/图生视频/Wan2.1(阿里万相)-图生视频_1904428749629358081.json
name: Wan2.1(阿里万相)-图生视频_1904428749629358081.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1904428749629358081.json
hash: 7912c023c8b85864
coverage: 1
learned_at: 2026-10-15 22:29:25
nodes: [WanImageToVideo, CLIPLoader, UNETLoader, VAELoader, CLIPVisionLoader, VAEDecode, VHS_VideoCombine, KSampler, CLIPTextEncode, ImageResizeKJ, CLIPTextEncode, LoadImage, CLIPVisionEncode]
patterns: []
missing: []
parameters: {"cfg": 8, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 752090980747703, "steps": 20}
---

# 视频生成/图生视频/Wan2.1(阿里万相)-图生视频_1904428749629358081.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1904428749629358081.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（13 个）：
- `WanImageToVideo`
- `CLIPLoader`
- `UNETLoader` ★核心
- `VAELoader`
- `CLIPVisionLoader`
- `VAEDecode` ★核心
- `VHS_VideoCombine`
- `KSampler` ★核心
- `CLIPTextEncode` ★核心
- `ImageResizeKJ`
- `CLIPTextEncode` ★核心
- `LoadImage`
- `CLIPVisionEncode`

## 关键参数

- `seed` = `752090980747703`
- `steps` = `20`
- `cfg` = `8`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **100%**（13/13）

**有卡**：`WanImageToVideo`、`CLIPLoader`、`UNETLoader`、`VAELoader`、`CLIPVisionLoader`、`VAEDecode`、`VHS_VideoCombine`、`KSampler`、`CLIPTextEncode`、`ImageResizeKJ`、`LoadImage`、`CLIPVisionEncode`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、CLIPVisionEncode

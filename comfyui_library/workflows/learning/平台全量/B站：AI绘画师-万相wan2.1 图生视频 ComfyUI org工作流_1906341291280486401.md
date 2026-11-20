---
key: 平台全量/B站：AI绘画师-万相wan2.1 图生视频 ComfyUI org工作流_1906341291280486401.json
name: B站：AI绘画师-万相wan2.1 图生视频 ComfyUI org工作流_1906341291280486401
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/B站：AI绘画师-万相wan2.1 图生视频 ComfyUI org工作流_1906341291280486401.json
hash: 53f95d0139f8b902
coverage: 0.823529
learned_at: 2026-11-14 00:21:29
nodes: [WanImageToVideo, VAELoader, KSampler, VAEDecode, CLIPTextEncode, CLIPTextEncode, UNETLoader, Note, CLIPLoader, VHS_VideoCombine, CLIPVisionEncode, CLIPVisionLoader, LoadImage, Note, Int, Note, ImageResizeKJ]
patterns: []
missing: []
parameters: {"cfg": 6, "denoise": 1, "sampler_name": "uni_pc", "scheduler": "simple", "seed": 396884691029010, "steps": 20}
---

# 平台全量/B站：AI绘画师-万相wan2.1 图生视频 ComfyUI org工作流_1906341291280486401.json

> 来源文件 `comfyui_library/workflows/平台全量/B站：AI绘画师-万相wan2.1 图生视频 ComfyUI org工作流_1906341291280486401.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（17 个）：
- `WanImageToVideo`
- `VAELoader`
- `KSampler` ★核心
- `VAEDecode` ★核心
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `UNETLoader` ★核心
- `Note`
- `CLIPLoader`
- `VHS_VideoCombine`
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `LoadImage`
- `Note`
- `Int`
- `Note`
- `ImageResizeKJ`

## 关键参数

- `seed` = `396884691029010`
- `steps` = `20`
- `cfg` = `6`
- `sampler_name` = `uni_pc`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **82%**（14/17）

**有卡**：`WanImageToVideo`、`VAELoader`、`KSampler`、`VAEDecode`、`CLIPTextEncode`、`UNETLoader`、`CLIPLoader`、`VHS_VideoCombine`、`CLIPVisionEncode`、`CLIPVisionLoader`、`LoadImage`、`Int`、`ImageResizeKJ`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPLoader、CLIPTextEncode、LoadImage、UNETLoader、CLIPVisionEncode

---
key: 视频生成/图生视频/Wan2.1-fun-Inp首尾帧视频_1911728190891720705.json
name: Wan2.1-fun-Inp首尾帧视频_1911728190891720705.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/Wan2.1-fun-Inp首尾帧视频_1911728190891720705.json
hash: 0d8df3bd1cad0646
coverage: 0.809524
learned_at: 2026-10-15 22:29:31
nodes: [CLIPTextEncode, CLIPVisionEncode, VAEDecode, CLIPVisionLoader, VAELoader, KSampler, PrimitiveNode, PrimitiveNode, LoadImage, LoadImage, CLIPLoader, UNETLoader, ImageResizeKJ, PreviewImage, ImageResizeKJ, PreviewImage, CLIPTextEncode, WanVideoEnhanceAVideoKJ, WanVideoTeaCacheKJ, WanFunInpaintToVideo, VHS_VideoCombine]
patterns: []
missing: []
parameters: {"cfg": 6, "denoise": 1, "sampler_name": "uni_pc", "scheduler": "simple", "seed": 409464873807543, "steps": 20}
---

# 视频生成/图生视频/Wan2.1-fun-Inp首尾帧视频_1911728190891720705.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1911728190891720705.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（21 个）：
- `CLIPTextEncode` ★核心
- `CLIPVisionEncode`
- `VAEDecode` ★核心
- `CLIPVisionLoader`
- `VAELoader`
- `KSampler` ★核心
- `PrimitiveNode`
- `PrimitiveNode`
- `LoadImage`
- `LoadImage`
- `CLIPLoader`
- `UNETLoader` ★核心
- `ImageResizeKJ`
- `PreviewImage`
- `ImageResizeKJ`
- `PreviewImage`
- `CLIPTextEncode` ★核心
- `WanVideoEnhanceAVideoKJ`
- `WanVideoTeaCacheKJ`
- `WanFunInpaintToVideo`
- `VHS_VideoCombine`

## 关键参数

- `seed` = `409464873807543`
- `steps` = `20`
- `cfg` = `6`
- `sampler_name` = `uni_pc`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **81%**（17/21）

**有卡**：`CLIPTextEncode`、`CLIPVisionEncode`、`VAEDecode`、`CLIPVisionLoader`、`VAELoader`、`KSampler`、`LoadImage`、`CLIPLoader`、`UNETLoader`、`ImageResizeKJ`、`WanVideoEnhanceAVideoKJ`、`WanVideoTeaCacheKJ`、`WanFunInpaintToVideo`、`VHS_VideoCombine`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、CLIPVisionEncode

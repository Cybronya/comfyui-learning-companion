---
key: 视频生成/图生视频/Wan2.1 万相图生视频_1902233258837303298.json
name: Wan2.1 万相图生视频_1902233258837303298.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1902233258837303298.json
hash: 6b8d632c76aff7f7
coverage: 0.9375
learned_at: 2026-10-15 22:29:24
nodes: [WanVideoTeaCacheKJ, VAEDecode, KSampler, UNETLoader, WanImageToVideo, VAELoader, CLIPTextEncode, ImageResizeKJ, CLIPVisionEncode, CLIPVisionLoader, LoadImage, Note, Int, CLIPLoader, VHS_VideoCombine, CLIPTextEncode]
patterns: []
missing: []
parameters: {"cfg": 6, "denoise": 1, "sampler_name": "uni_pc", "scheduler": "simple", "seed": 422880222198220, "steps": 20}
---

# 视频生成/图生视频/Wan2.1 万相图生视频_1902233258837303298.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1902233258837303298.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（16 个）：
- `WanVideoTeaCacheKJ`
- `VAEDecode` ★核心
- `KSampler` ★核心
- `UNETLoader` ★核心
- `WanImageToVideo`
- `VAELoader`
- `CLIPTextEncode` ★核心
- `ImageResizeKJ`
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `LoadImage`
- `Note`
- `Int`
- `CLIPLoader`
- `VHS_VideoCombine`
- `CLIPTextEncode` ★核心

## 关键参数

- `seed` = `422880222198220`
- `steps` = `20`
- `cfg` = `6`
- `sampler_name` = `uni_pc`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **94%**（15/16）

**有卡**：`WanVideoTeaCacheKJ`、`VAEDecode`、`KSampler`、`UNETLoader`、`WanImageToVideo`、`VAELoader`、`CLIPTextEncode`、`ImageResizeKJ`、`CLIPVisionEncode`、`CLIPVisionLoader`、`LoadImage`、`Int`、`CLIPLoader`、`VHS_VideoCombine`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、CLIPVisionEncode

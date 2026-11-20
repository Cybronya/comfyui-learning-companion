---
key: 平台全量/【趣味】wan2.1官方图生视频工作流+teacache加速_1897940491827105794.json
name: 【趣味】wan2.1官方图生视频工作流+teacache加速_1897940491827105794
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/【趣味】wan2.1官方图生视频工作流+teacache加速_1897940491827105794.json
hash: b12305db791fcc0c
coverage: 1
learned_at: 2026-11-14 01:25:29
nodes: [KSampler, VAELoader, VAEDecode, CLIPTextEncode, WanImageToVideo, CLIPVisionEncode, SimpleMath+, CLIPVisionLoader, CLIPLoader, ModelSamplingSD3, CLIPTextEncode, ImageScaleDownToSize, ImageResizeKJ, Label (rgthree), Label (rgthree), Int, VHS_VideoCombine, UNETLoader, LoadImage, LoadImage, TeaCache]
patterns: []
missing: []
parameters: {"cfg": 6, "denoise": 1, "sampler_name": "uni_pc", "scheduler": "simple", "seed": 566587641229909, "steps": 20}
---

# 平台全量/【趣味】wan2.1官方图生视频工作流+teacache加速_1897940491827105794.json

> 来源文件 `comfyui_library/workflows/平台全量/【趣味】wan2.1官方图生视频工作流+teacache加速_1897940491827105794.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（21 个）：
- `KSampler` ★核心
- `VAELoader`
- `VAEDecode` ★核心
- `CLIPTextEncode` ★核心
- `WanImageToVideo`
- `CLIPVisionEncode`
- `SimpleMath+`
- `CLIPVisionLoader`
- `CLIPLoader`
- `ModelSamplingSD3`
- `CLIPTextEncode` ★核心
- `ImageScaleDownToSize`
- `ImageResizeKJ`
- `Label (rgthree)`
- `Label (rgthree)`
- `Int`
- `VHS_VideoCombine`
- `UNETLoader` ★核心
- `LoadImage`
- `LoadImage`
- `TeaCache`

## 关键参数

- `seed` = `566587641229909`
- `steps` = `20`
- `cfg` = `6`
- `sampler_name` = `uni_pc`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **100%**（21/21）

**有卡**：`KSampler`、`VAELoader`、`VAEDecode`、`CLIPTextEncode`、`WanImageToVideo`、`CLIPVisionEncode`、`SimpleMath+`、`CLIPVisionLoader`、`CLIPLoader`、`ModelSamplingSD3`、`ImageScaleDownToSize`、`ImageResizeKJ`、`Label (rgthree)`、`Int`、`VHS_VideoCombine`、`UNETLoader`、`LoadImage`、`TeaCache`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPLoader、CLIPTextEncode、LoadImage、UNETLoader、CLIPVisionEncode

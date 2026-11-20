---
key: 平台全量/电商视频换服装 wan2.2 bernini_2067092091255222273.json
name: 电商视频换服装 wan2.2 bernini_2067092091255222273
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/电商视频换服装 wan2.2 bernini_2067092091255222273.json
hash: 3f2e6a53a38d56f1
coverage: 0.958333
learned_at: 2026-11-14 02:25:22
nodes: [UNETLoader, LoraLoaderModelOnly, UNETLoader, LoraLoaderModelOnly, CLIPLoader, CLIPTextEncode, CLIPTextEncode, CFGZeroStar, VAELoader, KSamplerAdvanced, ModelSamplingSD3, PathchSageAttentionKJ, WanVideoNAG, ModelSamplingSD3, BerniniConditioning, KSamplerAdvanced, VAEDecode, easy imageRemBg, VHS_VideoCombine, VHS_LoadVideo, ImageResizeKJv2, LoadImage, JjkText, LoadImage]
patterns: []
missing: []
parameters: {"cfg": 6, "denoise": "simple", "sampler_name": 1, "scheduler": "lcm", "seed": "disable", "steps": "fixed"}
---

# 平台全量/电商视频换服装 wan2.2 bernini_2067092091255222273.json

> 来源文件 `comfyui_library/workflows/平台全量/电商视频换服装 wan2.2 bernini_2067092091255222273.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（24 个）：
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `CLIPLoader`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `CFGZeroStar`
- `VAELoader`
- `KSamplerAdvanced` ★核心
- `ModelSamplingSD3`
- `PathchSageAttentionKJ`
- `WanVideoNAG`
- `ModelSamplingSD3`
- `BerniniConditioning`
- `KSamplerAdvanced` ★核心
- `VAEDecode` ★核心
- `easy imageRemBg`
- `VHS_VideoCombine`
- `VHS_LoadVideo`
- `ImageResizeKJv2`
- `LoadImage`
- `JjkText`
- `LoadImage`

## 关键参数

- `seed` = `disable`
- `steps` = `fixed`
- `cfg` = `6`
- `sampler_name` = `1`
- `scheduler` = `lcm`
- `denoise` = `simple`

## 知识

覆盖率 **96%**（23/24）

**有卡**：`UNETLoader`、`LoraLoaderModelOnly`、`CLIPLoader`、`CLIPTextEncode`、`CFGZeroStar`、`VAELoader`、`KSamplerAdvanced`、`ModelSamplingSD3`、`PathchSageAttentionKJ`、`WanVideoNAG`、`BerniniConditioning`、`VAEDecode`、`easy imageRemBg`、`VHS_VideoCombine`、`VHS_LoadVideo`、`ImageResizeKJv2`、`LoadImage`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、CLIPTextEncode、LoadImage、UNETLoader、CFGZeroStar

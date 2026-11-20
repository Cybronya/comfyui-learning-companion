---
key: 平台全量/电商视频换服装 wan2.2 bernini_2061072367056670722.json
name: 电商视频换服装 wan2.2 bernini_2061072367056670722
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/电商视频换服装 wan2.2 bernini_2061072367056670722.json
hash: 6c2c59f3e7f254c6
coverage: 0.88
learned_at: 2026-11-14 02:25:22
nodes: [UNETLoader, LoraLoaderModelOnly, UNETLoader, LoraLoaderModelOnly, CLIPLoader, CLIPTextEncode, CLIPTextEncode, CFGZeroStar, VAELoader, KSamplerAdvanced, ModelSamplingSD3, PathchSageAttentionKJ, WanVideoNAG, ModelSamplingSD3, BerniniConditioning, KSamplerAdvanced, VAEDecode, Note, easy imageRemBg, VHS_VideoCombine, VHS_LoadVideo, LoadImage, JjkText, ImageResizeKJv2, Note]
patterns: []
missing: []
parameters: {"cfg": 6, "denoise": "simple", "sampler_name": 1, "scheduler": "lcm", "seed": "disable", "steps": "fixed"}
---

# 平台全量/电商视频换服装 wan2.2 bernini_2061072367056670722.json

> 来源文件 `comfyui_library/workflows/平台全量/电商视频换服装 wan2.2 bernini_2061072367056670722.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（25 个）：
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
- `Note`
- `easy imageRemBg`
- `VHS_VideoCombine`
- `VHS_LoadVideo`
- `LoadImage`
- `JjkText`
- `ImageResizeKJv2`
- `Note`

## 关键参数

- `seed` = `disable`
- `steps` = `fixed`
- `cfg` = `6`
- `sampler_name` = `1`
- `scheduler` = `lcm`
- `denoise` = `simple`

## 知识

覆盖率 **88%**（22/25）

**有卡**：`UNETLoader`、`LoraLoaderModelOnly`、`CLIPLoader`、`CLIPTextEncode`、`CFGZeroStar`、`VAELoader`、`KSamplerAdvanced`、`ModelSamplingSD3`、`PathchSageAttentionKJ`、`WanVideoNAG`、`BerniniConditioning`、`VAEDecode`、`easy imageRemBg`、`VHS_VideoCombine`、`VHS_LoadVideo`、`LoadImage`、`ImageResizeKJv2`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、CLIPTextEncode、LoadImage、UNETLoader、CFGZeroStar

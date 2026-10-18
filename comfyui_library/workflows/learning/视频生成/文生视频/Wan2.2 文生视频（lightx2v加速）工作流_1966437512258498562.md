---
key: 视频生成/文生视频/Wan2.2 文生视频（lightx2v加速）工作流_1966437512258498562.json
name: Wan2.2 文生视频（lightx2v加速）工作流_1966437512258498562.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/Wan2.2 文生视频（lightx2v加速）工作流_1966437512258498562.json
hash: 4d1a9513592b7b77
coverage: 1
learned_at: 2026-10-15 22:43:45
nodes: [CLIPTextEncode, PathchSageAttentionKJ, PathchSageAttentionKJ, ModelSamplingSD3, ModelSamplingSD3, KSamplerAdvanced, KSamplerAdvanced, CLIPTextEncode, VHS_VideoCombine, Image_Upscaletile, VAEDecode, UNETLoader, UNETLoader, CLIPLoader, VAELoader, EmptyHunyuanLatentVideo, LoraLoaderModelOnly, LoraLoaderModelOnly, Image_Upscaletile]
patterns: []
missing: []
parameters: {"cfg": 8, "denoise": "simple", "sampler_name": 1, "scheduler": "euler", "seed": "disable", "steps": "fixed"}
---

# 视频生成/文生视频/Wan2.2 文生视频（lightx2v加速）工作流_1966437512258498562.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/1966437512258498562.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（19 个）：
- `CLIPTextEncode` ★核心
- `PathchSageAttentionKJ`
- `PathchSageAttentionKJ`
- `ModelSamplingSD3`
- `ModelSamplingSD3`
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `CLIPTextEncode` ★核心
- `VHS_VideoCombine`
- `Image_Upscaletile`
- `VAEDecode` ★核心
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `EmptyHunyuanLatentVideo`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `Image_Upscaletile`

## 关键参数

- `seed` = `disable`
- `steps` = `fixed`
- `cfg` = `8`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `simple`

## 知识

覆盖率 **100%**（19/19）

**有卡**：`CLIPTextEncode`、`PathchSageAttentionKJ`、`ModelSamplingSD3`、`KSamplerAdvanced`、`VHS_VideoCombine`、`Image_Upscaletile`、`VAEDecode`、`UNETLoader`、`CLIPLoader`、`VAELoader`、`EmptyHunyuanLatentVideo`、`LoraLoaderModelOnly`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、UNETLoader、KSamplerAdvanced、EmptyHunyuanLatentVideo

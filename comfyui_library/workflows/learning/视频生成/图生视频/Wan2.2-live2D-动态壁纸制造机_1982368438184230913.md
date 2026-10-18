---
key: 视频生成/图生视频/Wan2.2-live2D-动态壁纸制造机_1982368438184230913.json
name: Wan2.2-live2D-动态壁纸制造机_1982368438184230913.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/Wan2.2-live2D-动态壁纸制造机_1982368438184230913.json
hash: ca7f448d7747ae84
coverage: 0.952381
learned_at: 2026-10-15 22:32:41
nodes: [CLIPTextEncode, VAELoader, ModelSamplingSD3, ModelSamplingSD3, UNETLoader, CLIPLoader, PathchSageAttentionKJ, VAEDecode, CreateVideo, WanImageToVideo, SaveVideo, CFGZeroStar, UNETLoader, CLIPTextEncode, LoadImage, KSamplerAdvanced, KSamplerAdvanced, LoraLoaderModelOnly, LoraLoaderModelOnly, LoadImage, MarkdownNote]
patterns: []
missing: []
parameters: {"cfg": 20, "denoise": "simple", "sampler_name": 3.5, "scheduler": "euler", "seed": "disable", "steps": "fixed"}
---

# 视频生成/图生视频/Wan2.2-live2D-动态壁纸制造机_1982368438184230913.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1982368438184230913.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Output → Other

**节点**（21 个）：
- `CLIPTextEncode` ★核心
- `VAELoader`
- `ModelSamplingSD3`
- `ModelSamplingSD3`
- `UNETLoader` ★核心
- `CLIPLoader`
- `PathchSageAttentionKJ`
- `VAEDecode` ★核心
- `CreateVideo`
- `WanImageToVideo`
- `SaveVideo`
- `CFGZeroStar`
- `UNETLoader` ★核心
- `CLIPTextEncode` ★核心
- `LoadImage`
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoadImage`
- `MarkdownNote`

## 关键参数

- `seed` = `disable`
- `steps` = `fixed`
- `cfg` = `20`
- `sampler_name` = `3.5`
- `scheduler` = `euler`
- `denoise` = `simple`

## 知识

覆盖率 **95%**（20/21）

**有卡**：`CLIPTextEncode`、`VAELoader`、`ModelSamplingSD3`、`UNETLoader`、`CLIPLoader`、`PathchSageAttentionKJ`、`VAEDecode`、`CreateVideo`、`WanImageToVideo`、`SaveVideo`、`CFGZeroStar`、`LoadImage`、`KSamplerAdvanced`、`LoraLoaderModelOnly`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerAdvanced

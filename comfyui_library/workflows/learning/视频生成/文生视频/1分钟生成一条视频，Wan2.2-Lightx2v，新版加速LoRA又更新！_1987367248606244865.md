---
key: 视频生成/文生视频/1分钟生成一条视频，Wan2.2-Lightx2v，新版加速LoRA又更新！_1987367248606244865.json
name: 1分钟生成一条视频，Wan2.2-Lightx2v，新版加速LoRA又更新！_1987367248606244865
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/1分钟生成一条视频，Wan2.2-Lightx2v，新版加速LoRA又更新！_1987367248606244865.json
hash: 11c6e5a0e1963483
coverage: 0.857143
learned_at: 2026-10-15 22:43:47
nodes: [CLIPLoader, VAELoader, UNETLoader, CLIPTextEncode, MarkdownNote, CreateVideo, VAEDecode, Note, MarkdownNote, ModelSamplingSD3, ModelSamplingSD3, LoraLoaderModelOnly, LoraLoaderModelOnly, KSamplerAdvanced, UNETLoader, CLIPTextEncode, LoadImage, WanImageToVideo, KSamplerAdvanced, SaveVideo, Label (rgthree)]
patterns: []
missing: []
parameters: {"cfg": 8, "denoise": "simple", "sampler_name": 1, "scheduler": "euler", "seed": "enable", "steps": "fixed"}
---

# 视频生成/文生视频/1分钟生成一条视频，Wan2.2-Lightx2v，新版加速LoRA又更新！_1987367248606244865.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/1分钟生成一条视频，Wan2.2-Lightx2v，新版加速LoRA又更新！_1987367248606244865.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Output → Other

**节点**（21 个）：
- `CLIPLoader`
- `VAELoader`
- `UNETLoader` ★核心
- `CLIPTextEncode` ★核心
- `MarkdownNote`
- `CreateVideo`
- `VAEDecode` ★核心
- `Note`
- `MarkdownNote`
- `ModelSamplingSD3`
- `ModelSamplingSD3`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `KSamplerAdvanced` ★核心
- `UNETLoader` ★核心
- `CLIPTextEncode` ★核心
- `LoadImage`
- `WanImageToVideo`
- `KSamplerAdvanced` ★核心
- `SaveVideo`
- `Label (rgthree)`

## 关键参数

- `seed` = `enable`
- `steps` = `fixed`
- `cfg` = `8`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `simple`

## 知识

覆盖率 **86%**（18/21）

**有卡**：`CLIPLoader`、`VAELoader`、`UNETLoader`、`CLIPTextEncode`、`CreateVideo`、`VAEDecode`、`ModelSamplingSD3`、`LoraLoaderModelOnly`、`KSamplerAdvanced`、`LoadImage`、`WanImageToVideo`、`SaveVideo`、`Label (rgthree)`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerAdvanced

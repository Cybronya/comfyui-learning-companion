---
key: 视频生成/文生视频/Wan2.2 AI视频生成加速工作流_1954053840410857473.json
name: Wan2.2 AI视频生成加速工作流_1954053840410857473
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/Wan2.2 AI视频生成加速工作流_1954053840410857473.json
hash: dae7debab5471359
coverage: 0.95
learned_at: 2026-10-10 23:06:38
nodes: [MarkdownNote, ModelSamplingSD3, CreateVideo, CLIPTextEncode, VAEDecode, ModelSamplingSD3, PathchSageAttentionKJ, PathchSageAttentionKJ, SaveVideo, WanImageToVideo, UNETLoader, UNETLoader, CLIPLoader, VAELoader, LoraLoaderModelOnly, LoraLoaderModelOnly, KSamplerAdvanced, KSamplerAdvanced, LoadImage, CLIPTextEncode]
patterns: []
missing: []
parameters: {"cfg": 8, "denoise": "simple", "sampler_name": 1, "scheduler": "euler", "seed": "enable", "steps": "randomize"}
---

# 视频生成/文生视频/Wan2.2 AI视频生成加速工作流_1954053840410857473.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/Wan2.2 AI视频生成加速工作流_1954053840410857473.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Output → Other

**节点**（20 个）：
- `MarkdownNote`
- `ModelSamplingSD3`
- `CreateVideo`
- `CLIPTextEncode` ★核心
- `VAEDecode` ★核心
- `ModelSamplingSD3`
- `PathchSageAttentionKJ`
- `PathchSageAttentionKJ`
- `SaveVideo`
- `WanImageToVideo`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `LoadImage`
- `CLIPTextEncode` ★核心

## 关键参数

- `seed` = `enable`
- `steps` = `randomize`
- `cfg` = `8`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `simple`

## 知识

覆盖率 **95%**（19/20）

**有卡**：`ModelSamplingSD3`、`CreateVideo`、`CLIPTextEncode`、`VAEDecode`、`PathchSageAttentionKJ`、`SaveVideo`、`WanImageToVideo`、`UNETLoader`、`CLIPLoader`、`VAELoader`、`LoraLoaderModelOnly`、`KSamplerAdvanced`、`LoadImage`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerAdvanced

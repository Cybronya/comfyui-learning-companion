---
key: 视频生成/图生视频/动态壁纸快速生成Wan2.2-live2D_2046114491431133185.json
name: 动态壁纸快速生成Wan2.2-live2D_2046114491431133185.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/动态壁纸快速生成Wan2.2-live2D_2046114491431133185.json
hash: d72347f622d0abf2
coverage: 1
learned_at: 2026-10-15 22:36:54
nodes: [CLIPTextEncode, VAELoader, ModelSamplingSD3, ModelSamplingSD3, UNETLoader, CLIPLoader, PathchSageAttentionKJ, VAEDecode, CreateVideo, WanImageToVideo, SaveVideo, CFGZeroStar, UNETLoader, CLIPTextEncode, KSamplerAdvanced, KSamplerAdvanced, LoraLoaderModelOnly, LoraLoaderModelOnly, LoadImage]
patterns: []
missing: []
parameters: {"cfg": 20, "denoise": "simple", "sampler_name": 3.5, "scheduler": "euler", "seed": "disable", "steps": "fixed"}
---

# 视频生成/图生视频/动态壁纸快速生成Wan2.2-live2D_2046114491431133185.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2046114491431133185.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Output → Other

**节点**（19 个）：
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
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoadImage`

## 关键参数

- `seed` = `disable`
- `steps` = `fixed`
- `cfg` = `20`
- `sampler_name` = `3.5`
- `scheduler` = `euler`
- `denoise` = `simple`

## 知识

覆盖率 **100%**（19/19）

**有卡**：`CLIPTextEncode`、`VAELoader`、`ModelSamplingSD3`、`UNETLoader`、`CLIPLoader`、`PathchSageAttentionKJ`、`VAEDecode`、`CreateVideo`、`WanImageToVideo`、`SaveVideo`、`CFGZeroStar`、`KSamplerAdvanced`、`LoraLoaderModelOnly`、`LoadImage`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerAdvanced

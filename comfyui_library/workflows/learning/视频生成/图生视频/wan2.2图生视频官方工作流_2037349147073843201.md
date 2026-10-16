---
key: 视频生成/图生视频/wan2.2图生视频官方工作流_2037349147073843201.json
name: wan2.2图生视频官方工作流_2037349147073843201.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2037349147073843201.json
hash: e1ec91f6f180ca27
coverage: 1
learned_at: 2026-10-15 22:35:56
nodes: [CLIPLoader, VAEDecode, VHS_VideoCombine, VAELoader, LoadImage, CLIPTextEncode, CLIPTextEncode, WanImageToVideo, UNETLoader, UNETLoader, ModelSamplingSD3, ModelSamplingSD3, KSamplerAdvanced, KSamplerAdvanced, CLIPLoader, VAEDecode, VAELoader, LoadImage, CLIPTextEncode, CLIPTextEncode, UNETLoader, UNETLoader, LoraLoaderModelOnly, ModelSamplingSD3, WanImageToVideo, VHS_VideoCombine, ModelSamplingSD3, LoraLoaderModelOnly, KSamplerAdvanced, KSamplerAdvanced]
patterns: []
missing: []
parameters: {"cfg": 8, "denoise": "simple", "sampler_name": 3.5, "scheduler": "euler", "seed": "disable", "steps": "fixed"}
---

# 视频生成/图生视频/wan2.2图生视频官方工作流_2037349147073843201.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2037349147073843201.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Other

**节点**（30 个）：
- `CLIPLoader`
- `VAEDecode` ★核心
- `VHS_VideoCombine`
- `VAELoader`
- `LoadImage`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `WanImageToVideo`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `ModelSamplingSD3`
- `ModelSamplingSD3`
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `CLIPLoader`
- `VAEDecode` ★核心
- `VAELoader`
- `LoadImage`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `ModelSamplingSD3`
- `WanImageToVideo`
- `VHS_VideoCombine`
- `ModelSamplingSD3`
- `LoraLoaderModelOnly` ★核心
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心

## 关键参数

- `seed` = `disable`
- `steps` = `fixed`
- `cfg` = `8`
- `sampler_name` = `3.5`
- `scheduler` = `euler`
- `denoise` = `simple`

## 知识

覆盖率 **100%**（30/30）

**有卡**：`CLIPLoader`、`VAEDecode`、`VHS_VideoCombine`、`VAELoader`、`LoadImage`、`CLIPTextEncode`、`WanImageToVideo`、`UNETLoader`、`ModelSamplingSD3`、`KSamplerAdvanced`、`LoraLoaderModelOnly`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerAdvanced

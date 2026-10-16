---
key: 视频生成/图生视频/Wan2.2 14B图生视频工作流_1949853817082961922.json
name: Wan2.2 14B图生视频工作流_1949853817082961922.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1949853817082961922.json
hash: 131060795c24d450
coverage: 0.9
learned_at: 2026-10-15 22:30:50
nodes: [CLIPTextEncode, ModelSamplingSD3, ModelSamplingSD3, KSamplerAdvanced, CLIPLoader, UNETLoader, UNETLoader, VAELoader, Note, Note, KSamplerAdvanced, LoadImage, VAEDecode, VHS_VideoCombine, TeaCache, CLIPTextEncode, WanImageToVideo, JWInteger, JWInteger, JWInteger]
patterns: []
missing: []
parameters: {"cfg": 20, "denoise": "simple", "sampler_name": 3.5, "scheduler": "euler", "seed": "enable", "steps": "randomize"}
---

# 视频生成/图生视频/Wan2.2 14B图生视频工作流_1949853817082961922.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1949853817082961922.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Other

**节点**（20 个）：
- `CLIPTextEncode` ★核心
- `ModelSamplingSD3`
- `ModelSamplingSD3`
- `KSamplerAdvanced` ★核心
- `CLIPLoader`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `VAELoader`
- `Note`
- `Note`
- `KSamplerAdvanced` ★核心
- `LoadImage`
- `VAEDecode` ★核心
- `VHS_VideoCombine`
- `TeaCache`
- `CLIPTextEncode` ★核心
- `WanImageToVideo`
- `JWInteger`
- `JWInteger`
- `JWInteger`

## 关键参数

- `seed` = `enable`
- `steps` = `randomize`
- `cfg` = `20`
- `sampler_name` = `3.5`
- `scheduler` = `euler`
- `denoise` = `simple`

## 知识

覆盖率 **90%**（18/20）

**有卡**：`CLIPTextEncode`、`ModelSamplingSD3`、`KSamplerAdvanced`、`CLIPLoader`、`UNETLoader`、`VAELoader`、`LoadImage`、`VAEDecode`、`VHS_VideoCombine`、`TeaCache`、`WanImageToVideo`、`JWInteger`

**用到的条目**：VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerAdvanced、ModelSamplingSD3

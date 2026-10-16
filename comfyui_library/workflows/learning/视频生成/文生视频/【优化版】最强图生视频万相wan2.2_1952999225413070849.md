---
key: 视频生成/文生视频/【优化版】最强图生视频万相wan2.2_1952999225413070849.json
name: 【优化版】最强图生视频万相wan2.2_1952999225413070849.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/1952999225413070849.json
hash: 08b6c44404c3f6da
coverage: 1
learned_at: 2026-10-15 22:43:38
nodes: [ModelSamplingSD3, ModelSamplingSD3, KSamplerAdvanced, VAEDecode, KSamplerAdvanced, UNETLoader, CLIPLoader, VAELoader, UNETLoader, CLIPTextEncode, LoraLoaderModelOnly, LoadImage, WanImageToVideo, VHS_VideoCombine, CLIPTextEncode]
patterns: []
missing: []
parameters: {"cfg": 14, "denoise": "simple", "sampler_name": 1, "scheduler": "euler", "seed": "disable", "steps": "fixed"}
---

# 视频生成/文生视频/【优化版】最强图生视频万相wan2.2_1952999225413070849.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/1952999225413070849.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Other

**节点**（15 个）：
- `ModelSamplingSD3`
- `ModelSamplingSD3`
- `KSamplerAdvanced` ★核心
- `VAEDecode` ★核心
- `KSamplerAdvanced` ★核心
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `UNETLoader` ★核心
- `CLIPTextEncode` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoadImage`
- `WanImageToVideo`
- `VHS_VideoCombine`
- `CLIPTextEncode` ★核心

## 关键参数

- `seed` = `disable`
- `steps` = `fixed`
- `cfg` = `14`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `simple`

## 知识

覆盖率 **100%**（15/15）

**有卡**：`ModelSamplingSD3`、`KSamplerAdvanced`、`VAEDecode`、`UNETLoader`、`CLIPLoader`、`VAELoader`、`CLIPTextEncode`、`LoraLoaderModelOnly`、`LoadImage`、`WanImageToVideo`、`VHS_VideoCombine`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerAdvanced

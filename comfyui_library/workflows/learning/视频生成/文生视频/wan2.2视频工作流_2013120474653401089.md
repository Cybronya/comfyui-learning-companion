---
key: 视频生成/文生视频/wan2.2视频工作流_2013120474653401089.json
name: wan2.2视频工作流_2013120474653401089
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/wan2.2视频工作流_2013120474653401089.json
hash: 7832db3c04bb8174
coverage: 0.944444
learned_at: 2026-10-11 03:07:13
nodes: [CLIPLoader, VAEDecode, CLIPTextEncode, VAELoader, RIFE VFI, ModelSamplingSD3, ModelSamplingSD3, KSamplerAdvanced, KSamplerAdvanced, WanImageToVideo, CLIPTextEncode, LoraLoaderModelOnly, LoraLoaderModelOnly, VHS_VideoCombine, VHS_VideoCombine, UNETLoader, UNETLoader, LoadImage]
patterns: []
missing: [RIFE VFI]
parameters: {"cfg": 12, "denoise": "simple", "sampler_name": 3.5, "scheduler": "euler", "seed": "disable", "steps": "fixed"}
discoveries: [次要节点 `RIFE VFI` 知识库中没有该节点类型的任何知识]
---

# 视频生成/文生视频/wan2.2视频工作流_2013120474653401089.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/wan2.2视频工作流_2013120474653401089.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Other

**节点**（18 个）：
- `CLIPLoader`
- `VAEDecode` ★核心
- `CLIPTextEncode` ★核心
- `VAELoader`
- `RIFE VFI`
- `ModelSamplingSD3`
- `ModelSamplingSD3`
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `WanImageToVideo`
- `CLIPTextEncode` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `LoadImage`

## 关键参数

- `seed` = `disable`
- `steps` = `fixed`
- `cfg` = `12`
- `sampler_name` = `3.5`
- `scheduler` = `euler`
- `denoise` = `simple`

## 知识

覆盖率 **94%**（17/18）

**有卡**：`CLIPLoader`、`VAEDecode`、`CLIPTextEncode`、`VAELoader`、`ModelSamplingSD3`、`KSamplerAdvanced`、`WanImageToVideo`、`LoraLoaderModelOnly`、`VHS_VideoCombine`、`UNETLoader`、`LoadImage`

**缺卡**（1）：`RIFE VFI`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerAdvanced

## 学习发现

- 次要节点 `RIFE VFI` 知识库中没有该节点类型的任何知识

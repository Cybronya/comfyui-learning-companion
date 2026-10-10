---
key: 视频生成/文生视频/Wan2.2文生视频工作流_2011439259349159938.json
name: Wan2.2文生视频工作流_2011439259349159938
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/Wan2.2文生视频工作流_2011439259349159938.json
hash: 0d64d540312d1481
coverage: 1
learned_at: 2026-10-11 03:07:13
nodes: [CLIPTextEncode, CLIPTextEncode, ModelSamplingSD3, EmptyHunyuanLatentVideo, VHS_VideoCombine, UNETLoader, VAELoader, CLIPLoader, VAEDecode, KSampler]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "sa_solver", "scheduler": "beta", "seed": 0, "steps": 4}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/文生视频/Wan2.2文生视频工作流_2011439259349159938.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/Wan2.2文生视频工作流_2011439259349159938.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Other

**节点**（10 个）：
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `ModelSamplingSD3`
- `EmptyHunyuanLatentVideo`
- `VHS_VideoCombine`
- `UNETLoader` ★核心
- `VAELoader`
- `CLIPLoader`
- `VAEDecode` ★核心
- `KSampler` ★核心

## 关键参数

- `seed` = `0`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `sa_solver`
- `scheduler` = `beta`
- `denoise` = `1`

## 知识

覆盖率 **100%**（10/10）

**有卡**：`CLIPTextEncode`、`ModelSamplingSD3`、`EmptyHunyuanLatentVideo`、`VHS_VideoCombine`、`UNETLoader`、`VAELoader`、`CLIPLoader`、`VAEDecode`、`KSampler`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、UNETLoader、EmptyHunyuanLatentVideo、ModelSamplingSD3

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

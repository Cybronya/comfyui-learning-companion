---
key: 视频生成/文生视频/wan2.2_t2v 文生视频_2058371729084469249.json
name: wan2.2_t2v 文生视频_2058371729084469249
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/wan2.2_t2v 文生视频_2058371729084469249.json
hash: 3bfb17d53454f15e
coverage: 1
learned_at: 2026-10-11 19:49:45
nodes: [ModelSamplingSD3, EmptyHunyuanLatentVideo, VAEDecode, CLIPTextEncode, VHS_VideoCombine, CLIPLoader, CLIPTextEncode, UNETLoader, VAELoader, KSampler]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 334113100128820, "steps": 4}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/文生视频/wan2.2_t2v 文生视频_2058371729084469249.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/wan2.2_t2v 文生视频_2058371729084469249.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Other

**节点**（10 个）：
- `ModelSamplingSD3`
- `EmptyHunyuanLatentVideo`
- `VAEDecode` ★核心
- `CLIPTextEncode` ★核心
- `VHS_VideoCombine`
- `CLIPLoader`
- `CLIPTextEncode` ★核心
- `UNETLoader` ★核心
- `VAELoader`
- `KSampler` ★核心

## 关键参数

- `seed` = `334113100128820`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **100%**（10/10）

**有卡**：`ModelSamplingSD3`、`EmptyHunyuanLatentVideo`、`VAEDecode`、`CLIPTextEncode`、`VHS_VideoCombine`、`CLIPLoader`、`UNETLoader`、`VAELoader`、`KSampler`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、UNETLoader、EmptyHunyuanLatentVideo、ModelSamplingSD3

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

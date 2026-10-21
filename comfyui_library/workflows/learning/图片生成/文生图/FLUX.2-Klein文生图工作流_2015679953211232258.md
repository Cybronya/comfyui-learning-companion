---
key: 图片生成/文生图/FLUX.2-Klein文生图工作流_2015679953211232258.json
name: FLUX.2-Klein文生图工作流_2015679953211232258
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/FLUX.2-Klein文生图工作流_2015679953211232258.json
hash: ab758132f8c55678
coverage: 0.9
learned_at: 2026-10-19 22:14:58
nodes: [CLIPLoader, VAELoader, MarkdownNote, UNETLoader, KSampler, EmptyFlux2LatentImage, CLIPTextEncode, CLIPTextEncode, VAEDecode, SaveImage]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 316229828415714, "steps": 8}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/文生图/FLUX.2-Klein文生图工作流_2015679953211232258.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/FLUX.2-Klein文生图工作流_2015679953211232258.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（10 个）：
- `CLIPLoader`
- `VAELoader`
- `MarkdownNote`
- `UNETLoader` ★核心
- `KSampler` ★核心
- `EmptyFlux2LatentImage`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `VAEDecode` ★核心
- `SaveImage`

## 关键参数

- `seed` = `316229828415714`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **90%**（9/10）

**有卡**：`CLIPLoader`、`VAELoader`、`UNETLoader`、`KSampler`、`EmptyFlux2LatentImage`、`CLIPTextEncode`、`VAEDecode`、`SaveImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、UNETLoader、CLIPTextEncode、CLIPLoader、EmptyFlux2LatentImage、SaveImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

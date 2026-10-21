---
key: 图片生成/文生图/FLUX板块：FLUX.2-Klein多模态文生图工作流_2049841830287687681.json
name: FLUX板块：FLUX.2-Klein多模态文生图工作流_2049841830287687681
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/FLUX板块：FLUX.2-Klein多模态文生图工作流_2049841830287687681.json
hash: c337b6ed0f9927e0
coverage: 1
learned_at: 2026-10-21 02:52:00
nodes: [VAELoader, SaveImage, UNETLoader, CLIPTextEncode, CLIPLoader, EmptyFlux2LatentImage, KSampler, VAEDecode, CLIPTextEncode]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 1, "steps": 6}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/文生图/FLUX板块：FLUX.2-Klein多模态文生图工作流_2049841830287687681.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/FLUX板块：FLUX.2-Klein多模态文生图工作流_2049841830287687681.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output

**节点**（9 个）：
- `VAELoader`
- `SaveImage`
- `UNETLoader` ★核心
- `CLIPTextEncode` ★核心
- `CLIPLoader`
- `EmptyFlux2LatentImage`
- `KSampler` ★核心
- `VAEDecode` ★核心
- `CLIPTextEncode` ★核心

## 关键参数

- `seed` = `1`
- `steps` = `6`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **100%**（9/9）

**有卡**：`VAELoader`、`SaveImage`、`UNETLoader`、`CLIPTextEncode`、`CLIPLoader`、`EmptyFlux2LatentImage`、`KSampler`、`VAEDecode`

**用到的条目**：KSampler、VAEDecode、VAELoader、UNETLoader、CLIPTextEncode、CLIPLoader、EmptyFlux2LatentImage、SaveImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

---
key: 图片生成/文生图/FLUX.2-Klein多模态文生图工作流_2068581821109071873.json
name: FLUX.2-Klein多模态文生图工作流_2068581821109071873
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/FLUX.2-Klein多模态文生图工作流_2068581821109071873.json
hash: 0bd48b971ef5233a
coverage: 1
learned_at: 2026-10-19 23:21:20
nodes: [CLIPTextEncode, UNETLoader, CLIPLoader, SaveImage, VAEDecode, VAELoader, EmptyFlux2LatentImage, CLIPTextEncode, KSampler]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 0, "steps": 6}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/文生图/FLUX.2-Klein多模态文生图工作流_2068581821109071873.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/FLUX.2-Klein多模态文生图工作流_2068581821109071873.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output

**节点**（9 个）：
- `CLIPTextEncode` ★核心
- `UNETLoader` ★核心
- `CLIPLoader`
- `SaveImage`
- `VAEDecode` ★核心
- `VAELoader`
- `EmptyFlux2LatentImage`
- `CLIPTextEncode` ★核心
- `KSampler` ★核心

## 关键参数

- `seed` = `0`
- `steps` = `6`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **100%**（9/9）

**有卡**：`CLIPTextEncode`、`UNETLoader`、`CLIPLoader`、`SaveImage`、`VAEDecode`、`VAELoader`、`EmptyFlux2LatentImage`、`KSampler`

**用到的条目**：KSampler、VAEDecode、VAELoader、UNETLoader、CLIPTextEncode、CLIPLoader、EmptyFlux2LatentImage、SaveImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

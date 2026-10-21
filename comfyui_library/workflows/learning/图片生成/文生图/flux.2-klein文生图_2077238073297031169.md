---
key: 图片生成/文生图/flux.2-klein文生图_2077238073297031169.json
name: flux.2-klein文生图_2077238073297031169
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/flux.2-klein文生图_2077238073297031169.json
hash: ec1e6b1e460d78ae
coverage: 1
learned_at: 2026-10-20 00:20:33
nodes: [CLIPLoader, VAELoader, UNETLoader, CLIPTextEncode, KSampler, VAEDecode, SaveImage, CLIPTextEncode, EmptyFlux2LatentImage]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 316229828415716, "steps": 8}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/文生图/flux.2-klein文生图_2077238073297031169.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/flux.2-klein文生图_2077238073297031169.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output

**节点**（9 个）：
- `CLIPLoader`
- `VAELoader`
- `UNETLoader` ★核心
- `CLIPTextEncode` ★核心
- `KSampler` ★核心
- `VAEDecode` ★核心
- `SaveImage`
- `CLIPTextEncode` ★核心
- `EmptyFlux2LatentImage`

## 关键参数

- `seed` = `316229828415716`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **100%**（9/9）

**有卡**：`CLIPLoader`、`VAELoader`、`UNETLoader`、`CLIPTextEncode`、`KSampler`、`VAEDecode`、`SaveImage`、`EmptyFlux2LatentImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、UNETLoader、CLIPTextEncode、CLIPLoader、EmptyFlux2LatentImage、SaveImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

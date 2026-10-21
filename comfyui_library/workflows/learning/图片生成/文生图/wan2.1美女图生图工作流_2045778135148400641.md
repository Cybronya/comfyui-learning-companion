---
key: 图片生成/文生图/wan2.1美女图生图工作流_2045778135148400641.json
name: wan2.1美女图生图工作流_2045778135148400641
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/wan2.1美女图生图工作流_2045778135148400641.json
hash: 0b93a5f8f1094404
coverage: 0.909091
learned_at: 2026-10-19 22:46:14
nodes: [CLIPTextEncode, KSampler, PreviewImage, RHHiddenNodes, CompressImages, VAEDecode, SaveImage, CLIPTextEncode, EmptyHunyuanLatentVideo, Int, Int]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "res_2s", "scheduler": "bong_tangent", "seed": 114727214689768, "steps": 8}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/文生图/wan2.1美女图生图工作流_2045778135148400641.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/wan2.1美女图生图工作流_2045778135148400641.json`

## 结构

**生成流程**：Condition → Sampling → Decode → Process → Output → Other

**节点**（11 个）：
- `CLIPTextEncode` ★核心
- `KSampler` ★核心
- `PreviewImage`
- `RHHiddenNodes`
- `CompressImages`
- `VAEDecode` ★核心
- `SaveImage`
- `CLIPTextEncode` ★核心
- `EmptyHunyuanLatentVideo`
- `Int`
- `Int`

## 关键参数

- `seed` = `114727214689768`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `res_2s`
- `scheduler` = `bong_tangent`
- `denoise` = `1`

## 知识

覆盖率 **91%**（10/11）

**有卡**：`CLIPTextEncode`、`KSampler`、`RHHiddenNodes`、`CompressImages`、`VAEDecode`、`SaveImage`、`EmptyHunyuanLatentVideo`、`Int`

**用到的条目**：KSampler、VAEDecode、CLIPTextEncode、EmptyHunyuanLatentVideo、SaveImage、Int、RHHiddenNodes、CompressImages

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

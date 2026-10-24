---
key: 图片生成/图生图/FLUX板块：FLUX.2-Klein图洗图工作流_2049795289871073281.json
name: FLUX板块：FLUX.2-Klein图洗图工作流_2049795289871073281
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/FLUX板块：FLUX.2-Klein图洗图工作流_2049795289871073281.json
hash: fcf3d9a199f7fbca
coverage: 0.909091
learned_at: 2026-10-23 10:55:01
nodes: [CLIPLoader, UNETLoader, VAEEncode, VAEDecode, CLIPTextEncode, VAELoader, KSampler, SaveImage, Image Comparer (rgthree), LoadImage, CLIPTextEncode]
patterns: [image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 0.30000000000000004, "sampler_name": "euler", "scheduler": "simple", "seed": 0, "steps": 8}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/FLUX板块：FLUX.2-Klein图洗图工作流_2049795289871073281.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/FLUX板块：FLUX.2-Klein图洗图工作流_2049795289871073281.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Output → Other

**节点**（11 个）：
- `CLIPLoader`
- `UNETLoader` ★核心
- `VAEEncode` ★核心
- `VAEDecode` ★核心
- `CLIPTextEncode` ★核心
- `VAELoader`
- `KSampler` ★核心
- `SaveImage`
- `Image Comparer (rgthree)`
- `LoadImage`
- `CLIPTextEncode` ★核心

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `0`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `0.30000000000000004`

## 知识

覆盖率 **91%**（10/11）

**有卡**：`CLIPLoader`、`UNETLoader`、`VAEEncode`、`VAEDecode`、`CLIPTextEncode`、`VAELoader`、`KSampler`、`SaveImage`、`LoadImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、VAEEncode

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

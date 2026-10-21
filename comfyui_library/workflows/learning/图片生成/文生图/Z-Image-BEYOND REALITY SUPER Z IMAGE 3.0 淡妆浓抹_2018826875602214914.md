---
key: 图片生成/文生图/Z-Image-BEYOND REALITY SUPER Z IMAGE 3.0 淡妆浓抹_2018826875602214914.json
name: Z-Image-BEYOND REALITY SUPER Z IMAGE 3.0 淡妆浓抹_2018826875602214914
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Z-Image-BEYOND REALITY SUPER Z IMAGE 3.0 淡妆浓抹_2018826875602214914.json
hash: 72b72aa9d1eee519
coverage: 0.923077
learned_at: 2026-10-19 22:29:58
nodes: [CLIPTextEncode, EmptySD3LatentImage, CLIPTextEncode, UNETLoader, CLIPLoader, VAELoader, Note, ModelSamplingAuraFlow, KSampler, SDXL Resolutions (JPS), VAEDecode, easy cleanGpuUsed, SaveImage]
patterns: []
missing: []
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 657118378706618, "steps": 10}
---

# 图片生成/文生图/Z-Image-BEYOND REALITY SUPER Z IMAGE 3.0 淡妆浓抹_2018826875602214914.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Z-Image-BEYOND REALITY SUPER Z IMAGE 3.0 淡妆浓抹_2018826875602214914.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（13 个）：
- `CLIPTextEncode` ★核心
- `EmptySD3LatentImage`
- `CLIPTextEncode` ★核心
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `Note`
- `ModelSamplingAuraFlow`
- `KSampler` ★核心
- `SDXL Resolutions (JPS)`
- `VAEDecode` ★核心
- `easy cleanGpuUsed`
- `SaveImage`

## 关键参数

- `seed` = `657118378706618`
- `steps` = `10`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **92%**（12/13）

**有卡**：`CLIPTextEncode`、`EmptySD3LatentImage`、`UNETLoader`、`CLIPLoader`、`VAELoader`、`ModelSamplingAuraFlow`、`KSampler`、`SDXL Resolutions (JPS)`、`VAEDecode`、`easy cleanGpuUsed`、`SaveImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、UNETLoader、CLIPTextEncode、CLIPLoader、SDXL Resolutions (JPS)、EmptySD3LatentImage

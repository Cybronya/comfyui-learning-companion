---
key: 图片生成/文生图/Wan2.2——文生图_1950509671901810689.json
name: Wan2.2——文生图_1950509671901810689
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Wan2.2——文生图_1950509671901810689.json
hash: fd8aacb81062a0c5
coverage: 0.928571
learned_at: 2026-10-10 20:59:14
nodes: [CLIPTextEncode, ModelSamplingSD3, ModelSamplingSD3, KSamplerAdvanced, KSamplerAdvanced, PreviewImage, EmptyLatentImage, CLIPTextEncode, UNETLoader, UNETLoader, CLIPLoader, VAELoader, VAEDecode, SaveImage]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 20, "denoise": "beta", "height": 720, "sampler_name": 3.5, "scheduler": "heun", "seed": "enable", "steps": "fixed", "width": 1280}
---

# 图片生成/文生图/Wan2.2——文生图_1950509671901810689.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Wan2.2——文生图_1950509671901810689.json`

## 结构

**节点**（14 个）：
- `CLIPTextEncode`
- `ModelSamplingSD3`
- `ModelSamplingSD3`
- `KSamplerAdvanced`
- `KSamplerAdvanced`
- `PreviewImage`
- `EmptyLatentImage`
- `CLIPTextEncode`
- `UNETLoader`
- `UNETLoader`
- `CLIPLoader`
- `VAELoader`
- `VAEDecode`
- `SaveImage`

## 关键参数

- `batch_size` = `1`
- `cfg` = `20`
- `denoise` = `beta`
- `height` = `720`
- `sampler_name` = `3.5`
- `scheduler` = `heun`
- `seed` = `enable`
- `steps` = `fixed`
- `width` = `1280`

## 知识

覆盖率 **93%**（13/14）

**有卡**：`CLIPTextEncode`、`ModelSamplingSD3`、`KSamplerAdvanced`、`PreviewImage`、`EmptyLatentImage`、`UNETLoader`、`CLIPLoader`、`VAELoader`、`VAEDecode`

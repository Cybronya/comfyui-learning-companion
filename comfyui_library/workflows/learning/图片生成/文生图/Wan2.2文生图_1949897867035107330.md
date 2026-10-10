---
key: Wan2.2文生图_1949897867035107330.json
name: Wan2.2文生图_1949897867035107330
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Wan2.2文生图_1949897867035107330.json
hash: 6f7831583ce16fa0
coverage: 0.833333
learned_at: 2026-10-10 20:59:14
nodes: [VAEDecode, SaveImage, KSampler, ModelSamplingSD3, ModelSamplingSD3, KSampler, CLIPTextEncode, LoadImage, LoadImage, UNETLoader, UNETLoader, CLIPLoader, VAELoader, PrimitiveInt, PrimitiveInt, CLIPTextEncode, EmptyHunyuanLatentVideo, PreviewImage]
patterns: []
missing: []
parameters: {"cfg": 3.5, "denoise": 1, "sampler_name": "res_2s", "scheduler": "bong_tangent", "seed": 449735519400788, "steps": 20}
---

# Wan2.2文生图_1949897867035107330.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Wan2.2文生图_1949897867035107330.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Output → Other

**节点**（18 个）：
- `VAEDecode` ★核心
- `SaveImage`
- `KSampler` ★核心
- `ModelSamplingSD3`
- `ModelSamplingSD3`
- `KSampler` ★核心
- `CLIPTextEncode` ★核心
- `LoadImage`
- `LoadImage`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `PrimitiveInt`
- `PrimitiveInt`
- `CLIPTextEncode` ★核心
- `EmptyHunyuanLatentVideo`
- `PreviewImage`

## 关键参数

- `seed` = `449735519400788`
- `steps` = `20`
- `cfg` = `3.5`
- `sampler_name` = `res_2s`
- `scheduler` = `bong_tangent`
- `denoise` = `1`

## 知识

覆盖率 **83%**（15/18）

**有卡**：`VAEDecode`、`SaveImage`、`KSampler`、`ModelSamplingSD3`、`CLIPTextEncode`、`LoadImage`、`UNETLoader`、`CLIPLoader`、`VAELoader`、`EmptyHunyuanLatentVideo`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、EmptyHunyuanLatentVideo

---
key: 图片生成/文生图/Wan2.2文生图_1949897867035107330.json
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

# 图片生成/文生图/Wan2.2文生图_1949897867035107330.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Wan2.2文生图_1949897867035107330.json`

## 结构

**节点**（18 个）：
- `VAEDecode`
- `SaveImage`
- `KSampler`
- `ModelSamplingSD3`
- `ModelSamplingSD3`
- `KSampler`
- `CLIPTextEncode`
- `LoadImage`
- `LoadImage`
- `UNETLoader`
- `UNETLoader`
- `CLIPLoader`
- `VAELoader`
- `PrimitiveInt`
- `PrimitiveInt`
- `CLIPTextEncode`
- `EmptyHunyuanLatentVideo`
- `PreviewImage`

## 关键参数

- `cfg` = `3.5`
- `denoise` = `1`
- `sampler_name` = `res_2s`
- `scheduler` = `bong_tangent`
- `seed` = `449735519400788`
- `steps` = `20`

## 知识

覆盖率 **83%**（15/18）

**有卡**：`VAEDecode`、`SaveImage`、`KSampler`、`ModelSamplingSD3`、`CLIPTextEncode`、`LoadImage`、`UNETLoader`、`CLIPLoader`、`VAELoader`、`PrimitiveInt`

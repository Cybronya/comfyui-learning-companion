---
key: 图片生成/图生图/FLUX.1扩图_2055583012271730689.json
name: FLUX.1扩图_2055583012271730689
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/FLUX.1扩图_2055583012271730689.json
hash: dfb9a94e1364f31f
coverage: 1
learned_at: 2026-10-23 10:54:03
nodes: [DualCLIPLoader, EmptySD3LatentImage, VAELoader, UNETLoader, ConditioningZeroOut, InpaintModelConditioning, KSampler, VAEDecode, SaveImage, LoadImage, ImagePadForOutpaint, CLIPTextEncodeFlux]
patterns: []
missing: []
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 177986991850982, "steps": 20}
---

# 图片生成/图生图/FLUX.1扩图_2055583012271730689.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/FLUX.1扩图_2055583012271730689.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（12 个）：
- `DualCLIPLoader`
- `EmptySD3LatentImage`
- `VAELoader`
- `UNETLoader` ★核心
- `ConditioningZeroOut`
- `InpaintModelConditioning`
- `KSampler` ★核心
- `VAEDecode` ★核心
- `SaveImage`
- `LoadImage`
- `ImagePadForOutpaint`
- `CLIPTextEncodeFlux` ★核心

## 关键参数

- `seed` = `177986991850982`
- `steps` = `20`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **100%**（12/12）

**有卡**：`DualCLIPLoader`、`EmptySD3LatentImage`、`VAELoader`、`UNETLoader`、`ConditioningZeroOut`、`InpaintModelConditioning`、`KSampler`、`VAEDecode`、`SaveImage`、`LoadImage`、`ImagePadForOutpaint`、`CLIPTextEncodeFlux`

**用到的条目**：KSampler、VAEDecode、VAELoader、UNETLoader、ConditioningZeroOut、LoadImage、CLIPTextEncodeFlux、DualCLIPLoader

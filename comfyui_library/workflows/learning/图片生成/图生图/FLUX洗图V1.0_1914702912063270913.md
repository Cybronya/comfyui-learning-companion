---
key: 图片生成/图生图/FLUX洗图V1.0_1914702912063270913.json
name: FLUX洗图V1.0_1914702912063270913
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/FLUX洗图V1.0_1914702912063270913.json
hash: 56b0aed26f1730d7
coverage: 1
learned_at: 2026-10-23 10:55:02
nodes: [LoraLoaderModelOnly, LoraLoaderModelOnly, VAELoader, CLIPTextEncodeFlux, ConditioningZeroOut, VAEEncode, KSampler, VAEDecode, LoadImage, UNETLoader, DualCLIPLoader, SaveImage]
patterns: [image_to_image]
missing: []
parameters: {"cfg": 1, "denoise": 0.55, "sampler_name": "euler", "scheduler": "normal", "seed": 953689450986618, "steps": 20}
---

# 图片生成/图生图/FLUX洗图V1.0_1914702912063270913.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/FLUX洗图V1.0_1914702912063270913.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Output → Other

**节点**（12 个）：
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `VAELoader`
- `CLIPTextEncodeFlux` ★核心
- `ConditioningZeroOut`
- `VAEEncode` ★核心
- `KSampler` ★核心
- `VAEDecode` ★核心
- `LoadImage`
- `UNETLoader` ★核心
- `DualCLIPLoader`
- `SaveImage`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `953689450986618`
- `steps` = `20`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `normal`
- `denoise` = `0.55`

## 知识

覆盖率 **100%**（12/12）

**有卡**：`LoraLoaderModelOnly`、`VAELoader`、`CLIPTextEncodeFlux`、`ConditioningZeroOut`、`VAEEncode`、`KSampler`、`VAEDecode`、`LoadImage`、`UNETLoader`、`DualCLIPLoader`、`SaveImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、ConditioningZeroOut、LoadImage、CLIPTextEncodeFlux

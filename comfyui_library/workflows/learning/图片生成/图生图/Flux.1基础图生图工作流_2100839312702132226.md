---
key: 图片生成/图生图/Flux.1基础图生图工作流_2100839312702132226.json
name: Flux.1基础图生图工作流_2100839312702132226
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Flux.1基础图生图工作流_2100839312702132226.json
hash: d42d49d81302c05d
coverage: 1
learned_at: 2026-10-21 00:39:34
nodes: [VAELoader, DualCLIPLoader, FluxGuidance, CLIPTextEncode, EmptySD3LatentImage, CLIPTextEncode, UNETLoader, LoraLoaderModelOnly, VAEDecode, VAEEncode, ImageScale, KSampler, SaveImage, LoadImage]
patterns: [image_to_image]
missing: []
parameters: {"cfg": 1, "denoise": 0.5000000000000001, "sampler_name": "euler", "scheduler": "simple", "seed": 332128558434961, "steps": 30}
---

# 图片生成/图生图/Flux.1基础图生图工作流_2100839312702132226.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Flux.1基础图生图工作流_2100839312702132226.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（14 个）：
- `VAELoader`
- `DualCLIPLoader`
- `FluxGuidance`
- `CLIPTextEncode` ★核心
- `EmptySD3LatentImage`
- `CLIPTextEncode` ★核心
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `VAEDecode` ★核心
- `VAEEncode` ★核心
- `ImageScale`
- `KSampler` ★核心
- `SaveImage`
- `LoadImage`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `332128558434961`
- `steps` = `30`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `0.5000000000000001`

## 知识

覆盖率 **100%**（14/14）

**有卡**：`VAELoader`、`DualCLIPLoader`、`FluxGuidance`、`CLIPTextEncode`、`EmptySD3LatentImage`、`UNETLoader`、`LoraLoaderModelOnly`、`VAEDecode`、`VAEEncode`、`ImageScale`、`KSampler`、`SaveImage`、`LoadImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPTextEncode、LoadImage、FluxGuidance

---
key: 图片生成/图生图/Magic-Wan2.2-修手工作流_1995477299732656129.json
name: Magic-Wan2.2-修手工作流_1995477299732656129
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Magic-Wan2.2-修手工作流_1995477299732656129.json
hash: 605c4b5803cbb23c
coverage: 1
learned_at: 2026-10-23 11:09:16
nodes: [LoraLoaderModelOnly, MaskFillHoles, LayerUtility: ImageScaleByAspectRatio V2, SaveImage, DifferentialDiffusion, InpaintModelConditioning, VAEDecode, KSampler, CLIPTextEncode, CLIPTextEncode, UNETLoader, CLIPLoader, VAELoader, LoadImage]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 0.3600000000000001, "sampler_name": "euler", "scheduler": "beta", "seed": 747946126122118, "steps": 6}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/Magic-Wan2.2-修手工作流_1995477299732656129.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Magic-Wan2.2-修手工作流_1995477299732656129.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（14 个）：
- `LoraLoaderModelOnly` ★核心
- `MaskFillHoles`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `SaveImage`
- `DifferentialDiffusion`
- `InpaintModelConditioning`
- `VAEDecode` ★核心
- `KSampler` ★核心
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `LoadImage`

## 关键参数

- `seed` = `747946126122118`
- `steps` = `6`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `beta`
- `denoise` = `0.3600000000000001`

## 知识

覆盖率 **100%**（14/14）

**有卡**：`LoraLoaderModelOnly`、`MaskFillHoles`、`LayerUtility: ImageScaleByAspectRatio V2`、`SaveImage`、`DifferentialDiffusion`、`InpaintModelConditioning`、`VAEDecode`、`KSampler`、`CLIPTextEncode`、`UNETLoader`、`CLIPLoader`、`VAELoader`、`LoadImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

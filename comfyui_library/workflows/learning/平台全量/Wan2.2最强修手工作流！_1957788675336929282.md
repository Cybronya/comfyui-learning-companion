---
key: 平台全量/Wan2.2最强修手工作流！_1957788675336929282.json
name: Wan2.2最强修手工作流！_1957788675336929282
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/Wan2.2最强修手工作流！_1957788675336929282.json
hash: 0858dc102a0d7312
coverage: 1
learned_at: 2026-11-14 01:06:21
nodes: [ModelSamplingSD3, ModelSamplingSD3, UNETLoader, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, KSampler, InpaintModelConditioning, CLIPLoader, VAELoader, Mask Fill Holes, LayerUtility: ImageScaleByAspectRatio V2, CLIPTextEncode, CLIPTextEncode, LoadImage, KSampler, VAEDecode, SaveImage]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 3.5, "denoise": 0.30000000000000004, "sampler_name": "euler", "scheduler": "simple", "seed": 421330373561607, "steps": 6}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 平台全量/Wan2.2最强修手工作流！_1957788675336929282.json

> 来源文件 `comfyui_library/workflows/平台全量/Wan2.2最强修手工作流！_1957788675336929282.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（18 个）：
- `ModelSamplingSD3`
- `ModelSamplingSD3`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `KSampler` ★核心
- `InpaintModelConditioning`
- `CLIPLoader`
- `VAELoader`
- `Mask Fill Holes`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `LoadImage`
- `KSampler` ★核心
- `VAEDecode` ★核心
- `SaveImage`

## 关键参数

- `seed` = `421330373561607`
- `steps` = `6`
- `cfg` = `3.5`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `0.30000000000000004`

## 知识

覆盖率 **100%**（18/18）

**有卡**：`ModelSamplingSD3`、`UNETLoader`、`LoraLoaderModelOnly`、`KSampler`、`InpaintModelConditioning`、`CLIPLoader`、`VAELoader`、`Mask Fill Holes`、`LayerUtility: ImageScaleByAspectRatio V2`、`CLIPTextEncode`、`LoadImage`、`VAEDecode`、`SaveImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、CLIPTextEncode、LoadImage、UNETLoader

## 参数体检

发现 2 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

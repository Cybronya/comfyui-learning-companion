---
key: 图片生成/图生图/QwenEdit2511-融图-去塑料感-v5.0_2046110169540599810.json
name: QwenEdit2511-融图-去塑料感-v5.0_2046110169540599810
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/QwenEdit2511-融图-去塑料感-v5.0_2046110169540599810.json
hash: 1b89d29e56273a9a
coverage: 1
learned_at: 2026-10-23 11:20:23
nodes: [ModelSamplingAuraFlow, FluxKontextMultiReferenceLatentMethod, VAEDecode, LoadImage, CFGNorm, EmptyLatentImage, SaveImage, ConditioningZeroOut, TextEncodeQwenImageEditPlus, FluxKontextMultiReferenceLatentMethod, LoadImage, LoadImage, KSampler, CheckpointLoaderSimple]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 1.2, "checkpoint": "QwenRapidAIO 23-22-21_QwenRapidAIO 23.safetensors", "denoise": 1, "height": 1792, "sampler_name": "euler", "scheduler": "simple", "seed": 884041633022704, "steps": 4, "width": 1024}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/QwenEdit2511-融图-去塑料感-v5.0_2046110169540599810.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/QwenEdit2511-融图-去塑料感-v5.0_2046110169540599810.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（14 个）：
- `ModelSamplingAuraFlow`
- `FluxKontextMultiReferenceLatentMethod`
- `VAEDecode` ★核心
- `LoadImage`
- `CFGNorm`
- `EmptyLatentImage` ★核心
- `SaveImage`
- `ConditioningZeroOut`
- `TextEncodeQwenImageEditPlus`
- `FluxKontextMultiReferenceLatentMethod`
- `LoadImage`
- `LoadImage`
- `KSampler` ★核心
- `CheckpointLoaderSimple` ★核心

## 关键参数

- `width` = `1024`
- `height` = `1792`
- `batch_size` = `1`
- `seed` = `884041633022704`
- `steps` = `4`
- `cfg` = `1.2`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`
- `checkpoint` = `QwenRapidAIO 23-22-21_QwenRapidAIO 23.safetensors`

## 知识

覆盖率 **100%**（14/14）

**有卡**：`ModelSamplingAuraFlow`、`FluxKontextMultiReferenceLatentMethod`、`VAEDecode`、`LoadImage`、`CFGNorm`、`EmptyLatentImage`、`SaveImage`、`ConditioningZeroOut`、`TextEncodeQwenImageEditPlus`、`KSampler`、`CheckpointLoaderSimple`

**用到的条目**：KSampler、VAEDecode、CheckpointLoaderSimple、ConditioningZeroOut、EmptyLatentImage、LoadImage、CFGNorm、FluxKontextMultiReferenceLatentMethod

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

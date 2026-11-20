---
key: 平台全量/LORA系列05-fal-Krea-2-Style-LoRAs-用于Krea2-Turbo_2077273546866384898.json
name: LORA系列05-fal-Krea-2-Style-LoRAs-用于Krea2-Turbo_2077273546866384898
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/LORA系列05-fal-Krea-2-Style-LoRAs-用于Krea2-Turbo_2077273546866384898.json
hash: e696d764009c8600
coverage: 0.666667
learned_at: 2026-11-14 00:36:46
nodes: [Note, Label (rgthree), Note, Note, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, Note, Note, Note, LoadImage, LoraLoaderModelOnly, UNETLoader, KSampler, Seed (rgthree), CLIPLoader, VAELoader, ConditioningZeroOut, VAEDecode, CLIPTextEncode, Note, LoraLoaderModelOnly, Label (rgthree), CR SDXL Aspect Ratio, SaveImage, Note, Note]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "er_sde", "scheduler": "simple", "seed": 423831166134004, "steps": 8}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 平台全量/LORA系列05-fal-Krea-2-Style-LoRAs-用于Krea2-Turbo_2077273546866384898.json

> 来源文件 `comfyui_library/workflows/平台全量/LORA系列05-fal-Krea-2-Style-LoRAs-用于Krea2-Turbo_2077273546866384898.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Output → Other

**节点**（27 个）：
- `Note`
- `Label (rgthree)`
- `Note`
- `Note`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `Note`
- `Note`
- `Note`
- `LoadImage`
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `KSampler` ★核心
- `Seed (rgthree)`
- `CLIPLoader`
- `VAELoader`
- `ConditioningZeroOut`
- `VAEDecode` ★核心
- `CLIPTextEncode` ★核心
- `Note`
- `LoraLoaderModelOnly` ★核心
- `Label (rgthree)`
- `CR SDXL Aspect Ratio`
- `SaveImage`
- `Note`
- `Note`

## 关键参数

- `seed` = `423831166134004`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `er_sde`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **67%**（18/27）

**有卡**：`Label (rgthree)`、`LoraLoaderModelOnly`、`LoadImage`、`UNETLoader`、`KSampler`、`Seed (rgthree)`、`CLIPLoader`、`VAELoader`、`ConditioningZeroOut`、`VAEDecode`、`CLIPTextEncode`、`CR SDXL Aspect Ratio`、`SaveImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPLoader、CLIPTextEncode、ConditioningZeroOut

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

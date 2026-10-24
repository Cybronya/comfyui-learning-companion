---
key: 图片生成/图生图/QwenEdit Next Scane场景一致性lora批量跑图_1977738722605158402.json
name: QwenEdit Next Scane场景一致性lora批量跑图_1977738722605158402
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/QwenEdit Next Scane场景一致性lora批量跑图_1977738722605158402.json
hash: 2b3e022a409a2e5c
coverage: 0.944444
learned_at: 2026-10-23 11:20:03
nodes: [easy promptLine, UNETLoader, LoraLoaderModelOnly, KSampler, VAEDecode, KSampler, VAEDecode, TextEncodeQwenImageEditPlusAdvance_lrzjason, ConditioningZeroOut, ConditioningZeroOut, easy showAnything, RH_Captioner, LoadImage, SaveImage, VAELoader, CLIPLoader, LoraLoaderModelOnly, SaveImage]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "beta57", "seed": 1, "steps": 8}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/QwenEdit Next Scane场景一致性lora批量跑图_1977738722605158402.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/QwenEdit Next Scane场景一致性lora批量跑图_1977738722605158402.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Output → Other

**节点**（18 个）：
- `easy promptLine`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `KSampler` ★核心
- `VAEDecode` ★核心
- `KSampler` ★核心
- `VAEDecode` ★核心
- `TextEncodeQwenImageEditPlusAdvance_lrzjason`
- `ConditioningZeroOut`
- `ConditioningZeroOut`
- `easy showAnything`
- `RH_Captioner`
- `LoadImage`
- `SaveImage`
- `VAELoader`
- `CLIPLoader`
- `LoraLoaderModelOnly` ★核心
- `SaveImage`

## 关键参数

- `seed` = `1`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `beta57`
- `denoise` = `1`

## 知识

覆盖率 **94%**（17/18）

**有卡**：`easy promptLine`、`UNETLoader`、`LoraLoaderModelOnly`、`KSampler`、`VAEDecode`、`TextEncodeQwenImageEditPlusAdvance_lrzjason`、`ConditioningZeroOut`、`RH_Captioner`、`LoadImage`、`SaveImage`、`VAELoader`、`CLIPLoader`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、ConditioningZeroOut、LoadImage、UNETLoader

## 参数体检

发现 2 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

---
key: 图片生成/图生图/QwenEdit Next Scane场景一致性lora批量跑图_1978060571725680642.json
name: QwenEdit Next Scane场景一致性lora批量跑图_1978060571725680642
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/QwenEdit Next Scane场景一致性lora批量跑图_1978060571725680642.json
hash: b5afe3b28aa4096c
coverage: 0.944444
learned_at: 2026-10-23 11:20:03
nodes: [UNETLoader, CLIPLoader, LoraLoaderModelOnly, TextEncodeQwenImageEditPlusAdvance_lrzjason, VAELoader, ConditioningZeroOut, ConditioningZeroOut, VAEDecode, VAEDecode, LoraLoaderModelOnly, KSampler, KSampler, ShowText|pysssss, SaveImage, SaveImage, easy promptLine, LoadImage, RH_Captioner]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "beta57", "seed": 167147597114818, "steps": 8}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/QwenEdit Next Scane场景一致性lora批量跑图_1978060571725680642.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/QwenEdit Next Scane场景一致性lora批量跑图_1978060571725680642.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Output → Other

**节点**（18 个）：
- `UNETLoader` ★核心
- `CLIPLoader`
- `LoraLoaderModelOnly` ★核心
- `TextEncodeQwenImageEditPlusAdvance_lrzjason`
- `VAELoader`
- `ConditioningZeroOut`
- `ConditioningZeroOut`
- `VAEDecode` ★核心
- `VAEDecode` ★核心
- `LoraLoaderModelOnly` ★核心
- `KSampler` ★核心
- `KSampler` ★核心
- `ShowText|pysssss`
- `SaveImage`
- `SaveImage`
- `easy promptLine`
- `LoadImage`
- `RH_Captioner`

## 关键参数

- `seed` = `167147597114818`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `beta57`
- `denoise` = `1`

## 知识

覆盖率 **94%**（17/18）

**有卡**：`UNETLoader`、`CLIPLoader`、`LoraLoaderModelOnly`、`TextEncodeQwenImageEditPlusAdvance_lrzjason`、`VAELoader`、`ConditioningZeroOut`、`VAEDecode`、`KSampler`、`SaveImage`、`easy promptLine`、`LoadImage`、`RH_Captioner`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、ConditioningZeroOut、LoadImage、UNETLoader

## 参数体检

发现 2 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

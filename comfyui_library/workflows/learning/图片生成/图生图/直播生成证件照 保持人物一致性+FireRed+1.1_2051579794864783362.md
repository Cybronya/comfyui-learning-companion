---
key: 图片生成/图生图/直播生成证件照 保持人物一致性+FireRed+1.1_2051579794864783362.json
name: 直播生成证件照 保持人物一致性+FireRed+1.1_2051579794864783362
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/直播生成证件照 保持人物一致性+FireRed+1.1_2051579794864783362.json
hash: ed76d0934a16dcba
coverage: 0.666667
learned_at: 2026-10-23 13:18:30
nodes: [CLIPLoader, LoraLoaderModelOnly, ConditioningZeroOut, KSampler, VAELoader, VAEDecode, UNETLoader, TextEncodeQwenImageEditPlusAdvance_lrzjason, LoadImage, Reroute, Image Comparer (rgthree), SaveImage, Note, JjkText, Note]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "beta", "seed": 727923644901043, "steps": 4}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/直播生成证件照 保持人物一致性+FireRed+1.1_2051579794864783362.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/直播生成证件照 保持人物一致性+FireRed+1.1_2051579794864783362.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Output → Other

**节点**（15 个）：
- `CLIPLoader`
- `LoraLoaderModelOnly` ★核心
- `ConditioningZeroOut`
- `KSampler` ★核心
- `VAELoader`
- `VAEDecode` ★核心
- `UNETLoader` ★核心
- `TextEncodeQwenImageEditPlusAdvance_lrzjason`
- `LoadImage`
- `Reroute`
- `Image Comparer (rgthree)`
- `SaveImage`
- `Note`
- `JjkText`
- `Note`

## 关键参数

- `seed` = `727923644901043`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `beta`
- `denoise` = `1`

## 知识

覆盖率 **67%**（10/15）

**有卡**：`CLIPLoader`、`LoraLoaderModelOnly`、`ConditioningZeroOut`、`KSampler`、`VAELoader`、`VAEDecode`、`UNETLoader`、`TextEncodeQwenImageEditPlusAdvance_lrzjason`、`LoadImage`、`SaveImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、ConditioningZeroOut、LoadImage、UNETLoader

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

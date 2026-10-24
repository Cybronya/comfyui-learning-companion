---
key: 图片生成/图生图/小红书开源FireRed Image Edit 1.1最强一键换装_2031672315548798977.json
name: 小红书开源FireRed Image Edit 1.1最强一键换装_2031672315548798977
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/小红书开源FireRed Image Edit 1.1最强一键换装_2031672315548798977.json
hash: 51c94947c2e8e05e
coverage: 0.846154
learned_at: 2026-10-23 12:49:26
nodes: [CLIPLoader, VAELoader, TextEncodeQwenImageEditPlus_lrzjason, ConditioningZeroOut, UNETLoader, LoraLoaderModelOnly, VAEDecode, Anything Everywhere3, LoadImage, LoadImage, Image Comparer (rgthree), SaveImage, KSampler]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 915358980176832, "steps": 4}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/小红书开源FireRed Image Edit 1.1最强一键换装_2031672315548798977.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/小红书开源FireRed Image Edit 1.1最强一键换装_2031672315548798977.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Output → Other

**节点**（13 个）：
- `CLIPLoader`
- `VAELoader`
- `TextEncodeQwenImageEditPlus_lrzjason`
- `ConditioningZeroOut`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `VAEDecode` ★核心
- `Anything Everywhere3`
- `LoadImage`
- `LoadImage`
- `Image Comparer (rgthree)`
- `SaveImage`
- `KSampler` ★核心

## 关键参数

- `seed` = `915358980176832`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **85%**（11/13）

**有卡**：`CLIPLoader`、`VAELoader`、`TextEncodeQwenImageEditPlus_lrzjason`、`ConditioningZeroOut`、`UNETLoader`、`LoraLoaderModelOnly`、`VAEDecode`、`LoadImage`、`SaveImage`、`KSampler`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、ConditioningZeroOut、LoadImage、UNETLoader

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

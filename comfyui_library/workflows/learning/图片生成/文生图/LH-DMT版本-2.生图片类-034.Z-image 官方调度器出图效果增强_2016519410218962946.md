---
key: 图片生成/文生图/LH-DMT版本-2.生图片类-034.Z-image 官方调度器出图效果增强_2016519410218962946.json
name: LH-DMT版本-2.生图片类-034.Z-image 官方调度器出图效果增强_2016519410218962946
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/LH-DMT版本-2.生图片类-034.Z-image 官方调度器出图效果增强_2016519410218962946.json
hash: 28588e3cb5d89523
coverage: 0.952381
learned_at: 2026-10-19 22:15:12
nodes: [Seed (rgthree), UNETLoader, CLIPLoader, EmptyLatentImage, easy int, easy int, easy int, RandomNoise, BasicGuider, CLIPTextEncode, FlowMatchEulerDiscreteScheduler (Custom), SamplerCustomAdvanced, KSamplerSelect, VAEDecode, VAEDecode, ConditioningZeroOut, Image Comparer (rgthree), SaveImage, SaveImage, KSampler, VAELoader]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 2048, "sampler_name": "euler", "scheduler": "sgm_uniform", "seed": 30557922910419, "steps": 9, "width": 2048}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/文生图/LH-DMT版本-2.生图片类-034.Z-image 官方调度器出图效果增强_2016519410218962946.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/LH-DMT版本-2.生图片类-034.Z-image 官方调度器出图效果增强_2016519410218962946.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（21 个）：
- `Seed (rgthree)`
- `UNETLoader` ★核心
- `CLIPLoader`
- `EmptyLatentImage` ★核心
- `easy int`
- `easy int`
- `easy int`
- `RandomNoise`
- `BasicGuider`
- `CLIPTextEncode` ★核心
- `FlowMatchEulerDiscreteScheduler (Custom)`
- `SamplerCustomAdvanced` ★核心
- `KSamplerSelect` ★核心
- `VAEDecode` ★核心
- `VAEDecode` ★核心
- `ConditioningZeroOut`
- `Image Comparer (rgthree)`
- `SaveImage`
- `SaveImage`
- `KSampler` ★核心
- `VAELoader`

**识别到的模式**：text_to_image

## 关键参数

- `width` = `2048`
- `height` = `2048`
- `batch_size` = `1`
- `seed` = `30557922910419`
- `steps` = `9`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `sgm_uniform`
- `denoise` = `1`

## 知识

覆盖率 **95%**（20/21）

**有卡**：`Seed (rgthree)`、`UNETLoader`、`CLIPLoader`、`EmptyLatentImage`、`easy int`、`RandomNoise`、`BasicGuider`、`CLIPTextEncode`、`FlowMatchEulerDiscreteScheduler (Custom)`、`SamplerCustomAdvanced`、`KSamplerSelect`、`VAEDecode`、`ConditioningZeroOut`、`SaveImage`、`KSampler`、`VAELoader`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、EmptyLatentImage、UNETLoader

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

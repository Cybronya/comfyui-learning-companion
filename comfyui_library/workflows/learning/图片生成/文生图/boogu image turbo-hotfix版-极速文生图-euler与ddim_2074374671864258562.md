---
key: 图片生成/文生图/boogu image turbo-hotfix版-极速文生图-euler与ddim_2074374671864258562.json
name: boogu image turbo-hotfix版-极速文生图-euler与ddim_2074374671864258562
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/boogu image turbo-hotfix版-极速文生图-euler与ddim_2074374671864258562.json
hash: df72f34d9f853e44
coverage: 0.944444
learned_at: 2026-10-20 00:20:31
nodes: [QwenImageEngineer, VAEDecode, easy cleanGpuUsed, PreviewAny, CLIPLoader, UNETLoader, CLIPTextEncode, ConditioningZeroOut, EmptyLatentImage, VAELoader, VAEDecode, SaveImage, easy seed, ResolutionSelector, KSampler, KSampler, SaveImage, CR Prompt Text]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "ddim", "scheduler": "beta57", "seed": 980835690271613, "steps": 4, "width": 1024}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/文生图/boogu image turbo-hotfix版-极速文生图-euler与ddim_2074374671864258562.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/boogu image turbo-hotfix版-极速文生图-euler与ddim_2074374671864258562.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（18 个）：
- `QwenImageEngineer`
- `VAEDecode` ★核心
- `easy cleanGpuUsed`
- `PreviewAny`
- `CLIPLoader`
- `UNETLoader` ★核心
- `CLIPTextEncode` ★核心
- `ConditioningZeroOut`
- `EmptyLatentImage` ★核心
- `VAELoader`
- `VAEDecode` ★核心
- `SaveImage`
- `easy seed`
- `ResolutionSelector`
- `KSampler` ★核心
- `KSampler` ★核心
- `SaveImage`
- `CR Prompt Text`

**识别到的模式**：text_to_image

## 关键参数

- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`
- `seed` = `980835690271613`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `ddim`
- `scheduler` = `beta57`
- `denoise` = `1`

## 知识

覆盖率 **94%**（17/18）

**有卡**：`QwenImageEngineer`、`VAEDecode`、`easy cleanGpuUsed`、`CLIPLoader`、`UNETLoader`、`CLIPTextEncode`、`ConditioningZeroOut`、`EmptyLatentImage`、`VAELoader`、`SaveImage`、`easy seed`、`ResolutionSelector`、`KSampler`、`CR Prompt Text`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、EmptyLatentImage、ResolutionSelector

## 参数体检

发现 2 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

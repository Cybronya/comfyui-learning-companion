---
key: 图片生成/图生图/Krea2单图风格参考Style+Reference+seedvr2超清8K放大_2074739996078206977.json
name: Krea2单图风格参考Style+Reference+seedvr2超清8K放大_2074739996078206977
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Krea2单图风格参考Style+Reference+seedvr2超清8K放大_2074739996078206977.json
hash: b5cc14e08df8f1ba
coverage: 0.944444
learned_at: 2026-10-23 11:08:10
nodes: [CLIPLoader, VAELoader, KSampler, CLIPTextEncode, ConditioningZeroOut, UNETLoader, SaveImage, Krea2StyleTransfer, CR Text, Krea2SizePreset, Krea2StyleReference, SeedVR2LoadVAEModel, SeedVR2LoadDiTModel, Note, easy int, VAEDecode, SeedVR2VideoUpscaler, LoadImage]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 241012162443833, "steps": 8}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/Krea2单图风格参考Style+Reference+seedvr2超清8K放大_2074739996078206977.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Krea2单图风格参考Style+Reference+seedvr2超清8K放大_2074739996078206977.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（18 个）：
- `CLIPLoader`
- `VAELoader`
- `KSampler` ★核心
- `CLIPTextEncode` ★核心
- `ConditioningZeroOut`
- `UNETLoader` ★核心
- `SaveImage`
- `Krea2StyleTransfer`
- `CR Text`
- `Krea2SizePreset`
- `Krea2StyleReference`
- `SeedVR2LoadVAEModel`
- `SeedVR2LoadDiTModel`
- `Note`
- `easy int`
- `VAEDecode` ★核心
- `SeedVR2VideoUpscaler`
- `LoadImage`

## 关键参数

- `seed` = `241012162443833`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **94%**（17/18）

**有卡**：`CLIPLoader`、`VAELoader`、`KSampler`、`CLIPTextEncode`、`ConditioningZeroOut`、`UNETLoader`、`SaveImage`、`Krea2StyleTransfer`、`CR Text`、`Krea2SizePreset`、`Krea2StyleReference`、`SeedVR2LoadVAEModel`、`SeedVR2LoadDiTModel`、`easy int`、`VAEDecode`、`SeedVR2VideoUpscaler`、`LoadImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、LoadImage、UNETLoader

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

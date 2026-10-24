---
key: 图片生成/图生图/Qwen-edit-2511-服装迁移（Utils 2.2）_2007382960336543746.json
name: Qwen-edit-2511-服装迁移（Utils 2.2）_2007382960336543746
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen-edit-2511-服装迁移（Utils 2.2）_2007382960336543746.json
hash: 52b1ae0a52d30011
coverage: 0.9375
learned_at: 2026-10-23 11:17:49
nodes: [UNETLoader, CLIPLoader, VAELoader, LoraLoaderModelOnly, ConditioningZeroOut, LoadImage, Mask Fill Holes, QwenEditConfigPreparer, QwenEditConfigPreparer, TextEncodeQwenImageEditPlusCustom_lrzjason, LoraLoaderModelOnly, KSampler, Image Comparer (rgthree), LoadImage, VAEDecode, SaveImage]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 998680565426703, "steps": 6}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/Qwen-edit-2511-服装迁移（Utils 2.2）_2007382960336543746.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen-edit-2511-服装迁移（Utils 2.2）_2007382960336543746.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Output → Other

**节点**（16 个）：
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `LoraLoaderModelOnly` ★核心
- `ConditioningZeroOut`
- `LoadImage`
- `Mask Fill Holes`
- `QwenEditConfigPreparer`
- `QwenEditConfigPreparer`
- `TextEncodeQwenImageEditPlusCustom_lrzjason`
- `LoraLoaderModelOnly` ★核心
- `KSampler` ★核心
- `Image Comparer (rgthree)`
- `LoadImage`
- `VAEDecode` ★核心
- `SaveImage`

## 关键参数

- `seed` = `998680565426703`
- `steps` = `6`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **94%**（15/16）

**有卡**：`UNETLoader`、`CLIPLoader`、`VAELoader`、`LoraLoaderModelOnly`、`ConditioningZeroOut`、`LoadImage`、`Mask Fill Holes`、`QwenEditConfigPreparer`、`TextEncodeQwenImageEditPlusCustom_lrzjason`、`KSampler`、`VAEDecode`、`SaveImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、ConditioningZeroOut、LoadImage、UNETLoader

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

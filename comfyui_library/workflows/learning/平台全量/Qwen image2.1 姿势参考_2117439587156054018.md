---
key: 平台全量/Qwen image2.1 姿势参考_2117439587156054018.json
name: Qwen image2.1 姿势参考_2117439587156054018
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/Qwen image2.1 姿势参考_2117439587156054018.json
hash: 21b36b8e285c2e0f
coverage: 0.9375
learned_at: 2026-11-14 00:50:47
nodes: [VAEDecode, VAELoader, CLIPLoader, EmptyLatentImage, SaveImage, LoadImage, UNETLoader, KSampler, ResolutionSelector, LoadImage, QwenEditConfigPreparer, QwenEditConfigPreparer, TextEncodeQwenImageEditPlusCustom_lrzjason, ConditioningZeroOut, DWPreprocessor, JjkText]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1920, "sampler_name": "euler", "scheduler": "simple", "seed": 449547881104339, "steps": 8, "width": 1024}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 平台全量/Qwen image2.1 姿势参考_2117439587156054018.json

> 来源文件 `comfyui_library/workflows/平台全量/Qwen image2.1 姿势参考_2117439587156054018.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（16 个）：
- `VAEDecode` ★核心
- `VAELoader`
- `CLIPLoader`
- `EmptyLatentImage` ★核心
- `SaveImage`
- `LoadImage`
- `UNETLoader` ★核心
- `KSampler` ★核心
- `ResolutionSelector`
- `LoadImage`
- `QwenEditConfigPreparer`
- `QwenEditConfigPreparer`
- `TextEncodeQwenImageEditPlusCustom_lrzjason`
- `ConditioningZeroOut`
- `DWPreprocessor`
- `JjkText`

## 关键参数

- `width` = `1024`
- `height` = `1920`
- `batch_size` = `1`
- `seed` = `449547881104339`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **94%**（15/16）

**有卡**：`VAEDecode`、`VAELoader`、`CLIPLoader`、`EmptyLatentImage`、`SaveImage`、`LoadImage`、`UNETLoader`、`KSampler`、`ResolutionSelector`、`QwenEditConfigPreparer`、`TextEncodeQwenImageEditPlusCustom_lrzjason`、`ConditioningZeroOut`、`DWPreprocessor`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPLoader、ConditioningZeroOut、EmptyLatentImage、ResolutionSelector、LoadImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

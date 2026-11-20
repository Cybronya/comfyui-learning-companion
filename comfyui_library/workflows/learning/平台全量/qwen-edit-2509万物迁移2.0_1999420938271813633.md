---
key: 平台全量/qwen-edit-2509万物迁移2.0_1999420938271813633.json
name: qwen-edit-2509万物迁移2.0_1999420938271813633
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/qwen-edit-2509万物迁移2.0_1999420938271813633.json
hash: 5bac6687be7eeea1
coverage: 0.954545
learned_at: 2026-11-14 01:16:04
nodes: [VAEDecode, VAELoader, QwenEditAdaptiveLongestEdge, CLIPLoader, QwenEditConfigPreparer, LoraLoaderModelOnly, LoraLoaderModelOnly, KSampler, LoadImage, QwenEditAdaptiveLongestEdge, UNETLoader, CR Text, QwenEditConfigPreparer, LoraLoaderModelOnly, TextEncodeQwenImageEditPlusCustom_lrzjason, ConditioningZeroOut, ImageConcanate, ImageConcanate, Image Comparer (rgthree), SaveImage, SaveImage, LoadImage]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "beta57", "seed": 1072401702498330, "steps": 8}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 平台全量/qwen-edit-2509万物迁移2.0_1999420938271813633.json

> 来源文件 `comfyui_library/workflows/平台全量/qwen-edit-2509万物迁移2.0_1999420938271813633.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（22 个）：
- `VAEDecode` ★核心
- `VAELoader`
- `QwenEditAdaptiveLongestEdge`
- `CLIPLoader`
- `QwenEditConfigPreparer`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `KSampler` ★核心
- `LoadImage`
- `QwenEditAdaptiveLongestEdge`
- `UNETLoader` ★核心
- `CR Text`
- `QwenEditConfigPreparer`
- `LoraLoaderModelOnly` ★核心
- `TextEncodeQwenImageEditPlusCustom_lrzjason`
- `ConditioningZeroOut`
- `ImageConcanate`
- `ImageConcanate`
- `Image Comparer (rgthree)`
- `SaveImage`
- `SaveImage`
- `LoadImage`

## 关键参数

- `seed` = `1072401702498330`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `beta57`
- `denoise` = `1`

## 知识

覆盖率 **95%**（21/22）

**有卡**：`VAEDecode`、`VAELoader`、`QwenEditAdaptiveLongestEdge`、`CLIPLoader`、`QwenEditConfigPreparer`、`LoraLoaderModelOnly`、`KSampler`、`LoadImage`、`UNETLoader`、`CR Text`、`TextEncodeQwenImageEditPlusCustom_lrzjason`、`ConditioningZeroOut`、`ImageConcanate`、`SaveImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、ConditioningZeroOut、LoadImage、UNETLoader

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

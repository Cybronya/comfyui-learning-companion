---
key: 平台全量/Qwen-image-2.1文生图改版 (角色资产)_2112442533413482497.json
name: Qwen-image-2.1文生图改版 (角色资产)_2112442533413482497
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/Qwen-image-2.1文生图改版 (角色资产)_2112442533413482497.json
hash: 472cca00e33d4a6a
coverage: 0.842105
learned_at: 2026-11-14 00:52:06
nodes: [MarkdownNote, Note, CLIPLoader, EmptyLatentImage, ShowText|pysssss, easy promptLine, UNETLoader, VAELoader, TextEncodeQwenImage21, ResolutionSelector, 1hew_AnySwitchSelect, easy promptLine, CR Prompt List, CR Text, KSampler, CR Prompt List, VAEDecode, SaveImage, SaveImageAdvanced]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1920, "sampler_name": "euler", "scheduler": "simple", "seed": 1003561522633901, "steps": 8, "width": 1088}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 平台全量/Qwen-image-2.1文生图改版 (角色资产)_2112442533413482497.json

> 来源文件 `comfyui_library/workflows/平台全量/Qwen-image-2.1文生图改版 (角色资产)_2112442533413482497.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（19 个）：
- `MarkdownNote`
- `Note`
- `CLIPLoader`
- `EmptyLatentImage` ★核心
- `ShowText|pysssss`
- `easy promptLine`
- `UNETLoader` ★核心
- `VAELoader`
- `TextEncodeQwenImage21`
- `ResolutionSelector`
- `1hew_AnySwitchSelect`
- `easy promptLine`
- `CR Prompt List`
- `CR Text`
- `KSampler` ★核心
- `CR Prompt List`
- `VAEDecode` ★核心
- `SaveImage`
- `SaveImageAdvanced`

## 关键参数

- `width` = `1088`
- `height` = `1920`
- `batch_size` = `1`
- `seed` = `1003561522633901`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **84%**（16/19）

**有卡**：`CLIPLoader`、`EmptyLatentImage`、`easy promptLine`、`UNETLoader`、`VAELoader`、`TextEncodeQwenImage21`、`ResolutionSelector`、`1hew_AnySwitchSelect`、`CR Prompt List`、`CR Text`、`KSampler`、`VAEDecode`、`SaveImage`、`SaveImageAdvanced`

**用到的条目**：KSampler、TextEncodeQwenImage21、VAEDecode、VAELoader、CLIPLoader、EmptyLatentImage、ResolutionSelector、UNETLoader

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

---
key: 图片生成/图生图/Qwen-edit-2511 multianglelighting重打光工作流_2011415104608276481.json
name: Qwen-edit-2511 multianglelighting重打光工作流_2011415104608276481
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen-edit-2511 multianglelighting重打光工作流_2011415104608276481.json
hash: 25ffd8d929607c32
coverage: 0.85
learned_at: 2026-10-23 11:17:43
nodes: [ModelSamplingAuraFlow, CFGNorm, VAEDecode, VAELoader, TextEncodeQwenImageEditPlus, PreviewImage, Label (rgthree), Label (rgthree), LoraLoaderModelOnly, CLIPLoader, UNETLoader, TextEncodeQwenImageEditPlusPro_lrzjason, PreviewImage, LoraLoaderModelOnly, KSampler, SynVowColorPicker, SaveImage, ShowText|pysssss, QwenMultiangleLightningNode, LoadImage]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 1111040859824588, "steps": 4}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/Qwen-edit-2511 multianglelighting重打光工作流_2011415104608276481.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen-edit-2511 multianglelighting重打光工作流_2011415104608276481.json`

## 结构

**生成流程**：Model → Sampling → Decode → Output → Other

**节点**（20 个）：
- `ModelSamplingAuraFlow`
- `CFGNorm`
- `VAEDecode` ★核心
- `VAELoader`
- `TextEncodeQwenImageEditPlus`
- `PreviewImage`
- `Label (rgthree)`
- `Label (rgthree)`
- `LoraLoaderModelOnly` ★核心
- `CLIPLoader`
- `UNETLoader` ★核心
- `TextEncodeQwenImageEditPlusPro_lrzjason`
- `PreviewImage`
- `LoraLoaderModelOnly` ★核心
- `KSampler` ★核心
- `SynVowColorPicker`
- `SaveImage`
- `ShowText|pysssss`
- `QwenMultiangleLightningNode`
- `LoadImage`

## 关键参数

- `seed` = `1111040859824588`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **85%**（17/20）

**有卡**：`ModelSamplingAuraFlow`、`CFGNorm`、`VAEDecode`、`VAELoader`、`TextEncodeQwenImageEditPlus`、`Label (rgthree)`、`LoraLoaderModelOnly`、`CLIPLoader`、`UNETLoader`、`TextEncodeQwenImageEditPlusPro_lrzjason`、`KSampler`、`SynVowColorPicker`、`SaveImage`、`QwenMultiangleLightningNode`、`LoadImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、LoadImage、UNETLoader、CFGNorm

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

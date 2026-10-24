---
key: 图片生成/图生图/Storyboards + Automatic Storyboa分镜+自动分镜++短剧分镜+漫剧分镜_2110526506236735489.json
name: Storyboards + Automatic Storyboa分镜+自动分镜++短剧分镜+漫剧分镜_2110526506236735489
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Storyboards + Automatic Storyboa分镜+自动分镜++短剧分镜+漫剧分镜_2110526506236735489.json
hash: 8d4a1f422bb427be
coverage: 0.95
learned_at: 2026-10-23 11:26:16
nodes: [LoraLoaderModelOnly, ProcessString, JDCN_StringToList, RH_LLMAPI_NODE, CLIPLoader, VAELoader, TextEncodeQwenImageEditPlusAdvance_lrzjason, TextEncodeQwenImageEditPlus, CFGNorm, ModelSamplingAuraFlow, UNETLoader, LoraLoaderModelOnly, CR Text, KSampler, SaveImage, CR Text, VAEDecode, SaveImage, LoadImage, PreviewImage]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "er_sde", "scheduler": "FlowMatchEulerDiscreteScheduler", "seed": 367134607577785, "steps": 6}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/Storyboards + Automatic Storyboa分镜+自动分镜++短剧分镜+漫剧分镜_2110526506236735489.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Storyboards + Automatic Storyboa分镜+自动分镜++短剧分镜+漫剧分镜_2110526506236735489.json`

## 结构

**生成流程**：Model → Sampling → Decode → Output → Other

**节点**（20 个）：
- `LoraLoaderModelOnly` ★核心
- `ProcessString`
- `JDCN_StringToList`
- `RH_LLMAPI_NODE`
- `CLIPLoader`
- `VAELoader`
- `TextEncodeQwenImageEditPlusAdvance_lrzjason`
- `TextEncodeQwenImageEditPlus`
- `CFGNorm`
- `ModelSamplingAuraFlow`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `CR Text`
- `KSampler` ★核心
- `SaveImage`
- `CR Text`
- `VAEDecode` ★核心
- `SaveImage`
- `LoadImage`
- `PreviewImage`

## 关键参数

- `seed` = `367134607577785`
- `steps` = `6`
- `cfg` = `1`
- `sampler_name` = `er_sde`
- `scheduler` = `FlowMatchEulerDiscreteScheduler`
- `denoise` = `1`

## 知识

覆盖率 **95%**（19/20）

**有卡**：`LoraLoaderModelOnly`、`ProcessString`、`JDCN_StringToList`、`RH_LLMAPI_NODE`、`CLIPLoader`、`VAELoader`、`TextEncodeQwenImageEditPlusAdvance_lrzjason`、`TextEncodeQwenImageEditPlus`、`CFGNorm`、`ModelSamplingAuraFlow`、`UNETLoader`、`CR Text`、`KSampler`、`SaveImage`、`VAEDecode`、`LoadImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、LoadImage、UNETLoader、CFGNorm

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

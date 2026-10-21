---
key: 图片生成/图生图/分镜+自动分镜++短剧分镜+漫剧分镜Storyboards + Automatic Storyboa_2107993998911692802.json
name: 分镜+自动分镜++短剧分镜+漫剧分镜Storyboards + Automatic Storyboa_2107993998911692802
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/分镜+自动分镜++短剧分镜+漫剧分镜Storyboards + Automatic Storyboa_2107993998911692802.json
hash: d8d169d206fe6499
coverage: 0.95
learned_at: 2026-10-21 00:49:43
nodes: [LoraLoaderModelOnly, ProcessString, JDCN_StringToList, RH_LLMAPI_NODE, CLIPLoader, VAELoader, TextEncodeQwenImageEditPlusAdvance_lrzjason, TextEncodeQwenImageEditPlus, CFGNorm, ModelSamplingAuraFlow, UNETLoader, LoraLoaderModelOnly, CR Text, CR Text, KSampler, SaveImage, PreviewImage, LoadImage, VAEDecode, SaveImage]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "er_sde", "scheduler": "FlowMatchEulerDiscreteScheduler", "seed": 956470586670291, "steps": 6}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/分镜+自动分镜++短剧分镜+漫剧分镜Storyboards + Automatic Storyboa_2107993998911692802.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/分镜+自动分镜++短剧分镜+漫剧分镜Storyboards + Automatic Storyboa_2107993998911692802.json`

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
- `CR Text`
- `KSampler` ★核心
- `SaveImage`
- `PreviewImage`
- `LoadImage`
- `VAEDecode` ★核心
- `SaveImage`

## 关键参数

- `seed` = `956470586670291`
- `steps` = `6`
- `cfg` = `1`
- `sampler_name` = `er_sde`
- `scheduler` = `FlowMatchEulerDiscreteScheduler`
- `denoise` = `1`

## 知识

覆盖率 **95%**（19/20）

**有卡**：`LoraLoaderModelOnly`、`ProcessString`、`JDCN_StringToList`、`RH_LLMAPI_NODE`、`CLIPLoader`、`VAELoader`、`TextEncodeQwenImageEditPlusAdvance_lrzjason`、`TextEncodeQwenImageEditPlus`、`CFGNorm`、`ModelSamplingAuraFlow`、`UNETLoader`、`CR Text`、`KSampler`、`SaveImage`、`LoadImage`、`VAEDecode`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、LoadImage、UNETLoader、CFGNorm

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

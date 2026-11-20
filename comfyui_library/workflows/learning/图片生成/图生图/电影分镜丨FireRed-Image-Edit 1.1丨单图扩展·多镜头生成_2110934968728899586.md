---
key: 图片生成/图生图/电影分镜丨FireRed-Image-Edit 1.1丨单图扩展·多镜头生成_2110934968728899586.json
name: 电影分镜丨FireRed-Image-Edit 1.1丨单图扩展·多镜头生成_2110934968728899586
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/电影分镜丨FireRed-Image-Edit 1.1丨单图扩展·多镜头生成_2110934968728899586.json
hash: 87dd51d44c41f943
coverage: 0.809524
learned_at: 2026-11-02 19:14:49
nodes: [CLIPLoader, VAELoader, UNETLoader, LoadImage, PrimitiveStringMultiline, PrimitiveStringMultiline, PrimitiveStringMultiline, ModelSamplingAuraFlow, TextEncodeQwenImageEditPlus, RH_LLMAPI_NODE, LoraLoaderModelOnly, ComfySwitchNode, LoraLoaderModelOnly, ProcessString, CFGNorm, JDCN_StringToList, TextEncodeQwenImageEditPlusAdvance_lrzjason, KSampler, VAEDecode, CropWithPadInfo, SaveImage]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "er_sde", "scheduler": "FlowMatchEulerDiscreteScheduler", "seed": 472203483989029, "steps": 6}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/电影分镜丨FireRed-Image-Edit 1.1丨单图扩展·多镜头生成_2110934968728899586.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/电影分镜丨FireRed-Image-Edit 1.1丨单图扩展·多镜头生成_2110934968728899586.json`

## 结构

**生成流程**：Model → Sampling → Decode → Output → Other

**节点**（21 个）：
- `CLIPLoader`
- `VAELoader`
- `UNETLoader` ★核心
- `LoadImage`
- `PrimitiveStringMultiline`
- `PrimitiveStringMultiline`
- `PrimitiveStringMultiline`
- `ModelSamplingAuraFlow`
- `TextEncodeQwenImageEditPlus`
- `RH_LLMAPI_NODE`
- `LoraLoaderModelOnly` ★核心
- `ComfySwitchNode`
- `LoraLoaderModelOnly` ★核心
- `ProcessString`
- `CFGNorm`
- `JDCN_StringToList`
- `TextEncodeQwenImageEditPlusAdvance_lrzjason`
- `KSampler` ★核心
- `VAEDecode` ★核心
- `CropWithPadInfo`
- `SaveImage`

## 关键参数

- `seed` = `472203483989029`
- `steps` = `6`
- `cfg` = `1`
- `sampler_name` = `er_sde`
- `scheduler` = `FlowMatchEulerDiscreteScheduler`
- `denoise` = `1`

## 知识

覆盖率 **81%**（17/21）

**有卡**：`CLIPLoader`、`VAELoader`、`UNETLoader`、`LoadImage`、`ModelSamplingAuraFlow`、`TextEncodeQwenImageEditPlus`、`RH_LLMAPI_NODE`、`LoraLoaderModelOnly`、`ProcessString`、`CFGNorm`、`JDCN_StringToList`、`TextEncodeQwenImageEditPlusAdvance_lrzjason`、`KSampler`、`VAEDecode`、`CropWithPadInfo`、`SaveImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、LoadImage、UNETLoader、CFGNorm

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

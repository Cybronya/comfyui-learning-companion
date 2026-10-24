---
key: 图片生成/图生图/Chromoed_comfyUI_native 英伟达图像编辑_1987385808426569730.json
name: Chromoed_comfyUI_native 英伟达图像编辑_1987385808426569730
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Chromoed_comfyUI_native 英伟达图像编辑_1987385808426569730.json
hash: 21c64b2c99425d13
coverage: 0.458333
learned_at: 2026-10-23 10:51:56
nodes: [GetNode, GetNode, GetNode, GetNode, GetNode, VAEDecode, SaveImage, GetImageRangeFromBatch, LoraLoaderModelOnly, wanBlockSwap, ModelSamplingSD3, SetNode, CLIPLoader, SetNode, VAELoader, SetNode, CLIPVisionLoader, SetNode, SetNode, SetNode, SetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, SetNode, SetNode, SetNode, ConditioningZeroOut, GetNode, SetNode, SetNode, VHS_VideoCombine, WanImageToVideo, CLIPVisionEncode, GetNode, UNETLoader, INTConstant, INTConstant, CLIPTextEncode, ImageResizeKJv2, INTConstant, PreviewAny, KSampler, LoadImage, AILab_QwenVL]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 42, "steps": 8}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/Chromoed_comfyUI_native 英伟达图像编辑_1987385808426569730.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Chromoed_comfyUI_native 英伟达图像编辑_1987385808426569730.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（48 个）：
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `VAEDecode` ★核心
- `SaveImage`
- `GetImageRangeFromBatch`
- `LoraLoaderModelOnly` ★核心
- `wanBlockSwap`
- `ModelSamplingSD3`
- `SetNode`
- `CLIPLoader`
- `SetNode`
- `VAELoader`
- `SetNode`
- `CLIPVisionLoader`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `ConditioningZeroOut`
- `GetNode`
- `SetNode`
- `SetNode`
- `VHS_VideoCombine`
- `WanImageToVideo`
- `CLIPVisionEncode`
- `GetNode`
- `UNETLoader` ★核心
- `INTConstant`
- `INTConstant`
- `CLIPTextEncode` ★核心
- `ImageResizeKJv2`
- `INTConstant`
- `PreviewAny`
- `KSampler` ★核心
- `LoadImage`
- `AILab_QwenVL`

## 关键参数

- `seed` = `42`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **46%**（22/48）

**有卡**：`VAEDecode`、`SaveImage`、`GetImageRangeFromBatch`、`LoraLoaderModelOnly`、`wanBlockSwap`、`ModelSamplingSD3`、`CLIPLoader`、`VAELoader`、`CLIPVisionLoader`、`ConditioningZeroOut`、`VHS_VideoCombine`、`WanImageToVideo`、`CLIPVisionEncode`、`UNETLoader`、`INTConstant`、`CLIPTextEncode`、`ImageResizeKJv2`、`KSampler`、`LoadImage`、`AILab_QwenVL`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、LoadImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

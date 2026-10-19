---
key: 图片生成/文生图/影视分镜批量生成Qwen-Edit-AIO+Next+Scene_1998418153245958146.json
name: 影视分镜批量生成Qwen-Edit-AIO+Next+Scene_1998418153245958146
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/影视分镜批量生成Qwen-Edit-AIO+Next+Scene_1998418153245958146.json
hash: c3a0dd3e7b5150bb
coverage: 0.517241
learned_at: 2026-10-19 21:47:42
nodes: [CheckpointLoaderSimple, CLIPLoader, VAELoader, SetNode, SetNode, GetNode, GetNode, GetNode, GetNode, ConditioningZeroOut, VAEDecode, GetNode, TextEncodeQwenImageEditPlusAdvance_lrzjason, SetNode, KSampler, SaveImage, Text, ProcessString, PreviewAny, ImageResizeKJv2, SetNode, SetNode, easy promptLine, PreviewImage, Note, Note, LoadImage, LoraLoaderModelOnly, LoraLoaderModelOnly]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "checkpoint": "Qwen-Rapid-AIO-NSFW-v5.3.safetensors", "denoise": 1, "sampler_name": "sa_solver", "scheduler": "beta", "seed": 861502171244519, "steps": 4}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/文生图/影视分镜批量生成Qwen-Edit-AIO+Next+Scene_1998418153245958146.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/影视分镜批量生成Qwen-Edit-AIO+Next+Scene_1998418153245958146.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（29 个）：
- `CheckpointLoaderSimple` ★核心
- `CLIPLoader`
- `VAELoader`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `ConditioningZeroOut`
- `VAEDecode` ★核心
- `GetNode`
- `TextEncodeQwenImageEditPlusAdvance_lrzjason`
- `SetNode`
- `KSampler` ★核心
- `SaveImage`
- `Text`
- `ProcessString`
- `PreviewAny`
- `ImageResizeKJv2`
- `SetNode`
- `SetNode`
- `easy promptLine`
- `PreviewImage`
- `Note`
- `Note`
- `LoadImage`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心

## 关键参数

- `checkpoint` = `Qwen-Rapid-AIO-NSFW-v5.3.safetensors`
- `seed` = `861502171244519`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `sa_solver`
- `scheduler` = `beta`
- `denoise` = `1`

## 知识

覆盖率 **52%**（15/29）

**有卡**：`CheckpointLoaderSimple`、`CLIPLoader`、`VAELoader`、`ConditioningZeroOut`、`VAEDecode`、`TextEncodeQwenImageEditPlusAdvance_lrzjason`、`KSampler`、`SaveImage`、`Text`、`ProcessString`、`ImageResizeKJv2`、`easy promptLine`、`LoadImage`、`LoraLoaderModelOnly`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CheckpointLoaderSimple、CLIPLoader、ConditioningZeroOut、LoadImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

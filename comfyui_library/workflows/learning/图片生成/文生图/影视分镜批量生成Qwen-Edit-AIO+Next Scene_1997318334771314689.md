---
key: 图片生成/文生图/影视分镜批量生成Qwen-Edit-AIO+Next Scene_1997318334771314689.json
name: 影视分镜批量生成Qwen-Edit-AIO+Next Scene_1997318334771314689
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/影视分镜批量生成Qwen-Edit-AIO+Next Scene_1997318334771314689.json
hash: acfff53e9985dd90
coverage: 0.517241
learned_at: 2026-10-19 21:47:42
nodes: [ConditioningZeroOut, SetNode, SetNode, GetNode, GetNode, GetNode, GetNode, GetNode, KSampler, TextEncodeQwenImageEditPlusAdvance_lrzjason, ImageResizeKJv2, CLIPLoader, VAELoader, LoraLoaderModelOnly, CheckpointLoaderSimple, SetNode, LoraLoaderModelOnly, SetNode, SetNode, easy promptLine, PreviewAny, ProcessString, VAEDecode, SaveImage, Note, Note, PreviewImage, LoadImage, Text]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "checkpoint": "Qwen-Rapid-AIO-NSFW-v5.3.safetensors", "denoise": 1, "sampler_name": "sa_solver", "scheduler": "beta", "seed": 311617839626938, "steps": 4}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/文生图/影视分镜批量生成Qwen-Edit-AIO+Next Scene_1997318334771314689.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/影视分镜批量生成Qwen-Edit-AIO+Next Scene_1997318334771314689.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（29 个）：
- `ConditioningZeroOut`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `KSampler` ★核心
- `TextEncodeQwenImageEditPlusAdvance_lrzjason`
- `ImageResizeKJv2`
- `CLIPLoader`
- `VAELoader`
- `LoraLoaderModelOnly` ★核心
- `CheckpointLoaderSimple` ★核心
- `SetNode`
- `LoraLoaderModelOnly` ★核心
- `SetNode`
- `SetNode`
- `easy promptLine`
- `PreviewAny`
- `ProcessString`
- `VAEDecode` ★核心
- `SaveImage`
- `Note`
- `Note`
- `PreviewImage`
- `LoadImage`
- `Text`

## 关键参数

- `seed` = `311617839626938`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `sa_solver`
- `scheduler` = `beta`
- `denoise` = `1`
- `checkpoint` = `Qwen-Rapid-AIO-NSFW-v5.3.safetensors`

## 知识

覆盖率 **52%**（15/29）

**有卡**：`ConditioningZeroOut`、`KSampler`、`TextEncodeQwenImageEditPlusAdvance_lrzjason`、`ImageResizeKJv2`、`CLIPLoader`、`VAELoader`、`LoraLoaderModelOnly`、`CheckpointLoaderSimple`、`easy promptLine`、`ProcessString`、`VAEDecode`、`SaveImage`、`LoadImage`、`Text`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CheckpointLoaderSimple、CLIPLoader、ConditioningZeroOut、LoadImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

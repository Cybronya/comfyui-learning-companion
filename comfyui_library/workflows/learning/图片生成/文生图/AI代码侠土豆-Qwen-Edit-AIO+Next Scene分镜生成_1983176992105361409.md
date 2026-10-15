---
key: 图片生成/文生图/AI代码侠土豆-Qwen-Edit-AIO+Next Scene分镜生成_1983176992105361409.json
name: AI代码侠土豆-Qwen-Edit-AIO+Next Scene分镜生成_1983176992105361409
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/AI代码侠土豆-Qwen-Edit-AIO+Next Scene分镜生成_1983176992105361409.json
hash: 46be6772095eb4fc
coverage: 0.518519
learned_at: 2026-10-10 21:25:59
nodes: [ConditioningZeroOut, SetNode, SetNode, GetNode, GetNode, GetNode, GetNode, GetNode, KSampler, TextEncodeQwenImageEditPlusAdvance_lrzjason, ImageResizeKJv2, CLIPLoader, VAELoader, LoraLoaderModelOnly, CheckpointLoaderSimple, SetNode, LoraLoaderModelOnly, SetNode, SetNode, easy promptLine, PreviewAny, Text, ProcessString, PreviewImage, LoadImage, VAEDecode, SaveImage]
patterns: []
missing: [easy promptLine]
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "checkpoint": "Qwen-Rapid-AIO-NSFW-v5.3.safetensors", "denoise": 1, "sampler_name": "sa_solver", "scheduler": "beta", "seed": 375178709195536, "steps": 4}
discoveries: [次要节点 `easy promptLine` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/文生图/AI代码侠土豆-Qwen-Edit-AIO+Next Scene分镜生成_1983176992105361409.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/AI代码侠土豆-Qwen-Edit-AIO+Next Scene分镜生成_1983176992105361409.json`

## 结构

**节点**（27 个）：
- `ConditioningZeroOut`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `KSampler`
- `TextEncodeQwenImageEditPlusAdvance_lrzjason`
- `ImageResizeKJv2`
- `CLIPLoader`
- `VAELoader`
- `LoraLoaderModelOnly`
- `CheckpointLoaderSimple`
- `SetNode`
- `LoraLoaderModelOnly`
- `SetNode`
- `SetNode`
- `easy promptLine`
- `PreviewAny`
- `Text`
- `ProcessString`
- `PreviewImage`
- `LoadImage`
- `VAEDecode`
- `SaveImage`

## 关键参数

- `cfg` = `1`
- `checkpoint` = `Qwen-Rapid-AIO-NSFW-v5.3.safetensors`
- `denoise` = `1`
- `sampler_name` = `sa_solver`
- `scheduler` = `beta`
- `seed` = `375178709195536`
- `steps` = `4`

## 知识

覆盖率 **52%**（14/27）

**有卡**：`ConditioningZeroOut`、`SetNode`、`GetNode`、`KSampler`、`TextEncodeQwenImageEditPlusAdvance_lrzjason`、`ImageResizeKJv2`、`CLIPLoader`、`VAELoader`、`LoraLoaderModelOnly`

**缺卡**（1）：`easy promptLine`

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- 次要节点 `easy promptLine` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

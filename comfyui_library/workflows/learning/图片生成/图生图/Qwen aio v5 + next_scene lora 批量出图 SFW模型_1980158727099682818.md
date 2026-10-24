---
key: 图片生成/图生图/Qwen aio v5 + next_scene lora 批量出图 SFW模型_1980158727099682818.json
name: Qwen aio v5 + next_scene lora 批量出图 SFW模型_1980158727099682818
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen aio v5 + next_scene lora 批量出图 SFW模型_1980158727099682818.json
hash: a21eab3f810ce20e
coverage: 0.439024
learned_at: 2026-10-23 11:13:43
nodes: [SetNode, GetNode, GetNode, GetNode, GetNode, GetNode, Evaluate Strings, CR String To Number, SetNode, VAEDecode, ImpactStringSelector, SetNode, PrimitiveStringMultiline, SetNode, LoadImage, EmptyLatentImage, SetNode, Reroute, GetNode, SetNode, GetNode, LayerUtility: ImageScaleByAspectRatio V2, easy batchAnything, GetNode, GetNode, easy ifElse, TextEncodeQwenImageEditPlus, TextEncodeQwenImageEditPlus, easy forLoopEnd, easy forLoopStart, SetNode, easy int, easy boolean, SaveImage, Note, SetNode, PrimitiveStringMultiline, KSampler, CheckpointLoaderSimple, Note, LoraLoaderModelOnly]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 1, "checkpoint": "Qwen-Rapid-AIO-SFW-v5.safetensors", "denoise": 1, "height": 1920, "sampler_name": "lcm", "scheduler": "beta", "seed": 65454653, "steps": 4, "width": 1080}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/Qwen aio v5 + next_scene lora 批量出图 SFW模型_1980158727099682818.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen aio v5 + next_scene lora 批量出图 SFW模型_1980158727099682818.json`

## 结构

**生成流程**：Model → Latent → Sampling → Decode → Process → Output → Other

**节点**（41 个）：
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `Evaluate Strings`
- `CR String To Number`
- `SetNode`
- `VAEDecode` ★核心
- `ImpactStringSelector`
- `SetNode`
- `PrimitiveStringMultiline`
- `SetNode`
- `LoadImage`
- `EmptyLatentImage` ★核心
- `SetNode`
- `Reroute`
- `GetNode`
- `SetNode`
- `GetNode`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `easy batchAnything`
- `GetNode`
- `GetNode`
- `easy ifElse`
- `TextEncodeQwenImageEditPlus`
- `TextEncodeQwenImageEditPlus`
- `easy forLoopEnd`
- `easy forLoopStart`
- `SetNode`
- `easy int`
- `easy boolean`
- `SaveImage`
- `Note`
- `SetNode`
- `PrimitiveStringMultiline`
- `KSampler` ★核心
- `CheckpointLoaderSimple` ★核心
- `Note`
- `LoraLoaderModelOnly` ★核心

## 关键参数

- `width` = `1080`
- `height` = `1920`
- `batch_size` = `1`
- `seed` = `65454653`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `lcm`
- `scheduler` = `beta`
- `denoise` = `1`
- `checkpoint` = `Qwen-Rapid-AIO-SFW-v5.safetensors`

## 知识

覆盖率 **44%**（18/41）

**有卡**：`Evaluate Strings`、`CR String To Number`、`VAEDecode`、`ImpactStringSelector`、`LoadImage`、`EmptyLatentImage`、`LayerUtility: ImageScaleByAspectRatio V2`、`easy batchAnything`、`TextEncodeQwenImageEditPlus`、`easy forLoopEnd`、`easy forLoopStart`、`easy int`、`easy boolean`、`SaveImage`、`KSampler`、`CheckpointLoaderSimple`、`LoraLoaderModelOnly`

**用到的条目**：KSampler、VAEDecode、LoraLoaderModelOnly、CheckpointLoaderSimple、EmptyLatentImage、LoadImage、TextEncodeQwenImageEditPlus、SaveImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

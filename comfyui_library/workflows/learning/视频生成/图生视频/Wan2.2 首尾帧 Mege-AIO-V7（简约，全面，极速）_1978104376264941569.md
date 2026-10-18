---
key: 视频生成/图生视频/Wan2.2 首尾帧 Mege-AIO-V7（简约，全面，极速）_1978104376264941569.json
name: Wan2.2 首尾帧 Mege-AIO-V7（简约，全面，极速）_1978104376264941569.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/Wan2.2 首尾帧 Mege-AIO-V7（简约，全面，极速）_1978104376264941569.json
hash: 9accf70663f95ec8
coverage: 0.633333
learned_at: 2026-10-15 22:32:17
nodes: [LoadImage, Int, SetNode, SetNode, easy textSwitch, SetNode, GetNode, GetNode, KSampler, GetNode, SimpleMath+, CheckpointLoaderSimple, LoadImage, Int, Note, Int, Primitive integer [Crystools], PreviewImage, ImageConcatMulti, Anything Everywhere3, CLIPTextEncode, CLIPTextEncode, WanVaceToVideo, ModelSamplingSD3, WanVideoVACEStartToEndFrame, VAEDecode, VHS_VideoCombine, RH_LLMAPI_NODE, PrimitiveStringMultiline, easy showAnything]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "checkpoint": "wan2.2-rapid-mega-aio-v7-nsfw.safetensors", "denoise": 1, "sampler_name": "euler_ancestral", "scheduler": "beta", "seed": 1005823297156039, "steps": 4}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/图生视频/Wan2.2 首尾帧 Mege-AIO-V7（简约，全面，极速）_1978104376264941569.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1978104376264941569.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（30 个）：
- `LoadImage`
- `Int`
- `SetNode`
- `SetNode`
- `easy textSwitch`
- `SetNode`
- `GetNode`
- `GetNode`
- `KSampler` ★核心
- `GetNode`
- `SimpleMath+`
- `CheckpointLoaderSimple` ★核心
- `LoadImage`
- `Int`
- `Note`
- `Int`
- `Primitive integer [Crystools]`
- `PreviewImage`
- `ImageConcatMulti`
- `Anything Everywhere3`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `WanVaceToVideo`
- `ModelSamplingSD3`
- `WanVideoVACEStartToEndFrame`
- `VAEDecode` ★核心
- `VHS_VideoCombine`
- `RH_LLMAPI_NODE`
- `PrimitiveStringMultiline`
- `easy showAnything`

## 关键参数

- `seed` = `1005823297156039`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `euler_ancestral`
- `scheduler` = `beta`
- `denoise` = `1`
- `checkpoint` = `wan2.2-rapid-mega-aio-v7-nsfw.safetensors`

## 知识

覆盖率 **63%**（19/30）

**有卡**：`LoadImage`、`Int`、`easy textSwitch`、`KSampler`、`SimpleMath+`、`CheckpointLoaderSimple`、`Primitive integer [Crystools]`、`ImageConcatMulti`、`CLIPTextEncode`、`WanVaceToVideo`、`ModelSamplingSD3`、`WanVideoVACEStartToEndFrame`、`VAEDecode`、`VHS_VideoCombine`、`RH_LLMAPI_NODE`

**用到的条目**：KSampler、VAEDecode、CheckpointLoaderSimple、CLIPTextEncode、LoadImage、ImageConcatMulti、Int、ModelSamplingSD3

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

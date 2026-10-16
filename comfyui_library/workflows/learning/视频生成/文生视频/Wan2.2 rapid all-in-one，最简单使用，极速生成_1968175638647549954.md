---
key: 视频生成/文生视频/Wan2.2 rapid all-in-one，最简单使用，极速生成_1968175638647549954.json
name: Wan2.2 rapid all-in-one，最简单使用，极速生成_1968175638647549954.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/1968175638647549954.json
hash: 0bec7c9c8ce50725
coverage: 0.456522
learned_at: 2026-10-15 22:43:45
nodes: [LoadImage, WanVideoVACEStartToEndFrame, LoadImage, easy int, easy int, easy int, easy int, SetNode, SetNode, SetNode, KSampler, SetNode, VHS_VideoCombine, GetNode, GetNode, INTConstant, SimpleMath+, ModelSamplingSD3, WanVaceToVideo, SetNode, Text Multiline, SetNode, VAEDecode, SetNode, GetNode, GetNode, SetNode, SetNode, Note, SetNode, SetNode, easy float, GetNode, GetNode, GetNode, CLIPTextEncode, CLIPTextEncode, GetNode, GetNode, GetNode, Fast Groups Bypasser (rgthree), Text Multiline, CheckpointLoaderSimple, GetNode, GetNode, CM_IntToFloat]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "checkpoint": "wan2.2-rapid-mega-aio-v1.safetensors", "denoise": 1, "sampler_name": "ipndm", "scheduler": "sgm_uniform", "seed": 7567358653673, "steps": 4}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/文生视频/Wan2.2 rapid all-in-one，最简单使用，极速生成_1968175638647549954.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/1968175638647549954.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Other

**节点**（46 个）：
- `LoadImage`
- `WanVideoVACEStartToEndFrame`
- `LoadImage`
- `easy int`
- `easy int`
- `easy int`
- `easy int`
- `SetNode`
- `SetNode`
- `SetNode`
- `KSampler` ★核心
- `SetNode`
- `VHS_VideoCombine`
- `GetNode`
- `GetNode`
- `INTConstant`
- `SimpleMath+`
- `ModelSamplingSD3`
- `WanVaceToVideo`
- `SetNode`
- `Text Multiline`
- `SetNode`
- `VAEDecode` ★核心
- `SetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `Note`
- `SetNode`
- `SetNode`
- `easy float`
- `GetNode`
- `GetNode`
- `GetNode`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `GetNode`
- `GetNode`
- `GetNode`
- `Fast Groups Bypasser (rgthree)`
- `Text Multiline`
- `CheckpointLoaderSimple` ★核心
- `GetNode`
- `GetNode`
- `CM_IntToFloat`

## 关键参数

- `seed` = `7567358653673`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `ipndm`
- `scheduler` = `sgm_uniform`
- `denoise` = `1`
- `checkpoint` = `wan2.2-rapid-mega-aio-v1.safetensors`

## 知识

覆盖率 **46%**（21/46）

**有卡**：`LoadImage`、`WanVideoVACEStartToEndFrame`、`easy int`、`KSampler`、`VHS_VideoCombine`、`INTConstant`、`SimpleMath+`、`ModelSamplingSD3`、`WanVaceToVideo`、`Text Multiline`、`VAEDecode`、`easy float`、`CLIPTextEncode`、`CheckpointLoaderSimple`、`CM_IntToFloat`

**用到的条目**：KSampler、VAEDecode、CheckpointLoaderSimple、CLIPTextEncode、LoadImage、CM_IntToFloat、INTConstant、ModelSamplingSD3

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

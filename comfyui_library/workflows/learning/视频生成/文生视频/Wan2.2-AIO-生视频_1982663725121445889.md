---
key: 视频生成/文生视频/Wan2.2-AIO-生视频_1982663725121445889.json
name: Wan2.2-AIO-生视频_1982663725121445889
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/Wan2.2-AIO-生视频_1982663725121445889.json
hash: 3e1fddb3d8c87064
coverage: 0.468085
learned_at: 2026-10-15 22:47:12
nodes: [SetNode, SetNode, SetNode, GetNode, GetNode, INTConstant, SimpleMath+, SetNode, SetNode, GetNode, SetNode, GetNode, CLIPTextEncode, GetNode, easy convertAnything, GetNode, SetNode, SetNode, easy int, easy int, easy int, easy int, LoadImage, LoadImage, VHS_VideoCombine, SetNode, Text Multiline, WanVideoVACEStartToEndFrame, GetNode, GetNode, SetNode, GetNode, GetNode, GetNode, ModelSamplingSD3, VAEDecode, Evaluate Strings, SimpleMath+, SetNode, CLIPTextEncode, GetNode, WanVaceToVideo, KSampler, easy showAnything, Fast Groups Bypasser (rgthree), Text Multiline, CheckpointLoaderSimple]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "checkpoint": "wan2.2-rapid-mega-aio-nsfw-v11.safetensors", "denoise": 1, "sampler_name": "sa_solver", "scheduler": "beta", "seed": 7567358653673, "steps": 4}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/文生视频/Wan2.2-AIO-生视频_1982663725121445889.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/Wan2.2-AIO-生视频_1982663725121445889.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Other

**节点**（47 个）：
- `SetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `INTConstant`
- `SimpleMath+`
- `SetNode`
- `SetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `CLIPTextEncode` ★核心
- `GetNode`
- `easy convertAnything`
- `GetNode`
- `SetNode`
- `SetNode`
- `easy int`
- `easy int`
- `easy int`
- `easy int`
- `LoadImage`
- `LoadImage`
- `VHS_VideoCombine`
- `SetNode`
- `Text Multiline`
- `WanVideoVACEStartToEndFrame`
- `GetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `ModelSamplingSD3`
- `VAEDecode` ★核心
- `Evaluate Strings`
- `SimpleMath+`
- `SetNode`
- `CLIPTextEncode` ★核心
- `GetNode`
- `WanVaceToVideo`
- `KSampler` ★核心
- `easy showAnything`
- `Fast Groups Bypasser (rgthree)`
- `Text Multiline`
- `CheckpointLoaderSimple` ★核心

## 关键参数

- `seed` = `7567358653673`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `sa_solver`
- `scheduler` = `beta`
- `denoise` = `1`
- `checkpoint` = `wan2.2-rapid-mega-aio-nsfw-v11.safetensors`

## 知识

覆盖率 **47%**（22/47）

**有卡**：`INTConstant`、`SimpleMath+`、`CLIPTextEncode`、`easy convertAnything`、`easy int`、`LoadImage`、`VHS_VideoCombine`、`Text Multiline`、`WanVideoVACEStartToEndFrame`、`ModelSamplingSD3`、`VAEDecode`、`Evaluate Strings`、`WanVaceToVideo`、`KSampler`、`CheckpointLoaderSimple`

**用到的条目**：KSampler、VAEDecode、CheckpointLoaderSimple、CLIPTextEncode、LoadImage、INTConstant、ModelSamplingSD3、VHS_VideoCombine

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

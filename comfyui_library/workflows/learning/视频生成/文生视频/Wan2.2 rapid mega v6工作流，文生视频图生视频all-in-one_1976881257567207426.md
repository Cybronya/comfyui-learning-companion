---
key: 视频生成/文生视频/Wan2.2 rapid mega v6工作流，文生视频图生视频all-in-one_1976881257567207426.json
name: Wan2.2 rapid mega v6工作流，文生视频图生视频all-in-one_1976881257567207426
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/Wan2.2 rapid mega v6工作流，文生视频图生视频all-in-one_1976881257567207426.json
hash: dad5bdec0a0a5f07
coverage: 0.25
learned_at: 2026-10-10 23:07:00
nodes: [SetNode, SetNode, SetNode, SetNode, GetNode, GetNode, INTConstant, SimpleMath+, ModelSamplingSD3, WanVaceToVideo, SetNode, SetNode, VAEDecode, SetNode, GetNode, GetNode, SetNode, GetNode, GetNode, GetNode, CLIPTextEncode, CLIPTextEncode, GetNode, GetNode, GetNode, GetNode, easy convertAnything, GetNode, WanVideoVACEStartToEndFrame, easy showAnything, SimpleMath+, SetNode, SetNode, SetNode, VHS_VideoCombine, easy int, easy int, easy int, Text Multiline, easy int, easy showAnything, LoadImage, LoadImage, Evaluate Strings, KSampler, CheckpointLoaderSimple, Fast Groups Bypasser (rgthree), Text Multiline]
patterns: []
missing: [Evaluate Strings, SimpleMath+, SimpleMath+, Text Multiline, Text Multiline, easy convertAnything, easy int, easy int, easy int, easy int]
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "checkpoint": "wan2.2-rapid-mega-aio-nsfw-v6.safetensors", "denoise": 1, "sampler_name": "sa_solver", "scheduler": "beta", "seed": 7567358653673, "steps": 4}
discoveries: [次要节点 `Evaluate Strings` 知识库中没有该节点类型的任何知识, 次要节点 `SimpleMath+` 知识库中没有该节点类型的任何知识, 次要节点 `SimpleMath+` 知识库中没有该节点类型的任何知识, 次要节点 `Text Multiline` 知识库中没有该节点类型的任何知识, 次要节点 `Text Multiline` 知识库中没有该节点类型的任何知识, 次要节点 `easy convertAnything` 知识库中没有该节点类型的任何知识, 次要节点 `easy int` 知识库中没有该节点类型的任何知识, 次要节点 `easy int` 知识库中没有该节点类型的任何知识, 次要节点 `easy int` 知识库中没有该节点类型的任何知识, 次要节点 `easy int` 知识库中没有该节点类型的任何知识, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/文生视频/Wan2.2 rapid mega v6工作流，文生视频图生视频all-in-one_1976881257567207426.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/Wan2.2 rapid mega v6工作流，文生视频图生视频all-in-one_1976881257567207426.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Other

**节点**（48 个）：
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `INTConstant`
- `SimpleMath+`
- `ModelSamplingSD3`
- `WanVaceToVideo`
- `SetNode`
- `SetNode`
- `VAEDecode` ★核心
- `SetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `easy convertAnything`
- `GetNode`
- `WanVideoVACEStartToEndFrame`
- `easy showAnything`
- `SimpleMath+`
- `SetNode`
- `SetNode`
- `SetNode`
- `VHS_VideoCombine`
- `easy int`
- `easy int`
- `easy int`
- `Text Multiline`
- `easy int`
- `easy showAnything`
- `LoadImage`
- `LoadImage`
- `Evaluate Strings`
- `KSampler` ★核心
- `CheckpointLoaderSimple` ★核心
- `Fast Groups Bypasser (rgthree)`
- `Text Multiline`

## 关键参数

- `seed` = `7567358653673`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `sa_solver`
- `scheduler` = `beta`
- `denoise` = `1`
- `checkpoint` = `wan2.2-rapid-mega-aio-nsfw-v6.safetensors`

## 知识

覆盖率 **25%**（12/48）

**有卡**：`INTConstant`、`ModelSamplingSD3`、`WanVaceToVideo`、`VAEDecode`、`CLIPTextEncode`、`WanVideoVACEStartToEndFrame`、`VHS_VideoCombine`、`LoadImage`、`KSampler`、`CheckpointLoaderSimple`

**缺卡**（10）：`Evaluate Strings`、`SimpleMath+`、`SimpleMath+`、`Text Multiline`、`Text Multiline`、`easy convertAnything`、`easy int`、`easy int`、`easy int`、`easy int`

**用到的条目**：KSampler、VAEDecode、CheckpointLoaderSimple、CLIPTextEncode、LoadImage、INTConstant、ModelSamplingSD3、VHS_VideoCombine

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- 次要节点 `Evaluate Strings` 知识库中没有该节点类型的任何知识
- 次要节点 `SimpleMath+` 知识库中没有该节点类型的任何知识
- 次要节点 `SimpleMath+` 知识库中没有该节点类型的任何知识
- 次要节点 `Text Multiline` 知识库中没有该节点类型的任何知识
- 次要节点 `Text Multiline` 知识库中没有该节点类型的任何知识
- 次要节点 `easy convertAnything` 知识库中没有该节点类型的任何知识
- 次要节点 `easy int` 知识库中没有该节点类型的任何知识
- 次要节点 `easy int` 知识库中没有该节点类型的任何知识
- 次要节点 `easy int` 知识库中没有该节点类型的任何知识
- 次要节点 `easy int` 知识库中没有该节点类型的任何知识
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

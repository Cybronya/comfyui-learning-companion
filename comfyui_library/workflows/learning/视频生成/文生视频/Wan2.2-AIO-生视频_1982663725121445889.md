---
key: 视频生成/文生视频/Wan2.2-AIO-生视频_1982663725121445889.json
name: Wan2.2-AIO-生视频_1982663725121445889
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/Wan2.2-AIO-生视频_1982663725121445889.json
hash: 3e1fddb3d8c87064
coverage: 0.255319
learned_at: 2026-10-11 02:45:02
nodes: [SetNode, SetNode, SetNode, GetNode, GetNode, INTConstant, SimpleMath+, SetNode, SetNode, GetNode, SetNode, GetNode, CLIPTextEncode, GetNode, easy convertAnything, GetNode, SetNode, SetNode, easy int, easy int, easy int, easy int, LoadImage, LoadImage, VHS_VideoCombine, SetNode, Text Multiline, WanVideoVACEStartToEndFrame, GetNode, GetNode, SetNode, GetNode, GetNode, GetNode, ModelSamplingSD3, VAEDecode, Evaluate Strings, SimpleMath+, SetNode, CLIPTextEncode, GetNode, WanVaceToVideo, KSampler, easy showAnything, Fast Groups Bypasser (rgthree), Text Multiline, CheckpointLoaderSimple]
patterns: []
missing: [Evaluate Strings, SimpleMath+, SimpleMath+, Text Multiline, Text Multiline, easy convertAnything, easy int, easy int, easy int, easy int]
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "checkpoint": "wan2.2-rapid-mega-aio-nsfw-v11.safetensors", "denoise": 1, "sampler_name": "sa_solver", "scheduler": "beta", "seed": 7567358653673, "steps": 4}
discoveries: [次要节点 `Evaluate Strings` 知识库中没有该节点类型的任何知识, 次要节点 `SimpleMath+` 知识库中没有该节点类型的任何知识, 次要节点 `SimpleMath+` 知识库中没有该节点类型的任何知识, 次要节点 `Text Multiline` 知识库中没有该节点类型的任何知识, 次要节点 `Text Multiline` 知识库中没有该节点类型的任何知识, 次要节点 `easy convertAnything` 知识库中没有该节点类型的任何知识, 次要节点 `easy int` 知识库中没有该节点类型的任何知识, 次要节点 `easy int` 知识库中没有该节点类型的任何知识, 次要节点 `easy int` 知识库中没有该节点类型的任何知识, 次要节点 `easy int` 知识库中没有该节点类型的任何知识, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
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

覆盖率 **26%**（12/47）

**有卡**：`INTConstant`、`CLIPTextEncode`、`LoadImage`、`VHS_VideoCombine`、`WanVideoVACEStartToEndFrame`、`ModelSamplingSD3`、`VAEDecode`、`WanVaceToVideo`、`KSampler`、`CheckpointLoaderSimple`

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

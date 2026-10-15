---
key: 图片生成/文生图/FluxKrea - ImageGeneration  文生图工作流_1951504768676122625.json
name: FluxKrea - ImageGeneration  文生图工作流_1951504768676122625
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/FluxKrea - ImageGeneration  文生图工作流_1951504768676122625.json
hash: edd7be3fd6d2cadb
coverage: 0.782609
learned_at: 2026-10-10 20:58:36
nodes: [SetNode, SetNode, CLIPTextEncode, ModelSamplingFlux, SamplerCustomAdvanced, BasicGuider, FluxGuidance, PathchSageAttentionKJ, BasicScheduler, EmptyLatentImage, RandomNoise, VAELoader, LoraLoader, VAEDecode, SaveImage, Primitive string multiline [Crystools], KSamplerSelect, UNETLoader, DualCLIPLoader, easy int, easy int, UnetLoaderGGUF, DualCLIPLoaderGGUF]
patterns: [lora]
missing: [Primitive string multiline [Crystools], easy int, easy int]
parameters: {"batch_size": 1, "height": 1280, "lora_name": "blonde.sft", "strength_clip": 0.9, "strength_model": 0.9, "width": 904}
discoveries: [次要节点 `Primitive string multiline [Crystools]` 知识库中没有该节点类型的任何知识, 次要节点 `easy int` 知识库中没有该节点类型的任何知识, 次要节点 `easy int` 知识库中没有该节点类型的任何知识]
---

# 图片生成/文生图/FluxKrea - ImageGeneration  文生图工作流_1951504768676122625.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/FluxKrea - ImageGeneration  文生图工作流_1951504768676122625.json`

## 结构

**节点**（23 个）：
- `SetNode`
- `SetNode`
- `CLIPTextEncode`
- `ModelSamplingFlux`
- `SamplerCustomAdvanced`
- `BasicGuider`
- `FluxGuidance`
- `PathchSageAttentionKJ`
- `BasicScheduler`
- `EmptyLatentImage`
- `RandomNoise`
- `VAELoader`
- `LoraLoader`
- `VAEDecode`
- `SaveImage`
- `Primitive string multiline [Crystools]`
- `KSamplerSelect`
- `UNETLoader`
- `DualCLIPLoader`
- `easy int`
- `easy int`
- `UnetLoaderGGUF`
- `DualCLIPLoaderGGUF`

**识别到的模式**：lora

## 关键参数

- `batch_size` = `1`
- `height` = `1280`
- `lora_name` = `blonde.sft`
- `strength_clip` = `0.9`
- `strength_model` = `0.9`
- `width` = `904`

## 知识

覆盖率 **78%**（18/23）

**有卡**：`SetNode`、`CLIPTextEncode`、`ModelSamplingFlux`、`SamplerCustomAdvanced`、`BasicGuider`、`FluxGuidance`、`PathchSageAttentionKJ`、`BasicScheduler`、`EmptyLatentImage`、`RandomNoise`、`VAELoader`、`LoraLoader`、`VAEDecode`、`SaveImage`、`Primitive string multiline [Crystools]`、`KSamplerSelect`、`UNETLoader`

**缺卡**（3）：`Primitive string multiline [Crystools]`、`easy int`、`easy int`

## 学习发现

- 次要节点 `Primitive string multiline [Crystools]` 知识库中没有该节点类型的任何知识
- 次要节点 `easy int` 知识库中没有该节点类型的任何知识
- 次要节点 `easy int` 知识库中没有该节点类型的任何知识

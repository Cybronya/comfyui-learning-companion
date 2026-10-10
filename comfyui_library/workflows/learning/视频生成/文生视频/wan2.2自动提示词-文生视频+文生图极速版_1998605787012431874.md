---
key: 视频生成/文生视频/wan2.2自动提示词-文生视频+文生图极速版_1998605787012431874.json
name: wan2.2自动提示词-文生视频+文生图极速版_1998605787012431874
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/wan2.2自动提示词-文生视频+文生图极速版_1998605787012431874.json
hash: 88e69aff3eed03b6
coverage: 0.62
learned_at: 2026-10-11 02:57:39
nodes: [SimpleMath+, easy getNode, easy getNode, easy getNode, DF_Integer, easy getNode, easy getNode, easy getNode, KSampler, ImageUpscaleWithModel, VAEEncode, ImageScaleBy, VAEDecode, VAEDecode, ModelPatchTorchSettings, PathchSageAttentionKJ, CLIPTextEncode, easy setNode, easy setNode, easy setNode, easy getNode, SaveImage, WanMoeKSampler, WanMoeKSampler, LoraLoaderModelOnly, CLIPLoader, EmptyHunyuanLatentVideo, easy setNode, VAELoader, easy setNode, EmptyHunyuanLatentVideo, easy getNode, easy getNode, ModelPatchTorchSettings, PathchSageAttentionKJ, LoraLoaderModelOnly, UNETLoader, UNETLoader, Fast Groups Bypasser (rgthree), UpscaleModelLoader, CLIPTextEncode, easy showAnything, RH_LLMAPI_NODE, Text Multiline, MuyeTextEditOutput, VAEDecode, VHS_VideoCombine, easy getNode, LoraLoaderModelOnly, LoraLoaderModelOnly]
patterns: []
missing: [SimpleMath+, Text Multiline, easy getNode, easy getNode, easy getNode, easy getNode, easy getNode, easy getNode, easy getNode, easy getNode, easy getNode, easy getNode, easy setNode, easy setNode, easy setNode, easy setNode, easy setNode]
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 4, "denoise": "euler", "sampler_name": 1, "scheduler": 1, "seed": 0.875, "steps": "fixed"}
discoveries: [次要节点 `SimpleMath+` 知识库中没有该节点类型的任何知识, 次要节点 `Text Multiline` 知识库中没有该节点类型的任何知识, 次要节点 `easy getNode` 知识库中没有该节点类型的任何知识, 次要节点 `easy getNode` 知识库中没有该节点类型的任何知识, 次要节点 `easy getNode` 知识库中没有该节点类型的任何知识, 次要节点 `easy getNode` 知识库中没有该节点类型的任何知识, 次要节点 `easy getNode` 知识库中没有该节点类型的任何知识, 次要节点 `easy getNode` 知识库中没有该节点类型的任何知识, 次要节点 `easy getNode` 知识库中没有该节点类型的任何知识, 次要节点 `easy getNode` 知识库中没有该节点类型的任何知识, 次要节点 `easy getNode` 知识库中没有该节点类型的任何知识, 次要节点 `easy getNode` 知识库中没有该节点类型的任何知识, 次要节点 `easy setNode` 知识库中没有该节点类型的任何知识, 次要节点 `easy setNode` 知识库中没有该节点类型的任何知识, 次要节点 `easy setNode` 知识库中没有该节点类型的任何知识, 次要节点 `easy setNode` 知识库中没有该节点类型的任何知识, 次要节点 `easy setNode` 知识库中没有该节点类型的任何知识, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/文生视频/wan2.2自动提示词-文生视频+文生图极速版_1998605787012431874.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/wan2.2自动提示词-文生视频+文生图极速版_1998605787012431874.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（50 个）：
- `SimpleMath+`
- `easy getNode`
- `easy getNode`
- `easy getNode`
- `DF_Integer`
- `easy getNode`
- `easy getNode`
- `easy getNode`
- `KSampler` ★核心
- `ImageUpscaleWithModel`
- `VAEEncode` ★核心
- `ImageScaleBy`
- `VAEDecode` ★核心
- `VAEDecode` ★核心
- `ModelPatchTorchSettings`
- `PathchSageAttentionKJ`
- `CLIPTextEncode` ★核心
- `easy setNode`
- `easy setNode`
- `easy setNode`
- `easy getNode`
- `SaveImage`
- `WanMoeKSampler` ★核心
- `WanMoeKSampler` ★核心
- `LoraLoaderModelOnly` ★核心
- `CLIPLoader`
- `EmptyHunyuanLatentVideo`
- `easy setNode`
- `VAELoader`
- `easy setNode`
- `EmptyHunyuanLatentVideo`
- `easy getNode`
- `easy getNode`
- `ModelPatchTorchSettings`
- `PathchSageAttentionKJ`
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `Fast Groups Bypasser (rgthree)`
- `UpscaleModelLoader`
- `CLIPTextEncode` ★核心
- `easy showAnything`
- `RH_LLMAPI_NODE`
- `Text Multiline`
- `MuyeTextEditOutput`
- `VAEDecode` ★核心
- `VHS_VideoCombine`
- `easy getNode`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心

## 关键参数

- `seed` = `0.875`
- `steps` = `fixed`
- `cfg` = `4`
- `sampler_name` = `1`
- `scheduler` = `1`
- `denoise` = `euler`

## 知识

覆盖率 **62%**（31/50）

**有卡**：`DF_Integer`、`KSampler`、`ImageUpscaleWithModel`、`VAEEncode`、`ImageScaleBy`、`VAEDecode`、`ModelPatchTorchSettings`、`PathchSageAttentionKJ`、`CLIPTextEncode`、`SaveImage`、`WanMoeKSampler`、`LoraLoaderModelOnly`、`CLIPLoader`、`EmptyHunyuanLatentVideo`、`VAELoader`、`UNETLoader`、`UpscaleModelLoader`、`RH_LLMAPI_NODE`、`MuyeTextEditOutput`、`VHS_VideoCombine`

**缺卡**（17）：`SimpleMath+`、`Text Multiline`、`easy getNode`、`easy getNode`、`easy getNode`、`easy getNode`、`easy getNode`、`easy getNode`、`easy getNode`、`easy getNode`、`easy getNode`、`easy getNode`、`easy setNode`、`easy setNode`、`easy setNode`、`easy setNode`、`easy setNode`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、SaveImage、UNETLoader

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- 次要节点 `SimpleMath+` 知识库中没有该节点类型的任何知识
- 次要节点 `Text Multiline` 知识库中没有该节点类型的任何知识
- 次要节点 `easy getNode` 知识库中没有该节点类型的任何知识
- 次要节点 `easy getNode` 知识库中没有该节点类型的任何知识
- 次要节点 `easy getNode` 知识库中没有该节点类型的任何知识
- 次要节点 `easy getNode` 知识库中没有该节点类型的任何知识
- 次要节点 `easy getNode` 知识库中没有该节点类型的任何知识
- 次要节点 `easy getNode` 知识库中没有该节点类型的任何知识
- 次要节点 `easy getNode` 知识库中没有该节点类型的任何知识
- 次要节点 `easy getNode` 知识库中没有该节点类型的任何知识
- 次要节点 `easy getNode` 知识库中没有该节点类型的任何知识
- 次要节点 `easy getNode` 知识库中没有该节点类型的任何知识
- 次要节点 `easy setNode` 知识库中没有该节点类型的任何知识
- 次要节点 `easy setNode` 知识库中没有该节点类型的任何知识
- 次要节点 `easy setNode` 知识库中没有该节点类型的任何知识
- 次要节点 `easy setNode` 知识库中没有该节点类型的任何知识
- 次要节点 `easy setNode` 知识库中没有该节点类型的任何知识
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

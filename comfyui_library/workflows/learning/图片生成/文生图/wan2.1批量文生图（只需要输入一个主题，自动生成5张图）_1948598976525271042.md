---
key: 图片生成/文生图/wan2.1批量文生图（只需要输入一个主题，自动生成5张图）_1948598976525271042.json
name: wan2.1批量文生图（只需要输入一个主题，自动生成5张图）_1948598976525271042.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/wan2.1批量文生图（只需要输入一个主题，自动生成5张图）_1948598976525271042.json
hash: 3d0a37139b223c8f
coverage: 0.441176
learned_at: 2026-10-07 22:53:12
nodes: [GetNode, GetNode, GetNode, SetNode, SetNode, SetNode, UNETLoader, VAELoader, PathchSageAttentionKJ, LoraLoaderModelOnly, SetNode, EmptySD3LatentImage, CLIPTextEncode, SetNode, SetNode, ModelSamplingSD3, CLIPTextEncode, KSampler, SetNode, VAEDecode, WanVideoNAG, CLIPLoader, easy forLoopStart, Text Find and Replace, easy showAnything, Text Load Line From File, ShowText|pysssss, easy forLoopEnd, SaveImage, RH_LLMAPI_NODE, ShowText|pysssss, Text Multiline, SaveImage, Text Multiline]
patterns: []
missing: [Text Find and Replace, Text Load Line From File, Text Multiline, Text Multiline, easy forLoopEnd, easy forLoopStart]
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "uni_pc", "scheduler": "simple", "seed": 97746812058490, "steps": 8}
discoveries: [次要节点 `Text Find and Replace` 知识库中没有该节点类型的任何知识, 次要节点 `Text Load Line From File` 知识库中没有该节点类型的任何知识, 次要节点 `Text Multiline` 知识库中没有该节点类型的任何知识, 次要节点 `Text Multiline` 知识库中没有该节点类型的任何知识, 次要节点 `easy forLoopEnd` 知识库中没有该节点类型的任何知识, 次要节点 `easy forLoopStart` 知识库中没有该节点类型的任何知识, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/文生图/wan2.1批量文生图（只需要输入一个主题，自动生成5张图）_1948598976525271042.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/1948598976525271042.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（34 个）：
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `UNETLoader` ★核心
- `VAELoader`
- `PathchSageAttentionKJ`
- `LoraLoaderModelOnly` ★核心
- `SetNode`
- `EmptySD3LatentImage`
- `CLIPTextEncode` ★核心
- `SetNode`
- `SetNode`
- `ModelSamplingSD3`
- `CLIPTextEncode` ★核心
- `KSampler` ★核心
- `SetNode`
- `VAEDecode` ★核心
- `WanVideoNAG`
- `CLIPLoader`
- `easy forLoopStart`
- `Text Find and Replace`
- `easy showAnything`
- `Text Load Line From File`
- `ShowText|pysssss`
- `easy forLoopEnd`
- `SaveImage`
- `RH_LLMAPI_NODE`
- `ShowText|pysssss`
- `Text Multiline`
- `SaveImage`
- `Text Multiline`

## 关键参数

- `seed` = `97746812058490`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `uni_pc`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **44%**（15/34）

**有卡**：`UNETLoader`、`VAELoader`、`PathchSageAttentionKJ`、`LoraLoaderModelOnly`、`EmptySD3LatentImage`、`CLIPTextEncode`、`ModelSamplingSD3`、`KSampler`、`VAEDecode`、`WanVideoNAG`、`CLIPLoader`、`SaveImage`、`RH_LLMAPI_NODE`

**缺卡**（6）：`Text Find and Replace`、`Text Load Line From File`、`Text Multiline`、`Text Multiline`、`easy forLoopEnd`、`easy forLoopStart`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、UNETLoader、SaveImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- 次要节点 `Text Find and Replace` 知识库中没有该节点类型的任何知识
- 次要节点 `Text Load Line From File` 知识库中没有该节点类型的任何知识
- 次要节点 `Text Multiline` 知识库中没有该节点类型的任何知识
- 次要节点 `Text Multiline` 知识库中没有该节点类型的任何知识
- 次要节点 `easy forLoopEnd` 知识库中没有该节点类型的任何知识
- 次要节点 `easy forLoopStart` 知识库中没有该节点类型的任何知识
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

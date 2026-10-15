---
key: 图片生成/文生图/wan2.1批量文生图（只需要输入一个主题，自动生成5张图）_1948598976525271042.json
name: wan2.1批量文生图（只需要输入一个主题，自动生成5张图）_1948598976525271042
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/wan2.1批量文生图（只需要输入一个主题，自动生成5张图）_1948598976525271042.json
hash: 3d0a37139b223c8f
coverage: 0.441176
learned_at: 2026-10-10 20:59:26
nodes: [GetNode, GetNode, GetNode, SetNode, SetNode, SetNode, UNETLoader, VAELoader, PathchSageAttentionKJ, LoraLoaderModelOnly, SetNode, EmptySD3LatentImage, CLIPTextEncode, SetNode, SetNode, ModelSamplingSD3, CLIPTextEncode, KSampler, SetNode, VAEDecode, WanVideoNAG, CLIPLoader, easy forLoopStart, Text Find and Replace, easy showAnything, Text Load Line From File, ShowText|pysssss, easy forLoopEnd, SaveImage, RH_LLMAPI_NODE, ShowText|pysssss, Text Multiline, SaveImage, Text Multiline]
patterns: []
missing: [Text Find and Replace, Text Load Line From File, Text Multiline, Text Multiline, easy forLoopEnd, easy forLoopStart]
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "uni_pc", "scheduler": "simple", "seed": 97746812058490, "steps": 8}
discoveries: [次要节点 `Text Find and Replace` 知识库中没有该节点类型的任何知识, 次要节点 `Text Load Line From File` 知识库中没有该节点类型的任何知识, 次要节点 `Text Multiline` 知识库中没有该节点类型的任何知识, 次要节点 `Text Multiline` 知识库中没有该节点类型的任何知识, 次要节点 `easy forLoopEnd` 知识库中没有该节点类型的任何知识, 次要节点 `easy forLoopStart` 知识库中没有该节点类型的任何知识, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/文生图/wan2.1批量文生图（只需要输入一个主题，自动生成5张图）_1948598976525271042.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/wan2.1批量文生图（只需要输入一个主题，自动生成5张图）_1948598976525271042.json`

## 结构

**节点**（34 个）：
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `UNETLoader`
- `VAELoader`
- `PathchSageAttentionKJ`
- `LoraLoaderModelOnly`
- `SetNode`
- `EmptySD3LatentImage`
- `CLIPTextEncode`
- `SetNode`
- `SetNode`
- `ModelSamplingSD3`
- `CLIPTextEncode`
- `KSampler`
- `SetNode`
- `VAEDecode`
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

- `cfg` = `1`
- `denoise` = `1`
- `sampler_name` = `uni_pc`
- `scheduler` = `simple`
- `seed` = `97746812058490`
- `steps` = `8`

## 知识

覆盖率 **44%**（15/34）

**有卡**：`GetNode`、`SetNode`、`UNETLoader`、`VAELoader`、`PathchSageAttentionKJ`、`LoraLoaderModelOnly`、`EmptySD3LatentImage`、`CLIPTextEncode`

**缺卡**（6）：`Text Find and Replace`、`Text Load Line From File`、`Text Multiline`、`Text Multiline`、`easy forLoopEnd`、`easy forLoopStart`

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

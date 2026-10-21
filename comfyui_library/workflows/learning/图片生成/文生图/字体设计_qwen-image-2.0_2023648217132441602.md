---
key: 图片生成/文生图/字体设计_qwen-image-2.0_2023648217132441602.json
name: 字体设计_qwen-image-2.0_2023648217132441602
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/字体设计_qwen-image-2.0_2023648217132441602.json
hash: c218312b26c8768c
coverage: 0.814815
learned_at: 2026-10-19 22:30:29
nodes: [ConditioningZeroOut, CLIPLoader, UNETLoader, ModelSamplingAuraFlow, KSampler, easy promptList, easy promptList, easy promptList, easy promptList, easy promptList, easy promptList, CR Text Replace, easy promptList, easy promptList, easy promptList, CR Text Input Switch (4 way), CLIPTextEncode, VAEDecode, SaveImage, VAELoader, EmptySD3LatentImage, CR Text, PrimitiveNode, PreviewImage, MarkdownNote, MarkdownNote, MarkdownNote]
patterns: []
missing: []
parameters: {"cfg": 4, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 1106831587485563, "steps": 20}
---

# 图片生成/文生图/字体设计_qwen-image-2.0_2023648217132441602.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/字体设计_qwen-image-2.0_2023648217132441602.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（27 个）：
- `ConditioningZeroOut`
- `CLIPLoader`
- `UNETLoader` ★核心
- `ModelSamplingAuraFlow`
- `KSampler` ★核心
- `easy promptList`
- `easy promptList`
- `easy promptList`
- `easy promptList`
- `easy promptList`
- `easy promptList`
- `CR Text Replace`
- `easy promptList`
- `easy promptList`
- `easy promptList`
- `CR Text Input Switch (4 way)`
- `CLIPTextEncode` ★核心
- `VAEDecode` ★核心
- `SaveImage`
- `VAELoader`
- `EmptySD3LatentImage`
- `CR Text`
- `PrimitiveNode`
- `PreviewImage`
- `MarkdownNote`
- `MarkdownNote`
- `MarkdownNote`

## 关键参数

- `seed` = `1106831587485563`
- `steps` = `20`
- `cfg` = `4`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **81%**（22/27）

**有卡**：`ConditioningZeroOut`、`CLIPLoader`、`UNETLoader`、`ModelSamplingAuraFlow`、`KSampler`、`easy promptList`、`CR Text Replace`、`CR Text Input Switch (4 way)`、`CLIPTextEncode`、`VAEDecode`、`SaveImage`、`VAELoader`、`EmptySD3LatentImage`、`CR Text`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、UNETLoader、easy promptList

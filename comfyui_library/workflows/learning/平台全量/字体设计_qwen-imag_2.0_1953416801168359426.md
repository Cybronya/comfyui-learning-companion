---
key: 平台全量/字体设计_qwen-imag_2.0_1953416801168359426.json
name: 字体设计_qwen-imag_2.0_1953416801168359426
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/字体设计_qwen-imag_2.0_1953416801168359426.json
hash: 63c42391166aa689
coverage: 0.916667
learned_at: 2026-11-14 01:59:25
nodes: [ConditioningZeroOut, EmptySD3LatentImage, VAELoader, CLIPLoader, UNETLoader, ModelSamplingAuraFlow, PreviewImage, KSampler, easy promptList, easy promptList, easy promptList, easy promptList, easy promptList, easy promptList, PrimitiveNode, CR Text, CR Text Replace, easy promptList, easy promptList, easy promptList, CR Text Input Switch (4 way), CLIPTextEncode, VAEDecode, SaveImage]
patterns: []
missing: []
parameters: {"cfg": 4, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 997706183229220, "steps": 20}
---

# 平台全量/字体设计_qwen-imag_2.0_1953416801168359426.json

> 来源文件 `comfyui_library/workflows/平台全量/字体设计_qwen-imag_2.0_1953416801168359426.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（24 个）：
- `ConditioningZeroOut`
- `EmptySD3LatentImage`
- `VAELoader`
- `CLIPLoader`
- `UNETLoader` ★核心
- `ModelSamplingAuraFlow`
- `PreviewImage`
- `KSampler` ★核心
- `easy promptList`
- `easy promptList`
- `easy promptList`
- `easy promptList`
- `easy promptList`
- `easy promptList`
- `PrimitiveNode`
- `CR Text`
- `CR Text Replace`
- `easy promptList`
- `easy promptList`
- `easy promptList`
- `CR Text Input Switch (4 way)`
- `CLIPTextEncode` ★核心
- `VAEDecode` ★核心
- `SaveImage`

## 关键参数

- `seed` = `997706183229220`
- `steps` = `20`
- `cfg` = `4`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **92%**（22/24）

**有卡**：`ConditioningZeroOut`、`EmptySD3LatentImage`、`VAELoader`、`CLIPLoader`、`UNETLoader`、`ModelSamplingAuraFlow`、`KSampler`、`easy promptList`、`CR Text`、`CR Text Replace`、`CR Text Input Switch (4 way)`、`CLIPTextEncode`、`VAEDecode`、`SaveImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPLoader、CLIPTextEncode、ConditioningZeroOut、UNETLoader、easy promptList

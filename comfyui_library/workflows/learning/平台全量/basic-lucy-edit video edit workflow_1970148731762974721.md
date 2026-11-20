---
key: 平台全量/basic-lucy-edit video edit workflow_1970148731762974721.json
name: basic-lucy-edit video edit workflow_1970148731762974721
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/basic-lucy-edit video edit workflow_1970148731762974721.json
hash: 54a7c202ddf89f97
coverage: 0.8125
learned_at: 2026-11-14 01:09:31
nodes: [CLIPTextEncode, MarkdownNote, CLIPLoader, UNETLoader, VAELoader, VAEEncode, VAEDecode, VHS_VideoCombine, PrimitiveInt, PrimitiveNode, VHS_LoadVideo, ImageResizeKJv2, CLIPTextEncode, LucyConditionConcatNode, ModelSamplingSD3, KSampler]
patterns: []
missing: []
parameters: {"cfg": 5, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 851528374349405, "steps": 50}
---

# 平台全量/basic-lucy-edit video edit workflow_1970148731762974721.json

> 来源文件 `comfyui_library/workflows/平台全量/basic-lucy-edit video edit workflow_1970148731762974721.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Other

**节点**（16 个）：
- `CLIPTextEncode` ★核心
- `MarkdownNote`
- `CLIPLoader`
- `UNETLoader` ★核心
- `VAELoader`
- `VAEEncode` ★核心
- `VAEDecode` ★核心
- `VHS_VideoCombine`
- `PrimitiveInt`
- `PrimitiveNode`
- `VHS_LoadVideo`
- `ImageResizeKJv2`
- `CLIPTextEncode` ★核心
- `LucyConditionConcatNode`
- `ModelSamplingSD3`
- `KSampler` ★核心

## 关键参数

- `seed` = `851528374349405`
- `steps` = `50`
- `cfg` = `5`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **81%**（13/16）

**有卡**：`CLIPTextEncode`、`CLIPLoader`、`UNETLoader`、`VAELoader`、`VAEEncode`、`VAEDecode`、`VHS_VideoCombine`、`VHS_LoadVideo`、`ImageResizeKJv2`、`LucyConditionConcatNode`、`ModelSamplingSD3`、`KSampler`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPLoader、CLIPTextEncode、UNETLoader、VAEEncode、ImageResizeKJv2

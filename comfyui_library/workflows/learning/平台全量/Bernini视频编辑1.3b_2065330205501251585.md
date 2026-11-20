---
key: 平台全量/Bernini视频编辑1.3b_2065330205501251585.json
name: Bernini视频编辑1.3b_2065330205501251585
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/Bernini视频编辑1.3b_2065330205501251585.json
hash: 8663251e29f75d03
coverage: 0.96
learned_at: 2026-11-14 00:20:43
nodes: [VHS_VideoCombine, CLIPTextEncode, MathExpression|pysssss, CLIPLoader, VAELoader, VHS_VideoInfoLoaded, easy setNode, easy setNode, easy setNode, easy getNode, easy getNode, easy getNode, easy getNode, VAEDecode, PathchSageAttentionKJ, LoraLoaderModelOnly, easy setNode, KSampler, BerniniConditioning, UNETLoader, LayerUtility: ImageScaleByAspectRatio V2, MarkdownNote, Int, VHS_LoadVideo, CLIPTextEncode]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "res_multistep", "scheduler": "simple", "seed": 815326312237678, "steps": 6}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 平台全量/Bernini视频编辑1.3b_2065330205501251585.json

> 来源文件 `comfyui_library/workflows/平台全量/Bernini视频编辑1.3b_2065330205501251585.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（25 个）：
- `VHS_VideoCombine`
- `CLIPTextEncode` ★核心
- `MathExpression|pysssss`
- `CLIPLoader`
- `VAELoader`
- `VHS_VideoInfoLoaded`
- `easy setNode`
- `easy setNode`
- `easy setNode`
- `easy getNode`
- `easy getNode`
- `easy getNode`
- `easy getNode`
- `VAEDecode` ★核心
- `PathchSageAttentionKJ`
- `LoraLoaderModelOnly` ★核心
- `easy setNode`
- `KSampler` ★核心
- `BerniniConditioning`
- `UNETLoader` ★核心
- `LayerUtility: ImageScaleByAspectRatio V2`
- `MarkdownNote`
- `Int`
- `VHS_LoadVideo`
- `CLIPTextEncode` ★核心

## 关键参数

- `seed` = `815326312237678`
- `steps` = `6`
- `cfg` = `1`
- `sampler_name` = `res_multistep`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **96%**（24/25）

**有卡**：`VHS_VideoCombine`、`CLIPTextEncode`、`MathExpression|pysssss`、`CLIPLoader`、`VAELoader`、`VHS_VideoInfoLoaded`、`easy setNode`、`easy getNode`、`VAEDecode`、`PathchSageAttentionKJ`、`LoraLoaderModelOnly`、`KSampler`、`BerniniConditioning`、`UNETLoader`、`LayerUtility: ImageScaleByAspectRatio V2`、`Int`、`VHS_LoadVideo`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、CLIPTextEncode、UNETLoader、BerniniConditioning

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

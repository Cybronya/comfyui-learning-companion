---
key: 图片生成/文生图/Wan2.2剪辑师出图工作流V1_1995323733445369858.json
name: Wan2.2剪辑师出图工作流V1_1995323733445369858
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Wan2.2剪辑师出图工作流V1_1995323733445369858.json
hash: 87586ded0053d1f1
coverage: 0.888889
learned_at: 2026-10-19 21:32:44
nodes: [easy setNode, UNETLoader, CLIPLoader, VAELoader, LoraLoader, easy getNode, VAEDecode, EmptyHunyuanLatentVideo, PathchSageAttentionKJ, RHHiddenNodes, easy int, easy int, FastFilmGrain, CLIPTextEncode, SaveImage, Note, CLIPTextEncode, Note]
patterns: [lora]
missing: []
parameters: {"lora_name": "FastWan_T2V_14B_480p_lora_rank_128_bf16.safetensors", "strength_clip": 1.0000000000000002, "strength_model": 1.0000000000000002}
---

# 图片生成/文生图/Wan2.2剪辑师出图工作流V1_1995323733445369858.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Wan2.2剪辑师出图工作流V1_1995323733445369858.json`

## 结构

**生成流程**：Model → Condition → Decode → Output → Other

**节点**（18 个）：
- `easy setNode`
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `LoraLoader` ★核心
- `easy getNode`
- `VAEDecode` ★核心
- `EmptyHunyuanLatentVideo`
- `PathchSageAttentionKJ`
- `RHHiddenNodes`
- `easy int`
- `easy int`
- `FastFilmGrain`
- `CLIPTextEncode` ★核心
- `SaveImage`
- `Note`
- `CLIPTextEncode` ★核心
- `Note`

**识别到的模式**：lora

## 关键参数

- `lora_name` = `FastWan_T2V_14B_480p_lora_rank_128_bf16.safetensors`
- `strength_model` = `1.0000000000000002`
- `strength_clip` = `1.0000000000000002`

## 知识

覆盖率 **89%**（16/18）

**有卡**：`easy setNode`、`UNETLoader`、`CLIPLoader`、`VAELoader`、`LoraLoader`、`easy getNode`、`VAEDecode`、`EmptyHunyuanLatentVideo`、`PathchSageAttentionKJ`、`RHHiddenNodes`、`easy int`、`FastFilmGrain`、`CLIPTextEncode`、`SaveImage`

**用到的条目**：VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、UNETLoader、EmptyHunyuanLatentVideo、LoraLoader、LoraLoader

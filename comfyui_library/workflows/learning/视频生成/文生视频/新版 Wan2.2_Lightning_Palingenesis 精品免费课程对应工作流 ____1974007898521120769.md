---
key: 视频生成/文生视频/新版 Wan2.2_Lightning_Palingenesis 精品免费课程对应工作流 ____1974007898521120769.json
name: 新版 Wan2.2_Lightning_Palingenesis 精品免费课程对应工作流 ____1974007898521120769
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/新版 Wan2.2_Lightning_Palingenesis 精品免费课程对应工作流 ____1974007898521120769.json
hash: 1c8aca385843021c
coverage: 0.724138
learned_at: 2026-10-10 23:13:14
nodes: [CLIPTextEncode, VAEDecode, CLIPLoader, VAELoader, ModelSamplingSD3, ModelSamplingSD3, KSamplerAdvanced, KSamplerAdvanced, EmptyHunyuanLatentVideo, MarkdownNote, RIFE VFI, VHS_VideoCombine, VHS_VideoCombine, PathchSageAttentionKJ, PathchSageAttentionKJ, TorchCompileModel, TorchCompileModel, UNETLoader, UNETLoader, LoraLoaderModelOnly, Note, Note, Note, Note, Note, Note, LoraLoaderModelOnly, CLIPTextEncode, LoraLoaderModelOnly]
patterns: []
missing: [RIFE VFI]
parameters: {"cfg": 6, "denoise": "simple", "sampler_name": 1, "scheduler": "euler", "seed": "disable", "steps": "fixed"}
discoveries: [次要节点 `RIFE VFI` 知识库中没有该节点类型的任何知识]
---

# 视频生成/文生视频/新版 Wan2.2_Lightning_Palingenesis 精品免费课程对应工作流 ____1974007898521120769.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/新版 Wan2.2_Lightning_Palingenesis 精品免费课程对应工作流 ____1974007898521120769.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Other

**节点**（29 个）：
- `CLIPTextEncode` ★核心
- `VAEDecode` ★核心
- `CLIPLoader`
- `VAELoader`
- `ModelSamplingSD3`
- `ModelSamplingSD3`
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `EmptyHunyuanLatentVideo`
- `MarkdownNote`
- `RIFE VFI`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `PathchSageAttentionKJ`
- `PathchSageAttentionKJ`
- `TorchCompileModel`
- `TorchCompileModel`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `LoraLoaderModelOnly` ★核心
- `CLIPTextEncode` ★核心
- `LoraLoaderModelOnly` ★核心

## 关键参数

- `seed` = `disable`
- `steps` = `fixed`
- `cfg` = `6`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `simple`

## 知识

覆盖率 **72%**（21/29）

**有卡**：`CLIPTextEncode`、`VAEDecode`、`CLIPLoader`、`VAELoader`、`ModelSamplingSD3`、`KSamplerAdvanced`、`EmptyHunyuanLatentVideo`、`VHS_VideoCombine`、`PathchSageAttentionKJ`、`TorchCompileModel`、`UNETLoader`、`LoraLoaderModelOnly`

**缺卡**（1）：`RIFE VFI`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、UNETLoader、KSamplerAdvanced、EmptyHunyuanLatentVideo

## 学习发现

- 次要节点 `RIFE VFI` 知识库中没有该节点类型的任何知识

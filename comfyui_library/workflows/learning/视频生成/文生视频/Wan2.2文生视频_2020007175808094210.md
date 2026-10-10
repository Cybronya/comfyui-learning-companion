---
key: 视频生成/文生视频/Wan2.2文生视频_2020007175808094210.json
name: Wan2.2文生视频_2020007175808094210
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/Wan2.2文生视频_2020007175808094210.json
hash: b0417fece7550cc4
coverage: 0.875
learned_at: 2026-10-11 03:16:50
nodes: [CLIPLoader, UNETLoader, CLIPTextEncode, ModelSamplingSD3, PathchSageAttentionKJ, ModelSamplingSD3, VAELoader, VAEDecode, easy cleanGpuUsed, ModelPatchTorchSettings, UNETLoader, ModelPatchTorchSettings, LoraLoaderModelOnly, KSamplerAdvanced, KSamplerAdvanced, PathchSageAttentionKJ, LoraLoaderModelOnly, Int, Int, MathExpression|pysssss, easy showAnything, CLIPTextEncode, EmptyHunyuanLatentVideo, VHS_VideoCombine]
patterns: []
missing: [MathExpression|pysssss, easy cleanGpuUsed]
parameters: {"cfg": 6, "denoise": "simple", "sampler_name": 1, "scheduler": "euler", "seed": "disable", "steps": "fixed"}
discoveries: [次要节点 `MathExpression|pysssss` 知识库中没有该节点类型的任何知识, 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识]
---

# 视频生成/文生视频/Wan2.2文生视频_2020007175808094210.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/Wan2.2文生视频_2020007175808094210.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Other

**节点**（24 个）：
- `CLIPLoader`
- `UNETLoader` ★核心
- `CLIPTextEncode` ★核心
- `ModelSamplingSD3`
- `PathchSageAttentionKJ`
- `ModelSamplingSD3`
- `VAELoader`
- `VAEDecode` ★核心
- `easy cleanGpuUsed`
- `ModelPatchTorchSettings`
- `UNETLoader` ★核心
- `ModelPatchTorchSettings`
- `LoraLoaderModelOnly` ★核心
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `PathchSageAttentionKJ`
- `LoraLoaderModelOnly` ★核心
- `Int`
- `Int`
- `MathExpression|pysssss`
- `easy showAnything`
- `CLIPTextEncode` ★核心
- `EmptyHunyuanLatentVideo`
- `VHS_VideoCombine`

## 关键参数

- `seed` = `disable`
- `steps` = `fixed`
- `cfg` = `6`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `simple`

## 知识

覆盖率 **88%**（21/24）

**有卡**：`CLIPLoader`、`UNETLoader`、`CLIPTextEncode`、`ModelSamplingSD3`、`PathchSageAttentionKJ`、`VAELoader`、`VAEDecode`、`ModelPatchTorchSettings`、`LoraLoaderModelOnly`、`KSamplerAdvanced`、`Int`、`EmptyHunyuanLatentVideo`、`VHS_VideoCombine`

**缺卡**（2）：`MathExpression|pysssss`、`easy cleanGpuUsed`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、UNETLoader、KSamplerAdvanced、EmptyHunyuanLatentVideo

## 学习发现

- 次要节点 `MathExpression|pysssss` 知识库中没有该节点类型的任何知识
- 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识

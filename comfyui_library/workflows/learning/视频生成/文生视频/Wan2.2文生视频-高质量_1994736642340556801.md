---
key: 视频生成/文生视频/Wan2.2文生视频-高质量_1994736642340556801.json
name: Wan2.2文生视频-高质量_1994736642340556801
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/Wan2.2文生视频-高质量_1994736642340556801.json
hash: 5cc49d08ceceace3
coverage: 0.904762
learned_at: 2026-10-11 02:57:38
nodes: [CLIPLoader, PathchSageAttentionKJ, UNETLoader, CLIPTextEncode, ModelSamplingSD3, PathchSageAttentionKJ, ModelSamplingSD3, VAELoader, VAEDecode, EmptyHunyuanLatentVideo, easy cleanGpuUsed, CLIPTextEncode, ModelPatchTorchSettings, UNETLoader, ModelPatchTorchSettings, LoraLoaderModelOnly, KSamplerAdvanced, KSamplerAdvanced, LoraLoaderModelOnly, Note, VHS_VideoCombine]
patterns: []
missing: [easy cleanGpuUsed]
parameters: {"cfg": 6, "denoise": "simple", "sampler_name": 1, "scheduler": "euler", "seed": "disable", "steps": "fixed"}
discoveries: [次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识]
---

# 视频生成/文生视频/Wan2.2文生视频-高质量_1994736642340556801.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/Wan2.2文生视频-高质量_1994736642340556801.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Other

**节点**（21 个）：
- `CLIPLoader`
- `PathchSageAttentionKJ`
- `UNETLoader` ★核心
- `CLIPTextEncode` ★核心
- `ModelSamplingSD3`
- `PathchSageAttentionKJ`
- `ModelSamplingSD3`
- `VAELoader`
- `VAEDecode` ★核心
- `EmptyHunyuanLatentVideo`
- `easy cleanGpuUsed`
- `CLIPTextEncode` ★核心
- `ModelPatchTorchSettings`
- `UNETLoader` ★核心
- `ModelPatchTorchSettings`
- `LoraLoaderModelOnly` ★核心
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `LoraLoaderModelOnly` ★核心
- `Note`
- `VHS_VideoCombine`

## 关键参数

- `seed` = `disable`
- `steps` = `fixed`
- `cfg` = `6`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `simple`

## 知识

覆盖率 **90%**（19/21）

**有卡**：`CLIPLoader`、`PathchSageAttentionKJ`、`UNETLoader`、`CLIPTextEncode`、`ModelSamplingSD3`、`VAELoader`、`VAEDecode`、`EmptyHunyuanLatentVideo`、`ModelPatchTorchSettings`、`LoraLoaderModelOnly`、`KSamplerAdvanced`、`VHS_VideoCombine`

**缺卡**（1）：`easy cleanGpuUsed`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、UNETLoader、KSamplerAdvanced、EmptyHunyuanLatentVideo

## 学习发现

- 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识

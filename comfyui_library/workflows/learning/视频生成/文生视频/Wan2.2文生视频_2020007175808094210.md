---
key: 视频生成/文生视频/Wan2.2文生视频_2020007175808094210.json
name: Wan2.2文生视频_2020007175808094210
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/Wan2.2文生视频_2020007175808094210.json
hash: b0417fece7550cc4
coverage: 0.958333
learned_at: 2026-10-15 22:47:15
nodes: [CLIPLoader, UNETLoader, CLIPTextEncode, ModelSamplingSD3, PathchSageAttentionKJ, ModelSamplingSD3, VAELoader, VAEDecode, easy cleanGpuUsed, ModelPatchTorchSettings, UNETLoader, ModelPatchTorchSettings, LoraLoaderModelOnly, KSamplerAdvanced, KSamplerAdvanced, PathchSageAttentionKJ, LoraLoaderModelOnly, Int, Int, MathExpression|pysssss, easy showAnything, CLIPTextEncode, EmptyHunyuanLatentVideo, VHS_VideoCombine]
patterns: []
missing: []
parameters: {"cfg": 6, "denoise": "simple", "sampler_name": 1, "scheduler": "euler", "seed": "disable", "steps": "fixed"}
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

覆盖率 **96%**（23/24）

**有卡**：`CLIPLoader`、`UNETLoader`、`CLIPTextEncode`、`ModelSamplingSD3`、`PathchSageAttentionKJ`、`VAELoader`、`VAEDecode`、`easy cleanGpuUsed`、`ModelPatchTorchSettings`、`LoraLoaderModelOnly`、`KSamplerAdvanced`、`Int`、`MathExpression|pysssss`、`EmptyHunyuanLatentVideo`、`VHS_VideoCombine`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、UNETLoader、KSamplerAdvanced、EmptyHunyuanLatentVideo

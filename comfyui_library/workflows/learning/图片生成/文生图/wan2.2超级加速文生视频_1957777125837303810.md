---
key: 图片生成/文生图/wan2.2超级加速文生视频_1957777125837303810.json
name: wan2.2超级加速文生视频_1957777125837303810.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/wan2.2超级加速文生视频_1957777125837303810.json
hash: d21033698ce25374
coverage: 1
learned_at: 2026-10-07 23:31:16
nodes: [CLIPLoader, VAELoader, VAEDecode, SaveVideo, CreateVideo, UNETLoader, UNETLoader, LoraLoaderModelOnly, PathchSageAttentionKJ, LoraLoaderModelOnly, PathchSageAttentionKJ, ModelPatchTorchSettings, EmptyHunyuanLatentVideo, ModelSamplingSD3, ModelSamplingSD3, CLIPTextEncode, CLIPTextEncode, ModelPatchTorchSettings, KSamplerAdvanced, KSamplerAdvanced]
patterns: []
missing: []
parameters: {"cfg": 10, "denoise": "beta", "sampler_name": 1, "scheduler": "euler", "seed": "disable", "steps": "fixed"}
---

# 图片生成/文生图/wan2.2超级加速文生视频_1957777125837303810.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/1957777125837303810.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Output → Other

**节点**（20 个）：
- `CLIPLoader`
- `VAELoader`
- `VAEDecode` ★核心
- `SaveVideo`
- `CreateVideo`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `PathchSageAttentionKJ`
- `LoraLoaderModelOnly` ★核心
- `PathchSageAttentionKJ`
- `ModelPatchTorchSettings`
- `EmptyHunyuanLatentVideo`
- `ModelSamplingSD3`
- `ModelSamplingSD3`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `ModelPatchTorchSettings`
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心

## 关键参数

- `seed` = `disable`
- `steps` = `fixed`
- `cfg` = `10`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `beta`

## 知识

覆盖率 **100%**（20/20）

**有卡**：`CLIPLoader`、`VAELoader`、`VAEDecode`、`SaveVideo`、`CreateVideo`、`UNETLoader`、`LoraLoaderModelOnly`、`PathchSageAttentionKJ`、`ModelPatchTorchSettings`、`EmptyHunyuanLatentVideo`、`ModelSamplingSD3`、`CLIPTextEncode`、`KSamplerAdvanced`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、UNETLoader、KSamplerAdvanced、EmptyHunyuanLatentVideo

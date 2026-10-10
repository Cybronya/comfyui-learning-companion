---
key: 视频生成/文生视频/Wan2.2-T2V-A14B-4steps-250928-dyno-NativeComfy_1974515256741507074.json
name: Wan2.2-T2V-A14B-4steps-250928-dyno-NativeComfy_1974515256741507074
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/Wan2.2-T2V-A14B-4steps-250928-dyno-NativeComfy_1974515256741507074.json
hash: a9ade7d350da21cc
coverage: 0.823529
learned_at: 2026-10-10 23:07:16
nodes: [CLIPTextEncode, Note, MarkdownNote, ModelSamplingSD3, Note, ModelSamplingSD3, KSamplerAdvanced, KSamplerAdvanced, VHS_VideoCombine, CLIPTextEncode, UNETLoader, CLIPLoader, VAELoader, UNETLoader, LoraLoaderModelOnly, EmptyHunyuanLatentVideo, VAEDecode]
patterns: []
missing: []
parameters: {"cfg": 6, "denoise": "simple", "sampler_name": 1, "scheduler": "euler", "seed": "enable", "steps": "randomize"}
---

# 视频生成/文生视频/Wan2.2-T2V-A14B-4steps-250928-dyno-NativeComfy_1974515256741507074.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/Wan2.2-T2V-A14B-4steps-250928-dyno-NativeComfy_1974515256741507074.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Other

**节点**（17 个）：
- `CLIPTextEncode` ★核心
- `Note`
- `MarkdownNote`
- `ModelSamplingSD3`
- `Note`
- `ModelSamplingSD3`
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `VHS_VideoCombine`
- `CLIPTextEncode` ★核心
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `EmptyHunyuanLatentVideo`
- `VAEDecode` ★核心

## 关键参数

- `seed` = `enable`
- `steps` = `randomize`
- `cfg` = `6`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `simple`

## 知识

覆盖率 **82%**（14/17）

**有卡**：`CLIPTextEncode`、`ModelSamplingSD3`、`KSamplerAdvanced`、`VHS_VideoCombine`、`UNETLoader`、`CLIPLoader`、`VAELoader`、`LoraLoaderModelOnly`、`EmptyHunyuanLatentVideo`、`VAEDecode`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、UNETLoader、KSamplerAdvanced、EmptyHunyuanLatentVideo

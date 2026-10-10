---
key: 视频生成/文生视频/wan2.2最新加速文生图250928-dyno损失小_1972558589065949185.json
name: wan2.2最新加速文生图250928-dyno损失小_1972558589065949185
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/wan2.2最新加速文生图250928-dyno损失小_1972558589065949185.json
hash: 1d183a7856700560
coverage: 0.833333
learned_at: 2026-10-10 23:09:49
nodes: [CLIPTextEncode, Note, VAEDecode, ModelSamplingSD3, EmptyHunyuanLatentVideo, CLIPTextEncode, KSamplerAdvanced, KSamplerAdvanced, UNETLoader, ModelSamplingSD3, UNETLoader, LoraLoaderModelOnly, CLIPLoader, VAELoader, MarkdownNote, Note, CreateVideo, SaveVideo]
patterns: []
missing: []
parameters: {"cfg": 4, "denoise": "simple", "sampler_name": 1, "scheduler": "euler", "seed": "disable", "steps": "fixed"}
---

# 视频生成/文生视频/wan2.2最新加速文生图250928-dyno损失小_1972558589065949185.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/wan2.2最新加速文生图250928-dyno损失小_1972558589065949185.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Output → Other

**节点**（18 个）：
- `CLIPTextEncode` ★核心
- `Note`
- `VAEDecode` ★核心
- `ModelSamplingSD3`
- `EmptyHunyuanLatentVideo`
- `CLIPTextEncode` ★核心
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `UNETLoader` ★核心
- `ModelSamplingSD3`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `CLIPLoader`
- `VAELoader`
- `MarkdownNote`
- `Note`
- `CreateVideo`
- `SaveVideo`

## 关键参数

- `seed` = `disable`
- `steps` = `fixed`
- `cfg` = `4`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `simple`

## 知识

覆盖率 **83%**（15/18）

**有卡**：`CLIPTextEncode`、`VAEDecode`、`ModelSamplingSD3`、`EmptyHunyuanLatentVideo`、`KSamplerAdvanced`、`UNETLoader`、`LoraLoaderModelOnly`、`CLIPLoader`、`VAELoader`、`CreateVideo`、`SaveVideo`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、UNETLoader、KSamplerAdvanced、EmptyHunyuanLatentVideo

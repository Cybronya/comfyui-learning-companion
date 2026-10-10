---
key: 视频生成/文生视频/Wan2.2 dyno高噪文生视频极速版V2（官方版）_1974800997673512961.json
name: Wan2.2 dyno高噪文生视频极速版V2（官方版）_1974800997673512961
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/Wan2.2 dyno高噪文生视频极速版V2（官方版）_1974800997673512961.json
hash: e1b11ecdfe350c2a
coverage: 0.833333
learned_at: 2026-10-10 23:06:58
nodes: [VAELoader, CLIPTextEncode, Note, CreateVideo, VAEDecode, MarkdownNote, ModelSamplingSD3, CLIPLoader, ModelSamplingSD3, Note, EmptyHunyuanLatentVideo, KSamplerAdvanced, UNETLoader, UNETLoader, LoraLoaderModelOnly, KSamplerAdvanced, SaveVideo, LoraLoaderModelOnly, LoraLoaderModelOnly, JWInteger, JWInteger, JWInteger, CLIPTextEncode, CR Prompt Text]
patterns: []
missing: [CR Prompt Text]
parameters: {"cfg": 4, "denoise": "simple", "sampler_name": 1, "scheduler": "euler", "seed": "enable", "steps": "fixed"}
discoveries: [次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明]
---

# 视频生成/文生视频/Wan2.2 dyno高噪文生视频极速版V2（官方版）_1974800997673512961.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/Wan2.2 dyno高噪文生视频极速版V2（官方版）_1974800997673512961.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Output → Other

**节点**（24 个）：
- `VAELoader`
- `CLIPTextEncode` ★核心
- `Note`
- `CreateVideo`
- `VAEDecode` ★核心
- `MarkdownNote`
- `ModelSamplingSD3`
- `CLIPLoader`
- `ModelSamplingSD3`
- `Note`
- `EmptyHunyuanLatentVideo`
- `KSamplerAdvanced` ★核心
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `KSamplerAdvanced` ★核心
- `SaveVideo`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `JWInteger`
- `JWInteger`
- `JWInteger`
- `CLIPTextEncode` ★核心
- `CR Prompt Text`

## 关键参数

- `seed` = `enable`
- `steps` = `fixed`
- `cfg` = `4`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `simple`

## 知识

覆盖率 **83%**（20/24）

**有卡**：`VAELoader`、`CLIPTextEncode`、`CreateVideo`、`VAEDecode`、`ModelSamplingSD3`、`CLIPLoader`、`EmptyHunyuanLatentVideo`、`KSamplerAdvanced`、`UNETLoader`、`LoraLoaderModelOnly`、`SaveVideo`、`JWInteger`

**缺卡**（1）：`CR Prompt Text`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、UNETLoader、KSamplerAdvanced、EmptyHunyuanLatentVideo

## 学习发现

- 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明

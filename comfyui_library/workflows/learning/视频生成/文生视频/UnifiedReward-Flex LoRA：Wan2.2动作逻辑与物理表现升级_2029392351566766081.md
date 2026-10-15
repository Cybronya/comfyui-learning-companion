---
key: 视频生成/文生视频/UnifiedReward-Flex LoRA：Wan2.2动作逻辑与物理表现升级_2029392351566766081.json
name: UnifiedReward-Flex LoRA：Wan2.2动作逻辑与物理表现升级_2029392351566766081
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/UnifiedReward-Flex LoRA：Wan2.2动作逻辑与物理表现升级_2029392351566766081.json
hash: e52292205d264ae0
coverage: 0.9
learned_at: 2026-10-15 22:47:02
nodes: [VAELoader, SaveVideo, VAEDecode, MarkdownNote, UNETLoader, UNETLoader, CLIPLoader, CLIPTextEncode, KSamplerAdvanced, LoraLoaderModelOnly, EmptyHunyuanLatentVideo, KSamplerAdvanced, LoraLoaderModelOnly, LoraLoaderModelOnly, MarkdownNote, ModelSamplingSD3, ModelSamplingSD3, CreateVideo, CLIPTextEncode, LoraLoaderModelOnly]
patterns: []
missing: []
parameters: {"cfg": 6, "denoise": "simple", "sampler_name": 1, "scheduler": "euler", "seed": "enable", "steps": "fixed"}
---

# 视频生成/文生视频/UnifiedReward-Flex LoRA：Wan2.2动作逻辑与物理表现升级_2029392351566766081.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/UnifiedReward-Flex LoRA：Wan2.2动作逻辑与物理表现升级_2029392351566766081.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Output → Other

**节点**（20 个）：
- `VAELoader`
- `SaveVideo`
- `VAEDecode` ★核心
- `MarkdownNote`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `CLIPLoader`
- `CLIPTextEncode` ★核心
- `KSamplerAdvanced` ★核心
- `LoraLoaderModelOnly` ★核心
- `EmptyHunyuanLatentVideo`
- `KSamplerAdvanced` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `MarkdownNote`
- `ModelSamplingSD3`
- `ModelSamplingSD3`
- `CreateVideo`
- `CLIPTextEncode` ★核心
- `LoraLoaderModelOnly` ★核心

## 关键参数

- `seed` = `enable`
- `steps` = `fixed`
- `cfg` = `6`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `simple`

## 知识

覆盖率 **90%**（18/20）

**有卡**：`VAELoader`、`SaveVideo`、`VAEDecode`、`UNETLoader`、`CLIPLoader`、`CLIPTextEncode`、`KSamplerAdvanced`、`LoraLoaderModelOnly`、`EmptyHunyuanLatentVideo`、`ModelSamplingSD3`、`CreateVideo`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、UNETLoader、KSamplerAdvanced、EmptyHunyuanLatentVideo

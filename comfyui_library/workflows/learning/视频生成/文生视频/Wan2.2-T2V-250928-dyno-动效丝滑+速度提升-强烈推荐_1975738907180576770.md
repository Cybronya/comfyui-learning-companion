---
key: 视频生成/文生视频/Wan2.2-T2V-250928-dyno-动效丝滑+速度提升-强烈推荐_1975738907180576770.json
name: Wan2.2-T2V-250928-dyno-动效丝滑+速度提升-强烈推荐_1975738907180576770
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/Wan2.2-T2V-250928-dyno-动效丝滑+速度提升-强烈推荐_1975738907180576770.json
hash: d7b7a014e43394a2
coverage: 0.777778
learned_at: 2026-10-10 23:07:15
nodes: [CLIPTextEncode, Note, MarkdownNote, ModelSamplingSD3, EmptyHunyuanLatentVideo, VAEDecode, ModelSamplingSD3, CLIPTextEncode, KSamplerAdvanced, KSamplerAdvanced, Note, easy int, UNETLoader, UNETLoader, LoraLoaderModelOnly, CLIPLoader, VAELoader, VHS_VideoCombine]
patterns: []
missing: [easy int]
parameters: {"cfg": 6, "denoise": "simple", "sampler_name": 1, "scheduler": "euler", "seed": "disable", "steps": "fixed"}
discoveries: [次要节点 `easy int` 知识库中没有该节点类型的任何知识]
---

# 视频生成/文生视频/Wan2.2-T2V-250928-dyno-动效丝滑+速度提升-强烈推荐_1975738907180576770.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/Wan2.2-T2V-250928-dyno-动效丝滑+速度提升-强烈推荐_1975738907180576770.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Other

**节点**（18 个）：
- `CLIPTextEncode` ★核心
- `Note`
- `MarkdownNote`
- `ModelSamplingSD3`
- `EmptyHunyuanLatentVideo`
- `VAEDecode` ★核心
- `ModelSamplingSD3`
- `CLIPTextEncode` ★核心
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `Note`
- `easy int`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `CLIPLoader`
- `VAELoader`
- `VHS_VideoCombine`

## 关键参数

- `seed` = `disable`
- `steps` = `fixed`
- `cfg` = `6`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `simple`

## 知识

覆盖率 **78%**（14/18）

**有卡**：`CLIPTextEncode`、`ModelSamplingSD3`、`EmptyHunyuanLatentVideo`、`VAEDecode`、`KSamplerAdvanced`、`UNETLoader`、`LoraLoaderModelOnly`、`CLIPLoader`、`VAELoader`、`VHS_VideoCombine`

**缺卡**（1）：`easy int`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、UNETLoader、KSamplerAdvanced、EmptyHunyuanLatentVideo

## 学习发现

- 次要节点 `easy int` 知识库中没有该节点类型的任何知识

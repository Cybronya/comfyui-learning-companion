---
key: 视频生成/文生视频/UnifiedReward-Flex LoRA-Wan2.2-动作优化-文生视频_2031576870059249666.json
name: UnifiedReward-Flex LoRA-Wan2.2-动作优化-文生视频_2031576870059249666
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/UnifiedReward-Flex LoRA-Wan2.2-动作优化-文生视频_2031576870059249666.json
hash: 4ee7f269a9cef3be
coverage: 0.851852
learned_at: 2026-10-11 03:16:49
nodes: [VAELoader, UNETLoader, UNETLoader, CLIPLoader, ModelSamplingSD3, CLIPTextEncode, KSamplerAdvanced, LoraLoaderModelOnly, EmptyHunyuanLatentVideo, KSamplerAdvanced, ModelSamplingSD3, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, MarkdownNote, CLIPTextEncode, VAEDecode, CreateVideo, VHS_VideoCombine, SaveVideo, Int, Int, Int, MarkdownNote, SimpleMath+, JjkText, CustomAddLabel]
patterns: []
missing: [SimpleMath+]
parameters: {"cfg": 6, "denoise": "simple", "sampler_name": 1, "scheduler": "euler", "seed": "enable", "steps": "fixed"}
discoveries: [次要节点 `SimpleMath+` 知识库中没有该节点类型的任何知识]
---

# 视频生成/文生视频/UnifiedReward-Flex LoRA-Wan2.2-动作优化-文生视频_2031576870059249666.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/UnifiedReward-Flex LoRA-Wan2.2-动作优化-文生视频_2031576870059249666.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Output → Other

**节点**（27 个）：
- `VAELoader`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `CLIPLoader`
- `ModelSamplingSD3`
- `CLIPTextEncode` ★核心
- `KSamplerAdvanced` ★核心
- `LoraLoaderModelOnly` ★核心
- `EmptyHunyuanLatentVideo`
- `KSamplerAdvanced` ★核心
- `ModelSamplingSD3`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `MarkdownNote`
- `CLIPTextEncode` ★核心
- `VAEDecode` ★核心
- `CreateVideo`
- `VHS_VideoCombine`
- `SaveVideo`
- `Int`
- `Int`
- `Int`
- `MarkdownNote`
- `SimpleMath+`
- `JjkText`
- `CustomAddLabel`

## 关键参数

- `seed` = `enable`
- `steps` = `fixed`
- `cfg` = `6`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `simple`

## 知识

覆盖率 **85%**（23/27）

**有卡**：`VAELoader`、`UNETLoader`、`CLIPLoader`、`ModelSamplingSD3`、`CLIPTextEncode`、`KSamplerAdvanced`、`LoraLoaderModelOnly`、`EmptyHunyuanLatentVideo`、`VAEDecode`、`CreateVideo`、`VHS_VideoCombine`、`SaveVideo`、`Int`、`CustomAddLabel`

**缺卡**（1）：`SimpleMath+`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、UNETLoader、KSamplerAdvanced、EmptyHunyuanLatentVideo

## 学习发现

- 次要节点 `SimpleMath+` 知识库中没有该节点类型的任何知识

---
key: 视频生成/文生视频/Wan2.2-4steps-250928-dyno-high-lightx2v-文生视频_1976432692420059138.json
name: Wan2.2-4steps-250928-dyno-high-lightx2v-文生视频_1976432692420059138
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/Wan2.2-4steps-250928-dyno-high-lightx2v-文生视频_1976432692420059138.json
hash: abcc66a2b9ca3405
coverage: 0.769231
learned_at: 2026-10-10 23:07:07
nodes: [CLIPTextEncode, Note, MarkdownNote, ModelSamplingSD3, Note, ModelSamplingSD3, KSamplerAdvanced, KSamplerAdvanced, CLIPLoader, VAELoader, UNETLoader, LoraLoaderModelOnly, VAEDecode, EmptyHunyuanLatentVideo, Int, SimpleMath+, Int, CLIPTextEncode, ImageResizeKJv2, LoadImage, ImageConcatMulti, Int, GetNode, UNETLoader, VHS_VideoCombine, SetNode]
patterns: []
missing: [SimpleMath+]
parameters: {"cfg": 6, "denoise": "simple", "sampler_name": 1, "scheduler": "euler", "seed": "enable", "steps": "randomize"}
discoveries: [次要节点 `SimpleMath+` 知识库中没有该节点类型的任何知识]
---

# 视频生成/文生视频/Wan2.2-4steps-250928-dyno-high-lightx2v-文生视频_1976432692420059138.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/Wan2.2-4steps-250928-dyno-high-lightx2v-文生视频_1976432692420059138.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（26 个）：
- `CLIPTextEncode` ★核心
- `Note`
- `MarkdownNote`
- `ModelSamplingSD3`
- `Note`
- `ModelSamplingSD3`
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `CLIPLoader`
- `VAELoader`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `VAEDecode` ★核心
- `EmptyHunyuanLatentVideo`
- `Int`
- `SimpleMath+`
- `Int`
- `CLIPTextEncode` ★核心
- `ImageResizeKJv2`
- `LoadImage`
- `ImageConcatMulti`
- `Int`
- `GetNode`
- `UNETLoader` ★核心
- `VHS_VideoCombine`
- `SetNode`

## 关键参数

- `seed` = `enable`
- `steps` = `randomize`
- `cfg` = `6`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `simple`

## 知识

覆盖率 **77%**（20/26）

**有卡**：`CLIPTextEncode`、`ModelSamplingSD3`、`KSamplerAdvanced`、`CLIPLoader`、`VAELoader`、`UNETLoader`、`LoraLoaderModelOnly`、`VAEDecode`、`EmptyHunyuanLatentVideo`、`Int`、`ImageResizeKJv2`、`LoadImage`、`ImageConcatMulti`、`VHS_VideoCombine`

**缺卡**（1）：`SimpleMath+`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerAdvanced

## 学习发现

- 次要节点 `SimpleMath+` 知识库中没有该节点类型的任何知识

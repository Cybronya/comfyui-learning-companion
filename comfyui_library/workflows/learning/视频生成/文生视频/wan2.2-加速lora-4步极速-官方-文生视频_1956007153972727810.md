---
key: 视频生成/文生视频/wan2.2-加速lora-4步极速-官方-文生视频_1956007153972727810.json
name: wan2.2-加速lora-4步极速-官方-文生视频_1956007153972727810.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/wan2.2-加速lora-4步极速-官方-文生视频_1956007153972727810.json
hash: 8ea5674c49d84a15
coverage: 0.909091
learned_at: 2026-10-15 22:43:40
nodes: [CLIPLoader, VAELoader, UNETLoader, VAEDecode, CreateVideo, UNETLoader, ModelSamplingSD3, ModelSamplingSD3, MarkdownNote, MarkdownNote, SaveVideo, KSamplerAdvanced, LoraLoaderModelOnly, LoraLoaderModelOnly, EmptyHunyuanLatentVideo, Int, SimpleMath+, Int, Int, KSamplerAdvanced, CLIPTextEncode, CLIPTextEncode]
patterns: []
missing: []
parameters: {"cfg": 4, "denoise": "simple", "sampler_name": 1, "scheduler": "euler", "seed": "disable", "steps": "fixed"}
---

# 视频生成/文生视频/wan2.2-加速lora-4步极速-官方-文生视频_1956007153972727810.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/1956007153972727810.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Output → Other

**节点**（22 个）：
- `CLIPLoader`
- `VAELoader`
- `UNETLoader` ★核心
- `VAEDecode` ★核心
- `CreateVideo`
- `UNETLoader` ★核心
- `ModelSamplingSD3`
- `ModelSamplingSD3`
- `MarkdownNote`
- `MarkdownNote`
- `SaveVideo`
- `KSamplerAdvanced` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `EmptyHunyuanLatentVideo`
- `Int`
- `SimpleMath+`
- `Int`
- `Int`
- `KSamplerAdvanced` ★核心
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心

## 关键参数

- `seed` = `disable`
- `steps` = `fixed`
- `cfg` = `4`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `simple`

## 知识

覆盖率 **91%**（20/22）

**有卡**：`CLIPLoader`、`VAELoader`、`UNETLoader`、`VAEDecode`、`CreateVideo`、`ModelSamplingSD3`、`SaveVideo`、`KSamplerAdvanced`、`LoraLoaderModelOnly`、`EmptyHunyuanLatentVideo`、`Int`、`SimpleMath+`、`CLIPTextEncode`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、UNETLoader、KSamplerAdvanced、EmptyHunyuanLatentVideo

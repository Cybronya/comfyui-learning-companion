---
key: 视频生成/文生视频/文生视频（解禁模型）：Wan2.2_Remix_2068556222554533890.json
name: 文生视频（解禁模型）：Wan2.2_Remix_2068556222554533890
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/文生视频（解禁模型）：Wan2.2_Remix_2068556222554533890.json
hash: 954e50f990cde652
coverage: 1
learned_at: 2026-10-15 22:48:45
nodes: [UNETLoader, UNETLoader, CLIPLoader, VAELoader, EmptyHunyuanLatentVideo, LoraLoaderModelOnly, ModelSamplingSD3, LoraLoaderModelOnly, ModelSamplingSD3, CLIPTextEncode, KSamplerAdvanced, KSamplerAdvanced, CreateVideo, VAEDecode, SaveVideo, CLIPTextEncode]
patterns: []
missing: []
parameters: {"cfg": 4, "denoise": "simple", "sampler_name": 1, "scheduler": "euler", "seed": "disable", "steps": "fixed"}
---

# 视频生成/文生视频/文生视频（解禁模型）：Wan2.2_Remix_2068556222554533890.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/文生视频（解禁模型）：Wan2.2_Remix_2068556222554533890.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Output → Other

**节点**（16 个）：
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `EmptyHunyuanLatentVideo`
- `LoraLoaderModelOnly` ★核心
- `ModelSamplingSD3`
- `LoraLoaderModelOnly` ★核心
- `ModelSamplingSD3`
- `CLIPTextEncode` ★核心
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `CreateVideo`
- `VAEDecode` ★核心
- `SaveVideo`
- `CLIPTextEncode` ★核心

## 关键参数

- `seed` = `disable`
- `steps` = `fixed`
- `cfg` = `4`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `simple`

## 知识

覆盖率 **100%**（16/16）

**有卡**：`UNETLoader`、`CLIPLoader`、`VAELoader`、`EmptyHunyuanLatentVideo`、`LoraLoaderModelOnly`、`ModelSamplingSD3`、`CLIPTextEncode`、`KSamplerAdvanced`、`CreateVideo`、`VAEDecode`、`SaveVideo`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、UNETLoader、KSamplerAdvanced、EmptyHunyuanLatentVideo

---
key: 视频生成/文生视频/UnifiedReward-Flex LoRA实测：Wan2.2动作逻辑与物理表现提升_2029085278756937729.json
name: UnifiedReward-Flex LoRA实测：Wan2.2动作逻辑与物理表现提升_2029085278756937729
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/UnifiedReward-Flex LoRA实测：Wan2.2动作逻辑与物理表现提升_2029085278756937729.json
hash: 5de8bf96d96703f3
coverage: 0.909091
learned_at: 2026-10-15 22:47:02
nodes: [VAELoader, MarkdownNote, CreateVideo, SaveVideo, VAEDecode, MarkdownNote, UNETLoader, UNETLoader, CLIPLoader, ModelSamplingSD3, CLIPTextEncode, KSamplerAdvanced, LoraLoaderModelOnly, CLIPTextEncode, EmptyHunyuanLatentVideo, KSamplerAdvanced, ModelSamplingSD3, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, Label (rgthree), Label (rgthree)]
patterns: []
missing: []
parameters: {"cfg": 6, "denoise": "simple", "sampler_name": 1, "scheduler": "euler", "seed": "enable", "steps": "fixed"}
---

# 视频生成/文生视频/UnifiedReward-Flex LoRA实测：Wan2.2动作逻辑与物理表现提升_2029085278756937729.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/UnifiedReward-Flex LoRA实测：Wan2.2动作逻辑与物理表现提升_2029085278756937729.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Output → Other

**节点**（22 个）：
- `VAELoader`
- `MarkdownNote`
- `CreateVideo`
- `SaveVideo`
- `VAEDecode` ★核心
- `MarkdownNote`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `CLIPLoader`
- `ModelSamplingSD3`
- `CLIPTextEncode` ★核心
- `KSamplerAdvanced` ★核心
- `LoraLoaderModelOnly` ★核心
- `CLIPTextEncode` ★核心
- `EmptyHunyuanLatentVideo`
- `KSamplerAdvanced` ★核心
- `ModelSamplingSD3`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `Label (rgthree)`
- `Label (rgthree)`

## 关键参数

- `seed` = `enable`
- `steps` = `fixed`
- `cfg` = `6`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `simple`

## 知识

覆盖率 **91%**（20/22）

**有卡**：`VAELoader`、`CreateVideo`、`SaveVideo`、`VAEDecode`、`UNETLoader`、`CLIPLoader`、`ModelSamplingSD3`、`CLIPTextEncode`、`KSamplerAdvanced`、`LoraLoaderModelOnly`、`EmptyHunyuanLatentVideo`、`Label (rgthree)`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、UNETLoader、KSamplerAdvanced、EmptyHunyuanLatentVideo

---
key: 平台全量/Wan2.2 文生视频_2059204209505030146.json
name: Wan2.2 文生视频_2059204209505030146
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/Wan2.2 文生视频_2059204209505030146.json
hash: 00f74b08f1f7dca7
coverage: 0.545455
learned_at: 2026-11-14 01:05:46
nodes: [MarkdownNote, MarkdownNote, CLIPLoader, VAELoader, UNETLoader, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, ModelSamplingSD3, ModelSamplingSD3, CLIPTextEncode, KSamplerAdvanced, CreateVideo, VAEDecode, CLIPTextEncode, EmptyHunyuanLatentVideo, KSamplerAdvanced, PrimitiveInt, PrimitiveInt, PrimitiveInt, PrimitiveInt, PrimitiveFloat, PrimitiveFloat, ComfySwitchNode, ComfySwitchNode, ComfySwitchNode, ComfySwitchNode, ComfySwitchNode, PrimitiveFloat, PrimitiveFloat, PrimitiveBoolean, ComfyMathExpression, SaveVideo]
patterns: []
missing: []
parameters: {"cfg": 4, "denoise": "simple", "sampler_name": 1, "scheduler": "euler", "seed": "disable", "steps": "fixed"}
---

# 平台全量/Wan2.2 文生视频_2059204209505030146.json

> 来源文件 `comfyui_library/workflows/平台全量/Wan2.2 文生视频_2059204209505030146.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Output → Other

**节点**（33 个）：
- `MarkdownNote`
- `MarkdownNote`
- `CLIPLoader`
- `VAELoader`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `ModelSamplingSD3`
- `ModelSamplingSD3`
- `CLIPTextEncode` ★核心
- `KSamplerAdvanced` ★核心
- `CreateVideo`
- `VAEDecode` ★核心
- `CLIPTextEncode` ★核心
- `EmptyHunyuanLatentVideo`
- `KSamplerAdvanced` ★核心
- `PrimitiveInt`
- `PrimitiveInt`
- `PrimitiveInt`
- `PrimitiveInt`
- `PrimitiveFloat`
- `PrimitiveFloat`
- `ComfySwitchNode`
- `ComfySwitchNode`
- `ComfySwitchNode`
- `ComfySwitchNode`
- `ComfySwitchNode`
- `PrimitiveFloat`
- `PrimitiveFloat`
- `PrimitiveBoolean`
- `ComfyMathExpression`
- `SaveVideo`

## 关键参数

- `seed` = `disable`
- `steps` = `fixed`
- `cfg` = `4`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `simple`

## 知识

覆盖率 **55%**（18/33）

**有卡**：`CLIPLoader`、`VAELoader`、`UNETLoader`、`LoraLoaderModelOnly`、`ModelSamplingSD3`、`CLIPTextEncode`、`KSamplerAdvanced`、`CreateVideo`、`VAEDecode`、`EmptyHunyuanLatentVideo`、`PrimitiveBoolean`、`ComfyMathExpression`、`SaveVideo`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、CLIPTextEncode、UNETLoader、KSamplerAdvanced、EmptyHunyuanLatentVideo

---
key: 平台全量/Wan2.2 图生视频_2059204223493042177.json
name: Wan2.2 图生视频_2059204223493042177
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/Wan2.2 图生视频_2059204223493042177.json
hash: 4582b38c478c7a3d
coverage: 0.542857
learned_at: 2026-11-14 01:05:44
nodes: [MarkdownNote, MarkdownNote, LoadImage, SaveVideo, MarkdownNote, WanImageToVideo, CreateVideo, ModelSamplingSD3, CLIPTextEncode, PrimitiveInt, VAEDecode, CLIPTextEncode, PrimitiveBoolean, VAELoader, CLIPLoader, UNETLoader, UNETLoader, PrimitiveInt, PrimitiveFloat, LoraLoaderModelOnly, LoraLoaderModelOnly, KSamplerAdvanced, KSamplerAdvanced, PrimitiveFloat, PrimitiveInt, PrimitiveInt, ComfySwitchNode, ComfySwitchNode, ComfySwitchNode, ComfySwitchNode, ModelSamplingSD3, ComfySwitchNode, PrimitiveFloat, PrimitiveFloat, ComfyMathExpression]
patterns: []
missing: []
parameters: {"cfg": 4, "denoise": "simple", "sampler_name": 1, "scheduler": "euler", "seed": "disable", "steps": "fixed"}
---

# 平台全量/Wan2.2 图生视频_2059204223493042177.json

> 来源文件 `comfyui_library/workflows/平台全量/Wan2.2 图生视频_2059204223493042177.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Output → Other

**节点**（35 个）：
- `MarkdownNote`
- `MarkdownNote`
- `LoadImage`
- `SaveVideo`
- `MarkdownNote`
- `WanImageToVideo`
- `CreateVideo`
- `ModelSamplingSD3`
- `CLIPTextEncode` ★核心
- `PrimitiveInt`
- `VAEDecode` ★核心
- `CLIPTextEncode` ★核心
- `PrimitiveBoolean`
- `VAELoader`
- `CLIPLoader`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `PrimitiveInt`
- `PrimitiveFloat`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `PrimitiveFloat`
- `PrimitiveInt`
- `PrimitiveInt`
- `ComfySwitchNode`
- `ComfySwitchNode`
- `ComfySwitchNode`
- `ComfySwitchNode`
- `ModelSamplingSD3`
- `ComfySwitchNode`
- `PrimitiveFloat`
- `PrimitiveFloat`
- `ComfyMathExpression`

## 关键参数

- `seed` = `disable`
- `steps` = `fixed`
- `cfg` = `4`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `simple`

## 知识

覆盖率 **54%**（19/35）

**有卡**：`LoadImage`、`SaveVideo`、`WanImageToVideo`、`CreateVideo`、`ModelSamplingSD3`、`CLIPTextEncode`、`VAEDecode`、`PrimitiveBoolean`、`VAELoader`、`CLIPLoader`、`UNETLoader`、`LoraLoaderModelOnly`、`KSamplerAdvanced`、`ComfyMathExpression`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、CLIPTextEncode、LoadImage、UNETLoader、KSamplerAdvanced

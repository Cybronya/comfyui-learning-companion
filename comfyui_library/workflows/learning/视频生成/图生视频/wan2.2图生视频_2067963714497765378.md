---
key: 视频生成/图生视频/wan2.2图生视频_2067963714497765378.json
name: wan2.2图生视频_2067963714497765378.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2067963714497765378.json
hash: 4daf5f0521a8f475
coverage: 0.558824
learned_at: 2026-10-15 22:40:15
nodes: [MarkdownNote, MarkdownNote, CreateVideo, ModelSamplingSD3, CLIPTextEncode, PrimitiveInt, VAEDecode, PrimitiveBoolean, VAELoader, CLIPLoader, UNETLoader, PrimitiveInt, PrimitiveFloat, LoraLoaderModelOnly, KSamplerAdvanced, KSamplerAdvanced, PrimitiveFloat, PrimitiveInt, ComfySwitchNode, ComfySwitchNode, ComfySwitchNode, ComfySwitchNode, ModelSamplingSD3, ComfySwitchNode, PrimitiveFloat, PrimitiveFloat, ComfyMathExpression, SaveVideo, UNETLoader, LoraLoaderModelOnly, PrimitiveInt, LoadImage, CLIPTextEncode, WanImageToVideo]
patterns: []
missing: []
parameters: {"cfg": 4, "denoise": "simple", "sampler_name": 1, "scheduler": "euler", "seed": "disable", "steps": "fixed"}
---

# 视频生成/图生视频/wan2.2图生视频_2067963714497765378.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2067963714497765378.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Output → Other

**节点**（34 个）：
- `MarkdownNote`
- `MarkdownNote`
- `CreateVideo`
- `ModelSamplingSD3`
- `CLIPTextEncode` ★核心
- `PrimitiveInt`
- `VAEDecode` ★核心
- `PrimitiveBoolean`
- `VAELoader`
- `CLIPLoader`
- `UNETLoader` ★核心
- `PrimitiveInt`
- `PrimitiveFloat`
- `LoraLoaderModelOnly` ★核心
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `PrimitiveFloat`
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
- `SaveVideo`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `PrimitiveInt`
- `LoadImage`
- `CLIPTextEncode` ★核心
- `WanImageToVideo`

## 关键参数

- `seed` = `disable`
- `steps` = `fixed`
- `cfg` = `4`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `simple`

## 知识

覆盖率 **56%**（19/34）

**有卡**：`CreateVideo`、`ModelSamplingSD3`、`CLIPTextEncode`、`VAEDecode`、`PrimitiveBoolean`、`VAELoader`、`CLIPLoader`、`UNETLoader`、`LoraLoaderModelOnly`、`KSamplerAdvanced`、`ComfyMathExpression`、`SaveVideo`、`LoadImage`、`WanImageToVideo`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerAdvanced

---
key: 视频生成/文生视频/wan2.2图生视频工作流_2034905327635795970.json
name: wan2.2图生视频工作流_2034905327635795970
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/wan2.2图生视频工作流_2034905327635795970.json
hash: 35d9718630770e8e
coverage: 0.6
learned_at: 2026-10-15 22:47:36
nodes: [SaveVideo, MarkdownNote, WanImageToVideo, CreateVideo, ModelSamplingSD3, CLIPTextEncode, PrimitiveInt, VAEDecode, CLIPTextEncode, PrimitiveBoolean, VAELoader, CLIPLoader, UNETLoader, UNETLoader, PrimitiveInt, PrimitiveFloat, ComfySwitchNode, ComfySwitchNode, ComfySwitchNode, ComfySwitchNode, LoraLoaderModelOnly, LoraLoaderModelOnly, ComfySwitchNode, ModelSamplingSD3, KSamplerAdvanced, KSamplerAdvanced, PrimitiveFloat, PrimitiveInt, PrimitiveInt, LoadImage]
patterns: []
missing: []
parameters: {"cfg": 4, "denoise": "simple", "sampler_name": 1, "scheduler": "euler", "seed": "disable", "steps": "fixed"}
---

# 视频生成/文生视频/wan2.2图生视频工作流_2034905327635795970.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/wan2.2图生视频工作流_2034905327635795970.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Output → Other

**节点**（30 个）：
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
- `ComfySwitchNode`
- `ComfySwitchNode`
- `ComfySwitchNode`
- `ComfySwitchNode`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `ComfySwitchNode`
- `ModelSamplingSD3`
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `PrimitiveFloat`
- `PrimitiveInt`
- `PrimitiveInt`
- `LoadImage`

## 关键参数

- `seed` = `disable`
- `steps` = `fixed`
- `cfg` = `4`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `simple`

## 知识

覆盖率 **60%**（18/30）

**有卡**：`SaveVideo`、`WanImageToVideo`、`CreateVideo`、`ModelSamplingSD3`、`CLIPTextEncode`、`VAEDecode`、`PrimitiveBoolean`、`VAELoader`、`CLIPLoader`、`UNETLoader`、`LoraLoaderModelOnly`、`KSamplerAdvanced`、`LoadImage`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerAdvanced

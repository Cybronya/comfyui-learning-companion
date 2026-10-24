---
key: 图片生成/图生图/图生视频（解禁模型）：Wan2.2_Remix_2052630486182309890.json
name: 图生视频（解禁模型）：Wan2.2_Remix_2052630486182309890
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/图生视频（解禁模型）：Wan2.2_Remix_2052630486182309890.json
hash: 68b7394b8e9e9fec
coverage: 0.62069
learned_at: 2026-10-23 12:44:10
nodes: [UNETLoader, UNETLoader, CLIPLoader, VAELoader, LoraLoaderModelOnly, CLIPTextEncode, LoraLoaderModelOnly, WanImageToVideo, PrimitiveBoolean, ComfySwitchNode, ComfySwitchNode, PrimitiveInt, PrimitiveInt, PrimitiveFloat, PrimitiveFloat, PrimitiveInt, PrimitiveInt, ModelSamplingSD3, ModelSamplingSD3, ComfySwitchNode, ComfySwitchNode, KSamplerAdvanced, KSamplerAdvanced, VAEDecode, CreateVideo, SaveVideo, ComfySwitchNode, LoadImage, CLIPTextEncode]
patterns: []
missing: []
parameters: {"cfg": 4, "denoise": "simple", "sampler_name": 1, "scheduler": "euler", "seed": "enable", "steps": "randomize"}
---

# 图片生成/图生图/图生视频（解禁模型）：Wan2.2_Remix_2052630486182309890.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/图生视频（解禁模型）：Wan2.2_Remix_2052630486182309890.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Output → Other

**节点**（29 个）：
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `LoraLoaderModelOnly` ★核心
- `CLIPTextEncode` ★核心
- `LoraLoaderModelOnly` ★核心
- `WanImageToVideo`
- `PrimitiveBoolean`
- `ComfySwitchNode`
- `ComfySwitchNode`
- `PrimitiveInt`
- `PrimitiveInt`
- `PrimitiveFloat`
- `PrimitiveFloat`
- `PrimitiveInt`
- `PrimitiveInt`
- `ModelSamplingSD3`
- `ModelSamplingSD3`
- `ComfySwitchNode`
- `ComfySwitchNode`
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `VAEDecode` ★核心
- `CreateVideo`
- `SaveVideo`
- `ComfySwitchNode`
- `LoadImage`
- `CLIPTextEncode` ★核心

## 关键参数

- `seed` = `enable`
- `steps` = `randomize`
- `cfg` = `4`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `simple`

## 知识

覆盖率 **62%**（18/29）

**有卡**：`UNETLoader`、`CLIPLoader`、`VAELoader`、`LoraLoaderModelOnly`、`CLIPTextEncode`、`WanImageToVideo`、`PrimitiveBoolean`、`ModelSamplingSD3`、`KSamplerAdvanced`、`VAEDecode`、`CreateVideo`、`SaveVideo`、`LoadImage`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerAdvanced

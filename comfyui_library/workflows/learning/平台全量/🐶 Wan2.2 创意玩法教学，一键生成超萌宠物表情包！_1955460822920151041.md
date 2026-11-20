---
key: 平台全量/🐶 Wan2.2 创意玩法教学，一键生成超萌宠物表情包！_1955460822920151041.json
name: 🐶 Wan2.2 创意玩法教学，一键生成超萌宠物表情包！_1955460822920151041
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/🐶 Wan2.2 创意玩法教学，一键生成超萌宠物表情包！_1955460822920151041.json
hash: 79b86a7c198dab96
coverage: 0.806452
learned_at: 2026-11-14 02:54:46
nodes: [CLIPLoader, CLIPTextEncode, UNETLoader, UNETLoader, ModelSamplingSD3, ModelSamplingSD3, VAELoader, Note, LoraLoaderModelOnly, KSamplerAdvanced, VAELoader, CLIPLoader, CLIPTextEncode, Note, ModelSamplingAuraFlow, MarkdownNote, KSamplerAdvanced, KSampler, UNETLoader, VAEDecode, SetNode, WanFirstLastFrameToVideo, LoraLoaderModelOnly, EmptySD3LatentImage, VHS_VideoCombine, Note, VAEDecode, PreviewImage, CLIPTextEncode, CLIPTextEncode, Label (rgthree)]
patterns: []
missing: []
parameters: {"cfg": 2.5, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 66, "steps": 20}
---

# 平台全量/🐶 Wan2.2 创意玩法教学，一键生成超萌宠物表情包！_1955460822920151041.json

> 来源文件 `comfyui_library/workflows/平台全量/🐶 Wan2.2 创意玩法教学，一键生成超萌宠物表情包！_1955460822920151041.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（31 个）：
- `CLIPLoader`
- `CLIPTextEncode` ★核心
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `ModelSamplingSD3`
- `ModelSamplingSD3`
- `VAELoader`
- `Note`
- `LoraLoaderModelOnly` ★核心
- `KSamplerAdvanced` ★核心
- `VAELoader`
- `CLIPLoader`
- `CLIPTextEncode` ★核心
- `Note`
- `ModelSamplingAuraFlow`
- `MarkdownNote`
- `KSamplerAdvanced` ★核心
- `KSampler` ★核心
- `UNETLoader` ★核心
- `VAEDecode` ★核心
- `SetNode`
- `WanFirstLastFrameToVideo`
- `LoraLoaderModelOnly` ★核心
- `EmptySD3LatentImage`
- `VHS_VideoCombine`
- `Note`
- `VAEDecode` ★核心
- `PreviewImage`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `Label (rgthree)`

## 关键参数

- `seed` = `66`
- `steps` = `20`
- `cfg` = `2.5`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **81%**（25/31）

**有卡**：`CLIPLoader`、`CLIPTextEncode`、`UNETLoader`、`ModelSamplingSD3`、`VAELoader`、`LoraLoaderModelOnly`、`KSamplerAdvanced`、`ModelSamplingAuraFlow`、`KSampler`、`VAEDecode`、`WanFirstLastFrameToVideo`、`EmptySD3LatentImage`、`VHS_VideoCombine`、`Label (rgthree)`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、CLIPTextEncode、UNETLoader、KSamplerAdvanced

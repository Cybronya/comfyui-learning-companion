---
key: 视频生成/图生视频/wan2.2-360旋转_1955685244381773826.json
name: wan2.2-360旋转_1955685244381773826.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1955685244381773826.json
hash: 22661cc1e077e5da
coverage: 1
learned_at: 2026-10-15 22:31:09
nodes: [CLIPLoader, easy int, KSamplerAdvanced, ModelSamplingSD3, VAELoader, WanImageToVideo, CLIPTextEncode, LoraLoaderModelOnly, SimpleMath+, ModelSamplingSD3, PathchSageAttentionKJ, KSamplerAdvanced, UNETLoader, UNETLoader, PathchSageAttentionKJ, CR Text, CLIPTextEncode, CR Text Concatenate, LoadImage, LoraLoaderModelOnly, VAEDecode, VHS_VideoCombine, easy int, easy int, LoadImage, LoraLoaderModelOnly, CR Text]
patterns: []
missing: []
parameters: {"cfg": 14, "denoise": "simple", "sampler_name": 1, "scheduler": "euler", "seed": "disable", "steps": "randomize"}
---

# 视频生成/图生视频/wan2.2-360旋转_1955685244381773826.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1955685244381773826.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Other

**节点**（27 个）：
- `CLIPLoader`
- `easy int`
- `KSamplerAdvanced` ★核心
- `ModelSamplingSD3`
- `VAELoader`
- `WanImageToVideo`
- `CLIPTextEncode` ★核心
- `LoraLoaderModelOnly` ★核心
- `SimpleMath+`
- `ModelSamplingSD3`
- `PathchSageAttentionKJ`
- `KSamplerAdvanced` ★核心
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `PathchSageAttentionKJ`
- `CR Text`
- `CLIPTextEncode` ★核心
- `CR Text Concatenate`
- `LoadImage`
- `LoraLoaderModelOnly` ★核心
- `VAEDecode` ★核心
- `VHS_VideoCombine`
- `easy int`
- `easy int`
- `LoadImage`
- `LoraLoaderModelOnly` ★核心
- `CR Text`

## 关键参数

- `seed` = `disable`
- `steps` = `randomize`
- `cfg` = `14`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `simple`

## 知识

覆盖率 **100%**（27/27）

**有卡**：`CLIPLoader`、`easy int`、`KSamplerAdvanced`、`ModelSamplingSD3`、`VAELoader`、`WanImageToVideo`、`CLIPTextEncode`、`LoraLoaderModelOnly`、`SimpleMath+`、`PathchSageAttentionKJ`、`UNETLoader`、`CR Text`、`CR Text Concatenate`、`LoadImage`、`VAEDecode`、`VHS_VideoCombine`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerAdvanced

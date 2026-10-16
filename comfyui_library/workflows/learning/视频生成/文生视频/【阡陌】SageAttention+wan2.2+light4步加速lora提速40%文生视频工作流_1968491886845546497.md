---
key: 视频生成/文生视频/【阡陌】SageAttention+wan2.2+light4步加速lora提速40%文生视频工作流_1968491886845546497.json
name: 【阡陌】SageAttention+wan2.2+light4步加速lora提速40%文生视频工作流_1968491886845546497.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/1968491886845546497.json
hash: b61e8e38a887a01a
coverage: 1
learned_at: 2026-10-15 22:43:45
nodes: [VAEDecode, LoadImage, KSamplerAdvanced, KSamplerAdvanced, VAELoader, CreateVideo, SaveVideo, CLIPLoader, ModelSamplingSD3, ModelPatchTorchSettings, PathchSageAttentionKJ, UNETLoader, LoraLoaderModelOnly, ModelSamplingSD3, ModelPatchTorchSettings, UNETLoader, LoraLoaderModelOnly, PathchSageAttentionKJ, CLIPTextEncode, CLIPTextEncode, EmptyHunyuanLatentVideo]
patterns: []
missing: []
parameters: {"cfg": 4, "denoise": "simple", "sampler_name": 1, "scheduler": "euler", "seed": "enable", "steps": "randomize"}
---

# 视频生成/文生视频/【阡陌】SageAttention+wan2.2+light4步加速lora提速40%文生视频工作流_1968491886845546497.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/1968491886845546497.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Output → Other

**节点**（21 个）：
- `VAEDecode` ★核心
- `LoadImage`
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `VAELoader`
- `CreateVideo`
- `SaveVideo`
- `CLIPLoader`
- `ModelSamplingSD3`
- `ModelPatchTorchSettings`
- `PathchSageAttentionKJ`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `ModelSamplingSD3`
- `ModelPatchTorchSettings`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `PathchSageAttentionKJ`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `EmptyHunyuanLatentVideo`

## 关键参数

- `seed` = `enable`
- `steps` = `randomize`
- `cfg` = `4`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `simple`

## 知识

覆盖率 **100%**（21/21）

**有卡**：`VAEDecode`、`LoadImage`、`KSamplerAdvanced`、`VAELoader`、`CreateVideo`、`SaveVideo`、`CLIPLoader`、`ModelSamplingSD3`、`ModelPatchTorchSettings`、`PathchSageAttentionKJ`、`UNETLoader`、`LoraLoaderModelOnly`、`CLIPTextEncode`、`EmptyHunyuanLatentVideo`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerAdvanced

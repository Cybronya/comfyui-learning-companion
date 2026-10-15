---
key: 视频生成/文生视频/wan2.2文生视频工作流_1992207253564444674.json
name: wan2.2文生视频工作流_1992207253564444674
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/wan2.2文生视频工作流_1992207253564444674.json
hash: 9a241b8b9a54cb8b
coverage: 1
learned_at: 2026-10-15 22:47:36
nodes: [UnetLoaderGGUF, UnetLoaderGGUF, CLIPLoader, VAELoader, PathchSageAttentionKJ, PathchSageAttentionKJ, EmptyHunyuanLatentVideo, VAEDecode, CLIPTextEncode, CLIPTextEncode, ModelSamplingSD3, ModelSamplingSD3, KSamplerAdvanced, KSamplerAdvanced, VHS_VideoCombine, LoraLoaderModelOnly, LoraLoaderModelOnly]
patterns: []
missing: []
parameters: {"cfg": 4, "denoise": "simple", "sampler_name": 1, "scheduler": "euler", "seed": "enable", "steps": "randomize"}
---

# 视频生成/文生视频/wan2.2文生视频工作流_1992207253564444674.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/wan2.2文生视频工作流_1992207253564444674.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Other

**节点**（17 个）：
- `UnetLoaderGGUF` ★核心
- `UnetLoaderGGUF` ★核心
- `CLIPLoader`
- `VAELoader`
- `PathchSageAttentionKJ`
- `PathchSageAttentionKJ`
- `EmptyHunyuanLatentVideo`
- `VAEDecode` ★核心
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `ModelSamplingSD3`
- `ModelSamplingSD3`
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `VHS_VideoCombine`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心

## 关键参数

- `seed` = `enable`
- `steps` = `randomize`
- `cfg` = `4`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `simple`

## 知识

覆盖率 **100%**（17/17）

**有卡**：`UnetLoaderGGUF`、`CLIPLoader`、`VAELoader`、`PathchSageAttentionKJ`、`EmptyHunyuanLatentVideo`、`VAEDecode`、`CLIPTextEncode`、`ModelSamplingSD3`、`KSamplerAdvanced`、`VHS_VideoCombine`、`LoraLoaderModelOnly`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、KSamplerAdvanced、EmptyHunyuanLatentVideo、ModelSamplingSD3

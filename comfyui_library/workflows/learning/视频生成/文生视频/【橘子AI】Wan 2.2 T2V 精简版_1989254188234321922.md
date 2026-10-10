---
key: 视频生成/文生视频/【橘子AI】Wan 2.2 T2V 精简版_1989254188234321922.json
name: 【橘子AI】Wan 2.2 T2V 精简版_1989254188234321922
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/【橘子AI】Wan 2.2 T2V 精简版_1989254188234321922.json
hash: b209482ae4cf3b9c
coverage: 1
learned_at: 2026-10-11 02:57:39
nodes: [CLIPTextEncode, KSamplerAdvanced, KSamplerAdvanced, ModelSamplingSD3, ModelSamplingSD3, PathchSageAttentionKJ, PathchSageAttentionKJ, UNETLoader, UNETLoader, LoraLoaderModelOnly, CLIPLoader, VAELoader, CLIPTextEncode, EmptyHunyuanLatentVideo, LoraLoaderModelOnly, VAEDecode, VHS_VideoCombine]
patterns: []
missing: []
parameters: {"cfg": 4, "denoise": "simple", "sampler_name": 1, "scheduler": "euler", "seed": "enable", "steps": "randomize"}
---

# 视频生成/文生视频/【橘子AI】Wan 2.2 T2V 精简版_1989254188234321922.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/【橘子AI】Wan 2.2 T2V 精简版_1989254188234321922.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Other

**节点**（17 个）：
- `CLIPTextEncode` ★核心
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `ModelSamplingSD3`
- `ModelSamplingSD3`
- `PathchSageAttentionKJ`
- `PathchSageAttentionKJ`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `CLIPLoader`
- `VAELoader`
- `CLIPTextEncode` ★核心
- `EmptyHunyuanLatentVideo`
- `LoraLoaderModelOnly` ★核心
- `VAEDecode` ★核心
- `VHS_VideoCombine`

## 关键参数

- `seed` = `enable`
- `steps` = `randomize`
- `cfg` = `4`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `simple`

## 知识

覆盖率 **100%**（17/17）

**有卡**：`CLIPTextEncode`、`KSamplerAdvanced`、`ModelSamplingSD3`、`PathchSageAttentionKJ`、`UNETLoader`、`LoraLoaderModelOnly`、`CLIPLoader`、`VAELoader`、`EmptyHunyuanLatentVideo`、`VAEDecode`、`VHS_VideoCombine`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、UNETLoader、KSamplerAdvanced、EmptyHunyuanLatentVideo

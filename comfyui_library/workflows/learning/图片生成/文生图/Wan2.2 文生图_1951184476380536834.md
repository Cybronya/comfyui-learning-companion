---
key: 图片生成/文生图/Wan2.2 文生图_1951184476380536834.json
name: Wan2.2 文生图_1951184476380536834.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Wan2.2 文生图_1951184476380536834.json
hash: d8225e24e956af97
coverage: 1
learned_at: 2026-10-07 22:59:07
nodes: [ModelSamplingSD3, ModelSamplingSD3, PathchSageAttentionKJ, CLIPTextEncode, PathchSageAttentionKJ, EmptyHunyuanLatentVideo, VAEDecode, SaveImage, KSampler, CLIPTextEncode, CLIPLoader, KSampler, VAELoader, UNETLoader, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly]
patterns: []
missing: []
parameters: {"cfg": 1, "denoise": 0.30000000000000004, "sampler_name": "euler", "scheduler": "simple", "seed": 14, "steps": 10}
---

# 图片生成/文生图/Wan2.2 文生图_1951184476380536834.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/1951184476380536834.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Output → Other

**节点**（17 个）：
- `ModelSamplingSD3`
- `ModelSamplingSD3`
- `PathchSageAttentionKJ`
- `CLIPTextEncode` ★核心
- `PathchSageAttentionKJ`
- `EmptyHunyuanLatentVideo`
- `VAEDecode` ★核心
- `SaveImage`
- `KSampler` ★核心
- `CLIPTextEncode` ★核心
- `CLIPLoader`
- `KSampler` ★核心
- `VAELoader`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心

## 关键参数

- `seed` = `14`
- `steps` = `10`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `0.30000000000000004`

## 知识

覆盖率 **100%**（17/17）

**有卡**：`ModelSamplingSD3`、`PathchSageAttentionKJ`、`CLIPTextEncode`、`EmptyHunyuanLatentVideo`、`VAEDecode`、`SaveImage`、`KSampler`、`CLIPLoader`、`VAELoader`、`UNETLoader`、`LoraLoaderModelOnly`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、UNETLoader、EmptyHunyuanLatentVideo

---
key: 视频生成/文生视频/一键运行：最新 WAN2.2 融合模型 文生视频_1958711143466483714.json
name: 一键运行：最新 WAN2.2 融合模型 文生视频_1958711143466483714.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/一键运行：最新 WAN2.2 融合模型 文生视频_1958711143466483714.json
hash: d688ddeb65682358
coverage: 0.888889
learned_at: 2026-10-15 22:43:42
nodes: [Seed Everywhere, KSampler (Efficient), VHS_VideoCombine, EmptyHunyuanLatentVideo, ModelSamplingSD3, CheckpointLoaderSimple, CLIPTextEncode, CLIPTextEncode, Note]
patterns: []
missing: []
parameters: {"cfg": 1, "checkpoint": "wan2.2-t2v-rapid-aio-v8.1.safetensors", "denoise": 1, "sampler_name": "sa_solver", "scheduler": "beta", "seed": 984000706479306, "steps": 8}
---

# 视频生成/文生视频/一键运行：最新 WAN2.2 融合模型 文生视频_1958711143466483714.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/1958711143466483714.json`

## 结构

**生成流程**：Model → Condition → Sampling → Other

**节点**（9 个）：
- `Seed Everywhere`
- `KSampler (Efficient)` ★核心
- `VHS_VideoCombine`
- `EmptyHunyuanLatentVideo`
- `ModelSamplingSD3`
- `CheckpointLoaderSimple` ★核心
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `Note`

## 关键参数

- `seed` = `984000706479306`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `sa_solver`
- `scheduler` = `beta`
- `denoise` = `1`
- `checkpoint` = `wan2.2-t2v-rapid-aio-v8.1.safetensors`

## 知识

覆盖率 **89%**（8/9）

**有卡**：`Seed Everywhere`、`KSampler (Efficient)`、`VHS_VideoCombine`、`EmptyHunyuanLatentVideo`、`ModelSamplingSD3`、`CheckpointLoaderSimple`、`CLIPTextEncode`

**用到的条目**：CheckpointLoaderSimple、CLIPTextEncode、KSampler (Efficient)、Seed Everywhere、EmptyHunyuanLatentVideo、ModelSamplingSD3、VHS_VideoCombine、KSampler

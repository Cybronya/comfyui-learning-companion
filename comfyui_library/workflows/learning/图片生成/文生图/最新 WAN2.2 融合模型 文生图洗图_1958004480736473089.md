---
key: 图片生成/文生图/最新 WAN2.2 融合模型 文生图洗图_1958004480736473089.json
name: 最新 WAN2.2 融合模型 文生图洗图_1958004480736473089
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/最新 WAN2.2 融合模型 文生图洗图_1958004480736473089.json
hash: f961ed05a71a5c4b
coverage: 0.818182
learned_at: 2026-10-15 22:28:53
nodes: [PreviewImage, ModelSamplingSD3, Seed Everywhere, CLIPTextEncode, EmptySD3LatentImage, CheckpointLoaderSimple, CLIPTextEncode, Prompts Everywhere, KSampler (Efficient), SaveImage, Note]
patterns: []
missing: []
parameters: {"cfg": 1, "checkpoint": "wan2.2-t2v-rapid-aio-v8.1.safetensors", "denoise": 1, "sampler_name": "sa_solver", "scheduler": "beta", "seed": 193226821865994, "steps": 8}
---

# 图片生成/文生图/最新 WAN2.2 融合模型 文生图洗图_1958004480736473089.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/最新 WAN2.2 融合模型 文生图洗图_1958004480736473089.json`

## 结构

**生成流程**：Model → Condition → Sampling → Process → Output → Other

**节点**（11 个）：
- `PreviewImage`
- `ModelSamplingSD3`
- `Seed Everywhere`
- `CLIPTextEncode` ★核心
- `EmptySD3LatentImage`
- `CheckpointLoaderSimple` ★核心
- `CLIPTextEncode` ★核心
- `Prompts Everywhere`
- `KSampler (Efficient)` ★核心
- `SaveImage`
- `Note`

## 关键参数

- `checkpoint` = `wan2.2-t2v-rapid-aio-v8.1.safetensors`
- `seed` = `193226821865994`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `sa_solver`
- `scheduler` = `beta`
- `denoise` = `1`

## 知识

覆盖率 **82%**（9/11）

**有卡**：`ModelSamplingSD3`、`Seed Everywhere`、`CLIPTextEncode`、`EmptySD3LatentImage`、`CheckpointLoaderSimple`、`Prompts Everywhere`、`KSampler (Efficient)`、`SaveImage`

**用到的条目**：CheckpointLoaderSimple、CLIPTextEncode、KSampler (Efficient)、Seed Everywhere、Prompts Everywhere、SaveImage、EmptySD3LatentImage、ModelSamplingSD3
